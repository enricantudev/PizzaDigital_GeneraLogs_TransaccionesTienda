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
    {"ciudad": "CDMX", "nombre_sucursal": "Xochimilco", "lat": 19.2600, "lon": -99.0900},
    {"ciudad": "Monterrey", "nombre_sucursal": "Morelos", "lat": 25.6667, "lon": -100.3167},
    {"ciudad": "Monterrey", "nombre_sucursal": "Madero Oriente", "lat": 25.6789, "lon": -100.2567},
    {"ciudad": "Monterrey", "nombre_sucursal": "Lincoln", "lat": 25.7250, "lon": -100.3500},
    {"ciudad": "Monterrey", "nombre_sucursal": "Garza Sada", "lat": 25.6133, "lon": -100.2833},
    {"ciudad": "Monterrey", "nombre_sucursal": "Sierra Del Fraile", "lat": 25.6500, "lon": -100.3000},
    {"ciudad": "Monterrey", "nombre_sucursal": "Plaza Real", "lat": 25.7255, "lon": -100.3505},
    {"ciudad": "Monterrey", "nombre_sucursal": "Constitucion PTE", "lat": 25.6660, "lon": -100.3160},
    {"ciudad": "Monterrey", "nombre_sucursal": "Boulevard Acapulco", "lat": 25.6505, "lon": -100.2905},
    {"ciudad": "Monterrey", "nombre_sucursal": "Plaza Barletta", "lat": 25.7000, "lon": -100.3500},
    {"ciudad": "Monterrey", "nombre_sucursal": "Carretera Nacional", "lat": 25.6000, "lon": -100.2500},
    {"ciudad": "Monterrey", "nombre_sucursal": "Pino Suarez", "lat": 25.6665, "lon": -100.3165},
    {"ciudad": "Monterrey", "nombre_sucursal": "Guerrero", "lat": 25.6700, "lon": -100.3200},
    {"ciudad": "Monterrey", "nombre_sucursal": "Solidaridad", "lat": 25.7100, "lon": -100.3400},
    {"ciudad": "Monterrey", "nombre_sucursal": "Aaron Saenz", "lat": 25.6800, "lon": -100.3000},
    {"ciudad": "Monterrey", "nombre_sucursal": "Junco de la Vega", "lat": 25.6500, "lon": -100.2900},
    {"ciudad": "Monterrey", "nombre_sucursal": "Plaza La Rioja", "lat": 25.6005, "lon": -100.2505},
    {"ciudad": "Monterrey", "nombre_sucursal": "Dionisio Gonzalez", "lat": 25.6705, "lon": -100.3205},
    {"ciudad": "Monterrey", "nombre_sucursal": "Puerta de Hierro", "lat": 25.7200, "lon": -100.3500},
    {"ciudad": "Monterrey", "nombre_sucursal": "Plaza Bendetti", "lat": 25.7300, "lon": -100.3600},
    {"ciudad": "Monterrey", "nombre_sucursal": "Cumbres Elite", "lat": 25.7400, "lon": -100.3700},
    {"ciudad":"Guadalajara","nombre_sucursal": "Plaza Alcalde 915", "lat": 20.6935, "lon": -103.3506},
    {"ciudad":"Guadalajara","nombre_sucursal": "Av Revolucion", "lat": 20.6500, "lon": -103.3000},
    {"ciudad":"Guadalajara","nombre_sucursal": "Pablo Neruda", "lat": 20.7000, "lon": -103.4000},
    {"ciudad":"Guadalajara","nombre_sucursal": "Carretera GDL", "lat": 20.6000, "lon": -103.2000},
    {"ciudad":"Guadalajara","nombre_sucursal": "Lopez Cotilla", "lat": 20.6700, "lon": -103.3500},
    {"ciudad":"Guadalajara","nombre_sucursal": "Lopez Mateos", "lat": 20.6500, "lon": -103.4000},
    {"ciudad":"Guadalajara","nombre_sucursal": "Chapultepec Norte", "lat": 20.6700, "lon": -103.3500},
    {"ciudad":"Guadalajara","nombre_sucursal": "Plaza del Norte", "lat": 20.7000, "lon": -103.3500},
    {"ciudad":"Guadalajara","nombre_sucursal": "Cruz del Sur", "lat": 20.6000, "lon": -103.3000},
    {"ciudad":"Guadalajara","nombre_sucursal": "Ruben Dario", "lat": 20.6800, "lon": -103.4000},
    {"ciudad":"Guadalajara","nombre_sucursal": "Adolph Horn", "lat": 20.6000, "lon": -103.3000},
    {"ciudad":"Guadalajara","nombre_sucursal": "Cruz del Sur", "lat": 20.6000, "lon": -103.3000},
    {"ciudad":"Guadalajara","nombre_sucursal": "Vallarta", "lat": 20.6700, "lon": -103.3500},
    {"ciudad":"Guadalajara","nombre_sucursal": "Mariano Otero", "lat": 20.6500, "lon": -103.4000},
    {"ciudad":"Guadalajara","nombre_sucursal": "Robledo", "lat": 20.6500, "lon": -103.3000},
    {"ciudad":"Guadalajara","nombre_sucursal": "Plaza Guadalupe", "lat": 20.6500, "lon": -103.4000},
    {"ciudad":"Guadalajara","nombre_sucursal": "Golfo de Cortez", "lat": 20.7000, "lon": -103.3500},
    {"ciudad":"Guadalajara","nombre_sucursal": "Calzada Oblatos", "lat": 20.6500, "lon": -103.3000},
    {"ciudad":"Guadalajara","nombre_sucursal": "Plaza Morelia", "lat": 20.6000, "lon": -103.2000},
    {"ciudad":"Guadalajara","nombre_sucursal": "Plaza los Santos", "lat": 20.7000, "lon": -103.3500}
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
  # log = f'{{"timestamp":"{fecha_hora.replace("2025-01-28","2025-01-27")}","id_pedido":"{id_pedido}","tipo_pizza":"{tipo_pizza}","tamano":"{tamano}","cantidad":"{cantidad}","metodos_pago":"{metodos_pago}","promociones":"{promociones}","precio":"{precio}",{json.dumps(sucursal).replace("}", "").replace("{", "")}}}'
  log = f'{{"timestamp":"{fecha_hora}","id_pedido":"{id_pedido}","tipo_pizza":"{tipo_pizza}","tamano":"{tamano}","cantidad":"{cantidad}","metodos_pago":"{metodos_pago}","promociones":"{promociones}","precio":"{precio}",{json.dumps(sucursal).replace("}", "").replace("{", "")}}}'

  return log


def escribir_logs(nombre_archivo, num_logs):
  """Escribe logs en el archivo especificado."""

  with open(nombre_archivo, "a") as archivo:
    for _ in range(num_logs):
      log = generar_log_pizza()
      archivo.write(log + "\n")
      print(f"Log generado: {log}") # Imprimir en la consola para verificación
      time.sleep(2)  # Esperar 2 segundos para simular actividad


if __name__ == "__main__":
  nombre_archivo = "C:/Dev/PizzaDigital_GeneraLogs_TransaccionesTienda/Logs/PizzaDigitalTienda.log"
  num_logs = 350  # Número de logs a generar

  escribir_logs(nombre_archivo, num_logs)
  print(f"Se generaron {num_logs} logs en el archivo {nombre_archivo}")