import random
# guess = random.randint(0,100)
guess = 100
while True:
    try:
        x = int(input("Please enter a number: "))
    except Exception as e:
        print ("The Exception is {}".format(e))
    else:
        print("no error")
    finally:
        print("go on")
    try:
        if x <guess:
            print ("too small")
        elif x > guess:
            print ("too big")
        else:
            print("you are right")
            break
    except Exception as e:
        print ("The Exception is {}".format(e))
