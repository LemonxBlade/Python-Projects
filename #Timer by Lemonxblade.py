#Timer by Anton 

from sqlite3 import Time
import time

print("This is The Timer App By Anton ")
#Ask to Begin Timer
start = input("Start Timer (y/n)?:")
if start == "y":
    timeloop = True


#variables / display 
Sec = 0
Min = 0
# Process x
timeloop = start
while timeloop:
    Sec+= 1
    print(str(Min) + " Mins " + str(Sec) + " Sec ")
    time.sleep(1)
    if Sec == 60:
        Sec = 0
        Min += 1
        print(str(Min) + "Minute" ) 
#program will stop when x is pressed!
 
## will find out how soon!


print("Timer Stoped") 