from tkinter import *
import mouse
import datetime
#############################################
#############################################
end = 0
lt55s = "False"
endtimesecond = "-1"
endtimeminute = "-1"
endtimehour = "-1"
endtimeday = "-1"
endtimemonth = "-1"
endtimeyear = "-1"
start = 1
now = datetime.datetime.now()
xx = 0
time = 0
stext = 0
#############################################
###############################################
def fivefivesec():
    global lt55s
    global start
    now = datetime.datetime.now()
    if endtimesecond == "-1":
        while lt55s == "false" or start == 1:
            start = 0
            if now.second >= 55:
                print("Please wait 5 seconds")
                lt55s = "False"
                text.delete(1.0, 2.0)
                text.insert(END, "Please wait 5 seconds") 
            else:
                lt55s = "true"
                break
#############################################
def fail():
    global end
    print("Failed")
    end = "true"
    xyy = str("CPS: ") + str(xx/imput) + str("   ") + str("Total Clicks: ") + str(xx)
    text.delete(1.0, 2.0)
    text.insert(END, xyy) 
    text.pack()
#############################################
def setendtime():
    global endtimesecond
    global endtimeminute
    global endtimehour
    global endtimeday
    global endtimemonth
    global endtimeyear
    global imput
    now = datetime.datetime.now()
    if endtimesecond == "-1":
        endtimesecond = int(now.second + imput + 1)
        #endtimesecond = 10
        endtimeminute = now.minute + 1
        endtimehour = now.hour + 1
        endtimeday = now.day + 1
        endtimemonth = now.month + 1
        endtimeyear = now.year + 1
#############################################
def checkendtime():
    global end
    global now
    now = datetime.datetime.now()
    nowsec = int(now.second)
    #nowsec = 9
    nowmin = int(now.minute)
    nowhor = int(now.hour)
    nowday = int(now.day)
    nowmon = int(now.month)
    nowyer = int(now.year)
    if int(endtimesecond) <= int(nowsec):
        fail()
#    else:
#        end = "no"
    else:
        if int(endtimeminute) <= int(nowmin):
            fail()
        else:
            if int(endtimehour) <= int(nowhor):
                fail()
            else:
                if int(endtimeday) <= int(nowday):
                    fail()
                else:
                    if int(endtimemonth) <= int(nowmon):
                        fail()
                    else:
                        if int(endtimeyear) <= int(nowyer):
                            fail() 
                        else:
                            end = "no"
                        
    print("Now Sec")
    print(nowsec)
    print("Now Min")
    print(nowmin)
    print("Now Hour")
    print(nowhor)
    print("Now Day")
    print(nowday)
    print("Now month")
    print(nowmon)
    print("Now year")
    print(nowyer)
    print("end sec")
    print(endtimesecond)
    print("end min")
    print(endtimeminute)
    print("end hour")
    print(endtimehour)
    print("end month")
    print(endtimemonth)
    print("end day")
    print(endtimeday)
    print("end year")
    print(endtimeyear)
    print("input")
    print(imput)
    print("---------------------------")
#############################################
def track():
    global end
    global xx
    now = datetime.datetime.now()
    fivefivesec()
    now = datetime.datetime.now()
    setendtime()
    now = datetime.datetime.now()
    checkendtime()
    now = datetime.datetime.now()
    if end == "no":
        xx += 1
        text.delete(1.0, 2.0)
        text.insert(END, xx) 
        text.pack()
    else:
        fail()
#############################################
#############################################
imput = int(input("ammout of seconds: "))
#############################################
#############################################
master = Tk()
button = Button(master, text="Click Here", command=track)
button.pack()
text = Text(master, width=40, height=1)
text.pack()
mainloop()


