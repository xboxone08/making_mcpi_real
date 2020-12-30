import mcpi.minecraft as minecraft

game = minecraft.Minecraft.create()

while True:
    command = input()
    if command[0] != "/":
        game.postToChat("<StevePi_0> [ADMIN]" + command)
