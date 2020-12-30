import making_mcpi_real

while True:
    command = input()
    if command[0] != "/":
        game.postToChat(command)
