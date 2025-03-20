import random

def adivinhacao():
    print("Bem-vindo ao jogo de Adivinhação!")
    print("Eu escolhi um número entre 1 e 100. Tente adivinhar!")

    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    while not acertou:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1

            if palpite < 1 or palpite > 100:
                print("Por favor, escolha um número entre 1 e 100.")
                continue

            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                acertou = True
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
        except ValueError:
            print("Por favor, digite um número válido.")

if __name__ == "__main__":
    adivinhacao()