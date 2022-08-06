from json import load, dump

with open("gamerules.jsonc", 'r') as file:
    gamerules = load(file)
do_daylight_cycle: bool = gamerules["doDaylightCycle"]
do_immediate_respawn: bool = gamerules["doImmediateRespawn"]
do_mob_loot: bool = gamerules["doMobLoot"]
do_mob_spawning: bool = gamerules["doMobSpawning"]
fire_damage: bool = gamerules["fireDamage"]
keep_inventory: bool = gamerules["keepInventory"]
mob_griefing: bool = gamerules["mobGriefing"]
natural_regeneration: bool = gamerules["naturalRegeneration"]
pvp: bool = gamerules["pvp"]
respawn_blocks_explode: bool = gamerules["respawnBlocksExplode"]
show_death_messages: bool = gamerules["showDeathMessages"]
tnt_explodes: bool = gamerules["tntExplodes"]


def update():
    global do_daylight_cycle
    global do_immediate_respawn
    global do_mob_loot
    global do_mob_spawning
    global fire_damage
    global keep_inventory
    global mob_griefing
    global natural_regeneration
    global pvp
    global respawn_blocks_explode
    global show_death_messages
    global tnt_explodes

    do_daylight_cycle = gamerules["doDaylightCycle"]
    do_immediate_respawn = gamerules["doImmediateRespawn"]
    do_mob_loot = gamerules["doMobLoot"]
    do_mob_spawning = gamerules["doMobSpawning"]
    fire_damage = gamerules["fireDamage"]
    keep_inventory = gamerules["keepInventory"]
    mob_griefing = gamerules["mobGriefing"]
    natural_regeneration = gamerules["naturalRegeneration"]
    pvp = gamerules["pvp"]
    respawn_blocks_explode = gamerules["respawnBlocksExplode"]
    show_death_messages = gamerules["showDeathMessages"]
    tnt_explodes = gamerules["tntExplodes"]


def update_file():
    with open("gamerules.jsonc", 'w') as file:
        dump(gamerules, file, indent=4)


def change_gamerule(gamerule: str, value: bool, **kwargs):
    global gamerules
    gamerules[gamerule] = value
    if kwargs.get("update_vars", True):
        update()
    if kwargs.get("update_file", True):
        update_file()
