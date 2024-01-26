i = True
while i:
    daycode = input("Enter Day [x = Weekdays | y = Weekends]: ")
    print()
    timecode = input("Enter Time [a = Day | b = Night]: ")
    print()
    print("Destination: [1. American Region | 2. Asian Region | 3. African Region | 4. European Region]")
    descode = int(input("Enter Destination [1-4]: "))
    print()
    num = int(input("Enter Duration of the Call (in minutes): "))

    total = 0
    desti = ""
    day = ""
    time = ""

    if daycode == 'x':
        day = "Weekdays"
    elif daycode == 'y':
        day = "Weekends"
    else:
        day = ""

    if timecode == 'a':
        time = "Day time"
    elif timecode == 'b':
        time = "Night time"
    else:
        time = ""

    if descode == 1:
        desti = "American Region"
    elif descode == 2:
        desti = "Asian Region"
    elif descode == 3:
        desti = "African Region"
    elif descode == 4:
        desti = "European Region"
    else:
        desti = ""

    match daycode:
        case 'x':
            match timecode:
                case 'a':
                    match descode:
                        case 1:
                            if num<0:
                                print("Invalid")
                            elif num%3==0:
                                total = int(num/3)*50
                            else:
                                total= int((num/3)+1)*50
                        case 2:
                            if num < 0:
                                print("Invalid")
                            elif num % 2 == 0:
                                total = int(num / 2) * 30
                            else:
                                total = int((num / 2) + 1) * 30
                        case 3:
                            if num < 0:
                                print("Invalid")
                            elif num % 3 == 0:
                                total = int(num / 3) * 40
                            else:
                                total = int((num / 3) + 1) * 40
                        case 4:
                            if num < 0:
                                print("Invalid")
                            elif num % 2 == 0:
                                total = int(num / 2) * 35
                            else:
                                total = int((num / 2) + 1) * 35
                        case m:
                            print("Invalid")
                case 'b':
                    match descode:
                        case 1:
                            if num < 0:
                                print("Invalid")
                            elif num % 3 == 0:
                                total = int(num / 3) * 45
                            else:
                                total = int((num / 3) + 1) * 45
                        case 2:
                            if num < 0:
                                print("Invalid")
                            elif num % 2 == 0:
                                total = int(num / 2) * 27
                            else:
                                total = int((num / 2) + 1) * 27
                        case 3:
                            if num < 0:
                                print("Invalid")
                            elif num % 3 == 0:
                                total = int(num / 3) * 36
                            else:
                                total = int((num / 3) + 1) * 36
                        case 4:
                            if num < 0:
                                print("Invalid")
                            elif num % 2 == 0:
                                total = int(num / 2) * 30
                            else:
                                total = int((num / 2) + 1) * 30
                        case m:
                            print("Invalid")
                case m:
                    print("Invalid")
        case 'y':
            match timecode:
                case 'a':
                    match descode:
                        case 1:
                            if num < 0:
                                print("Invalid")
                            elif num % 3 == 0:
                                total = int(num / 3) * 40
                            else:
                                total = int((num / 3) + 1) * 40
                        case 2:
                            if num < 0:
                                print("Invalid")
                            elif num % 2 == 0:
                                total = int(num / 2) * 25
                            else:
                                total = int((num / 2) + 1) * 25
                        case 3:
                            if num < 0:
                                print("Invalid")
                            elif num % 3 == 0:
                                total = int(num / 3) * 35
                            else:
                                total = int((num / 3) + 1) * 35
                        case 4:
                            if num < 0:
                                print("Invalid")
                            elif num % 2 == 0:
                                total = int(num / 2) * 20
                            else:
                                total = int((num / 2) + 1) * 20
                        case m:
                            print("Invalid")
                case 'b':
                    match descode:
                        case 1:
                            if num < 0:
                                print("Invalid")
                            elif num % 3 == 0:
                                total = int(num / 3) * 38
                            else:
                                total = int((num / 3) + 1) * 38
                        case 2:
                            if num < 0:
                                print("Invalid")
                            elif num % 2 == 0:
                                total = int(num / 2) * 15
                            else:
                                total = int((num / 2) + 1) * 15
                        case 3:
                            if num < 0:
                                print("Invalid")
                            elif num % 3 == 0:
                                total = int(num / 3) * 22
                            else:
                                total = int((num / 3) + 1) * 22
                        case 4:
                            if num < 0:
                                print("Invalid")
                            elif num % 2 == 0:
                                total = int(num / 2) * 19
                            else:
                                total = int((num / 2) + 1) * 19
                        case m:
                            print("Invalid")
                case m:
                    print("Invalid")
        case m:
            print("Invalid")

    print()
    print("="*40)
    print("Day: ", day)
    print("Time: ", time)
    print("Destination: ", desti)
    print("Total: ", total)
    print("="*40)

    o=True
    while o:
        ans=input("Would you like to try again? (y/n): ")
        if ans=="y" or ans=="Y":
            o=False
        elif ans=="n" or ans =="N":
            print("Thank you")
            print("Exiting..")
            i=False
            break
        else:
            print("Invalid")
            continue
    else:
        continue