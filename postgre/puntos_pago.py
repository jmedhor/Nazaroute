from database import SessionLocal
from models import Punto

db = SessionLocal()

def generar_url(nombre):
    return "https://es.wikipedia.org/wiki/" + nombre.replace(" ", "_").replace("(", "").replace(")", "")

# IDs de puntos que normalmente son de pago
puntos_pago = {
    8,   # Bañuelo
    15, 16, 17, 18, 19, 20, 23, 24, 27, 29,
    32, 34, 35, 37, 39, 40, 47,
    50, 51, 54, 57,
    67,
    80, 82, 83, 85, 86, 87,
    88, 89
}

puntos = db.query(Punto).all()

for punto in puntos:
    # Pago
    punto.pago = punto.id in puntos_pago

    # URL
    punto.url = generar_url(punto.nombre)

db.commit()
db.close()

print("✅ Puntos actualizados con pago y URL")
