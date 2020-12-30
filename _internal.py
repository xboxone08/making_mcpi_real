from making_mcpi_real import game
from mcpi.vec3 import Vec3
from errors import *


def get_enchantment_id(enchantment):
    with (
            "Protection", "Fire Protection", "Feather Falling", "Blast Protection", "Projectile Protection",
            "Respiration",
            "Aqua Affinity", "Thorns", "Depth Strider", "Frost Walker", "Curse of Binding", "Sharpness", "Smite",
            "Bane of Arthropods", "Knockback", "Fire Aspect", "Looting", "Efficiency", "Silk Touch", "Unbreaking",
            "Fortune",
            "Power", "Punch", "Flame", "Infinity", "Luck of the Sea", "Lure", "Loyalty", "Impaling", "Riptide",
            "Channeling",
            "Curse of Vanishing") as enchantments:
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
    world_spawn = Vec3(0, y, 0)
    del y
