village = {
    "name": "The Village",
    "description": "You stand in a peaceful village on the edge of the Cursed Forest.",
    "actions": ["Go to Forest Entrance"]
}
forest_entrance = {
    "name" : "Forest Entrance",
    "description" : "You have reached at the entrance of cursed Forest",
    "actions" : ["Take the left path","Take the right path"] 

}
abandoned_cabin = {
    "name" : "The Abandoned Cabin",
    "description" : "You have arrived at an eriee, Abandoned Cabin",
    "actions" : ["Eaxmine the Cabin","Continue to Forest Entrance"]

}
enchantment_lake = {
    "name": "Enchanted Lake",
    "description": "You stand before a serene, enchanted lake. Mythical creatures guard the way across.",
    "actions": ["Solve the riddle", "Turn back to Forest Entrance"]
}

dark_cavern = {
    "name": "Dark Cavern",
    "description": "You venture deep into a dark cavern. Ancient inscriptions line the walls.",
    "actions": ["Decipher the inscriptions", "Return to Forest Entrance"]
}

treasure_chamber = {
    "name": "Treasure Chamber",
    "description": "You've reached the fabled Treasure Chamber. But a guardian blocks your path.",
    "actions": ["Face the guardian", "Use the treasure map"]
}
secret_door={
    "name" : "Mystic Door",
    "description" : "This is a mystic door you need a secret code to open it. ",
    "actions" : ["Put code to open door","Return to Treasure Chamber"]

}
conclusion = {
    "name": "Conclusion",
    "description": "You have reached the final stage of your adventure. The treasure is waiting for you but before that you have face the last guardian",
    "actions": ["Face the last guardian","Return to Forest Entrance"]
}


current_location = village
while True:
    print(current_location["description"]),
    print("Actions available:", ", ".join(current_location["actions"]))
    
    user_input = input("What will you do? ").lower()
    
    if current_location == village:
        if user_input == "go to forest entrance":
            current_location = forest_entrance
        else:
            print("Invalid action. Try again.")
    
    elif current_location == forest_entrance:
        if user_input == "take the left path":
            current_location = abandoned_cabin
        elif user_input == "take the right path":
            print("As you walk down the right path, you suddenly encounter a mystical guardian.")
            print("The guardian says, 'I'll let you pass if you can solve my riddle.'")
            answer = input("What has keys but can't open locks?         Hint:Music Instrument ").lower()
            if answer == "a piano":
                print("The guardian is impressed and lets you pass.")
                current_location = enchantment_lake 
            else:
                print("The guardian shakes its head. 'Incorrect. You may not pass.'")
        else:
            print("Invalid action. Try again.")
    
    elif current_location == abandoned_cabin:
        if user_input == "examine the cabin":
            print("You find a dusty journal with written VRNDER on it. ")
        elif user_input == "continue to forest entrance":
            current_location = forest_entrance
        else:
            print("Invalid action. Try again.")
    elif current_location == enchantment_lake:
        if user_input == "solve the riddle":
            print("The guardian presents a riddle: 'I'm taken from a mine, and shut up in a wooden case, from which I'm never released, and yet I am used by almost every person. What am I?'")
            answer = input("Your answer: ").lower()
            if answer=="lead" or "graphite" or "pencil":
                print("The guardian nods and allows you to cross the lake.")
                current_location = dark_cavern
            else:
                print("The guardian frowns. 'Wrong answer. Try again.'")
        elif user_input == "turn back to forest entrance":
            current_location = forest_entrance
        else:
            print("Invalid action. Try again.")
    
    elif current_location == dark_cavern:
        if user_input == "decipher the inscriptions":
            print("You carefully decipher the inscriptions, revealing the way forward.")
            current_location = treasure_chamber
        elif user_input == "return to forest entrance":
            current_location = forest_entrance
        else:
            print("Invalid action. Try again.")
    elif current_location == treasure_chamber:
        if user_input == "face the guardian":
            print("The guardian stands firm and says, 'You must answer my question to proceed. What is the sound of one hand clapping?'")
            answer = input("Your answer: ").lower()
            if answer == "silence" or "nothing" :
                print("Answer is correct. Guardian is revealing the way forward")
                current_location = conclusion

            else:
                print("The guardian remains resolute. 'Incorrect. You may not pass.'")
        elif user_input == "use the treasure map":
            print("You consult the treasure map and found a secret door.")
            current_location = secret_door
        else:
            print("Invalid action. Try again.")
            
    elif current_location == secret_door :
        if user_input == "put code to open door" :
            answer = input("enter the secret code : ")
            if answer == "VRNDER" :
                print("Door opens with a bright white light")
                current_location = conclusion
        elif user_input == "return to forest chamber" :
            print("You have returned to Forest Chamber.")
            current_location = forest_entrance
        else:
            print("Invalid code. Try again.")
    elif current_location == conclusion :
        if user_input == "face the last guardian":
            print("Last guardian says :'Answer my question and this treasure will be yours. I'm the key to knowledge and the gateway to power. Without me, you're lost in the dark. What am I?'")
            answer = input("Your answer : ").lower()
            if answer == "a book" :
                print("Guardian is satisfied with the answer. All this treasure is yours")
                print("Horray you have completed the final chapter. More chapters will be add in further updates")
                break

    