import { useState, useRef } from 'react'
import './App.css'
import Mapa from './components/Map.jsx'
import MenuRutas from './components/MenuRutas.jsx'
import MenuPuntos from './components/MenuPuntos.jsx'

function App() {
  const [rutaSeleccionada, setRutaSeleccionada] = useState(null)
  const mapRef = useRef()
  const [modoHistoriador, setModoHistoriador] = useState(false)
  const [modoRuta, setModoRuta] = useState("optima")

  // función para centrar en un punto desde MenuPuntos
  const centrarEnPunto = (punto) => {
    if (mapRef.current) {
      mapRef.current.setView([punto.latitud, punto.longitud], 1)
    }
  }

  return (
    <div className="App">
    <header className="App-header">
      <h1>NazaRoute</h1>

      <div className="selector-ruta">
        <h3>Tipo de ruta</h3>

        <label>
          <input
            type="radio"
            name="ruta"
            value="optima"
            checked={modoRuta === "optima"}
            onChange={() => setModoRuta("optima")}
          />
          🟢 Óptima (recomendada)
        </label>

        <label>
          <input
            type="radio"
            name="ruta"
            value="historica"
            checked={modoRuta === "historica"}
            onChange={() => setModoRuta("historica")}
          />
          🟥 Histórica (orden fijo)
        </label>
      </div>

    </header>



      <div className="contenedor-principal">
        <div className="map-container">
          <Mapa
            rutaSeleccionada={rutaSeleccionada}
            mapRef={mapRef}
            modoHistoriador={modoHistoriador}
            setModoHistoriador={setModoHistoriador}
            modoRuta={modoRuta}
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
