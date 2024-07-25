valid_values = ("piedra", "papel", "tijera")

opcion_user1 = input("Usuario 1 escoge una de las siguientes opciones: 'piedra', 'papel' o 'tijera' ->")

print(f"Usuario 1 escoge: {opcion_user1}")

opcion_user2 = input("Usuario 2 escoge una de las siguientes opciones: 'piedra', 'papel' o 'tijera' ->")

print(f"Usuario 2 escoge: {opcion_user2}")

if opcion_user1 in valid_values and opcion_user2 in valid_values:
    if opcion_user1 == opcion_user2:
        print("Quedan empatados porque ambos seleccionaron la misma opción")
    elif (opcion_user1 == "piedra" and opcion_user2 == "tijera") or \
         (opcion_user1 == "papel" and opcion_user2 == "piedra") or \
         (opcion_user1 == "tijera" and opcion_user2 == "papel"):
        print("El usuario 1 resulta ganador")
    else:
        print("El usuario 2 resulta ganador")
else:
    print("Alguna o ambas opciones ingresadas son diferentes a -> 'piedra', 'papel' o 'tijera'")
