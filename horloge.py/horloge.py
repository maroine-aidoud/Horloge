import time




def get_time(heure, minutes, secondes):
    while True:
        print(f"{heure:02}:{minutes:02}:{secondes:02}", end="\r")
        time.sleep(1)
        secondes +=1

        if secondes == 60:
            minutes +=1
            secondes = 0
        elif minutes == 60:
            heure += 1
            minutes = 0
        elif heure == 24:
            heure = 0

        if secondes == 10 and minutes == 10 and heure == 10:
            print("Votre heure a sonnée!")

#code non finis
def get_AM_time(heure, minutes, secondes):
    for h, m, s in get_time(heure, minutes, secondes):
        am_pm = "AM"
        if h >= 12:
            am_pm = "PM"
        if h > 12:
            h = 0
        print(f"{h:02}:{m:02}:{s:02} {am_pm}", end="\r")
        time.sleep(1)



get_AM_time(22, 30, 0)