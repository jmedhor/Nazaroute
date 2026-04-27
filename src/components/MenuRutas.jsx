import { useEffect, useState } from "react"

function MenuRutas({ rutaSeleccionada, setRutaSeleccionada }) {
  const [rutas, setRutas] = useState([])

  useEffect(() => {
    fetch("http://localhost:8000/rutas")
      .then(res => res.json())
      .then(data => setRutas(data))
      .catch(err => console.error(err))
  }, [])

  return (
    <div className="menu-rutas">

      <h2>Rutas disponibles</h2>

      <ul>
        {rutas.map(ruta => (
          <li
            key={ruta.id}
            onClick={() => setRutaSeleccionada(ruta)}
            className={rutaSeleccionada?.id === ruta.id ? "activa" : ""}
          >
            {ruta.nombre}
          </li>
        ))}
      </ul>

    </div>
  )
}

export default MenuRutas
