#final reveal
label final_reveal:
    "As the story unfolds, the culmination of your choices becomes clear."
    if corruption >= 50:
        "The digital world has taken its toll on you. Your mind feels fragmented, and reality blurs."
        "In the end, you become a mere echo in the vast expanse of cyberspace, lost to the world you once knew."
        "Your family, though safe, mourns the loss of the person you once were."
    elif trust >= 50 and family_health >= 50:
        "Your unwavering dedication to your family has paid off."
        "You find solace in their smiles and the warmth of their presence."
        "Though the digital world still beckons, you have chosen a path of love and connection."
        "Your family thrives, and you find peace in the bonds you've strengthened."
    elif sanity >= 50 and personal_health >= 50:
        "You have managed to maintain your sanity and health amidst the chaos."
        "The digital world remains a part of your life, but it no longer controls you."
        "You find a balance between technology and reality, embracing both worlds."
    elif personal_health < 50 or sanity < 50:
        "The toll of your choices has left you physically and mentally drained."
        "You struggle to find meaning in a world that feels increasingly alien."
        "Your family, though safe, worries about your well-being as you navigate the complexities of life."
    else:
        "The balance between the digital and real worlds has left you in a state of uncertainty."
        "You struggle to find your place, torn between the allure of technology and the warmth of human connection."
        "In the end, you realize that true fulfillment comes from embracing both worlds, finding harmony in their coexistence."
        "Your family remains a beacon of hope, guiding you through the complexities of life."