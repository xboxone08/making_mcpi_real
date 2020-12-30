from making_mcpi_real import *

while True:
    command = input()
    if command[0] != "/":
        game.postToChat("<StevePi_0> [ADMIN]" + command)
