-- ¿Cuantos empleados tenemos registrados?
SELECT COUNT(*) cant_empleados
FROM employees;

-- ¿Cuantos empleados hay en cada oficina?
SELECT e.officeCode, o.city, COUNT(*) cant_empleados
FROM employees e, offices o
WHERE e.officeCode = o.officeCode
GROUP BY e.officeCode, o.city;


-- ¿Cuantos productos tenemos por linea?
SELECT pl.productLine, COUNT(*) cant_productos
FROM products p, productlines pl
WHERE p.productLine = pl.productLine
GROUP BY pl.productLine;


-- Listar los productos de la linea PLANES
SELECT *
FROM products p
WHERE p.productLine = "Planes";


-- Listar solo los productos que vienen con logos oficiales
SELECT *
FROM products p
WHERE p.productDescription LIKE "%official logo%";

-- ¿Todos los clientes son del mismo pais? Que paises?
-- No son todos del mismo país
SELECT c.country, COUNT(*)
FROM customers c
GROUP BY c.country;

-- ¿Cual fue el ultimo pago que se registro?
SELECT *
FROM payments P
ORDER BY P.paymentDate DESC
LIMIT 1;


-- ¿Cual fue el pago mas chico?
SELECT *
FROM payments p
ORDER BY p.amount
LIMIT 1;

-- Listar los clientes que no tienen pagos
SELECT *
FROM customers c LEFT JOIN payments p
ON c.customerNumber = p.customerNumber
WHERE p.customerNumber IS NULL;


-- ¿Cuanto se recaudo en los ultimos 6 meses?
SELECT SUM(P.amount) recaudado_6_meses
FROM payments p
Where p.paymentDate BETWEEN '2005-01-01' AND '2005-06-31';


-- ¿Cual es el producto mas vendido?
SELECT p.productName, SUM(o.quantityOrdered) cant_ordenada 
FROM orderdetails o, products p
WHERE o.productCode = p.productCode
GROUP BY o.productCode
ORDER BY cant_ordenada DESC
LIMIT 1;


-- ¿Cual les son los 10 mejores clientes?
SELECT c.customerName, COUNT(o.orderNumber) cant_ordenes
FROM orders o, customers c 
WHERE o.customerNumber = c.customerNumber 
GROUP BY c.customerName 
ORDER BY cant_ordenes DESC
LIMIT 10;


-- ¿Cada cuanto tiempo regresa un cliente?
SELECT t1.anio, AVG(t1.cant_compras)
FROM (
    SELECT YEAR(o.orderDate) anio, count(o.orderNumber) cant_compras
    FROM orders o 
    GROUP BY YEAR(o.orderDate)
    ORDER BY o.customerNumber ASC
) t1
GROUP BY t1.anio;

-- ¿Cuantos clientes no tienen registrado su telefono?
-- ¿Quienes son?
SELECT *
FROM customers c
WHERE c.phone = '0';


-- ¿Listar los productos mas vendidos en el ultimo mes registrado y su precio?
SELECT o.orderDate , p.productCode, p.productName, p.MSRP, SUM(od.quantityOrdered)
FROM orders o, orderdetails od, products p
WHERE o.orderNumber = od.orderNumber
AND od.productCode = p.productCode
AND o.orderDate  BETWEEN '2005-04-31' AND '2005-05-31'
GROUP BY p.productCode, p.productName
ORDER BY SUM(od.quantityOrdered) DESC;


-- ¿Quien es el jefe de cada departamento?
SELECT *
FROM employees e
WHERE e.jobTitle LIKE "%VP%";

-- ¿Cual es el empleado que mas vende?
SELECT e.firstName nombre, e.lastName apellido, e.employeeNumber,
COUNT(c.customerNumber) cant_clientes_por_empleado
FROM customers c, employees e
WHERE c.salesRepEmployeeNumber = e.employeeNumber
GROUP BY e.employeeNumber
ORDER BY cant_clientes_por_empleado DESC
LIMIT 1;