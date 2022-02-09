from graphics import *
import random
from english_words import english_words_set

notfiveletter = True
while notfiveletter:
    word = random.choice(list(english_words_set))
    if len(word) == 6 and word[0].islower():
        notfiveletter = False

guess = ""

def row(num):
    global win
    global word
    global guess
    i = 0
    while i < 6:
        a = Circle(Point(30*i + 20, 30*num), 15)
        a.draw(win)
        i+=1
    g = 0
    while g < 6:
        letter = win.getKey()
        if letter.islower():
            le = Text(Point(30*g + 20, 30*num), letter)
            le.draw(win)
            guess += letter
            g+=1
        elif letter == "BackSpace" and g > 0:
            le.undraw()
            guess = guess[:-1]
            g-=1


    if guess == word:
        yay = Text(Point(240,50),"You Win!!!")
        yay.draw(win)
        i = 0
        while i < 6:
            if guess[i] == word[i]:
                a = Circle(Point(30 * i + 20, 30 * num), 15)
                a.setFill("green")
                a.draw(win)
                le = Text(Point(30 * i + 20, 30 * num), guess[i])
                le.draw(win)
            i+=1
    else:
        i = 0
        while i < 6:
            if guess[i] in word:
                a = Circle(Point(30 * i + 20, 30 * num), 15)
                a.setFill("yellow")
                a.draw(win)
                le = Text(Point(30 * i + 20, 30 * num), guess[i])
                le.draw(win)
            i += 1

        i = 0
        while i < 6:
            if guess[i] == word[i]:
                a = Circle(Point(30 * i + 20, 30 * num), 15)
                a.setFill("green")
                a.draw(win)
                le = Text(Point(30 * i + 20, 30 * num), guess[i])
                le.draw(win)
            i+=1

    guess = ""
    if num == 8:
        lose_mess = Text(Point(280,100), (f"The word was: {word}"))
        lose_mess.draw(win)


def main():
    global win
    win = GraphWin("Wordl6", 400, 400)

    row(1)
    row(2)
    row(3)
    row(4)
    row(5)
    row(6)
    row(7)
    row(8)
    win.getMouse() # pause for click in window
    win.close()


main()