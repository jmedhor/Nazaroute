from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="API Rutas Históricas Granada")

# Main ordenado por rutas, repitiendo 10 puntos

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
            PuntoDeInteres(id=4, nombre="Puerta del León", descripcion="", latitud=37.180912204679835, longitud=-3.5981591195633325),
            PuntoDeInteres(id=5, nombre="Puerta del Castro", descripcion="", latitud=37.18192752185929, longitud=-3.5929428694722967),
            PuntoDeInteres(id=6, nombre="Puerta de Monaita", descripcion="", latitud=37.182046, longitud=-3.597612),
            PuntoDeInteres(id=7, nombre="Iglesia de San José (alminar)", descripcion="", latitud=37.178663, longitud=-3.596172),
            PuntoDeInteres(id=8, nombre="El Bañuelo", descripcion="", latitud=37.178488, longitud=-3.592991),
            PuntoDeInteres(id=9, nombre="Torres Bermejas (castillo)", descripcion="", latitud=37.175526, longitud=-3.593412),

            PuntoDeInteres(id=10, nombre="Alcázar Genil", descripcion="", latitud=37.164720, longitud=-3.600530),
            PuntoDeInteres(id=11, nombre="Ermita de San Sebastián (antiguo morabito)", descripcion="", latitud=37.166295, longitud=-3.600021),
            PuntoDeInteres(id=12, nombre="Iglesia de San Juan de los Reyes (alminar)", descripcion="", latitud=37.179963, longitud=-3.591829),
            PuntoDeInteres(id=13, nombre="Iglesia de San Salvador (patio almohade)", descripcion="", latitud=37.18233409412579, longitud=-3.590666430403682),

            PuntoDeInteres(id=14, nombre="Cuarto Real de Santo Domingo", descripcion="", latitud=37.171700, longitud=-3.594911),
            PuntoDeInteres(id=15, nombre="Alcazaba (Alhambra)", descripcion="", latitud=37.177133, longitud=-3.591810),

            PuntoDeInteres(id=16, nombre="Corral del Carbón", descripcion="", latitud=37.174936, longitud=-3.597878),
            PuntoDeInteres(id=17, nombre="Palacios Nazaríes (Alhambra)", descripcion="", latitud=37.177383, longitud=-3.589630),
            PuntoDeInteres(id=18, nombre="Generalife (Alhambra)", descripcion="", latitud=37.176954, longitud=-3.585218),
            PuntoDeInteres(id=19, nombre="Puerta del Vino", descripcion="", latitud=37.176674, longitud=-3.590740),
            PuntoDeInteres(id=20, nombre="Puerta de los Siete Suelos", descripcion="", latitud=37.174780, longitud=-3.586738),
            PuntoDeInteres(id=21, nombre="La Madraza", descripcion="", latitud=37.17620994586816, longitud=-3.5980291531568094),
            PuntoDeInteres(id=22, nombre="Maristán", descripcion="", latitud=37.178727, longitud=-3.592840),
            PuntoDeInteres(id=23, nombre="Palacio de Dar al-Horra", descripcion="", latitud=37.181625, longitud=-3.596362),
            PuntoDeInteres(id=24, nombre="Dar al-Arusa", descripcion="", latitud=37.176449, longitud=-3.580661),
            PuntoDeInteres(id=25, nombre="Puerta de Bib Rambla", descripcion="", latitud=37.175545, longitud=-3.589992),
            PuntoDeInteres(id=26, nombre="Torre del Aceituno (San Miguel Alto)", descripcion="", latitud=37.184978088173416, longitud=-3.5874613339487915),
            PuntoDeInteres(id=27, nombre="Convento de San Francisco (casa de nobleza nazarí)", descripcion="", latitud=37.17584422292137, longitud=-3.587041628269308),
            PuntoDeInteres(id=28, nombre="Casa del Chapiz", descripcion="", latitud=37.180980, longitud=-3.588364),
            PuntoDeInteres(id=29, nombre="Casa de Zafra", descripcion="", latitud=37.178851, longitud=-3.592543),
            PuntoDeInteres(id=30, nombre="Casa del Cuerno de Oro", descripcion="", latitud=37.17980923127883, longitud=-3.5893071709512836),
            PuntoDeInteres(id=31, nombre="Alcaicería", descripcion="", latitud=37.175370, longitud=-3.599195),
        ]
    ),

    Ruta(
        id=2,
        nombre="Granada Cristiana e Imperial (siglos XV-XVI)",
        descripcion="Monumentos tras la conquista cristiana.",
        puntos=[
            PuntoDeInteres(id=32, nombre="Monasterio de San Jerónimo", descripcion="", latitud=37.17948576559224, longitud=-3.6035622285515676),
            PuntoDeInteres(id=33, nombre="Convento de San Francisco", descripcion="", latitud=37.17584422292137, longitud=-3.587041628269308),
            PuntoDeInteres(id=34, nombre="Convento de Santa Isabel la Real", descripcion="", latitud=37.181112, longitud=-3.596089),
            PuntoDeInteres(id=35, nombre="Hospital Real de Granada", descripcion="", latitud=37.184937, longitud=-3.601050),
            PuntoDeInteres(id=36, nombre="Capilla Real de Granada", descripcion="", latitud=37.176210, longitud=-3.598782),
            PuntoDeInteres(id=37, nombre="Lonja de Granada", descripcion="", latitud=37.176024, longitud=-3.598602),
            PuntoDeInteres(id=38, nombre="Catedral de Granada", descripcion="", latitud=37.176460, longitud=-3.599318),
            PuntoDeInteres(id=39, nombre="Iglesia de San Matías", descripcion="", latitud=37.173680, longitud=-3.596510),
            PuntoDeInteres(id=40, nombre="Palacio de Carlos V", descripcion="", latitud=37.176776, longitud=-3.590204),
            PuntoDeInteres(id=41, nombre="Casa de los Tiros", descripcion="", latitud=37.174750, longitud=-3.595531),
            PuntoDeInteres(id=42, nombre="Puerta de las Granadas", descripcion="", latitud=37.176039, longitud=-3.593074),
            PuntoDeInteres(id=43, nombre="Pilar de Carlos V", descripcion="", latitud=37.175866, longitud=-3.590072),
            PuntoDeInteres(id=44, nombre="Plaza Nueva", descripcion="", latitud=37.176849, longitud=-3.595971),
            PuntoDeInteres(id=45, nombre="Plaza de Bib-Rambla", descripcion="", latitud=37.175186, longitud=-3.599798),
            PuntoDeInteres(id=46, nombre="Palacio Arzobispal", descripcion="", latitud=37.175716, longitud=-3.599616),
            PuntoDeInteres(id=47, nombre="Iglesia de Santo Domingo", descripcion="", latitud=37.172964, longitud=-3.594482),
            PuntoDeInteres(id=48, nombre="Palacio de los Córdova", descripcion="", latitud=37.179798, longitud=-3.587165),
            PuntoDeInteres(id=49, nombre="Palacio de la Madraza (Ayuntamiento Viejo)", descripcion="", latitud=37.176086, longitud=-3.598151),
            PuntoDeInteres(id=50, nombre="Real Chancillería", descripcion="", latitud=37.177388373872965, longitud=-3.59517927828838),
        ]
    ),

    Ruta(
        id=3,
        nombre="Granada Barroca (siglos XVII-XVIII)",
        descripcion="Arquitectura barroca religiosa de Granada.",
        puntos=[
            PuntoDeInteres(id=51, nombre="Abadía del Sacromonte", descripcion="", latitud=37.183179, longitud=-3.577104),
            PuntoDeInteres(id=52, nombre="Monasterio de la Cartuja", descripcion="", latitud=37.192004, longitud=-3.599302),
            PuntoDeInteres(id=53, nombre="Iglesia del Sagrario", descripcion="", latitud=37.175921, longitud=-3.599036),
            PuntoDeInteres(id=54, nombre="Catedral de Granada", descripcion="", latitud=37.176464, longitud=-3.599307),
            PuntoDeInteres(id=55, nombre="Iglesia de San Justo y Pastor", descripcion="", latitud=37.17894056750491, longitud=-3.6011619610919987),
            PuntoDeInteres(id=56, nombre="Basílica y monasterio de San Juan de Dios", descripcion="", latitud=37.18097496132773, longitud=-3.60246015036501),
            PuntoDeInteres(id=57, nombre="Iglesia de Nuestra Señora del Perpetuo Socorro", descripcion="", latitud=37.17995177410415, longitud=-3.602287287646482),
            PuntoDeInteres(id=58, nombre="Iglesia de San Miguel Alto", descripcion="", latitud=37.18512760804898, longitud=-3.5871012745837176),
            PuntoDeInteres(id=59, nombre="Basílica de Nuestra Señora de las Angustias", descripcion="", latitud=37.170830991767794, longitud=-3.5950482403968214),
            PuntoDeInteres(id=60, nombre="Iglesia del Corpus Christi", descripcion="", latitud=37.156888084262015, longitud=-3.595533981516573),
            PuntoDeInteres(id=61, nombre="Colegio de San Pablo", descripcion="", latitud=37.17766255375001, longitud=-3.6017550128890203),
        ]
    ),

    Ruta(
        id=4,
        nombre="Granada Mudéjar",
        descripcion="Edificios cristianos con influencia islámica.",
        puntos=[
            PuntoDeInteres(id=62, nombre="Iglesia de San José", descripcion="", latitud=37.178646, longitud=-3.596156),
            PuntoDeInteres(id=63, nombre="Iglesia de San Gil y Santa Ana", descripcion="", latitud=37.177526, longitud=-3.594460),
            PuntoDeInteres(id=64, nombre="Iglesia de San Cristóbal", descripcion="", latitud=37.183585, longitud=-3.596459),
            PuntoDeInteres(id=65, nombre="Iglesia de San Miguel Bajo", descripcion="", latitud=37.180681, longitud=-3.596714),
            PuntoDeInteres(id=66, nombre="Iglesia de San Ildefonso", descripcion="", latitud=37.183841, longitud=-3.599356),
            PuntoDeInteres(id=67, nombre="Iglesia de San Andrés", descripcion="", latitud=37.181138, longitud=-3.599313),
            PuntoDeInteres(id=68, nombre="Iglesia de San Nicolás", descripcion="", latitud=37.181352, longitud=-3.592519),
            PuntoDeInteres(id=69, nombre="Casa de los Tiros", descripcion="", latitud=37.174752, longitud=-3.595528),
            PuntoDeInteres(id=70, nombre="Casa del Chapiz", descripcion="", latitud=37.180980, longitud=-3.588369),
            PuntoDeInteres(id=71, nombre="Palacio de los Córdova", descripcion="", latitud=37.179794, longitud=-3.587157),
            PuntoDeInteres(id=72, nombre="Casa de los Pisa", descripcion="", latitud=37.177719, longitud=-3.595212),
        ]
    ),

    Ruta(
        id=5,
        nombre="Granada del Siglo XIX",
        descripcion="Espacios urbanos del siglo XIX.",
        puntos=[
            PuntoDeInteres(id=73, nombre="Cementerio de San José", descripcion="", latitud=37.16976, longitud=-3.57841),
            PuntoDeInteres(id=74, nombre="Silla del Moro", descripcion="", latitud=37.178364, longitud=-3.583844),
            PuntoDeInteres(id=75, nombre="Calle Reyes Católicos", descripcion="", latitud=37.175390302152024, longitud=-3.5981201969560614),
            PuntoDeInteres(id=76, nombre="Puente Verde", descripcion="", latitud=37.167246, longitud=-3.589450),
            PuntoDeInteres(id=77, nombre="Paseo del Salón", descripcion="", latitud=37.169266, longitud=-3.594852),
            PuntoDeInteres(id=78, nombre="Ayuntamiento de Granada", descripcion="", latitud=37.174203, longitud=-3.598626),
            PuntoDeInteres(id=79, nombre="Plaza de Mariana Pineda", descripcion="", latitud=37.172271, longitud=-3.597137),
            PuntoDeInteres(id=80, nombre="Carmen de los Mártires", descripcion="", latitud=37.172741, longitud=-3.585955),
            PuntoDeInteres(id=81, nombre="Casa de Mariana Pineda", descripcion="", latitud=37.17312648972883, longitud=-3.603095190914233),
            PuntoDeInteres(id=82, nombre="Universidad de Granada (Colegio de San Pablo)", descripcion="", latitud=37.17766255375001, longitud=-3.6017550128890203),
            PuntoDeInteres(id=83, nombre="Plaza Nueva", descripcion="", latitud=37.176849, longitud=-3.595971),
        ]
    ),

    Ruta(
        id=6,
        nombre="Granada del Siglo XX",
        descripcion="Arquitectura y urbanismo contemporáneo.",
        puntos=[
            PuntoDeInteres(id=84, nombre="Gran Vía de Colón", descripcion="", latitud=37.182905, longitud=-3.601995),
            PuntoDeInteres(id=85, nombre="Gobierno Civil de Granada", descripcion="", latitud=37.178194265424885, longitud=-3.602791870015424),
            PuntoDeInteres(id=86, nombre="Puerta Real", descripcion="", latitud=37.173561725394485, longitud=-3.599572643063466),
            PuntoDeInteres(id=87, nombre="Alhambra Palace", descripcion="", latitud=37.173972, longitud=-3.590134),
            PuntoDeInteres(id=88, nombre="Iglesia del Sagrado Corazón", descripcion="", latitud=37.178864, longitud=-3.598873),
            PuntoDeInteres(id=89, nombre="Fundación Rodríguez-Acosta", descripcion="", latitud=37.175017, longitud=-3.592642),
            PuntoDeInteres(id=90, nombre="Huerta de San Vicente", descripcion="", latitud=37.170598, longitud=-3.609395),
            PuntoDeInteres(id=91, nombre="Calle Ángel Ganivet", descripcion="", latitud=37.173258, longitud=-3.598867),
            PuntoDeInteres(id=92, nombre="Parque de las Ciencias", descripcion="", latitud=37.162706, longitud=-3.605758),
            PuntoDeInteres(id=93, nombre="Museo Caja Granada", descripcion="", latitud=37.162354, longitud=-3.607992),
            PuntoDeInteres(id=94, nombre="Centro Federico García Lorca", descripcion="", latitud=37.176618, longitud=-3.600836),
        ]
    ),

    Ruta(
        id=7,
        nombre="Granada Lorquiana",
        descripcion="Lugares vinculados a Federico García Lorca.",
        puntos=[
            PuntoDeInteres(id=95, nombre="Casa Natal de Federico García Lorca (Fuente Vaqueros)", descripcion="", latitud=37.23167511184424, longitud=-3.745574166464271),
            PuntoDeInteres(id=96, nombre="Casa Museo Federico García Lorca (Valderrubio)", descripcion="", latitud=37.232614794741515, longitud=-3.816052205270329),
            PuntoDeInteres(id=97, nombre="Casa de Federico García Lorca (Acera del Darro)", descripcion="", latitud=37.171147858880914, longitud=-3.598585448543979),
            PuntoDeInteres(id=98, nombre="Casa de Federico García Lorca (Acera del Casino)", descripcion="", latitud=37.17235400853699, longitud=-3.59865469484417),
            PuntoDeInteres(id=99, nombre="Universidad de Granada - Facultad de Derecho", descripcion="", latitud=37.17830648990943, longitud=-3.601361359239792),
            PuntoDeInteres(id=100, nombre="Café Alameda", descripcion="", latitud=37.172374501702855, longitud=-3.598032443795111),
            PuntoDeInteres(id=101, nombre="Casa de Emilia Llanos", descripcion="", latitud=37.175040356145495, longitud=-3.5950595148767492),
            PuntoDeInteres(id=102, nombre="Casa de Manuel de Falla", descripcion="", latitud=37.17339366712911, longitud=-3.588671774442353),
            PuntoDeInteres(id=103, nombre="Plaza de los Aljibes", descripcion="", latitud=37.177039, longitud=-3.590944),
            PuntoDeInteres(id=104, nombre="Alhambra Palace", descripcion="", latitud=37.17405542387176, longitud=-3.590013100182198),
            PuntoDeInteres(id=105, nombre="Huerta de San Vicente", descripcion="", latitud=37.1706635975692, longitud=-3.6092696028937428),
            PuntoDeInteres(id=106, nombre="Casa de los Rosales", descripcion="", latitud=37.17619, longitud=-3.60261),
            PuntoDeInteres(id=107, nombre="Colonia de Víznar", descripcion="", latitud=37.23576126427313, longitud=-3.5495360402471894),
            PuntoDeInteres(id=108, nombre="Barranco de Víznar", descripcion="", latitud=37.240233674057556, longitud=-3.5432997438936797),
            PuntoDeInteres(id=109, nombre="Antiguo Gobierno Civil de Granada", descripcion="", latitud=37.180848905975324, longitud=-3.605540563857002),
            PuntoDeInteres(id=110, nombre="Centro Federico García Lorca", descripcion="", latitud=37.176622, longitud=-3.600833),
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
