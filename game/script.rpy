# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define g = Character("The Guide")
define you = Character("You")

default knowledge = 0
default question = 0
default number_question = 4

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bedroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show guide normal at left

    # These display lines of dialogue.

    g "Oh, wow, this thing works"
    "I think I can continue"
    call question_list from _call_question_list

    call combat from _call_combat

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
