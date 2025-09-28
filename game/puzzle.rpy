"""
init python:
    image progress = "images/bar.png"
    image circle = "images/circle.png"

    correct_position = {
        "circle": (0,240)
    }
"""

screen stat_box():
    frame:
        xalign 0.1 
        yalign 0.1 
        

        vbox:
            text "Stats:"
            text "Health: [personal_health]"
            text "Sanity: [sanity]"
            text "Family Health: [family_health]"
            text "Trust: [trust]"


