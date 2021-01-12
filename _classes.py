from _errors import *
from mcpi.vec3 import Vec3


class Sword:
    def __init__(self, sword_type: str, enchantments: dict, wielder) -> None:
        self.enchantments = enchantments
        assert (sword_type in ("none", "wood", "gold",
                               "stone", "iron", "diamond", "netherite"))
        self.type = sword_type

    def create(self, material="wood"):
        if self.type == "none":
            self.type = material if material in (
                "wood", "gold", "stone", "iron", "diamond", "netherite") else self.type
        
        if self.wielder.is_admin:
            with open("sword.dat", 'w') as sword_dat:
                sword_dat.write(self.sword.type + str(self.sword.enchantments))
                

    def upgrade(self, material="next") -> None:
        sword_types = ("wood", "gold", "stone", "iron", "diamond", "netherite")

        if material == "next":
            if material in sword_types:
                return sword_types[sword_types.index(material) + 1]
        elif material in ("gold", "stone", "iron", "diamond", "netherite"):
            self.enchantments.clear()
            self.type = material
        else:
            raise UnknownSwordError

        if self.wielder.is_admin:
            with open("sword.dat", 'w') as sword_dat:
                sword_dat.write(self.sword.type + str(self.sword.enchantments))

    def enchant(self, enchantment: str, level=1) -> None:
        if enchantment == "sharpness":
            if level <= 5:
                self.enchantments["sharpness"] = level
        if enchantment == "fire_aspect":
            if level <= 2:
                self.enchantments["fire_aspect"] = level
        
        if self.wielder.is_admin:
            with open("sword.dat", 'w') as sword_dat:
                sword_dat.write(self.sword.type + str(self.sword.enchantments))

    def get_attack_damage(self) -> int:
        # Numbers are from Bedrock Edition
        sword_types = ('', '', '', '', "gold", "stone",
                       "iron", "diamond", "netherite")
        if self.type == "wood":
            return 4
        elif self.type != '' and self.type in sword_types:
            return sword_types.index(self.type)

    def get_attack_damage_with_enchantments(self) -> float:
        if "sharpness" in self.enchantments:
            return self.get_attack_damage() + 1.25 * self.enchantments.get("sharpness")
        else:
            return self.get_attack_damage()


class Player:
    def __init__(self, player_id: int, sword_type="none", sword_enchantments={},
                 is_admin=False) -> None:
        self.id: int = player_id
        self.is_admin: bool = is_admin
        self.spawnpoint = Vec3(0, 0, 0)
        assert (sword_type in ("none", "wood", "gold",
                               "stone", "iron", "diamond", "netherite"))
        self.sword: Sword = Sword(sword_type, sword_enchantments, self)
        self.health = 20
        self.absorption = 0
        self.effects = {}
        self.xp = 0

    def create_sword(self, material="wood") -> None:
        self.sword.create(material)

    def upgrade_sword(self, material="next") -> None:
        self.sword.upgrade(material)
        open("sword.dat", 'w').write(
            self.sword.type + str(self.sword.enchantments))

    def enchant_sword(self, enchantment: str, level=1) -> None:
        self.sword.enchant(enchantment, level)
        open("sword.dat", 'w').write(
            self.sword.type + str(self.sword.enchantments))

    @staticmethod
    def get_player(player_id: int):
        for symbol in globals():
            if type(globals().get(symbol)) == Player:
                if globals().get(symbol).id == player_id:
                    return globals().get(symbol)
                else:
                    return None
