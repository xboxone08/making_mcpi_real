from time import sleep
import mcpi.minecraft as minecraft

game = minecraft.Minecraft.create()

helper = {
    "help": """Provides help/lists of commands.

Usage:
    /help <command: CommandName>
Reference:

"""
}



def help_(command):
    game.postToChat(helper.get(
        command, f'Syntax error: Unexpected "{command}": at "/help >>{command}<<"'))
    


while True:
    command = input("> ")
    # Not a command
    if command[0] != "/":
        game.postToChat("<StevePi_1> [ADMIN] " + command)
    # Commands
    else:
        if command[1:5] == "help":
            try:
                help_(command[6:])
            except IndexError:
                game.postToChat(str(helper))
    # Prevent lag
    sleep(1)
