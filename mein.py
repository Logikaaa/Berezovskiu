from turtle import *
from random import *

def start(x,y):
    penup()
    goto(x,y)
    pendown()

def write_ask(word):
    start(-170, 100)
    setheading(0)
    width(4)
    color("black")
    for w in word:
        fd(30)
        penup()
        fd(15)
        pendown()

def write_wrong(letter):
    color("black")
    write_wrong(letter, font=("Arial", 28))   
    color("red")
    width(2)
    setheading(180)
    penup()
    fd(20)
    setheading(270+45)
    pendown()
    fd(30)
    color("grey")

def write_right(letter):
    start(-170, 105)
    penup()
    color("black")
    setheading(0)
    count = 0
    for w in word:
        if w == letter:
            pendown()
            write(letter,font=("Arial", 32))
            penup()
            count += 1
        fd(45)
    return count

def end_game(col,txt):
    start(-50,-50)
    color(col)
    write(txt, font=("Arial",50))

x_ask_,y_ask= -170,100

x_wrong, y_wrong = -170, 50

count_right = 0
count_wrong = 0

speed(0)

words = ["пітушара"]

word = choice(words)

write_ask(word)

while True:

    letter = input("Ведіть літеру")

    if letter in word:
        c = write_right(letter)

        count_right(letter)

        count_right += c

    else:
        start("x_wrong,y_wrong")
        x_wrong += 45
        write_wrong(letter)

        count_wrong += 1
        
    if count_wrong == 7:
        end_game("red","Ти програв :(")
        break

    if count_right == len(word):
        end_game("blue","Ти виграв!")
        break