import { useState, useRef } from 'react'
import './App.css'
import Mapa from './components/Map.jsx'
import MenuRutas from './components/MenuRutas.jsx'
import MenuPuntos from './components/MenuPuntos.jsx'

function App() {
  const [rutaSeleccionada, setRutaSeleccionada] = useState(null)
  const mapRef = useRef()

  // función para centrar en un punto desde MenuPuntos
  const centrarEnPunto = (punto) => {
    const map = mapRef.current
    if (map) map.setView([punto.latitud, punto.longitud], 18)
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>Rutas Históricas de Granada</h1>
      </header>

      <div className="contenedor-principal">
        <div className="map-container">
          <Mapa
            rutaSeleccionada={rutaSeleccionada}
            mapRef={mapRef}
          />
        </div>

        {/* Mostrar MenuRutas o MenuPuntos según la selección */}
        {rutaSeleccionada ? (
          <MenuPuntos
            ruta={rutaSeleccionada}
            setRutaSeleccionada={setRutaSeleccionada}
            centrarEnPunto={centrarEnPunto}
          />
        ) : (
          <MenuRutas
            rutaSeleccionada={rutaSeleccionada}
            setRutaSeleccionada={setRutaSeleccionada}
          />
        )}
      </div>
    </div>
  )
}

export default App
