import making_mcpi_real as main

while True:
    command = input()
    if command[0] != "/":
        main.game.postToChat("<StevePi_0> [ADMIN]" + command)
