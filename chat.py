from making_mcpi_real import game

while True:
    command = input()
    if command[0] != "/":
        game.postToChat("<StevePi_0> [ADMIN]" + command)
