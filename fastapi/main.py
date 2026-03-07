from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="API Rutas Históricas Granada")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # puerto de Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------
# MODELOS
# ------------------------

class PuntoDeInteres(BaseModel):
    id: int
    nombre: str
    descripcion: str
    latitud: float
    longitud: float

class Ruta(BaseModel):
    id: int
    nombre: str
    descripcion: str
    puntos: List[PuntoDeInteres] = []

# ------------------------
# "BASE DE DATOS" TEMPORAL
# ------------------------

rutas_db = [

    Ruta(
        id=1,
        nombre="Granada Islámica (siglos XI-XV)",
        descripcion="Ruta por los principales restos de la Granada musulmana.",
        puntos=[
            PuntoDeInteres(id=1, nombre="Muralla zirí", descripcion="", latitud=37.182196, longitud=-3.594874),
            PuntoDeInteres(id=2, nombre="Puerta de Elvira", descripcion="", latitud=37.182125, longitud=-3.599586),
            PuntoDeInteres(id=3, nombre="Puerta de las Pesas", descripcion="", latitud=37.182512, longitud=-3.593787),
            PuntoDeInteres(id=4, nombre="Puerta de Monaita", descripcion="", latitud=37.182046, longitud=-3.597612),
            PuntoDeInteres(id=5, nombre="Iglesia de San José (alminar)", descripcion="", latitud=37.178663, longitud=-3.596172),
            PuntoDeInteres(id=6, nombre="El Bañuelo", descripcion="", latitud=37.178488, longitud=-3.592991),
            PuntoDeInteres(id=7, nombre="Torres Bermejas", descripcion="", latitud=37.175526, longitud=-3.593412),
            PuntoDeInteres(id=8, nombre="Alcázar Genil", descripcion="", latitud=37.164720, longitud=-3.600530),
            PuntoDeInteres(id=9, nombre="Cuarto Real de Santo Domingo", descripcion="", latitud=37.171700, longitud=-3.594911),
            PuntoDeInteres(id=10, nombre="Alcazaba (Alhambra)", descripcion="", latitud=37.177133, longitud=-3.591810),
            PuntoDeInteres(id=11, nombre="Corral del Carbón", descripcion="", latitud=37.174936, longitud=-3.597878),
            PuntoDeInteres(id=12, nombre="Palacios Nazaríes", descripcion="", latitud=37.177383, longitud=-3.589630),
            PuntoDeInteres(id=13, nombre="Generalife", descripcion="", latitud=37.176954, longitud=-3.585218),
            PuntoDeInteres(id=14, nombre="Palacio de Dar al-Horra", descripcion="", latitud=37.181625, longitud=-3.596362),
            PuntoDeInteres(id=15, nombre="Casa del Chapiz", descripcion="", latitud=37.180980, longitud=-3.588364),
        ]
    ),

    Ruta(
        id=2,
        nombre="Granada Cristiana e Imperial (siglos XV-XVI)",
        descripcion="Monumentos tras la conquista cristiana.",
        puntos=[
            PuntoDeInteres(id=16, nombre="Monasterio de San Jerónimo", descripcion="", latitud=37.423700, longitud=-5.986623),
            PuntoDeInteres(id=17, nombre="Hospital Real", descripcion="", latitud=37.184937, longitud=-3.601050),
            PuntoDeInteres(id=18, nombre="Capilla Real", descripcion="", latitud=37.176210, longitud=-3.598782),
            PuntoDeInteres(id=19, nombre="Catedral de Granada", descripcion="", latitud=37.176460, longitud=-3.599318),
            PuntoDeInteres(id=20, nombre="Palacio de Carlos V", descripcion="", latitud=37.176776, longitud=-3.590204),
            PuntoDeInteres(id=21, nombre="Casa de los Tiros", descripcion="", latitud=37.174750, longitud=-3.595531),
            PuntoDeInteres(id=22, nombre="Plaza Nueva", descripcion="", latitud=37.176849, longitud=-3.595971),
            PuntoDeInteres(id=23, nombre="Plaza Bib-Rambla", descripcion="", latitud=37.175186, longitud=-3.599798),
            PuntoDeInteres(id=24, nombre="Real Chancillería", descripcion="", latitud=37.177388, longitud=-3.595179),
        ]
    ),

    Ruta(
        id=3,
        nombre="Granada Barroca (siglos XVII-XVIII)",
        descripcion="Arquitectura barroca religiosa de Granada.",
        puntos=[
            PuntoDeInteres(id=25, nombre="Abadía del Sacromonte", descripcion="", latitud=37.183179, longitud=-3.577104),
            PuntoDeInteres(id=26, nombre="Monasterio de la Cartuja", descripcion="", latitud=37.192004, longitud=-3.599302),
            PuntoDeInteres(id=27, nombre="Iglesia del Sagrario", descripcion="", latitud=37.175921, longitud=-3.599036),
            PuntoDeInteres(id=28, nombre="Basílica San Juan de Dios", descripcion="", latitud=37.180974, longitud=-3.602460),
            PuntoDeInteres(id=29, nombre="Iglesia San Justo y Pastor", descripcion="", latitud=37.178940, longitud=-3.601161),
            PuntoDeInteres(id=30, nombre="Basílica Virgen de las Angustias", descripcion="", latitud=37.170830, longitud=-3.595048),
        ]
    ),

    Ruta(
        id=4,
        nombre="Granada Mudéjar",
        descripcion="Edificios cristianos con influencia islámica.",
        puntos=[
            PuntoDeInteres(id=31, nombre="Iglesia de San José", descripcion="", latitud=37.178646, longitud=-3.596156),
            PuntoDeInteres(id=32, nombre="San Gil y Santa Ana", descripcion="", latitud=37.177526, longitud=-3.594460),
            PuntoDeInteres(id=33, nombre="San Cristóbal", descripcion="", latitud=37.183585, longitud=-3.596459),
            PuntoDeInteres(id=34, nombre="San Nicolás", descripcion="", latitud=37.181352, longitud=-3.592519),
            PuntoDeInteres(id=35, nombre="Casa de los Pisa", descripcion="", latitud=37.177719, longitud=-3.595212),
        ]
    ),

    Ruta(
        id=5,
        nombre="Granada del Siglo XIX",
        descripcion="Espacios urbanos del siglo XIX.",
        puntos=[
            PuntoDeInteres(id=36, nombre="Cementerio de San José", descripcion="", latitud=37.16976, longitud=-3.57841),
            PuntoDeInteres(id=37, nombre="Silla del Moro", descripcion="", latitud=37.178364, longitud=-3.583844),
            PuntoDeInteres(id=38, nombre="Paseo del Salón", descripcion="", latitud=37.169266, longitud=-3.594852),
            PuntoDeInteres(id=39, nombre="Ayuntamiento de Granada", descripcion="", latitud=37.174203, longitud=-3.598626),
            PuntoDeInteres(id=40, nombre="Plaza Mariana Pineda", descripcion="", latitud=37.172271, longitud=-3.597137),
        ]
    ),

    Ruta(
        id=6,
        nombre="Granada del Siglo XX",
        descripcion="Arquitectura y urbanismo contemporáneo.",
        puntos=[
            PuntoDeInteres(id=41, nombre="Gran Vía de Colón", descripcion="", latitud=37.182905, longitud=-3.601995),
            PuntoDeInteres(id=42, nombre="Puerta Real", descripcion="", latitud=37.173561, longitud=-3.599572),
            PuntoDeInteres(id=43, nombre="Alhambra Palace", descripcion="", latitud=37.173972, longitud=-3.590134),
            PuntoDeInteres(id=44, nombre="Huerta de San Vicente", descripcion="", latitud=37.170598, longitud=-3.609395),
            PuntoDeInteres(id=45, nombre="Parque de las Ciencias", descripcion="", latitud=37.162706, longitud=-3.605758),
            PuntoDeInteres(id=46, nombre="Centro Federico García Lorca", descripcion="", latitud=37.176618, longitud=-3.600836),
        ]
    ),

    Ruta(
        id=7,
        nombre="Granada Lorquiana",
        descripcion="Lugares vinculados a Federico García Lorca.",
        puntos=[
            PuntoDeInteres(id=47, nombre="Casa Natal Fuente Vaqueros", descripcion="", latitud=37.231675, longitud=-3.745574),
            PuntoDeInteres(id=48, nombre="Casa Museo Valderrubio", descripcion="", latitud=37.232614, longitud=-3.816052),
            PuntoDeInteres(id=49, nombre="Casa de Lorca Acera del Darro", descripcion="", latitud=37.171147, longitud=-3.598585),
            PuntoDeInteres(id=50, nombre="Casa Manuel de Falla", descripcion="", latitud=37.173393, longitud=-3.588671),
            PuntoDeInteres(id=51, nombre="Plaza de los Aljibes", descripcion="", latitud=37.177039, longitud=-3.590944),
        ]
    )

]

# ------------------------
# ENDPOINTS
# ------------------------

@app.get("/")
def inicio():
    return {"mensaje": "API de rutas históricas funcionando 🚀"}

# Obtener todas las rutas
@app.get("/rutas", response_model=List[Ruta])
def obtener_rutas():
    return rutas_db

# Obtener una ruta por ID
@app.get("/rutas/{ruta_id}", response_model=Ruta)
def obtener_ruta(ruta_id: int):
    for ruta in rutas_db:
        if ruta.id == ruta_id:
            return ruta
    raise HTTPException(status_code=404, detail="Ruta no encontrada")

# Obtener puntos de una ruta
@app.get("/rutas/{ruta_id}/puntos", response_model=List[PuntoDeInteres])
def obtener_puntos(ruta_id: int):
    for ruta in rutas_db:
        if ruta.id == ruta_id:
            return ruta.puntos
    raise HTTPException(status_code=404, detail="Ruta no encontrada")

# Crear nueva ruta
@app.post("/rutas", response_model=Ruta)
def crear_ruta(ruta: Ruta):
    rutas_db.append(ruta)
    return ruta

# Añadir punto a una ruta
@app.post("/rutas/{ruta_id}/puntos", response_model=PuntoDeInteres)
def añadir_punto(ruta_id: int, punto: PuntoDeInteres):
    for ruta in rutas_db:
        if ruta.id == ruta_id:
            ruta.puntos.append(punto)
            return punto
    raise HTTPException(status_code=404, detail="Ruta no encontrada")
