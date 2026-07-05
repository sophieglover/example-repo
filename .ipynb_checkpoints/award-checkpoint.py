# design a program that determines the award a person competing in a triathlon will receive

# accept user inputs for time in mins of 1 swimming, 2 cycling, 3 running, and then calculate the total time to complete the triathlon

swimming = int(input("What was your swimming time in mins?"))

cycling = int(input("What was your cycling time in mins?"))

running = int(input("What was your running time in mins?"))

total_time = swimming + cycling + running

if total_time >= 111:
    print("No award receieved")
elif (total_time <= 110) and (total_time >= 106):
    print("Award: Provincial scroll")
elif (total_time <= 105) and (total_time >= 101):
    print("Award: Provincial half colours")
else:
    print("Pronvincial colours")

