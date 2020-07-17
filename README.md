from random import randint
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

player = False

def lose():
    speaker.Speak("you lose i got " + computer + " better luck next time")

def win():
    speaker.Speak("you win i got " + computer + " you were lucky")


while player == False:

    player = input("Rock, Paper, Scissors? ")
    if player == computer:
            speaker.Speak("i also got  " + computer + "  lets go again")
    elif player == "Rock":
        if computer == "Paper":
                lose()
        else:
                win()
    elif player == "Paper":
        if computer == "Scissors":
            lose()
        else:
            win()
    elif player == "Scissors":
        if computer == "Rock":
            lose()
        else:
            win()
    else:
        speaker.Speak("That's not a valid play. Check your spelling!")

    player = False
    computer = t[randint(0,2)]
