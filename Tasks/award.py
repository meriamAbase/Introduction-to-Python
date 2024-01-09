#We will ask the user how long it will take them to complete each section of their triathlon and then,
#Determining what award they will receive, if any, according to the time taken to complete the triathlon.

swimming = int(input("In minutes, how long will it take you to swim?"))
cycling = int(input("In minutes, how long will it take you to cycle?"))
running = int(input("In minutes, how long will it take you to run?"))
total_time = swimming + cycling + running
print(f"It will take you {total_time} minutes to complete your triathlon.")

if total_time >  110:
    print("Sorry, you will not receive an award. Don't give up!")
elif total_time >= 106:
    print("Well done, you will receive a 'Provincial Scroll' award!")
elif total_time > 100:
    print("Congrats! You will receive a 'Provincial Half Colours' award!")
elif total_time >= 0:
    print("Amazing! You will receive a 'Provincial Colours' award!")
else:
    print("Impossible!") 