from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List, Dict
from typing_extensions import Literal, final
from math import floor, sqrt
import mcpi.minecraft as minecraft
from mcpi.vec3 import Vec3
from gamerules import show_death_messages, keep_inventory

game = minecraft.Minecraft.create()


sword_material = Literal["wood", "gold", "stone", "iron", "diamond", "netherite"]
armor_material = Literal["leather", "gold", "iron", "diamond", "netherite"]
enchantment = Literal["sharpness", "smite", "bane_of_arthropods",
                      "fire_aspect", "unbreaking", "mending", "looting", "curse_of_vanishing"]


class Sword:
    def __init__(self, material: sword_material, enchantments: Dict[enchantment, int], wielder: Player):
        self.material = material
        self.enchantments = enchantments
        self.wielder = wielder

    def enchant(self, lapis: Literal[1, 2, 3], levels: Literal[1, 2, 3], bookshelves: Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]):
        pass


@dataclass
class Effect:
    duration: str
    potency: int


class Entity:
    def __init__(self, max_health: int, health: int) -> None:
        self.max_health: int = max_health
        self.health: int = health
        self.alive: bool = True
        self.effects: List[Effect] = []

    def die(self):
        self.alive = False

    def hurt(self, damage: int, time: int, source: Optional[str] = None) -> None:
        self.health -= damage
        self.hurt_events.update({source: time})
        if self.health <= 0:
            self.health = 0  # Sanitize
            self.die()


class Mob(Entity):
    pass


class Undead(Mob):
    pass


class Arthropod(Mob):
    pass


@final
class Player(Entity):
    players = []

    def __init__(self, player_id: int, is_admin: bool = False) -> None:
        super().__init__(20, 20)
        self.hurt_events: Dict[str, int] = {}
        self.id: int = player_id
        self.is_admin: bool = is_admin
        self.spawnpoint: Vec3 = Vec3(0, 0, 0)
        self.swords: List[Sword] = []
        self.sword: Optional[Sword] = None
        self.food_level = 20
        self.food_saturation_level = 5
        self.food_tick_timer = 0
        self.food_exhaustion_level = 0
        self.xp = 0
        self.gamemode: Literal["survival", "creative",
                               "adventure", "default", "spectator"] = "survival"

    def tp(self, x: int, y: int, z: int) -> None:
        game.entity.setTilePos(id, x, y, z)

    def die(self, forced=False) -> None:
        self.tp(self.spawnpoint)
        if not keep_inventory:
            self.sword = None
            self.swords.clear()
        self.health = 20
        self.food_level = 20
        self.food_saturation_level = 5
        if show_death_messages:
            if forced:
                game.postToChat(f"StevePi_{self.id} died")
            else:
                game.postToChat(f"StevePi_{self.id} died")

    def hurt(self, damage: int, time: int, source: Optional[str] = None) -> None:
        super().hurt(damage, time, source)

    def get_levels(self) -> int:
        if self.xp <= 352:
            return floor(sqrt(self.xp + 9) - 3)
        elif self.xp <= 1507:
            return floor(81/10 + sqrt(2/5 * (self.xp - 7839/40)))
        elif self.xp >= 1508:
            return floor(325/18 + sqrt(2/9 * (self.xp - 54215/72)))

    @classmethod
    def get_player(cls, player_id: int) -> Optional[Player]:
        for player in cls.player:
            if player.id == player_id:
                return player

    @classmethod
    def create(cls, player_id: int, is_admin: bool = False):
        player = cls(player_id, is_admin)
        cls.players.append(player)
        return player


class Chest:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.blocks: tuple = tuple()
        self.pos = Vec3(x, y, z)

    def stash_blocks(self, *args) -> list:
        self.blocks += tuple(args) if len(self.blocks) <= 27 else tuple()
        return self.blocks

    def retrieve_blocks(self) -> None:
        self.blocks = tuple()
        return self.blocks
