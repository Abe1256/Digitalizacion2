import datetime
import json
import os
import time
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

class AsistenteProductividadContextual:
    def __init__(self):
        self.ubicacion_actual = None
        self.hora_actual = None
        self.actividades = []
        self.configuracion = self.cargar_configuracion()

    def cargar_configuracion(self):
        if os.path.exists('config.json'):
            with open('config.json', 'r') as f:
                return json.load(f)
        else:
            return {
                "ubicaciones": {},
                "horarios_productivos": {"inicio": "09:00", "fin": "17:00"},
                "actividades": []
            }

    def guardar_configuracion(self):
        with open('config.json', 'w') as f:
            json.dump(self.configuracion, f)

    def actualizar_ubicacion(self):
        geolocator = Nominatim(user_agent="AsistenteProductividadContextual")
        location = geolocator.geocode(input("Ingresa tu ubicación actual: "))
        if location:
            self.ubicacion_actual = (location.latitude, location.longitude)
            print(f"Ubicación actualizada: {location.address}")
        else:
            print("No se pudo encontrar la ubicación.")

    def actualizar_hora(self):
        self.hora_actual = datetime.datetime.now().time()

    def agregar_actividad(self):
        actividad = input("Ingresa una nueva actividad: ")
        hora = input("Ingresa la hora de la actividad (HH:MM): ")
        self.configuracion["actividades"].append({"actividad": actividad, "hora": hora})
        self.guardar_configuracion()

    def verificar_productividad(self):
        self.actualizar_hora()
        hora_inicio = datetime.datetime.strptime(self.configuracion["horarios_productivos"]["inicio"], "%H:%M").time()
        hora_fin = datetime.datetime.strptime(self.configuracion["horarios_productivos"]["fin"], "%H:%M").time()

        if hora_inicio <= self.hora_actual <= hora_fin:
            print("Estás en horario productivo. ¡Enfócate en tus tareas!")
        else:
            print("Estás fuera del horario productivo. Tómate un descanso si lo necesitas.")

    def verificar_ubicacion(self):
        if self.ubicacion_actual:
            for nombre, coords in self.configuracion["ubicaciones"].items():
                distancia = geodesic(self.ubicacion_actual, coords).meters
                if distancia < 100:  # Si está a menos de 100 metros
                    print(f"Estás cerca de {nombre}. Ajusta tu enfoque según corresponda.")
                    return
            print("No estás cerca de ninguna ubicación conocida.")
        else:
            print("Ubicación no disponible.")

    def verificar_actividades(self):
        self.actualizar_hora()
        for actividad in self.configuracion["actividades"]:
            hora_actividad = datetime.datetime.strptime(actividad["hora"], "%H:%M").time()
            if self.hora_actual.hour == hora_actividad.hour and self.hora_actual.minute == hora_actividad.minute:
                print(f"¡Es hora de tu actividad: {actividad['actividad']}!")

    def ejecutar(self):
        while True:
            self.verificar_productividad()
            self.verificar_ubicacion()
            self.verificar_actividades()
            time.sleep(60)  # Espera 1 minuto antes de la próxima verificación

if __name__ == "__main__":
    asistente = AsistenteProductividadContextual()
    asistente.actualizar_ubicacion()
    asistente.ejecutar()
