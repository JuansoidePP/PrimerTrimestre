patente = input("Ingrese la patente: ")


#vehiculo = int(input("Si el vehiculo es una moto precione 0 - si es una auto precione 1 - si es un camion precione 2: "))


pais = int(input("Peaje pais 0: Argentina - 1: Bolivia - 2: Brasil - 3: Paraguay - 4: Uruguay: "))


#pago = int(input("Si paga manual precione 1 si paga por telepeaje precione 2: "))


#distancia = float(input("Distancia en km del ultimo peaje: "))


################ Inicio - Verificacion de patente ############################

if len(patente) == 7:

    patenteCaracter = tuple(patente)

    a, b, c, d, e, f, g = patenteCaracter

    ####Verificacion de a
    if a == "1" or a == "2" or a == "3" or a == "4" or a == "5"or a == "6" or a == "7"or a == "8"or a == "9" or a == "0":
        patentetipo = "N"
    else:
        patentetipo = "L"

    #### Verificacion de b
    if b == "1" or b == "2" or b == "3" or b == "4" or b == "5"or b == "6" or b == "7"or b == "8"or b == "9" or b == "0":
        patentetipo = patentetipo + "N"
    else:
        patentetipo = patentetipo + "L"

    #### Verificacion de c
    if c == "1" or c == "2" or c == "3" or c == "4" or c == "5"or c == "6" or c == "7" or c == "8" or c == "9" or c == "0":
        patentetipo = patentetipo + "N"
    else:
        patentetipo = patentetipo + "L"

    ### Verificacion de d
    if d == "1" or d == "2" or d == "3" or d == "4" or d == "5" or d == "6" or d == "7" or d == "8" or d == "9" or d == "0":
        patentetipo = patentetipo + "N"
    else:
        patentetipo = patentetipo + "L"

    ### Verificacion de e
    if e == "1" or e == "2" or e == "3" or e == "4" or e == "5" or e == "6" or e == "7" or e == "8" or e == "9" or e == "0":
        patentetipo = patentetipo + "N"
    else:
        patentetipo = patentetipo + "L"

    ### Verificacion de f
    if f == "1" or f == "2" or f == "3" or f == "4" or f == "5" or f == "6" or f == "7" or f == "8" or f == "9" or f == "0":
        patentetipo = patentetipo + "N"
    else:
        patentetipo = patentetipo + "L"

    ### Verificacion de g
    if g == "1" or g == "2" or g == "3" or g == "4" or g == "5" or g == "6" or g == "7" or g == "8" or g == "9" or g == "0":
        patentetipo = patentetipo + "N"
    else:
        patentetipo = patentetipo + "L"

    print(patentetipo)##############################################################################################
    ##################################################################################

    ##### Verificacion de pais de la patente ##########
    if patentetipo == "LLNNNLL":
        patentepais = "Argentina"

    elif patentetipo == "LLLNLNN":
        patentepais = "Brasil"

    elif patentetipo == "LLNNNNN":
        patentepais = "Bolivia"

    elif patentetipo == "LLLLNNN":
        patentepais = "Paraguay"

    elif patentetipo == "LLLNNNN":
        patentepais = "Uruguay"
    else:
        patentepais = "Otro"
else:
    patentepais = "Otro"

print(patentepais)
################ Fin - Verificacion de patente ############################


############# Inicio - Verificacion de vehiculo ####################

#if vehiculo == 0:
#    print("Moto = 0")
#elif vehiculo == 1:
#    print("Auto = 1")
#elif vehiculo == 2:
#    print("Camion = 2")

############## Fin - Verificacion de vehiculo ###################


#   "Peaje pais 0: Argentina - 1: Bolivia - 2: Brasil - 3: Paraguay - 4: Uruguay: "
########## Inicio - Verificacion de peaje ###############

if pais == 0:
    print("Argentina = 0")

elif pais == 1:
    print("Bolivia = 1")

elif pais == 2:
    print("Brasil = 2")

elif pais == 3:
    print("Paraguay = 3")

elif pais == 4:
    print("Uruguay = 4")

