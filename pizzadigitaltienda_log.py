import datetime
import random
import time
import json

def generar_log_pizza():
  """Genera un log de pedido de pizza para Splunk."""

  arrUbicaciones = [
    {"ciudad": "CDMX", "nombre_sucursal": "San Miguel Chapultepec", "lat": 19.4205, "lon": -99.1823},
    {"ciudad": "CDMX", "nombre_sucursal": "Daniel Garza", "lat": 19.4120, "lon": -99.1910},
    {"ciudad": "CDMX", "nombre_sucursal": "Centro", "lat": 19.4270, "lon": -99.1540},
    {"ciudad": "CDMX", "nombre_sucursal": "Irrigacion", "lat": 19.4480, "lon": -99.2110},
    {"ciudad": "CDMX", "nombre_sucursal": "Polanco", "lat": 19.4326, "lon": -99.2000},
    {"ciudad": "CDMX", "nombre_sucursal": "Tlatelolco", "lat": 19.4510, "lon": -99.1390},
    {"ciudad": "CDMX", "nombre_sucursal": "Tacubaya", "lat": 19.4030, "lon": -99.1870},
    {"ciudad": "CDMX", "nombre_sucursal": "Anahuac I Secc", "lat": 19.4450, "lon": -99.1740},
    {"ciudad": "CDMX", "nombre_sucursal": "San Diego Churubusco", "lat": 19.3550, "lon": -99.1410},
    {"ciudad": "CDMX", "nombre_sucursal": "Pantitlan", "lat": 19.4140, "lon": -99.0720},
    {"ciudad": "CDMX", "nombre_sucursal": "Santa Isabel Industrial", "lat": 19.3570, "lon": -99.0730},
    {"ciudad": "CDMX", "nombre_sucursal": "Napoles", "lat": 19.3936, "lon": -99.1745},
    {"ciudad": "CDMX", "nombre_sucursal": "Division del Norte", "lat": 19.3700, "lon": -99.1620},
    {"ciudad": "CDMX", "nombre_sucursal": "Universidad", "lat": 19.3550, "lon": -99.1620},
    {"ciudad": "CDMX", "nombre_sucursal": "Coyoacan", "lat": 19.3500, "lon": -99.1610},
    {"ciudad": "CDMX", "nombre_sucursal": "Santa Ana", "lat": 19.3200, "lon": -99.1300},
    {"ciudad": "CDMX", "nombre_sucursal": "Miramontes", "lat": 19.3000, "lon": -99.1200},
    {"ciudad": "CDMX", "nombre_sucursal": "Cafetales", "lat": 19.2900, "lon": -99.1100},
    {"ciudad": "CDMX", "nombre_sucursal": "Renato Leduc", "lat": 19.2800, "lon": -99.1000},
    {"ciudad": "CDMX", "nombre_sucursal": "Xochimilco", "lat": 19.2600, "lon": -99.0900}
  ]

  _sucursales = ["Roma", "Condesa", "Polanco", "Narvarte"]
  _tipos_pizza = ["Pepperoni", "Hawaiana", "Mexicana", "Vegetariana"]
  _tamanos = ["Chica", "Mediana", "Grande", "Familiar"]
  _metodos_pago = ["Efectivo", "Tarjeta"]
  _promociones = ["2x199","ComboFamiliar","SinPromocion"]

  sucursal = random.choice(arrUbicaciones)
  tipo_pizza = random.choice(_tipos_pizza)
  tamano = random.choice(_tamanos)
  cantidad = random.randint(1, 5)
  # precio = random.randint(150, 400)
  id_pedido = random.randint(1, 99999)
  fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  tamano = random.choice(_tamanos)
  metodos_pago = random.choice(_metodos_pago)
  promociones = random.choice(_promociones)

  precio = 0
  tam_chica = 99
  tam_mediana = 149
  tam_grande = 199
  tam_familiar = 249

  # Si no hay promoción, asignar precios basados en la promoción
  if promociones == "2x199":
      precio = 199
      cantidad = 1
  elif promociones == "ComboFamiliar":
      precio = 399
      cantidad = 1
  else:
      # Si no hay promoción válida, asigna un precio por defecto
      # Aquí asignas el precio normal sin promoción
      if tamano == "Chica":
          precio = tam_chica * cantidad
      elif tamano == "Mediana":
          precio = tam_mediana * cantidad
      elif tamano == "Grande":
          precio = tam_grande * cantidad
      elif tamano == "Familiar":
          precio = tam_familiar * cantidad

  # log = f"{fecha_hora}|{id_pedido}|{sucursal}|{tipo_pizza}|{tamano}|{cantidad}|{metodos_pago}|{promociones}|{precio}"
  # log = '{"ubicaion":"'+sucursal+'","timestamp":"'+fecha_hora+'","id_pedido":"'+str(id_pedido)+'","tipo_pizza":"'+tipo_pizza+'","tamano":"'+tamano+'","cantidad":"'+str(cantidad)+'","metodos_pago":"'+metodos_pago+'","promociones":"'+promociones+'","precio":"'+str(precio)+'"}'
  log = f'{{"timestamp":"{fecha_hora}","id_pedido":"{id_pedido}","tipo_pizza":"{tipo_pizza}","tamano":"{tamano}","cantidad":"{cantidad}","metodos_pago":"{metodos_pago}","promociones":"{promociones}","precio":"{precio}",{json.dumps(sucursal).replace("}", "").replace("{", "")}}}'

  return log


def escribir_logs(nombre_archivo, num_logs):
  """Escribe logs en el archivo especificado."""

  with open(nombre_archivo, "a") as archivo:
    for _ in range(num_logs):
      log = generar_log_pizza()
      archivo.write(log + "\n")
      print(f"Log generado: {log}") # Imprimir en la consola para verificación
      time.sleep(0)  # Esperar 2 segundos para simular actividad


if __name__ == "__main__":
  nombre_archivo = "C:/Dev/MasterInnovation-20241213T143052Z-001/MasterInnovation/PizzaDigitalTienda.log"
  num_logs = 500  # Número de logs a generar

  escribir_logs(nombre_archivo, num_logs)
  print(f"Se generaron {num_logs} logs en el archivo {nombre_archivo}")