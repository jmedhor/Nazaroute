import { useState } from 'react'
import './App.css'
import Mapa from './components/Map.jsx'
import MenuRutas from './components/MenuRutas.jsx'

function App() {
  const [rutaSeleccionada, setRutaSeleccionada] = useState(null)

  return (
    <div className="App">

      <header className="App-header">
        <h1>Rutas Históricas de Granada</h1>
      </header>

      <div className="contenedor-principal">

        <div className="map-container">
          <Mapa rutaSeleccionada={rutaSeleccionada} />
        </div>

        <MenuRutas
          rutaSeleccionada={rutaSeleccionada}
          setRutaSeleccionada={setRutaSeleccionada}
        />

      </div>

    </div>
  )
}

export default App
