import mcpi.minecraft as minecraft
from subprocess import Popen
import pygame

pygame.init()

clock = pygame.time.Clock()

game = minecraft.Minecraft.create()

Popen(["/usr/bin/python3", "/home/pi/Documents/making_mcpi_real/making_mcpi_real.py"])

while True:
    clock.tick(1)

    command = input()
    if command[0] != "/":
        game.postToChat("<StevePi_0> [ADMIN] " + command)
    else:
        if command[:7].lower() == "/sword":
            for line in open("sword.dat").read().split("\n"):
                if line[:line.index("=")] == "0":
                    game.postToChat(line[line.index("=") + 1:])
                    break
