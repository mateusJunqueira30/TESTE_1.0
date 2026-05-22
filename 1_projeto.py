import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

quantidade = int(input("qual será a quantidade de caractéres da sua senha? "))

senha = ""

for i in range (quantidade):
    senha += random.choice(caracteres)

print("Essa é sua senha: " + senha)

