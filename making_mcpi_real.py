import mcpi.minecraft as minecraft
from time import sleep
from _classes import *
from keyboard import on_release_key
game = minecraft.Minecraft.create()

# Recognize first player to join as admin
admin: Player = Player(game.getPlayerEntityIds()[0], sword_type="netherite", sword_enchantments={
    "sharpness": 5, "fire_aspect": 2}, is_admin=True)
i = 1

game.player.setting("autojump", False)

view: str = "1st"


def toggle_view(event):
    global view
    if view == "1st":
        view = "3rd"
        game.camera.setFollow(game.getPlayerEntityIds()[0])
    elif view == "3rd":
        view = "1st"
        game.camera.setNormal(game.getPlayerEntityIds()[0])

on_release_key("f5", toggle_view)

game.saveCheckpoint()

# If run with pythonw
try:
    if i == 1:
        print("Started mod")  # Only runs on first iteration
        game.postToChat("making_mcpi_real activated")
except:
    pass

while True:
    # Recognizing players
    for player in game.getPlayerEntityIds():
        if player == game.getPlayerEntityIds()[0]:
            continue
        Player(player)

    events = game.events.pollBlockHits()

    for event in events:
        if game.getBlock(event.pos) == 46:  # TNT
            game.setBlock(event.pos, 46, 1)  # Primeable TNT
        elif game.getBlock(event.pos) == 35 and game.getBlockWithData(event.pos).data == 11:  # Blue Wool
            game.setBlock(event.pos, 8)  # Flowing water
        elif game.getBlock(event.pos) == 35 and game.getBlockWithData(event.pos).data == 1:  # Orange wool
            game.setBlock(event.pos, 10)  # Flowing lava
        # Setting spawnpoint using bed
        elif game.getBlock(event.pos) == 26:
            open("rspnpt.dat", 'w').write(str(event.pos))
            game.postToChat("Respawn point set")
        # Write about how the world is right now
        elif game.getBlock(event.pos) == 47:  # Bookshelf
            game.saveCheckpoint()
            game.postToChat("Restore point set")
        # Go back to the written memories
        elif game.getBlock(event.pos) == 247 and (  # Nether Reactor Core
                game.getBlock(event.pos.x - 1, event.pos.y, event.pos.z) == 47  # Bookshelf anywhere around it
                    or game.getBlock(event.pos.x - 1, event.pos.y, event.pos.z) == 47
                    or game.getBlock(event.pos.x + 1, event.pos.y, event.pos.z) == 47
                    or game.getBlock(event.pos.x, event.pos.y, event.pos.z - 1) == 47
                    or game.getBlock(event.pos.x, event.pos.y, event.pos.z + 1) == 47
                    or game.getBlock(event.pos.x, event.pos.y - 1, event.pos.z) == 47
                    or game.getBlock(event.pos.x, event.pos.y + 1, event.pos.z) == 47):
            game.setBlock(event.pos, 247, 1)
            game.restoreCheckpoint()
            game.postToChat("Restoration complete")
        elif game.getBlock(event.pos) == 49:  # Obsidian
            game.setBlock(event.pos, 7)  # Bedrock
        elif game.getBlock(event.pos) == 20:  # Glass
            game.setBlock(event.pos, 95)  # Invisible Bedrock
        elif game.getBlock(event.pos) == 50:
            game.setBlock(event.pos, 51)
        elif game.getBlock(event.pos) == 35 and game.getBlockWithData(event.pos).data == 14:
            game.setBlock(event.pos, 246)
        # Chests
        # Prevents lag, VERY slow fps
        sleep(1)
