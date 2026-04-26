import { MapContainer, TileLayer, Marker, Popup, Polyline, useMapEvents } from 'react-leaflet'
import { useEffect, useState } from 'react'
import { obtenerRutaHistorica, obtenerRutaOptima } from '../../services/osrm.js'
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'
import PopupRuta from './Popup'
import gpsRed from '../assets/gps_red.png'
import gpsBlue from '../assets/gps_blue.png'
import gpsOrange from '../assets/gps_orange.png'
import gpsGreen from '../assets/gps_green.png'
import gpsPink from '../assets/gps_pink.png'
import gpsBlack from '../assets/gps_black.png'
import gpsPurple from '../assets/gps_purple.png'


// Iconos por ruta
const iconosRutas = {
  1: new L.Icon({ iconUrl: gpsRed, iconSize: [40, 40], iconAnchor: [20, 40], popupAnchor: [0, -40] }),
  2: new L.Icon({ iconUrl: gpsBlue, iconSize: [40, 40], iconAnchor: [20, 40], popupAnchor: [0, -40] }),
  3: new L.Icon({ iconUrl: gpsOrange, iconSize: [40, 40], iconAnchor: [20, 40], popupAnchor: [0, -40] }),
  4: new L.Icon({ iconUrl: gpsGreen, iconSize: [40, 40], iconAnchor: [20, 40], popupAnchor: [0, -40] }),
  5: new L.Icon({ iconUrl: gpsPink, iconSize: [40, 40], iconAnchor: [20, 40], popupAnchor: [0, -40] }),
  6: new L.Icon({ iconUrl: gpsBlack, iconSize: [30, 30], iconAnchor: [15, 30], popupAnchor: [0, -30] }),
  7: new L.Icon({ iconUrl: gpsPurple, iconSize: [30, 30], iconAnchor: [15, 30], popupAnchor: [0, -30] }),
}

const colores = ["red", "blue", "green", "orange", "purple", "black"]



function Mapa({ rutaSeleccionada, mapRef, modoHistoriador, setModoHistoriador, modoRuta }) {
  const [todosPuntos, setTodosPuntos] = useState([])
  const [rutaLinea, setRutaLinea] = useState(null)
  const [userLocation, setUserLocation] = useState({
    lat: 37.1773,
    lon: -3.5986
  })
  const [rutasSegmentos, setRutasSegmentos] = useState([])
  const [cargandoRuta, setCargandoRuta] = useState(false)


  function MapaClickHandler() {
    useMapEvents({
      click(e) {
        console.log("testing")
        setUserLocation({
          lat: e.latlng.lat,
          lon: e.latlng.lng
        })
      }
    })

    return null
  }

  useEffect(() => {
    fetch("http://localhost:8000/puntos")
      .then(res => res.json())
      .then(data => setTodosPuntos(data))
      .catch(err => console.error(err))
  }, [])

  useEffect(() => {
    if (!rutaSeleccionada) {
      setRutasSegmentos([])
    }
  }, [rutaSeleccionada])

  let puntos = rutaSeleccionada
    ? todosPuntos.filter(p => p.ruta_id === rutaSeleccionada.id)
    : todosPuntos

  useEffect(() => {
    const cargarRuta = async () => {
      if (!rutaSeleccionada || puntos.length === 0) return

      setCargandoRuta(true)   // 🔴 empieza carga

      try {
        let legs

        if (modoRuta === "historica") {
          legs = await obtenerRutaHistorica(puntos, userLocation)
        } else {
          legs = await obtenerRutaOptima(puntos, userLocation)
        }

        setRutasSegmentos(legs)

      } catch (err) {
        console.error("Error cargando ruta:", err)
      } finally {
        setCargandoRuta(false)  // 🟢 termina carga
      }
    }

    cargarRuta()
  }, [rutaSeleccionada, todosPuntos, modoRuta, userLocation])
  return (
    <MapContainer
      center={[37.1773, -3.5986]}
      zoom={15}
      style={{ height: "80vh", width: "80vw" }}
      whenCreated={(mapInstance) => {
        mapRef.current = mapInstance
      }}
    >
    <MapaClickHandler />

      <TileLayer
        attribution='© OpenStreetMap contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />

      {cargandoRuta && (
        <div className="loading-overlay">
          Cargando ruta...
        </div>
      )}

      {rutasSegmentos.map((leg, index) => {

        const coords = leg.steps.flatMap(step =>
          step.geometry.coordinates
        )

        return (
          <Polyline
            key={index}
            positions={coords.map(([lon, lat]) => [lat, lon])}
            color={colores[index % colores.length]}
            weight={5}
          />
        )
      })}

      <Marker position={[userLocation.lat, userLocation.lon]}>
        <Popup>📍 Inicio (usuario)</Popup>
      </Marker>

      {puntos.map(punto => (
        <Marker
          key={`${punto.id}-${punto.ruta_id}`}
          position={[punto.latitud, punto.longitud]}
          icon={iconosRutas[punto.ruta_id] || iconosRutas[1]}
        >
          <Popup>
            <PopupRuta
              punto={punto}
              ruta={{ nombre: punto.ruta_nombre }}
              modoHistoriador={modoHistoriador}
              setModoHistoriador={setModoHistoriador}
            />
          </Popup>
        </Marker>
      ))}


    </MapContainer>
  )
}

export default Mapa
