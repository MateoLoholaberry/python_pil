import logo from './logo.svg';
import './App.css';
import Welcome from './components/Welcome';
import SimpleStateFunction from './components/React_Class_Function/componente_clase'
// import Coordenandas from './components/React_Class_Function/componente_clase_avanzado'
import Coordenadas from './components/React_Class_Function/componente_funcion_avanzado'


function App(props) {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      <div>
      <SimpleStateFunction></SimpleStateFunction>
      <Coordenadas></Coordenadas>
      {/* <Coordenadas></Coordenadas> */}
       {/* <Welcome></Welcome> */}
      </div>
      </header> 
    </div>
  );
}

export default App;
