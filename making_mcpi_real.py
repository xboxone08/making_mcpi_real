import mcpi.minecraft as minecraft
from random import choice
from time import sleep
from _classes import *
import pygame

game = minecraft.Minecraft.create()

pygame.init()

clock = pygame.time.Clock()

iteration: int = 1

# Recognize first player to join as admin
admin: Player = Player(game.getPlayerEntityIds()[0], sword_type="netherite", sword_enchantments={
    "sharpness": 5, "fire_aspect": 2}, is_admin=True)

sleep(9)

while True:
    # Prevents lag, VERY slow fps
    clock.tick(1)

    # Recognizing players
    for player in game.getPlayerEntityIds():
        Player(player)

    events = game.events.pollBlockHits()

    for event in events:
        if game.getBlock(event.pos) == 46:  # TNT
            game.setBlock(event.pos, 46, 1)  # Primeable TNT
        # Setting spawnpoint using bed
        elif game.getBlock(event.pos) == 26:
            # NW
            if (game.getBlock(event.pos.x - 1, event.pos.y, event.pos.z - 1) == 0
                    and game.getBlock(event.pos.x - 1,
                                      event.pos.y + 1,
                                      event.pos.z - 1) == 0
                    and game.getBlock(event.pos.x - 1,
                                      event.pos.y - 1,
                                      event.pos.z - 1)) != 0:
                Player.get_player(event.entityId).spawnpoint = Vec3(
                    event.pos.x - 1, event.pos.y, event.pos.z - 1)
                game.postToChat("Respawn point set")

            # S
            elif (game.getBlock(event.pos.x, event.pos.y, event.pos.z + 1) == 0
                  and game.getBlock(event.pos.x,
                                    event.pos.y + 1,
                                    event.pos.z + 1) == 0
                  and game.getBlock(
                    event.pos.x - 1,
                    event.pos.y - 1,
                    event.pos.z - 1) != 0) != 0:
                Player.get_player(event.entityId).spawnpoint = Vec3(
                    event.pos.x, event.pos.y, event.pos.z + 1)
                game.postToChat("Respawn point set")

            # E
            elif (game.getBlock(event.pos.x + 1, event.pos.y, event.pos.z) == 0
                  and game.getBlock(event.pos.x + 1,
                                    event.pos.y + 1,
                                    event.pos.z) == 0
                  and game.getBlock(event.pos.x - 1,
                                    event.pos.y - 1,
                                    event.pos.z - 1) != 0):
                Player.get_player(event.entityId).spawnpoint = Vec3(
                    event.pos.x + 1, event.pos.y, event.pos.z)
                game.postToChat("Respawn point set")
            else:
                rand_dir: str = choice(("SE", "SW", "NE", "W", "N"))
                if (rand_dir == "W" and game.getBlock(event.pos.x - 1, event.pos.y, event.pos.z) == 0
                        and game.getBlock(
                            event.pos.x - 1,
                            event.pos.y + 1,
                            event.pos.z) == 0
                        and game.getBlock(
                            event.pos.x - 1,
                            event.pos.y - 1,
                            event.pos.z) != 0):
                    Player.get_player(event.entityId).spawnpoint = Vec3(
                        event.pos.x - 1, event.pos.y, event.pos.z)
                    game.postToChat("Respawn point set")

                elif (rand_dir == "NE" and game.getBlock(event.pos.x + 1, event.pos.y, event.pos.z - 1) == 0
                        and game.getBlock(
                            event.pos.x + 1,
                            event.pos.y + 1,
                            event.pos.z - 1) == 0
                        and game.getBlock(
                            event.pos.x + 1,
                            event.pos.y - 1,
                            event.pos.z - 1) != 0):
                    Player.get_player(event.entityId).spawnpoint = Vec3(
                        event.pos.x - 1, event.pos.y, event.pos.z)
                    game.postToChat("Respawn point set")

                elif (rand_dir == "SW" and game.getBlock(event.pos.x - 1, event.pos.y, event.pos.z + 1) == 0
                        and game.getBlock(
                            event.pos.x - 1,
                            event.pos.y + 1,
                            event.pos.z + 1) == 0
                        and game.getBlock(
                            event.pos.x - 1,
                            event.pos.y - 1,
                            event.pos.z + 1) != 0):
                    Player.get_player(event.entityId).spawnpoint = Vec3(
                        event.pos.x - 1, event.pos.y, event.pos.z)
                    game.postToChat("Respawn point set")

                elif (rand_dir == "SE" and game.getBlock(event.pos.x + 1, event.pos.y, event.pos.z + 1) == 0
                        and game.getBlock(
                            event.pos.x + 1,
                            event.pos.y + 1,
                            event.pos.z + 1) == 0
                        and game.getBlock(
                            event.pos.x + 1,
                            event.pos.y - 1,
                            event.pos.z + 1) != 0):
                    Player.get_player(event.entityId).spawnpoint = Vec3(
                        event.pos.x - 1, event.pos.y, event.pos.z)
                    game.postToChat("Respawn point set")

                elif (rand_dir == "N" and game.getBlock(event.pos.x - 1, event.pos.y, event.pos.z - 1) == 0
                        and game.getBlock(
                            event.pos.x,
                            event.pos.y + 1,
                            event.pos.z - 1) == 0
                        and game.getBlock(
                            event.pos.x - 1,
                            event.pos.y - 1,
                            event.pos.z - 1) != 0):
                    Player.get_player(event.entityId).spawnpoint = Vec3(
                        event.pos.x - 1, event.pos.y, event.pos.z)
                    game.postToChat("Respawn point set")
        elif game.getBlock(event.pos) == 22:  # Lapis Lazuli Block
            game.setBlock(event.pos, 8)  # Water
        # elif game.getBlock(event.pos) == 8:
        #     game.setBlock(79)

    iteration += 1
