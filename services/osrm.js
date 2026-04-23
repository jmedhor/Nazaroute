const OSRM_BASE = "https://router.project-osrm.org"

// La ruta historica por ahora solo sigue los puntos en orden
// La intencion es que el usuario sigue el orden "definido por la UGR"

export async function obtenerRutaHistorica(puntos, userLocation) {

  const coords = [
    `${userLocation.lon},${userLocation.lat}`,
    ...puntos.map(p => `${p.longitud},${p.latitud}`)
  ].join(";")

  const url = `https://router.project-osrm.org/route/v1/driving/${coords}?overview=full&geometries=geojson`

  const res = await fetch(url)
  const data = await res.json()

  return data.routes[0].geometry.coordinates
}

// La ruta optima parte de la localizacion inicial y calcula la
// ruta mas eficiente para pasar por todos los puntos

export async function obtenerRutaOptima(puntos, userLocation) {

  const coords = [
    `${userLocation.lon},${userLocation.lat}`,
    ...puntos.map(p => `${p.longitud},${p.latitud}`)
  ].join(";")

  const url = `https://router.project-osrm.org/trip/v1/driving/${coords}?overview=full&geometries=geojson&source=first&destination=any`

  const res = await fetch(url)
  const data = await res.json()

  return data.trips[0].geometry.coordinates
}
