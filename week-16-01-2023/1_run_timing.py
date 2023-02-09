# 1. Run timing1
#Write a program (run_timing) that asks how long it took for
# you to run 10 km. The program continues to ask how long (in minutes) it took for
# additional runs, until the user presses Enter. At that point, the program exits—but
# only after calculating and displaying the average time that the 10 km runs took.

total_time=0
count=0
while True:
    running_time=input("How long it took you to run 10 km?---")
    if (running_time =="") :
        #e string gol pentru ca enter returns an empty value
        break
    elif(running_time.isdecimal()):
        total_time+=int(running_time)
        count+=1
    else:
        pass
if total_time!=0 or count !=0:
    print("Your average running time for 10 km is "+str(total_time/count)+" minutes over"+str(count))