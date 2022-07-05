from time import sleep
import mcpi.minecraft as minecraft

game = minecraft.Minecraft.create()

while True:
    command = input(">")
    # Not a command
    if command[0] != "/":
        game.postToChat("<StevePi_0> [ADMIN] " + command)
    # Commands
    else:
        if command[:5] == "/sword":
            with open("sword.dat") as sword_dat:
                for line in sword_dat.read().split("\n"):
                    if line[:line.index("=")] == "0":
                        game.postToChat("[@]" + line[line.index("=") + 1:])
                        break
    # Prevent lag
    sleep(0.2)
