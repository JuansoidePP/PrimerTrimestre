#Definir duracion de viaje sabiendo el horario de salida y de llegada

salida = input("Ingrese el horario de salida de forma hh:mm: ")

llegada = input("Ingrese el horario de llegada de forma hh:mm: ")

#Separar y convertir horas y minutos de salida
sepHoraSal = int(salida[0]+salida[1])
convertirHSalida = sepHoraSal * 60

minutosSalida = int(salida[3]+salida[4]) + convertirHSalida


#Separar y convertir horas y minutos de llegada
sepHoraLleg = int(llegada[0]+llegada[1])

convertirHLleg = sepHoraLleg * 60
minutosLlegada = int(llegada[3]+llegada[4]) + convertirHLleg


#Duracion en horas
horas = int((convertirHLleg - convertirHSalida)/60)

#Duracion en minutos
minutos = int(minutosLlegada - minutosSalida)

print("duracion de vuelo", minutos//60, "horas", minutos % 60, "minutos")

#Al no usar condicionales, este algoritmo esta mal