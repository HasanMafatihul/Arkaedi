# The script of the game goes in this file.

init python:
    def click():
        renpy.music.play("audio/click.wav",channel="sound")

    import random # Get the random functionality for Python


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("The Guide")
define you = Character("You")
define mc = Character("Dorian")
define rhea = Character("Rhea")
define senpai = Character("Laurel")
define pelayan = Character("Randall")
define eloise = Character("Eloise")
define maria = Character("Maria")
define runa = Character("Runa")

default knowledge = 0
default question = 0
default number_question = 4

transform bounce:
    linear 0.5 yalign 1.0
    linear 0.5 yalign 0.5
    repeat

transform rightish:
    xalign 0.75

transform leftish:
    xalign 0.25

# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #jump tram_station

    jump day_1

label ending:

    show guide normal at left

    # This ends the game.

    if knowledge == number_question:
        g "You have done well."
        g "Your knowledge will be rewarded."
        "A gift of parting has been given to you."
        "Ending 1: The Gift"
    elif knowledge >= number_question/2:
        g "You have done well."
        g "But you are still lacking."
        g "You must polish yourself."
        g "Return when you have learnt more."
        "The Guide disappeared in a black mist."
        "Ending 2: Uhh.. try again I guess?"
    else:
        g "Your knowledge is embarrassing."
        g "You alone are a disgrace to your kind."
        g "You shall repent forever."
        "You died(?)"
        "Ending 3: I Think You Died"

    return
