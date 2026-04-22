import { useState, useRef } from 'react'
import './App.css'
import Mapa from './components/Map.jsx'
import MenuRutas from './components/MenuRutas.jsx'
import MenuPuntos from './components/MenuPuntos.jsx'

function App() {
  const [rutaSeleccionada, setRutaSeleccionada] = useState(null)
  const mapRef = useRef()
  const [modoHistoriador, setModoHistoriador] = useState(false)


  // función para centrar en un punto desde MenuPuntos
  const centrarEnPunto = (punto) => {
    console.log("helloo")
    if (mapRef.current) {
      console.log("h2")
      mapRef.current.setView([punto.latitud, punto.longitud], 1)
    }
  }

  return (
    <div className="App">
    <header className="App-header">
      <h1>NazaRoute</h1>
    </header>

      <div className="contenedor-principal">
        <div className="map-container">
          <Mapa
            rutaSeleccionada={rutaSeleccionada}
            mapRef={mapRef}
            modoHistoriador={modoHistoriador}
            setModoHistoriador={setModoHistoriador}
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
