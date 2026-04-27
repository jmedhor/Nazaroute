import { useEffect, useState } from "react"

function MenuPuntos({ ruta, setRutaSeleccionada, mapRef }) {
  const [puntos, setPuntos] = useState([])

  useEffect(() => {
    fetch(`http://localhost:8000/rutas/${ruta.id}/puntos`)
      .then(res => res.json())
      .then(data => setPuntos(data))
      .catch(err => console.error(err))
  }, [ruta])

  return (
    <div className="menu-puntos">
      <h3>{ruta.nombre}</h3>
      <ul>
        {puntos.map(punto => (
          <li
            key={punto.id}
            onClick={() => mapRef.current.centrarYAbrir(punto)}
          >
            {punto.nombre}
          </li>
        ))}
      </ul>
    </div>
  )
}

export default MenuPuntos
