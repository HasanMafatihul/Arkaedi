label know:
    $ knowledge += 1
    g "Good."
    jump question_list

label not_know:
    g "That's a shame."
    jump question_list

label question_list:
    $ question += 1
    if question > number_question:
        return
    $ renpy.jump("question_" + str(question))

menu question_1:
    g "Do you know who you are?"

    "Yes":
        jump know
    "No":
        jump not_know

menu question_2:
    g "How many sprite do you see?"

    "3":
        jump not_know
    "2":
        jump not_know
    "1":
        jump know

menu question_3:
    g "How much hand does a human being possess?"

    "3":
        jump not_know
    "2":
        jump know
    "1":
        jump not_know

menu question_4:
    g "Is this an adequate test?"

    "Yes":
        jump not_know
    "No":
        jump know
