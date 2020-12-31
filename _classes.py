from _internal import world_spawn
from errors import *


class Sword:
    def __init__(self, sword_type: str, enchantments: list) -> None:
        self.type = sword_type
        self.enchantments = enchantments

    def create(self, material="wood"):
        if self.type == "none":
            self.type = material if material in (
                "wood", "gold", "stone", "iron", "diamond") else self.type

    def upgrade(self, material="next") -> None:
        if material == "next":
            if self.type == "wood":
                self.type = "gold"
            elif self.type == "gold":
                self.type = "stone"
            elif self.type == "stone":
                self.type = "iron"
            elif self.type == "iron":
                self.type = "diamond"
            else:
                raise UnknownSwordError
        elif material in ("gold", "stone", "iron", "diamond"):
            self.type = material
        else:
            raise UnknownSwordError

    def enchant(self, enchantment: str) -> None:
        if enchantment == "sharpness" or enchantment == "fire_aspect":
            self.enchantments.append(enchantment)
        else:
            raise UnknownEnchantmentError

    def get_attack_damage(self) -> int:
        # Numbers are from Bedrock Edition
        if self.type == "wood" or self.type == "gold":
            return 5
        elif self.type == "stone":
            return 6
        elif self.type == "iron":
            return 7
        elif self.type == "diamond":
            return 8

    def get_attack_damage_with_enchantments(self) -> float:
        # Assumes Sharpness V, the enchanter always enchants to max level.
        if "sharpness" in self.enchantments:
            if self.type == "wood" or self.type == "gold":
                return 11.25
            elif self.type == "stone":
                return 12.25
            elif self.type == "iron":
                return 13.25
            elif self.type == "diamond":
                return 14.25
        else:
            return self.get_attack_damage()


class Player:
    def __init__(self, id: int, sword_type="none", enchantments=[],
                 is_admin=False) -> None:
        self.id: int = id
        self.is_admin: bool = is_admin
        assert (sword_type in ("none", "wood", "gold", "stone", "iron", "diamond"))
        self.sword: Sword = Sword(sword_type, enchantments)
        self.spawnpoint = world_spawn

    def create_sword(self, material="wood") -> None:
        self.sword.create()

    def upgrade_sword(self, material="next") -> None:
        self.sword.upgrade(material)

    def enchant_sword(self, enchantment: str) -> None:
        self.sword.enchant(enchantment)

    @staticmethod
    def get_player(player_id: int):
        for symbol in globals():
            if type(globals().get(symbol)) == Player:
                if globals().get(symbol).id == player_id:
                    return globals().get(symbol)
                else:
                    return None
            else:
                return None
