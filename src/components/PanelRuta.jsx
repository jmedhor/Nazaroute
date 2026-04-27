function traducirManiobra(tipo, modifier) {

  if (tipo === "depart") return "Sal"
  if (tipo === "arrive") return "Has llegado"

  if (tipo === "turn") {
    if (modifier === "left") return "Gira a la izquierda"
    if (modifier === "right") return "Gira a la derecha"
    if (modifier === "straight") return "Sigue recto"
  }

  if (tipo === "roundabout") return "En la rotonda"
  if (tipo === "merge") return "Incorpórate"

  return "Continúa"
}

function PanelRuta({ rutasSegmentos }) {

  if (!rutasSegmentos || rutasSegmentos.length === 0) {
    return (
      <div className="panel-ruta">
        <h3>🧭 Ruta</h3>
        <p>Selecciona una ruta</p>
      </div>
    )
  }

  let pasoGlobal = 1

  return (
    <div className="panel-ruta">
      <h3>🧭 Pasos de la ruta</h3>

      <ul>
        {rutasSegmentos.map((leg, i) =>
          leg.steps.map((step, j) => {

            const texto = `${traducirManiobra(
              step.maneuver.type,
              step.maneuver.modifier
            )} ${step.name || ""}`

            const distancia = step.distance
              ? ` (${Math.round(step.distance)} m)`
              : ""

            return (
              <li key={`${i}-${j}`}>
                <span className="paso-num">{pasoGlobal++}</span>
                <span className="paso-texto">
                  {texto} {distancia}
                </span>
              </li>
            )
          })
        )}
      </ul>
    </div>
  )
}

export default PanelRuta
