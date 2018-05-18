import random


def randomWord():  # Escolhe palavra ao acaso
    objetos = ["Algema", "Bola", "Casaco", "Xampu", "Agulha", "Travesseiro",
               "Computador", "Gaiola", "Hidrante", "Interruptor", "Leme", "Panela", "Dado", ]
    return random.choice(objetos).lower()
