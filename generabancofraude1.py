# Generajson.py  Gerardo Maya                                     - gmaya@splunk.com
#
#  Generador de datos para demo de fraude en ATM.
#
# Crea un archivo llamado healthcare.txt que contiene eventos de dispositivos medicos.
# Debe crear un entrada de datos para este archivo en su instancia de Splunk.
#     monitor:// 
#

import time, datetime, os, sys, random, re


filename = "bancotx.log"
filename1 = "biocatch.log"
filename2 = "rsa_token.log"
filename3 = "truId.log"
debug = False

###
### Valida por argumentos 
###
for arg in sys.argv:
   if (arg == "--debug"):
      debug = True


###
###  Definicion de datos validos
###
noCuentas = ["3767-123456-09120","3767-123456-10121","3767-123456-10122","3767-123456-09123","3767-123456-09124","3767-123456-09125",
             "3769-654321-08126","3769-654321-08127","3767-654321-08128","3768-654321-08129","3769-654321-08130","3768-654321-08131",
             "3767-123456-06132","3767-123456-06133","3767-123456-06134","3768-123456-06135","3769-123456-06136","3768-123456-06137",
             "3769-654321-07138","3769-654321-07139","3767-654321-07140","3768-654321-07141","3769-654321-07142","3768-654321-07143",
             "3768-123456-08144","3768-123456-08145","3767-123456-08146","3768-123456-08147","3769-123456-08148","3768-123456-08149"]

noClientes = ["12341908","12341909","12341910","12341911"]
ClientesFzaBruta = ["89341201","89431209","89430110"]
imeiClientes = ["89520009087001024","89520009087001026","89520009087001028","89520009087001030"]
direccionIPS = ["10.10.20.1","10.10.20.2","10.10.20.3","10.10.20.4"]
direccionMX = "189.209.64."
direccionBR = "2.18.126."
deviceIDS = ["01AE901","02F3210","03RAC01","04BA00F"]
badIDS = ["BOT0069","BOT0067","BOT0013","BOT0007"]
statuses = ["200","200","503","200","503","200"]
boleanos = ["true","false"]
biocatch_status = ["200","503","200","200","200","503","200","200","200","200"]
biocatch_reasons = [', reason=deviceOrientationFail', ', reason=reallyFastStrokeKeys', ', reason=UserLanguaje=NotRecognized']
tipoFraudes=["fuerzaBruta","loginFails", "multiplesAccesos", "loginFails", "fuerzaBruta", "multiplesAccesos"]

digitos=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
session_acts = ["inicioSesion","consultaCuentas","operacion","finSesion"]
#operaciones = ["creaCuenta","speiTX"]
operaciones = ["createAccount","speiTX","depositoMismaCuenta","pagoServicios"]
servicios = ["TELMEX","Totalplay","NetFlix","Uber"]
long = 16
i=0
sessionID=""
loop=True
esFraude=False

while (loop):
   ####
   #### Abre el archivo y agrega nuevos datos (append)
   ####
   if(debug == False):
      theFile = open(('./Logs/'+filename), 'a')
      theFile1 = open(('./Logs/'+filename1), 'a')
      theFile2 = open(('./Logs/'+filename2), 'a')
      theFile3 = open(('./Logs/'+filename3), 'a')

   ###
   ### Genera SessionID
   ###
   sessionID=""
   i=0
   while (i<long):
      sessionID=sessionID+digitos[random.randint(0,len(digitos)-1)]
      i+=1

   i=0
   while (i<len(session_acts)):
      sessionActivity=session_acts[i]
      parametro=""

      if (sessionActivity=="inicioSesion"):
         ###
         ### Se selecciona un cliente aleatorio
         ###
         selCliente=random.randint(0,len(noClientes)-1)
         ###
         ### Del cliente se toman sus datos noCliente, direccionIP, deviceID
         ###
         cliente=noClientes[selCliente]
         direccionIP=direccionIPS[selCliente]
         deviceID=deviceIDS[selCliente]
         imeiCliente=imeiClientes[selCliente]
         ###
         ### Se valida el acceso si exitoso o fallido (503)
         ###
         status = statuses[random.randint(0,len(statuses)-1)]
         ultimoOcteto = random.randint(120,245)
         direccionIP = direccionMX+str(ultimoOcteto)
         parametro='"noCliente":"'+cliente+'", '+'"status":"'+status+'" ,"direccionIP":"'+direccionIP+'", "deviceID":"'+deviceID+'" '
         ###
         ### Durante la autenticacion se generan eventos de BioCatch y RSA
         ### Si falla la autenticacion, sale
         ###

         minuto = datetime.datetime.now().minute

         ###
         ### Se generan eventos fraudulentos cada 10 minutos
         ###
         if (minuto%10==0):
            esFraude=True
            tipoFraude=tipoFraudes[random.randint(0,len(tipoFraudes)-1)]
         else:
            esFraude=False
          

         if (status=="503"):
            i=100
         else:
            ###
            ### Genera log de BioCatch
            ###
            status=biocatch_status[random.randint(0,len(biocatch_status)-1)]
            biocatchRisk=random.randint(0,100)
            if (biocatchRisk>75):
               reason=biocatch_reasons[random.randint(0,len(biocatch_reasons)-1)]
            else:
               reason=""
            line1 = datetime.datetime.today().strftime('%Y/%m/%d %H:%M:%S')+" api.biocatch, customerID=BCATCH090899, deviceID="+deviceID+", riskFactor="+str(biocatchRisk)+", status="+status+reason+" \n"
  
            if (debug):
               print(line1)
            else:
               theFile1.write(line1)
               theFile1.close()

            ###
            ### Genera logs de token
            ###
            noIntentos = random.randint(1,10)

            ###
            ### Si es par siempre autentica al primer intento
            ###
            if (noIntentos%2):
               noIntentos=1
            if (noIntentos>1):
               rsaRisk=noIntentos*3
               time.sleep(random.randint(2,8))
            else:
               rsaRisk=0
            time.sleep(random.randint(0,2))
            line2 = '{"timestamp":"'+datetime.datetime.today().strftime('%Y/%m/%d %H:%M:%S')+'", "deviceID":"'+deviceID+'", "rsaRisk": "'+str(rsaRisk)+'", "loginAttempts":"'+str(noIntentos)+'"}\n'
            if (debug):
               print(line2)
            else:
               theFile2.write(line2)
               theFile2.close()


            ###
            ### Genera TruID events
            ###
            time.sleep(random.randint(0,2))
            j=0
            sessionID=""
            while (j<16):
               sessionID=sessionID+digitos[random.randint(0,len(digitos)-1)]
               j=j+1

            boleano = boleanos[random.randint(0,1)]
            totalCalls = random.randint(0,50)
            totalSMSs = random.randint(20,150)

            line3 = '{"truID.API.sessionID":"'+sessionID+'", "timestamp":"'+datetime.datetime.today().strftime('%Y/%m/%d %H:%M:%S')+'", "deviceID":"'+deviceID+'", "isValidNumber": "'+boleano+'", "totalCalls":"'+str(totalCalls)+'", "SMSsent":"'+str(totalSMSs)+'"}\n'
            if (debug):
               print(line3)
            else:
               theFile3.write(line3)
               theFile3.close()


      ###
      ### En el campo parametro se crea el evento (autenticacion, operacion, speiTX, etc)
      ###
      ### operaciones = ["createAccount","speiTX","depositoMismaCuenta","pagoServicios"]

      if (sessionActivity=="operacion"):
         sessionActivity=operaciones[random.randint(0,len(operaciones)-1)]
         parametro='"sessionActivity":"'+sessionActivity+'", '

      if (sessionActivity=="speiTX"):
         monto=25*random.randint(1,30)
         cuenta=noCuentas[random.randint(0,len(noCuentas)-1)]
         parametro='"monto":"'+str(monto)+'.00"'+', "cuentaDestino":"'+cuenta+'"'
                  
      if (sessionActivity=="depositoMismaCuenta"):
         monto=25*random.randint(1,30)
         cuenta=noCuentas[random.randint(0,len(noCuentas)-1)]
         parametro='"monto":"'+str(monto)+'.00"'+', "cuentaDestino":"'+cuenta+'"'
                  
      if (sessionActivity=="pagoServicios"):
         monto=25*random.randint(1,30)
         servicio=servicios[random.randint(0,len(servicios)-1)]
         parametro='"monto":"'+str(monto)+'.00"'+', "servicio":"'+servicio+'"'
                  
      if (sessionActivity=="createAccount"):
         cuenta=noCuentas[random.randint(0,len(noCuentas)-1)]
         parametro=' "cuentaDestino":"'+cuenta+'"'
            
      if (sessionActivity=="consultaCuentas"):
         parametro='"cliente":"'+cliente+'"'
                  
      if (sessionActivity=="finSesion"):
         parametro='"cliente":"'+cliente+'"'
            
      line='{"timestamp":"'+datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')+'", "sessionID":"'+ sessionID+'", '+'"sessionActivity":"'+sessionActivity+'", '+parametro+'} \n'

      if (debug):
         print(line)
      else:
         theFile.write(line)
      
      ###
      ### Si es fraude, genera eventos maliciosos
      ###
      if (esFraude):
         print("Fraude: "+tipoFraude)
         if (tipoFraude=="loginFails"):
            fallos=random.randint(3,6)
            loginFail=0
            ultimoOcteto = random.randint(120,245)
            direccionIP = direccionMX+str(ultimoOcteto)
            while (loginFail<fallos):
               ###
               ### Genera una nueva sesion por cada login fallido
               ###
               s=0
               sessionID=""
               while (s<16):
                  sessionID=sessionID+digitos[random.randint(0,len(digitos)-1)]
                  s=s+1
               status = "503"
               parametro='"noCliente":"'+cliente+'", '+'"status":"'+status+'" ,"direccionIP":"'+direccionIP+'", "deviceID":"'+deviceID+'" '

               line='{"timestamp":"'+datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')+'", "sessionID":"'+ sessionID+'", '+'"sessionActivity":"'+sessionActivity+'", '+parametro+'} \n'
               time.sleep(random.randint(0,3))
               loginFail = loginFail+1

               if (debug):
                  print(line)
               else:
                  theFile.write(line)
      
         esFraude=False

         if (tipoFraude=="fuerzaBruta"):
            fallos=random.randint(4,10)
            loginFail=0
            ultimoOcteto = random.randint(120,245)
            direccionIP = direccionMX+str(ultimoOcteto)
            cliente=ClientesFzaBruta[random.randint(0,len(ClientesFzaBruta)-1)]
            
            while (loginFail<fallos):
               ###
               ### Genera una nueva sesion por cada login fallido
               ###
               s=0
               sessionID=""
               while (s<16):
                  sessionID=sessionID+digitos[random.randint(0,len(digitos)-1)]
                  s=s+1
               status = "503"
               parametro='"noCliente":"'+cliente+'", '+'"status":"'+status+'" ,"direccionIP":"'+direccionIP+'", "deviceID":"'+deviceID+'" '

               line='{"timestamp":"'+datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')+'", "sessionID":"'+ sessionID+'", '+'"sessionActivity":"'+sessionActivity+'", '+parametro+'} \n'
               time.sleep(random.randint(0,3))
               loginFail = loginFail+1

               if (debug):
                  print(line)
               else:
                  theFile.write(line)

               time.sleep(random.randint(0,7))
      
            ###
            ### Generando acceso Exitoso
            ###
            s=0
            sessionID=""
            while (s<16):
               sessionID=sessionID+digitos[random.randint(0,len(digitos)-1)]
               s=s+1
            status = "200"
            parametro='"noCliente":"'+cliente+'", '+'"status":"'+status+'" ,"direccionIP":"'+direccionIP+'", "deviceID":"'+deviceID+'" '

            time.sleep(random.randint(0,7))
            line='{"timestamp":"'+datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')+'", "sessionID":"'+ sessionID+'", '+'"sessionActivity":"'+sessionActivity+'", '+parametro+'} \n'
            time.sleep(random.randint(0,3))

            if (debug):
               print(line)
            else:
               theFile.write(line)


         esFraude=False
         if (tipoFraude=="multiplesAccesos"):
            totalAccesos=random.randint(2,4)
            accesos=0
            while (accesos<totalAccesos):
               ###
               ### Genera una nueva sesion por cada accesso
               ###
               s=0
               sessionID=""
               while (s<16):
                  sessionID=sessionID+digitos[random.randint(0,len(digitos)-1)]
                  s=s+1
               status = "200"
               ultimoOcteto = random.randint(120,245)
               cambioPais=random.randint(1,120)
               if (cambioPais%2==0):
                  direccionIP = direccionMX+str(ultimoOcteto)
               else:
                  direccionIP = direccionBR+str(ultimoOcteto)
                  deviceID=badIDS[random.randint(0,len(badIDS)-1)]
                  
               parametro='"noCliente":"'+cliente+'", '+'"status":"'+status+'" ,"direccionIP":"'+direccionIP+'", "deviceID":"'+deviceID+'" '

               line='{"timestamp":"'+datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')+'", "sessionID":"'+ sessionID+'", '+'"sessionActivity":"'+sessionActivity+'", '+parametro+'} \n'
               time.sleep(random.randint(0,3))
               accesos = accesos+1

               if (debug):
                  print(line)
               else:
                  theFile.write(line)
      
         esFraude=False
      

      ###
      ### Tiempo de espera
      ###
      time.sleep(random.randint(0,7))

      i+=1
#  loop=False
