# Update this text to match your story.

start = '''

You're driving down a really dark and winding road in the middle of nowhere...
   Your car breaks down and you stand there weighing your options.
   Should you walk into the forest to look for help or wait for a ride on the road?

 
'''
print(start)

print("Type 'go to forest' or 'wait for ride' .")
user_input = input ()
if user_input == ("go to forest"):
    print("You start to head to the forest deciding to look for help.")
    print("You see a small broken down shed. Should you go in or keep walking?")
    print("Type 'keep walking' or 'go in'")

    user_forest = input()
    if user_forest == "keep walking":
        print("You start to feel dizzy and your vision starts to grow blurry.")
        print("Should you find shelter and gather your energy there or keep walking?")
        print("Type 'shelter' or 'keep walking'")
        user_hal = input()
        if user_hal == "shelter":
            print("You pass out and someone finds you and you live!")
        elif user_hal == "keep walking":
            print("You walk off a cliff as you're halluinating and you die.")
        
    elif user_forest == "go in":
        print ("You walk towards the shed and after several tries, you manage to pull open the door.")
        print("Should you hope for the best or for the worst?")
        print("Type 'best' or 'worst'")
        user_option = input()
        if user_option == "best":
            print("You find a vault full of gold ingots and money and you live your best life.")
        elif user_option == "worst":
            print("There's a murderer inside and you die.")

if user_input == "wait for ride":
    print ("A guy pulls up looking sneaky af")
    print("should you get in the car with him or go int the forest")
    print("type 'car' or 'forest' ")
    user_ride = input()
    if user_ride == "car":
        print("This guy makes akaward conversation with you")
        print("should you hope for the best or worst")
        print("type 'best' or 'worst' ")
        user_option2 = input()
        if user_option2 == "best":
            print("you get home safe")
        elif user_option2 == "worst":
            print("turns out this guy is a murderer and stabs you")
    if user_ride == "forest":
        print("You start to head to the forest deciding to look for help.")
        print("You see a small broken down shed. Should you go in or keep walking?")
        print("Type 'keep walking' or 'go in'")

        user_forest = input()
        if user_forest == "keep walking":
            print("You start to feel dizzy and your vision starts to grow blurry.")
            print("Should you find shelter and gather your energy there or keep walking?")
            print("Type 'shelter' or 'keep walking'")
            user_hal = input()
            if user_hal == "shelter":
                print("You pass out and someone finds you and you live!")
            elif user_hal == "keep walking":
                print("You walk off a cliff as you're halluinating and you die.")
        
        elif user_forest == "go in":
            print ("You walk towards the shed and after several tries, you manage to pull open the door.")
            print("Should you hope for the best or for the worst?")
            print("Type 'best' or 'worst'")
            user_option = input()
            if user_option == "best":
                 print("You find a vault full of gold ingots and money and you live your best life.")
            elif user_option == "worst":
                print("There's a murderer inside and you die.")
        
        
