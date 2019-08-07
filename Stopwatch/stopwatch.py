# Made in Yoo Hyeong Jun 
# github : https://github.com/cocopambag
# email : jhdf1234@naver.com

# import time library
import time 

# time.gmtime(time.time()) is returned current time.


input("In order to start stopwatch, Please press any key. : ")

now = time.gmtime(time.time())

i = 0

# program start !
while True:
    temp = input("if you want to excute Lab, Please press enter key\nIn order to end stopwatch, Please press any key. : ")
    
    last = time.gmtime(time.time())

    # hour, minutes, second
    # variable name of "minutes" is "mins" because "min" is keyword.
    hour = last.tm_hour - now.tm_hour
    mins = last.tm_min - now.tm_min
    sec = last.tm_sec - now.tm_sec

    # if minutes over negative numbere
    if mins < 0:
        hour -= 1
        mins += 60

    # if second over negative number    
    if sec < 0:
        mins -= 1
        sec += 60

     
    i += 1

    # in case that input is blank
    if temp == "":
        print("Lab {}".format(i))
        print("{} minutes".format(hour*60 + mins))
        print("{} seconds".format(sec))
        continue
    
    # Print minutes and seconds
    print("{} minutes".format(hour*60 + mins))
    print("{} seconds".format(sec))
    break

# This is wait for display
input()
