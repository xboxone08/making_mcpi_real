from __future__ import annotations
from typing import Literal
from mcpi.vec3 import Vec3
import mcpi.minecraft as minecraft

game = minecraft.Minecraft.create()


class Sword:
    def __init__(self, sword_type: Literal["wood", "gold", "stone", "iron", "diamond", "netherite"], enchantments: dict, wielder: Player) -> None:
        self.enchantments = enchantments
        self.type = sword_type
        self.wielder = wielder

        if self.wielder.is_admin:
            with open("sword.dat", 'w') as sword_dat:
                sword_dat.write(self.type + "\n" + str(self.enchantments))

    def upgrade(self, material: Literal["wood", "gold", "stone", "iron", "diamond", "netherite", "next"] = "next") -> None:
        sword_types = ("none", "wood", "gold", "stone",
                       "iron", "diamond", "netherite")

        if material == "next":
            if material in sword_types:
                return sword_types[sword_types.index(material) + 1]
        elif material in ("gold", "stone", "iron", "diamond", "netherite"):
            self.enchantments.clear()
            self.type = material

        if self.wielder.is_admin:
            with open("sword.dat", 'w') as sword_dat:
                sword_dat.write(self.type + str(self.enchantments))

    def enchant(self, enchantment: str, level=1) -> None:
        self.enchantments[enchantment] = level

        if self.wielder.is_admin:
            with open("sword.dat", 'w') as sword_dat:
                sword_dat.write(self.type + str(self.enchantments))

    def get_attack_damage(self) -> int:
        # Numbers are from Bedrock Edition
        sword_types = ("none", '', '', '', "gold", "stone",
                       "iron", "diamond", "netherite")
        if self.type == "wood":
            return 4
        else:
            return sword_types.index(self.type)

    def get_attack_damage_with_enchantments(self) -> float:
        if "sharpness" in self.enchantments:
            return self.get_attack_damage() + 1.25 * self.enchantments.get("sharpness")
        else:
            return self.get_attack_damage()


class Player:
    def __init__(self, player_id: int, sword_type: Literal["none", "wood", "gold", "stone", "iron", "diamond", "netherite"] = "none", sword_enchantments={},
                 is_admin=False) -> None:
        self.id: int = player_id
        self.is_admin: bool = is_admin
        self.spawnpoint = Vec3(0, 0, 0)
        self.sword: Sword = Sword(sword_type, sword_enchantments, self)
        self.health = 20
        self.absorption = 0
        self.effects = {}  # e.g. {"poison: ["1:30", ]"}
        self.alive = True
        self.xp = 0

    def upgrade_sword(self, material: Literal["wood", "gold", "stone", "iron", "diamond", "netherite", "next"] = "next") -> None:
        self.sword.upgrade(material)
        open("sword.dat", 'w').write(
            self.sword.type + str(self.sword.enchantments))

    def enchant_sword(self, enchantment: str, level=1) -> None:
        self.sword.enchant(enchantment, level)
        open("sword.dat", 'w').write(
            self.sword.type + str(self.sword.enchantments))

    def tp(self, x: int, y: int, z: int):
        game.entity.setTilePos(id, x, y, z)

    def die(self):
        # TODO Implement situational death messages
        game.postToChat("StevePi #" + self.id + " died")
        self.tp(self.spawnpoint)

    def hurt(self, damage: int):
        self.health -= damage
        if self.health <= 0:
            self.health = 0  # Sanitize
            self.die()

    @classmethod
    def get_player(cls, player_id: int):
        for symbol in globals():
            if type(globals().get(symbol)) == cls:
                if globals().get(symbol).id == player_id:
                    return globals().get(symbol)
                else:
                    return None


class Chest:
    def __init__(self, x: int, y: int, z: int):
        self.blocks = []
        self.pos = Vec3(x, y, z)
