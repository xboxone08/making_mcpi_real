import mcpi.minecraft as minecraft
from mcpi.vec3 import Vec3
from classes import *
import pygame
import chat

pygame.init()

clock = pygame.time.Clock()

game = minecraft.Minecraft.create()

if open("world_spawn.dat").read() == "":
    y = 60
    while True:
        if game.getBlock(0, y, 0) != 0:
            break
        y -= 1
    world_spawn = Vec3(0, y, 0)
    del y

iteration: int = 1

while True:
    clock.tick(1)

    # Recognizing players
    admin: Player = Player(game.getPlayerEntityIds()[0], sword_type="diamond", enchantments={
                           "sharpness": 5, "fire_aspect": 2}, is_admin=True)
    counter: int = 1
    for player in game.getPlayerEntityIds():
        Player(player[counter])
        counter += 1

    if iteration % 5 == 0:
        for x in range(256):
            for y in range(-195, 60):
                for z in range(128):
                    if game.getBlock(x, y, z) in (58, 49, ):
                        pass

    events = game.pollBlockHits()

    for event in events:
        if game.getBlock(event.pos) == 46:  # TNT
            game.setBlock(event.pos, 46, 1)  # Primable TNT
        elif game.getBlock(event.pos) == 26:
            get_player(event.entityId).spawnpoint = event.pos.x
    
    iteration += 1
