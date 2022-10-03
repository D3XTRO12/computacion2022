class ColaDePacientes:
    def __init__(self):
        self.cola_de_pacientes = [] 
        
    #Anade elementos a la cola
    def nuevo_paciente(self,pacientes):
        self.cola_de_pacientes.append(pacientes)
        
    #Devuelve elemento de la cola 
    def proximo_paciente(self):
        print("EL SIGUIENTE PACIENTE ES: ", self.cola_de_pacientes.pop(0))
            
    def ver_cola(self):
        print(self.cola_de_pacientes)
      
       
cola_pacientes = ColaDePacientes()  
posicion=0
consultorio=[1,2,3]
union = list(zip(cola_pacientes.cola_de_pacientes, consultorio))  
while True:
    print("1 ---> AGREGAR NUEVO PACIENTE:") 
    print("2 ---> LLAMAR PROXIMO PACIENTE:")
    print("3 ---> MOSTRAR LISTA DE PACIENTES:")
    print("4 ---> INGRESAR CONSULTORIO LIBRE E INDICAR PRÓXIMO PACIENTE:")
    print("5 ---> FIN DE PROGRAMA....")
    opciones = int(input("ELIJA UNA DE LAS OPCIONES ANTERIORES:"))
    if opciones == 1:
        name = str(input("NOMBRE DEL NUEVO PACIENTE:")) 
        cola_pacientes.nuevo_paciente(name)
        input("PULSA CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL....")
        print(sep = "/n")

    elif opciones == 2:
        print(cola_pacientes.proximo_paciente())
        input("PULSA CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL....")
        print(sep = "/n")

    elif opciones == 3:
        print(cola_pacientes.ver_cola())
        input("PULSA CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL....")
        print(sep = "/n")
    
    elif opciones == 4:
        print(consultorio)
        consul = int(input("Numero del consultorio liberado:"))
        consultorio.remove(consul)
        print("CONSULTORIOS OCUPADOS:", consultorio ,"CONSULTORIO DISPONIBLE:", consul)
        print("EL PROXIMO PACIENTE EN ESPERA ES:",cola_pacientes.cola_de_pacientes.pop(0))
        input("PULSA CUALQUIER TECLA PARA VOLVER AL MENU PRINCIPAL....")
        print(sep = "/n")

    elif opciones == 5:
        break
    else:
        print("OPCION FUERA DE LOS LIMITES DE SELECCION, ELEGIR UN NUMERO DEL RANGO PERMITIDO..")