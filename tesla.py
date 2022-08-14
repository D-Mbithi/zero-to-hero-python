def checkDriverAge(age=0):

    message = ''

    if int(age) < 18:
        message = "Sorry, you are too young to drive this car. Powering off"
    elif int(age) > 18:
        message = "Powering On. Enjoy the ride!"
    elif int(age) == 18:
        message = "Congrats on your first year of driving. Enjoy the ride!"

    return message


print(checkDriverAge(92))
