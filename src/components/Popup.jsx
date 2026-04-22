function PopupRuta({ punto, ruta, modoHistoriador, setModoHistoriador }) {
  return (
    <div className="popup-contenido">
      <h3>{punto.nombre}</h3>
      {modoHistoriador && punto.descripcion && (
        <p>{punto.descripcion}</p>
      )}
      <p><b>Ruta:</b> {ruta.nombre}</p>
      <label className="popup-toggle">
        🎓 Modo Historiador
        <input
          type="checkbox"
          checked={modoHistoriador}
          onChange={() => setModoHistoriador(!modoHistoriador)}
        />
      </label>
    </div>
  )
}

export default PopupRuta;
