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

label q2:
    "Is it wiser to split the weight, or hold it alone?"

    menu:
        "Split the weight":
            $ personal_health -= 10
            $ family_health -= 10 
            "You feel lighter, but your family seems to struggle."

        "Hold it alone":
            $ personal_health -= 10
            $ family_health += 10
            $ sanity -= 10
            $ trust +=10
            "Your body aches, but your family looks relieved."

label q3:
    "What’s more cruel?"

    menu:
        "Happiness":
            $ sanity += 10
            $ corruption -= 10 
            "A fleeting moment of joy, but at what cost?"
        "Kindness":
            $ sanity -= 10
            $ trust += 10
            $ corruption += 10
            "A heavy heart, but a clear conscience."
            "Your family appreciates your kindness, but you feel the weight of the world."

label q4:
    "Would you rather be feared or forgotten?"
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

label q5:
    "What does it mean to be a good person?"
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

label q6:
    “Who deserves to suffer for a mistake?”
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

label q7:
    "What would you preserve if the world ended tomorrow?"
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