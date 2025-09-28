

label q2:
    c "Is it wiser to split the weight, or hold it alone?"

    menu:
        "Split the weight":
            $ personal_health -= 10
            $ family_health -= 10 
            "You feel lighter, but your family seems to struggle."

        "Hold it alone":
            $ personal_health -= 30
            $ family_health += 10
            $ sanity -= 10
            $ trust +=10
            "Your body aches, but your family looks relieved."
    return

label q3:
    c "What’s more cruel?"

    menu:
        "Honesty":
            $ sanity += 10
            $ corruption -= 10 
            "A fleeting moment of joy, but at what cost?"
        "Kindness":
            $ sanity -= 10
            $ trust += 10
            $ corruption += 10
            "A heavy heart, but a clear conscience."
            "Your family appreciates your kindness, but you feel the weight of the world."
    return

label q4:
    c "Would you rather be feared or forgotten?"
    menu:
        "Feared":
            $ corruption += 10
            $ trust -= 10 
            $ sanity -= 10
            "Power comes with a price, and loneliness is its companion."

        "Forgotten":
            $ corruption -= 10
            $ trust += 10
            $ sanity -= 10
            "In the shadows, you find solace and unexpected connections."
    return

label q5:
    c "What does it mean to be a good person?"
    menu:
        "Do what's right, but at the cost of others":
            $ trust += 10
            $ family_health -= 10 
            "Your actions are just, but they leave scars on those around you."
        "Protect those you love, no matter the cost":
            $ trust -= 10
            $ sanity -=10
            $ personal_health -= 10
            $ family_health += 10
        "Your loved ones are safe, but your soul feels the weight of compromise."

    return 

label q6:
    c "Who deserves to suffer for a mistake?"
    menu:
        "The perpetrator":
            $ trust -= 10
            $ sanity += 10
            $ corruption += 10
            "Understanding the perpetrator's motives can lead to deeper insights, but at what cost?"
        
        "The bystander":
            $ trust -= 10
            $ family_health -= 10
            $ personal_health -= 10
            $ sanity -= 10
            "Inaction can be as damaging as action, leaving wounds unhealed."
            "The bystander suffers, but so does the community around them."
        
        "The victim":
            $ trust -= 10
            $ family_health -= 10
            $ sanity -= 10
            $ corruption += 10
            $ personal_health -= 10
            "The victim's pain is real, but seeking retribution can lead to a cycle of suffering."
            "Empathy for the victim is crucial, but so is understanding the broader context of their pain."

        "No one":
            $ trust += 10
            $ family_health += 10
            $ sanity += 10
            "Forgiveness can be a powerful tool for healing, but it requires strength and understanding."
            "Choosing not to assign blame can lead to unexpected paths of reconciliation and growth."

        "Everyone":
            $ trust -= 10
            $ family_health -= 10
            $ sanity -= 10
            $ corruption += 10
            "Collective suffering can lead to shared understanding, but it can also breed resentment and despair."
            "When everyone suffers, the lines between right and wrong can become blurred, leading to a complex web of emotions and consequences."

    return

label q7:
    c "What would you preserve if the world ended tomorrow?"
    menu:
        "Memories":
            $ sanity += 10
            $ corruption -= 10 
            "Memories are the essence of our existence, a tapestry of moments that define us."
        "Relationships":
            $ trust += 10
            $ family_health += 10
            $ personal_health += 10
            "Relationships are the threads that connect us, weaving a fabric of support and love."
        "Knowledge":
            $ corruption += 10
            $ sanity -= 10
            "Knowledge is power, a beacon of light in the darkness, but it can also be a burden."
        "Material possessions":
            $ personal_health -= 10
            $ family_health -= 10
            $ sanity -= 10
            $ corruption += 10
            "Material possessions are fleeting, but they can provide comfort and security in uncertain times."
        "Hope":
            $ trust += 10
            $ family_health += 10
            $ personal_health += 10
            $ sanity -= 10
            "Hope is the light that guides us through the darkest of times, a beacon of possibility and resilience."
            "But it can also be a double-edged sword, leading us to cling to illusions and false promises."

    return

label q1:
    c "Do you prefer the truth, or a comforting lie?"

    menu:
        "Lie":
            $ trust -= 10
            $ family_health += 10 
            $ found_truth = False
            scene stuck
            "The warm blanket of lies is warm nonetheless."
            "Your family seems relieved, but you feel a pang of guilt."
            "You feel as though something is off, but you push the feeling aside."
            "Whats your name again?"
            "..."
            "The computer hums softly, the screen flickering with a comforting glow."
            "You realize that you don't remember much about your life before this moment."
            "Who am I?"

        "Truth":
            $ trust += 10
            $ family_health -= 10
            $ found_truth = True
            scene free

            "The cold, sharp edge of truth slices through the silence."
            "The computer flickers, displaying a time:"
            c "23:59:59 — March 17, 1899"
            c "00:00:00 — March 17, 1899"
            "For a moment, the screen goes black... then returns to the desktop."
            "{color=#FF0000}WELCOME BACK.{/color}"
            "The weight of reality settles heavily on your shoulders."
            "Your family looks shaken, distant... yet you feel an odd clarity."
            "The truth is difficult, but somehow, it feels like progress."
            

    return