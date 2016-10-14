print("In the magical land of Panera, one warrior is on his way to defeat the evil bread monster. You are that warrior.")
LeftOrRight = int(input("Would you like to..."+
                        "\n 1. Take the path going to the left"+
                        "\n 2. Take the path going to the right"))

if LeftOrRight == 1:
    left = int(input("There is a chicken in your path, do you..."+
                     "\n 1. Kill the chicken"+
                     "\n 2. Spare its life"))
    if left == 1:
        monster = int(input("Suddenly, the bread monster who smells your chicken appears, do you..."+
                           "\n 1. Fight the bread monster"+
                           "\n 2. Run away"))
        if monster == 1:
            print("You slayed the monster! You are the hero!")
        else:
            print("You are a coward! The people of Panera shame you and you live a bad life.")
    else:
        hobo = int(input("A hobo appears out of the bushes pleading for your chicken, do you..."+
                         "\n 1. Give him the chicken"+
                         "\n 2. Kick dirt in his face"))
        if hobo == 1:
            print("The homeless man is content, but now you have lost your chicken, your friend. Your sadness kills you.")
        else:
            print("The hobo is angry and stabs you and your chicken, both you and the chicken die and he eats both of you.")

else:
    right = int(input("A falled tree stands in your path, do you..."+
                      "\n 1. Clear the path with your sword"+
                      "\n 2. Walk around the tree"))
    if right == 1:
        squirrel = int(input("You have destroyed the tree, the home of a squirrel and his family, do you"+
                             "\n 1. Help the squirrel and his family move to a new tree"+
                             "\n 2. Kick dirt in the squirrel's face"))
        if squirrel == 1:
            print("The squirrel repays you for your help by giving you 3 acorns; you eat one, but realize they are poisonous to you and you die, the squirrel is sad.")
        else:
            print("The squirrel feels as though you have mocked him, he bites your neck continually until you die.")
    else:
        wizard = int(input("The path is clear and free of harm until a wizard apears on the path offering you a way to reach the bread monster easily, do you..."+
                           "\n 1. take his offer"+
                           "\n 2. tell him you aren't interested"))
        if wizard == 1:
            print("The wizard does not trick you, and you are at the bread monster's layer. But a bird poops on you and you fall of a clif because you can't see.")
        else:
            print("You continue on your way but with difficulty, years days pass, months, then years. You finally reach the bread monster's layer you take a breath, and a bird poops in your mouth and you choak to death.")
        
