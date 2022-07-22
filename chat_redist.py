from time import sleep
import mcpi.minecraft as minecraft

"""Provide chat (not command) capability to LAN players."""

# Replace <server_ip> with the local
#   IP of the Raspberry Pi hosting the game
game = minecraft.Minecraft.create("<host_ip>")

while True:
    game.postToChat(input(">"))
    sleep(0.2)
