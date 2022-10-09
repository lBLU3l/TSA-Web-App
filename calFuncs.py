from datetime import datetime

def findMonth():
    currentMonthNum = datetime.now().month

    Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month = list(Months)[currentMonthNum - 1]
    return month

def findYear():
    year = str(datetime.now().year)
    return year

def findDay():
    return datetime.today().strftime('%A')


def findDate():
    return datetime.now().day
    

def findHour():
    hour = str(datetime.now().hour)
    return hour

def timeGreet():
    hour = datetime.now().hour
    if 0 <= hour <= 4:
        greet = "Night"
    if 5 <= hour <= 12:
        greet = "Morning"
    if 12 <= hour <= 18:
        greet = "Afternoon"
    if 19 <= hour <= 23:
        greet = "Evening"
    return greet
    

    
