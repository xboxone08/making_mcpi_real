from time import sleep
import mcpi.minecraft as minecraft

game = minecraft.Minecraft.create("192.168.1.221")

while True:
    game.postToChat(input(">"))
