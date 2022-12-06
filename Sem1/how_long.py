import datetime as dt

def mostrarTempo(inicio=input(),fim=input()):
    inicio = list(map(int," ".join(inicio.split(":")).split()))
    fim = list(map(int," ".join(fim.split(":")).split()))

    horarios = list(zip(inicio, fim))
    horario_final = str(dt.timedelta(days=int(horarios[0][1])-int(horarios[0][0]),
                                hours=int(horarios[1][1])-int(horarios[1][0]),
                                minutes=int(horarios[2][1])-int(horarios[2][0]),
                                seconds=int(horarios[3][1])-int(horarios[3][0])))
    if "-" in horario_final or (horario_final == "0:00:00"):
        print("Data inválida!")
    else:
        horario_final = "".join(" ".join(horario_final.split(":")).split(",")).split()
        if ("day" in horario_final) or("days" in horario_final):
            horario_final.pop(1)
        else:
            horario_final.insert(0,0)
        print(f"{int(horario_final[0]):n} dia(s)")
        print(f"{int(horario_final[1]):n} hora(s)")
        print(f"{int(horario_final[2]):n} minuto(s)")
        print(f"{int(horario_final[3]):n} segundo(s)")
    return

mostrarTempo()

#Input
#5 08:12:23
#9 06:13:23
#
#1 2:2:2
#2 2:2:2
#
#8 08:53:12
#7 08:58:14
#
#
#
#Result
#3 dia(s)
#22 hora(s)
#1 minuto(s)
#0 segundo(s)
#
#1 dia(s)
#0 hora(s)
#0 minuto(s)
#0 segundo(s)
#
#Data inválida!
#