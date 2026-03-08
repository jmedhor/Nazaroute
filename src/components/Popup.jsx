function PopupRuta({ punto, ruta }) {
  return (
    <div>
      <h3>{punto.nombre}</h3>
      {punto.descripcion && <p>{punto.descripcion}</p>}
      <p><b>Ruta:</b> {ruta.nombre}</p>
    </div>
  );
}

export default PopupRuta;
