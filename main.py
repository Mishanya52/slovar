import random


def generate_password(password_len):
    password = ""
    for i in range(password_len):
        password += random.choice(chars)
    return password


chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = {}

while True:
    for i in passwords:
        print(i, password[i])

    name = input("Введите название приложения: ")
    password_len = int(input("Введите длину пароля: "))
    password[name] = generate_password(password_len)
