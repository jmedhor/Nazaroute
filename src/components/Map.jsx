import { MapContainer, TileLayer, Marker, Polyline, Popup } from 'react-leaflet'
import { useEffect, useState } from 'react'
import 'leaflet/dist/leaflet.css'
import PopupRuta from './Popup'

function Mapa({ rutaSeleccionada }) {
  const [puntos, setPuntos] = useState([])

  useEffect(() => {
    if (!rutaSeleccionada) return;

    fetch(`http://localhost:8000/rutas/${rutaSeleccionada.id}/puntos`)
      .then(res => res.json())
      .then(data => setPuntos(data))
      .catch(err => console.error(err))
  }, [rutaSeleccionada])

  return (
    <MapContainer
      center={[37.1773, -3.5986]}
      zoom={15}
      style={{ height: "80vh", width: "80vw" }}
    >

      <TileLayer
        attribution='© OpenStreetMap contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />

      {puntos.map(punto => (
        <Marker
          key={punto.id}
          position={[punto.latitud, punto.longitud]}
        >
          <Popup>
            <PopupRuta punto={punto} ruta={rutaSeleccionada} />
          </Popup>
        </Marker>
      ))}


    </MapContainer>
  )
}

export default Mapa
