hora = int(input("Qual é a hora}(0-23) ? "))

if hora < 0 or hora > 23:
    print("A hora", hora, "é inválida!")
elif hora > -1 and hora < 6:
    print("Agora são", hora, "hora(s). Boa Madrugada.")
elif hora > 5 and hora < 12:
    print("Agora são", hora, "hora(s). Bom dia.")
elif hora > 11 and hora < 18:
    print("Agora são", hora, "hora(s). Boa tarde.")
elif hora > 17 and hora < 24:
    print("Agora são", hora, "hora(s). Boa noite.")
