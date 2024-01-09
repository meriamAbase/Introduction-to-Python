#Asking users what triathlon they will be competing in and then,
#Determining what award they will receive, if any, according to the time taken to complete the triathlon.
triathlon = input("Which triathlon will you be patricipating in, swimming, cycling or running? ")
#Since python is case senstivie, I will convert the string to lowercase so the following if statements work!
triathlon = triathlon.lower()
if triathlon == "swimming":
    time1 = (int(input("In minutes, how long will it take you to complete your swim? ")))
    if time1 >  110:
        print("Sorry, no award.")
    elif time1 >= 106:
        print("Provincial Scroll")
    elif time1 > 100:
        print("Provincial Half Colours")
    elif time1 >= 0:
        print("Provincial Colours")
    else:
        print("Impossible!") 
        
if triathlon == "cycling":
    time2 = (int(input("In minutes, how long will it take you to complete your cycle? ")))
    if time2 >  110:
        print("Sorry, no award.")
    elif time2 >= 106:
        print("Provincial Scroll")
    elif time2 > 100:
        print("Provincial Half Colours")
    elif time2 >= 0:
        print("Provincial Colours")
    else:
        print("Impossible!")  
              
if triathlon == "running":
    time1 = (int(input("In minutes, how long will it take you to complete your run? ")))
    if time1 >  110:
        print("Sorry, no award.")
    elif time1 >= 106:
        print("Provincial Scroll")
    elif time1 > 100:
        print("Provincial Half Colours")
    elif time1 >= 0:
        print("Provincial Colours")
    else:
        print("Impossible!")  