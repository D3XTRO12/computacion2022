dia_semana = str(input("Ingrese el dia Actual de la semana en minuscula: "))
vacaciones = str(input("Estamos de vacaciones en minuscula: "))
laborales = ["lunes", "martes", "miercoles", "jueves", "viernes"]

def dormimos(dia_semana, vacaciones):
    z = False
    vac = False
    resultado = False
    for x in laborales:
        if x == dia_semana:
            resultado = True
    if vacaciones == "si":
        vac = True
    elif vacaciones == "no":
        vac = False        
    if resultado == False & vac == False:
        z = True
    elif resultado == True & vac == False:
        z = False
    elif resultado == False & vac == True:
        z = True

    return z

if dormimos(dia_semana, vacaciones) == True:
    print("Dormimos")
elif dormimos(dia_semana, vacaciones) == False:
    print("No Dormimos")


