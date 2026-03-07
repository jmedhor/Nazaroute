import { useState } from 'react'
import './App.css'
import Mapa from './components/Map.jsx'

function App() {

  return (
    <div className="App">

      <header className="App-header">
        <h1>Rutas Históricas de Granada</h1>
      </header>

      {/* Contenedor del mapa */}
      <div className="map-container" style={{ height: '80vh', width: '80vw' }}>
        <Mapa />
      </div>

    </div>
  )
}

export default App
