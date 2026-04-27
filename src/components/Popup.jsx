function PopupRuta({ punto, ruta, modoHistoriador, setModoHistoriador }) {
  return (
    <div className="popup-contenido">
      <h3>{punto.nombre}</h3>
      {modoHistoriador && punto.descripcion && (
        <p>{punto.descripcion}</p>
      )}
      <p><b>Ruta:</b> {ruta.nombre}</p>

      {/*  Estado de pago */}
      <p>
        <strong>Acceso:</strong>{" "}
        <span style={{ color: punto.pago ? "red" : "green" }}>
          {punto.pago ? "De pago " : "Gratis "}
        </span>
      </p>

      {/*  URL */}
      {punto.url && (
        <p>
          <a
            href={punto.url}
            target="_blank"
            rel="noopener noreferrer"
            style={{ color: "#0077cc", textDecoration: "underline" }}
          >
            Más información 🔗
          </a>
        </p>
      )}

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
