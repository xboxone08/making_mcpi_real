import mcpi.minecraft as minecraft
import pygame

pygame.init()

clock = pygame.time.Clock()

game = minecraft.Minecraft.create()


class UnknownSwordTypeError(ValueError):
    """The type of sword you passed to the Sword constructor was not
    recognized.
    """
    pass


class UnknownEnchantmentError(ValueError):
    """The enchantment you tried to add doesn't exist
    """
    pass


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
                raise UnknownSwordTypeError
        elif material in ("gold", "stone", "iron", "diamond"):
            self.type = material
        else:
            raise UnknownSwordTypeError

    def enchant(self, enchantment: str) -> None:
        # Enchants to max level as per Pocket Edition specifications.
        if enchantment == "sharpness" or enchantment == "fire_aspect":
            self.enchantments.append(enchantment)
        else:
            raise UnknownEnchantmentError

    def get_attack_damage(self) -> int:
        # Numbers are from Pocket Edition
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
    clock.tick(1)

    def __init__(self, id: int, sword_type="none", enchantments=[],
                 is_admin=False) -> None:
        self.id = id
        self.is_admin = is_admin
        assert(sword_type in ("none", "wood", "gold", "stone", "iron", "diamond"))
        self.sword = Sword(sword_type, enchantments)

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
                    return globals.get(symbol)
                else:
                    return None
            else:
                return None

iteration = 1

while True:
    # Recognizing players
    admin: Player = Player(game.getPlayerEntityIds()[0], sword_type="diamond", enchantments=[
                           "sharpness", "fire_aspect"], is_admin=True)
    counter: int = 1
    for player in game.getPlayerEntityIds():
        Player(player[counter])
        counter += 1

    if iteration % 5 == 0:
        for x in range(125):
            for y in range(-65, 60):
                for z in range(125):
                    game.getBlock()

    events = game.pollBlockHits()

    for event in events:
        if game.getBlock(event.pos) == 247:  # Nether Reactor Core
            pass
    
    iteration += 1
