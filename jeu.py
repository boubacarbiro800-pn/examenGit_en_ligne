# premiere ligne de jeu
import random

def jeu():
    nombre = random.randint(1, 10)
    essais = 0

    print("Devine le nombre entre 1 et 10")

    while True:
        guess = int(input("Entre un nombre : "))
        essais += 1

        if guess < nombre:
            print("Trop petit")
        elif guess > nombre:
            print("Trop grand")
        else:
            print(f"Bravo ! Trouvé en {essais} essais")
            break

if __name__ == "__main__":
    jeu()