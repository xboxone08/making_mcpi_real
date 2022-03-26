import mcpi.minecraft as minecraft
from time import sleep

game = minecraft.Minecraft.create()

while True:
    command = input(">")
    if command[0] != "/":
        game.postToChat("<StevePi_0> [ADMIN] " + command)
    else:
        if command[:7].lower() == "/sword":
            for line in open("sword.dat").read().split("\n"):
                if line[:line.index("=")] == "0":
                    game.postToChat("[@]" + line[line.index("=") + 1:])
                    break
    sleep(0.2)
