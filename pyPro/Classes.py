# i = 0
# numbers = []
#
# while i < 6:
#     print "At the top i is %d" % i
#     numbers.append(i)
#
#     i = i + 1
#     print "Numbers now:", numbers
#     print "At the bottom i is %d" % i
#
# print "The numbers:"
#
# for num in numbers:
#     print numbers


from sys import exit

def gold_room():
    print "This room is full og gold.How do you take it?"

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear looks at you, then slaps your face off. ")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."
    def cthulu_room():
        print "Here you see the great evil Cthulu."
        print "He, it, whatever stares at you and you go insane."
        print "Do you flee for your life or eat your head?"

    next = raw_input("> ")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    elif next == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
