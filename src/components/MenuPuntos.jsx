import { useEffect, useState } from "react"

function MenuPuntos({ ruta, setRutaSeleccionada, centrarEnPunto }) {
  const [puntos, setPuntos] = useState([])

  useEffect(() => {
    fetch(`http://localhost:8000/rutas/${ruta.id}/puntos`)
      .then(res => res.json())
      .then(data => setPuntos(data))
      .catch(err => console.error(err))
  }, [ruta])

  return (
    <div className="menu-puntos">
      <button
        onClick={() => setRutaSeleccionada(null)}
        className="volver-boton"
      >
        ← Volver
      </button>
      <h3>{ruta.nombre}</h3>
      <ul>
        {puntos.map(punto => (
          <li
            key={punto.id}
            onClick={() => centrarEnPunto(punto)}
          >
            {punto.nombre}
          </li>
        ))}
      </ul>
    </div>
  )
}

export default MenuPuntos
