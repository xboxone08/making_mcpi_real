import mcpi.minecraft as minecraft
from mcpi.vec3 import Vec3
from random import choice
from _errors import *

game = minecraft.Minecraft.create()

enchantments = ("Protection", "Fire Protection", "Feather Falling", "Blast Protection", "Projectile Protection")


def get_enchantment_id(enchantment):
    if enchantment in enchantments:
        return enchantments.index(enchantment)
    else:
        raise UnknownEnchantmentError


if open("world_spawn.dat").read() == "":
    y = 60
    while True:
        if game.getBlock(0, y, 0) != 0:
            break
        y -= 1
    open("world_spawn.dat", 'w').write(f"0, {y}, 0")
    world_spawn = Vec3(0, y, 0)

if open("nether.dat").read() == "":
    choice(["N", "N", "N", "N", "N", "N"])
