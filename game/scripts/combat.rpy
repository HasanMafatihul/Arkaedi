label combat:
    g "We shall now begin your combat test."

    hide g

default cur_action = "None"

python:
    player_hp = 100
    player_atk = 20
    enemy_hp = 100
    enemy_atk = 30
    heal_remain = 3
    stance = "None"
    import random # Get the random functionality for Python

    def getRandomNumber():
        options = range(101) # Create a list of numbers 0 to 49
        return random.choice(options)

menu action:

    "Enemy HP : [enemy_hp]\nYour HP : [player_hp]"


    "Attack":
        $ stance = "None"
        "You attacked!"
        if getRandomNumber() < 80:
            $ enemy_hp -= player_atk
            "Enemy suffered [player_atk] damage!"
            if enemy_hp <= 0:
                "Enemy died!"
                return
        else:
            "Enemy dodged!"
            jump enemy_action

    "Defend":
        "You defended!"
        jump enemy_action
        $ stance = "Defend"

    "Heal ([heal_remain])":
        if heal_remain > 0:
            "You healed yourself!"
            $ heal_remain -= 1
            $ player_hp += player_atk / 2
            $ temp = player_atk / 2
            "Your health increased by [temp]!"
            jump enemy_action

label enemy_action:
    "Enemy is taking action!"

    "Enemy attacked!"

    if getRandomNumber() < 60:
        "You suffered [enemy_atk] damage!"
        $ player_hp -= enemy_atk
        if player_hp <= 0:
            "You died!"
            return
        jump action
    else:
        "You dodged!"
        jump action
