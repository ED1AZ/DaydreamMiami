label q1:
    "Truth vs lie"

    menu:
        "Lie":
            $ trust -= 10
            $ family_health += 10 
            "The warm blanket of lies is warm nonetheless."

        "Truth":
            $ trust += 10
            $ family_health -= 10
            "The cold, hard truth seems to freeze the room."

