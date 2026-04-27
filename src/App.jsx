import { useState, useRef } from 'react'
import './App.css'
import Mapa from './components/Map.jsx'
import MenuRutas from './components/MenuRutas.jsx'
import MenuPuntos from './components/MenuPuntos.jsx'
import PanelRuta from './components/PanelRuta.jsx'

function App() {
  const [rutaSeleccionada, setRutaSeleccionada] = useState(null)
  const mapRef = useRef()
  const [modoHistoriador, setModoHistoriador] = useState(false)
  const [modoRuta, setModoRuta] = useState("optima")
  const [rutasSegmentos, setRutasSegmentos] = useState([])
  const [mostrarPuntos, setMostrarPuntos] = useState(false)
  const [modoNavegacion, setModoNavegacion] = useState(false)
  const [evitarPago, setEvitarPago] = useState(false)
  // función para centrar en un punto desde MenuPuntos
  const centrarEnPunto = (punto) => {
    if (!mapRef.current) return

    mapRef.current.flyTo(
      [punto.latitud, punto.longitud],
      16,
      { duration: 1.2 }
    )
  }

  return (

//--------

    <div className="App">

      {/* HEADER */}
      <header className="app-header">
        <div className="header-left">
          <h1>NazaRoute</h1>
        </div>

        <div className="header-right">
          <div className="selector-ruta">
            <label>
              <input
                type="radio"
                value="optima"
                checked={modoRuta === "optima"}
                onChange={() => setModoRuta("optima")}
              />
              Óptima
            </label>



            <label>
              <input
                type="radio"
                value="historica"
                checked={modoRuta === "historica"}
                onChange={() => setModoRuta("historica")}
              />
              Histórica
            </label>

            <label style={{ display: "block", marginTop: "10px" }}>
              <input
                type="checkbox"
                checked={evitarPago}
                onChange={(e) => setEvitarPago(e.target.checked)}
              />
              {" "}Evitar opciones de pago 💸
            </label>

          </div>
        </div>
      </header>

      {/* MAIN */}
      <div className="main-layout">

        {/* MAPA */}
        <div className="map-container">
          <Mapa
            rutaSeleccionada={rutaSeleccionada}
            mapRef={mapRef}
            modoHistoriador={modoHistoriador}
            setModoHistoriador={setModoHistoriador}
            modoRuta={modoRuta}
            setRutasSegmentos={setRutasSegmentos}
            evitarPago={evitarPago}
          />
        </div>

        {/* PANEL DERECHO ÚNICO */}
        <div className="panel-derecha">

          {/* SIN RUTA */}
          {!rutaSeleccionada && (
            <MenuRutas
              rutaSeleccionada={rutaSeleccionada}
              setRutaSeleccionada={setRutaSeleccionada}
            />
          )}

          {/* CON RUTA */}
          {rutaSeleccionada && (
            <>
              {/* BOTON VOLVER SIEMPRE ARRIBA */}
              <button
                className="btn-volver"
                onClick={() => {
                  setRutaSeleccionada(null)
                  setModoNavegacion(false)
                }}
              >
                ← Volver
              </button>

              {/* MODO PUNTOS */}
              {!modoNavegacion && (
                <>
                  <MenuPuntos
                    ruta={rutaSeleccionada}
                    centrarEnPunto={centrarEnPunto}
                    mapRef={mapRef}

                  />

                  <button
                    className="btn-start"
                    onClick={() => setModoNavegacion(true)}
                  >
                    🚀 Comenzar Ruta
                  </button>
                </>
              )}

              {/* MODO NAVEGACIÓN */}
              {modoNavegacion && (
                <>
                  <PanelRuta rutasSegmentos={rutasSegmentos} />

                  <button
                    className="btn-puntos"
                    onClick={() => setModoNavegacion(false)}
                  >
                    📍 Volver a lista de puntos
                  </button>
                </>
              )}
            </>
          )}

        </div>

      </div>
    </div>
//------------------

  )
}

export default App
