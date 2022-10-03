class TorreDeControl:  
    def __init__(self):
        self.espera = ["ES1","ES2","ES3","ES4","ES5","ES6","ES7","ES8"]
        self.esperando_a_volar = ["AV-03","AV-04","AV-06","AV-08","AV-010"]
        self.volando = ["AV-01","AV-05","AV-09","AV-02","AV-07"]
        self.por_aterrizar = []
        self.despegue=[]

    def accion(self, accion):
        if accion == 1:
            print("EL AVION QUE ESTA POR ATERRIZAR ES EL SIGUIENTE:")
            self.por_aterrizar.append(self.volando[0])
            print(self.volando[0])
            self.volando.remove(self.volando[0])
                                 
        if accion == 2:
            print("EL AVION QUE ESTA POR DESPEGAR ES EL SIGUIENTE:")
            print(self.esperando_a_volar[0])
            self.volando.append(self.esperando_a_volar[0])
            self.esperando_a_volar.remove(self.esperando_a_volar[0])
            
    def __str__(self):
       if len(self.por_aterrizar) == 0:
           print("NO HAY AVIONES EN LA COLA PARA ATERRIZAR")
       if len(self.por_aterrizar) > 0:
        print("LOS AVIONES ATERRIZADOS SON:")
        print(self.por_aterrizar, sep = " ")
       if len(self.volando) == 0:
          print("NO HAY AVIONES EN LA COLA PARA DESPEGAR")
       if len(self.volando) > 0:
        print("LOS AVIONES DESPEGADOS SON:")
        print(self.esperando_a_volar, sep = " ")

    def reconocimiento(self):
        print("EL NUMERO DE AVIONES ESPERANDO PARA REALIZAR EL ATERRIZAJE ES:", len(self.volando))
        if len(self.volando) == 0:
            print("NO HAY AVIONES ESPERANDO EL ATERRIZAJE")
        elif len(self.volando) > 0:
            print("LOS AVIONES QUE ESPERAN POR ATERRIZAR SON:")
            print(self.volando, sep = "\n")
            for i in range(0,len(self.volando),1):
                self.por_aterrizar.append(self.volando[i])
        print("EL NUMERO DE AVIONES POR REALIZAR DESPEGUE ES:",len(self.esperando_a_volar))
        if len(self.esperando_a_volar) == 0:
            print("NO HAY AVIONES ESPERANDO EL DESPEGUE")
        elif len(self.esperando_a_volar) > 0:
            print("LOS AVIONES QUE ESPERAN POR DESPEGAR SON:")
            print(self.esperando_a_volar, sep = "\n")
            for i in range(0 , len(self.esperando_a_volar),1):
                self.despegue.append(self.esperando_a_volar[i])



torre = TorreDeControl()  

while True:
    print("1 ----> ASIGNAR ESTACIONAMIENTO PARA AVIONES //ATERRIZAJE//") 
    print("3 ----> RECONOCIMIENTO ''''DESPEGUES/ATERRIZAJES'''' ")
    print("4 ----> FIN DEL PROGRAMA......")
    opciones = int(input("INGRESE LA OPCION REQUERIDA:"))
    if opciones == 1:
        ocupacion = int(input("PARA OCUPAR UN LUGAR POR ATERRIZAJE DE UN AVIÓN PRESIONA LA OPCION 1 //// PARA DESOCUPAR UN LUGAR POR DESPEGUE PRESIONE LA OPCION 2:"))
        print(torre.accion(ocupacion))
        
    elif opciones == 3:
        print("1 ----> VERIFICACION DE AVIONES ESPERANDO POR ATERRIZAR /// DESPEGAR")
        print("2 ----> MOSTRAR COLA DE ATERRIZAJES Y DESPEGUES")
        print("3 ----> VOLVER AL MENU PRINCIPAL")
        reconocer = int(input("INGRESE LA OPCION REQUERIDA:"))

        if reconocer == 1:
            print(torre.reconocimiento())
            input("PRESIONA CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL...")
        if reconocer == 2:
            print("LAS COLAS DE ATERRIZAJE Y DESPEGUE SON:")
            print(torre.__str__())
            input("PRESIONA CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL...")

        if reconocer == 3:
            input("PRESIONA CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL...")

    elif opciones == 4:
        break

    else:
        print("OPCION INVALIDA, INGRESE UNA OPCION DENTRO DEL RANGO ESTABLECIDO....")