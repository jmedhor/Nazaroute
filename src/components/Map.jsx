import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import { useEffect, useState } from 'react'
import 'leaflet/dist/leaflet.css'
import PopupRuta from './Popup'

function Mapa({ rutaSeleccionada }) {

  const [rutas, setRutas] = useState([])

  useEffect(() => {
    fetch("http://localhost:8000/rutas")
      .then(res => res.json())
      .then(data => setRutas(data))
  }, [])

  return (
    <MapContainer
      center={[37.1773, -3.5986]}
      zoom={13}
      style={{ height: "80vh", width: "80vw" }}
    >

      <TileLayer
        attribution='© OpenStreetMap contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />

      {rutaSeleccionada &&
        rutaSeleccionada.puntos.map(punto => (
          <Marker
            key={punto.id}
            position={[punto.latitud, punto.longitud]}
          >
            <Popup>
              <PopupRuta punto={punto} ruta={rutaSeleccionada} />
            </Popup>
          </Marker>
        ))
      }

    </MapContainer>
  )
}

export default Mapa
