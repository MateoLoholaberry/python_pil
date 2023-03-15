// react-router-dom imports
import { Link } from "react-router-dom";


// Navbar cuando el usuario esta sin "loguear";
const Navbar = () => {
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <div className="container-fluid">
                <a className="navbar-brand fw-bold">Notes App</a>
                <button
                    className="navbar-toggler"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#navbarNav"
                    aria-controls="navbarNav"
                    aria-expanded="false"
                    aria-label="Toggle navigation"
                >
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarNav">
                    <ul className="navbar-nav">
                        <li className="nav-item">
                            <Link className="nav-link" to="/">
                                Usuarios registrados
                            </Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link" to="/Registrar-usuario">
                                Registrar usuario
                            </Link>
                        </li>

                        <li className="nav-item">
                            <Link className="nav-link" to="/login-usuario">
                                Iniciar sesión
                            </Link>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;
