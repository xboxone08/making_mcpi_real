import mcpi.minecraft as minecraft
from random import choice
from _classes import *
import pygame

game = minecraft.Minecraft.create()

pygame.init()

clock = pygame.time.Clock()

iteration: int = 1

# Recognize first player to join as admin
admin: Player = Player(game.getPlayerEntityIds()[0], sword_type="netherite", enchantments={
        "sharpness": 5, "fire_aspect": 2}, is_admin=True)

while True:
    # Prevents lag, VERY slow fps
    clock.tick(1)

    # Recognizing players
    counter: int = 1
    for player in game.getPlayerEntityIds():
        Player(player[counter])
        counter += 1

    # REALLY prevents lag. Run once every **10** frames (10secs).
    if iteration % 10 == 0:
        # Does not help the lag situation scans every block in the game for structures
        for x in range(256):
            for y in range(61):
                for z in range(128):
                    pass
                    ## if game.getBlock(x, y, z) in (58, 49,):

    events = game.pollBlockHits()

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
                Player.get_player(event.entityId).spawnpoint = Vec3()

            # S
            elif (game.getBlock(event.pos.x, event.pos.y, event.pos.z + 1) == 0
                  and game.getBlock(event.pos.x,
                                    event.pos.y + 1,
                                    event.pos.z + 1) == 0
                  and game.getBlock(
                                    event.pos.x - 1,
                                    event.pos.y - 1,
                                    event.pos.z - 1) != 0) != 0:
                pass

            # E
            elif (game.getBlock(event.pos.x + 1, event.pos.y, event.pos.z) == 0
                  and game.getBlock(event.pos.x + 1,
                                    event.pos.y + 1,
                                    event.pos.z) == 0
                  and game.getBlock(event.pos.x - 1,
                                    event.pos.y - 1,
                                    event.pos.z - 1) != 0):
                pass
            else:
                rand_dir: str = choice(("SE", "SW", "NE", "W"))
                if (rand_dir == "W" and game.getBlock(event.pos.x - 1, event.pos.y, event.pos.z) == 0
                        and game.getBlock(
                            event.pos.x - 1,
                            event.pos.y + 1,
                            event.pos.z) == 0
                        and game.getBlock(
                            event.pos.x - 1,
                            event.pos.y - 1,
                            event.pos.z) != 0):
                    pass

    iteration += 1
