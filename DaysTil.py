# Days Til Methods and runner -- complete


import datetime
import time
import smtplib
from email.mime.text import MIMEText
import schedule


file = "C:/Users/Student/Desktop/Desktop/Safe/bdaypeople.txt"


# basic intro page -- branching methods aren't done, but they don't affect this one so far -- complete
def daysTil():
    num = input("1. To input a new person, type 1 and press enter. \n2. To check the status of people's _____ Day, "
                "type 2 and press enter.\n3. To exit program, type 3 and press enter.\n")
    if num.isdecimal():
        if int(num) == 1:
            addNew()
        elif int(num) == 2:
            checkStat()
        elif int(num) == 3:
            return
    else:
        print("\n")
        daysTil()


# Secondary page -- complete
def checkStat():
    choice = input("Do you want to:\n1. Check status of individual person?\n2. Check status of entire family?\n3. "
                   "Return to main page?\n")
    if choice.isdecimal() and int(choice) == 1:
        person = []
        person.append(input("What is the person's first name?\n"))
        person.append(input("What is the person's last name?\n"))
        date = input("What is the person's birthday? (MMDDYYYY format)\n")
        while not validDay(date):
           date = input("Incorrect format. Please re-enter using MMDDYYYY format:\n")
        person.append(date)
        print(findPerson(person))
        checkStat()
    elif choice.isdecimal() and int(choice) == 2:
        ap = input("What is the last name of the family?\n")
        print(findFam(ap))
        checkStat()
    elif choice.isdecimal() and int(choice) == 3:
        daysTil()
    else:
        checkStat()


# Complete
def addNew():
    nameF = input("Please enter first name:\n")
    apollido = input("Please enter last name:\n")
    bdayNum = str(input("Please enter birthday in the format MMDDYYYY:\n"))
    randomWord = "crow-range"
    while randomWord == "crow-range":
        if validDay(str(bdayNum)) == True:
            randomWord = "snow-range"
        else:
            bdayNum = str(input("Incorrect format. Please enter again using MMDDYYYY:\n"))
    email = input("Please enter your email:\n")
    person = [nameF, apollido, bdayNum, email]
    yon = input("Is the following information correct? (Input Y or N):\nName: " + apollido + ", " + nameF
                + "\nBirthday: " + birthMonth(bdayNum) + " " + bdayNum[2:4] + " " + bdayNum[4:] + ", " + email + "\n")
    while yon != "Y" and yon != "N":
        yon = input("Please enter your answer as Y or N:\n")
    while yon == "N":
        whatswrong = input("Which of the following is wrong?\n(Enter the number of the incorrect data; if more"
                               "than one section is incorrect, only enter the first and the other(s) will be fixed "
                               "later)\n1. First Name\n2. Last Name\n3. Birthday\n4. Email\n")
        if whatswrong.isdecimal() and int(whatswrong) == 1:
            person[0] = input("What is your correct first name?\n")
        elif whatswrong.isdecimal() and int(whatswrong) == 2:
            person[1] = input("What is your correct last name?\n")
        elif whatswrong.isdecimal() and int(whatswrong) == 3:
            bdayTest = input("What is your correct birthday? (MMDDYYYY format)\n")
            while not validDay(bdayTest):
                print("Incorrect format")
                bdayTest = input("What is your correct birthday? (MMDDYYYY format)\n")
            person[2] = bdayTest
        elif whatswrong.isdecimal() and int(whatswrong) == 4:
            person[3] = input("What is your correct email?\n")
        else:
            print("Response in incorrect format")
        yob = input("Is the following information correct? (Input Y or N):\nName: " + apollido + ", " + nameF
                + "\nBirthday: " + birthMonth(bdayNum) + " " + bdayNum[2:4] + " " + bdayNum[4:] + ", " + email + "\n")
        while yob != "Y" and yon != "N":
            yob = input("Please enter your answer as Y or N:\n")
        if yob == "Y":
            yon = "Y"
        else:
            yon = "N"
    if checkDatabase(person):
        with open(file, "a") as opened:
            opened.write(person[0] + "," + person[1] + "," + person[2] + "," + person[3] + "\n")
            print(person[1] + ", " + person[0] + " has been added our database! Congratulations!\n")
    else:
        print("Someone with that name and birthday is already in our system.\nEither you inputted multiple times,"
              "or there's been an extreme coincidence.\nWhichever it is, the first name is the one that's staying.\n\n")
    daysTil()


# Checks database to make sure person isn't a repeat -- complete
def checkDatabase(person):
    names = []
    x = True
    with open(file, 'r') as opened:
        for line in opened:
            name = line.strip().split(",")
            names.append(name)
    for i in range(len(names)):
        if person[0].lower() == names[i][0].lower():
            if person[1].lower() == names[i][1].lower():
                if person[2].lower() == names[i][2]:
                    return False
    return True


# Tests whether inputted day is valid bday -- complete
def validDay(bday):
    if len(bday) == 8:
        if bday.isdecimal():
            if int(bday[4:]) % 4 == 0:
                feb = 29
            else:
                feb = 28
            monthDays = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if 13 > int(bday[0:2]) > 0:
                if 0 < int(bday[2:4]) < monthDays[int(bday[0:2]) - 1] + 1:
                    return True
    return False


# returns string month of birth -- complete
def birthMonth(num):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October"
        , "November", "December"]
    personMonth = months[int(num[0:2]) - 1]
    return personMonth


# Self-explanatory -- complete
def calcAge(date):
    bday = datetime.date(int(date[4:8]), int(date[0:2]), int(date[2:4]))
    currentDay = datetime.date(int(time.strftime("%Y")), int(time.strftime("%m")), int(time.strftime("%d")))
    if currentDay.month > bday.month:
        age = int(currentDay.year) - int(bday.year)
    elif currentDay.month < bday.month:
        age = int(currentDay.year) - int(bday.year) - 1
    else:
        if currentDay.day >= bday.day:
            age = int(currentDay.year) - int(bday.year)
        else:
            age = int(currentDay.year) - int(bday.year) - 1
    return age


# This is the crux; returns the date of the day's til, and guess what? It's complete
def calcDayTil(age):
    currentDay = datetime.date(int(time.strftime("%Y")), int(time.strftime("%m")), int(time.strftime("%d")))
    bday = datetime.date(int(age[4:8]), int(age[0:2]), int(age[2:4]))
    if int(currentDay.month) < int(bday.month) or \
                            int(currentDay.month) == int(bday.month) and int(currentDay.day) < int(bday.day):
        nextBday = datetime.date(currentDay.year, bday.month, bday.day)
    else:
        nextBday = datetime.date(currentDay.year + 1, bday.month, bday.day)
    personAge = calcAge(age)
    switch = datetime.timedelta(days= personAge + 1)
    daysTilDay = nextBday - switch
    return daysTilDay


# Goes through every person, calculates their days til day based on age and current date. Needs to be done each time
# app is run since obviously the data changes by the day -- complete
def genData():
    personList = []
    with open(file, 'r') as opened:
        currentDay = datetime.date(int(time.strftime("%Y")), int(time.strftime("%m")), int(time.strftime("%d")))
        for line in opened:
            if line:
                name = line.strip().split(",")
                name.append(calcDayTil(name[2])) # Adds in days til day
                name.append(currentDay == name[4]) # Bool if it's their day
                personList.append(name)
    return personList


# Complete, pending a test. Test passed
def findPerson(person):
    tot = genData()
    guy = []
    s = ""
    for i in range(len(tot)):
        if tot[i][0].lower() == person[0].lower():
            if tot[i][1].lower() == person[1].lower():
                if tot[i][2].lower() == person[2].lower():
                    guy.append(tot[i])
    if guy:
        if guy[0][5]:
            s += guy[0][0]+" " + guy[0][1] + " celebrates his/her Days Til Day today! Congratulations, within reason.\n"
        else:
            s += guy[0][0] + " " + guy[0][1] + "'s Days Til Day is not until " + str(guy[0][4]) + ". Sorry, but then " \
                                                                                "again, it's not that big of a deal.\n"
    else:
        s += "Sorry, there is no person by that name and birthday in our database.\n"
    return s


# Gives everyone with the same last name, and their day til days -- complete
def findFam(ap):
    all = genData()
    fam = []
    f = ""
    for i in range(len(all)):
        if all[i][1].lower() == ap.lower():
            fam.append(all[i])
    if not fam:
        f += "Sorry, there is nobody with that last name in our database.\n"
    for i in range(len(fam)):
        if fam[i][5]:
            f+=fam[i][0] + " " + fam[i][1] + " celebrates his/her Days Til Day today! Congratulations, within reason.\n"
        else:
            f+=fam[i][0]+" "+fam[i][1]+"'s Days Til Day is not until "+str(fam[i][3])+". Sorry, but then again, it's " \
                                                                                      "not that big of a deal.\n"
    return f


# Complete
def sendMail(person):
    sender = 'daysTilBday@gmail.com'
    receiver = person[3]
    content = "Hello " + person[0] + "!\n\nIt is your Days 'Til Day! You will turn " + str(calcAge(person[2]) + 1) + \
            " on " + str(calcDayTil(person[2])) + ", exactly " + str(calcAge(person[2]) + 1) + " days from today.\n\n" \
            "Go treat yourself to something to celebrate, like an ice cream or something. Don't go too wild, though;" \
            " it's not your real birthday, after all.\n\nSincerely,\n\nRyan\n\nP.S. This isn't one of those 'Do Not" \
            " Respond' emails, but since this is all automated any response will most likely go unanswered. If you " \
            "have an actual question about our mission, you can send an email to our founder's tertiary (and " \
            "possibly nonexistent) email, qv17.torbicr@qvmail.org"
    msg = MIMEText(content)
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = 'Testing!'
    smtp_server_name = 'smtp.gmail.com'
    port = '587'
    server = smtplib.SMTP('{}:{}'.format(smtp_server_name, port))
    server.starttls()
    server.login(sender, 'qv11927!')
    server.send_message(msg)
    server.quit()
    return


# Complete
def sendAll():
    all = genData()
    toSend = []
    for i in range(len(all)):
        if all[i][5]:
            toSend.append(all)
    for i in range(len(toSend)):
        sendMail(toSend[i])
    return


daysTil()

print("\nThe program isn't actually going to exit, since it continuously runs in order to send the emails.\n"
      "You can press the red square though, if you want.")
schedule.every().day.at("15:01").do(sendAll)

while True:
    schedule.run_pending()
    time.sleep(1)
