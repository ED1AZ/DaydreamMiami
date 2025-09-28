# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Player", color="#dedede")
define c = Character("", what_color="#39FF14")

# The game starts here.

label start:
    show screen stat_box

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    image normalbg = im.Scale("computerbg.jpeg", config.screen_width, config.screen_height)
    image stuck = im.Scale("colorcomp.jpeg", config.screen_width, config.screen_height)
    image free = im.Scale("free.jpeg", config.screen_width, config.screen_height)


    scene normalbg

    # These display lines of dialogue.

    "..."
    "It's another day in your home office."
    "You turn on your computer, booting it up for work."

    "{color=#39FF14}KA-CHK!!{/color}"
    "{color=#FF0000}ERROR: SYSTEM COMPROMISED.{/color}"

    "..."
    "That doesn't usually happen."
    "You watch the screen's red letters vanish into the screen's void."
    "Sighing, you're about to pick up the phone to call tech support when-"

    "{color=#39FF14}hi! :){/color}"
    "Guess it's fixed? In a way.."
    "{color=#39FF14}your computer's got a virus. LOL! {/color}"
    "Nvm."
    c "i got a few riddles for u :D"
    "..."
    "Sure. Not like you want to work anyways."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # show eileen happy

    call q2

    call q3

    call q4

    call q5

    call q6

    call q7

    call final_reveal
    
    call q1

    
    # This ends the game.

    return
