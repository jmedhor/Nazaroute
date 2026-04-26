const OSRM_BASE = "https://router.project-osrm.org"

// La ruta historica por ahora solo sigue los puntos en orden
// La intencion es que el usuario sigue el orden "definido por la UGR"

export async function obtenerRutaHistorica(puntos, userLocation) {

  const coords = [
    `${userLocation.lon},${userLocation.lat}`,
    ...puntos.map(p => `${p.longitud},${p.latitud}`)
  ].join(";")

  const url = `${OSRM_BASE}/route/v1/walking/${coords}?overview=false&geometries=geojson&steps=true`

  const res = await fetch(url)
  const data = await res.json()

  return data.routes[0].legs
}

// La ruta optima parte de la localizacion inicial y calcula la
// ruta mas eficiente para pasar por todos los puntos

export async function obtenerRutaOptima(puntos, userLocation) {

  const coords = [
    `${userLocation.lon},${userLocation.lat}`,
    ...puntos.map(p => `${p.longitud},${p.latitud}`)
  ].join(";")

  const url = `${OSRM_BASE}/trip/v1/walking/${coords}?overview=false&geometries=geojson&steps=true`

  const res = await fetch(url)
  const data = await res.json()

  return data.trips[0].legs
}
