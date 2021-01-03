import mcpi.minecraft as minecraft
from subprocess import Popen
from time import sleep
import pygame

pygame.init()

clock = pygame.time.Clock()

game = minecraft.Minecraft.create()

print("Starting main mod")

sleep(5)

Popen(["/usr/bin/python3", "/home/pi/Documents/making_mcpi_real/making_mcpi_real.py"])

print("Done")

sleep(5)

print("Starting chat mod...")

iteration: int = 1

while True:
    clock.tick(1)

    if iteration == 1:
        print("Done")

    command = input(">")
    if command[0] != "/":
        game.postToChat("<StevePi_0> [ADMIN] " + command)
    else:
        if command[:7].lower() == "/sword":
            for line in open("sword.dat").read().split("\n"):
                if line[:line.index("=")] == "0":
                    game.postToChat("[@]" + line[line.index("=") + 1:])
                    break
