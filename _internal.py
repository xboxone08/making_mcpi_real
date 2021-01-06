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
