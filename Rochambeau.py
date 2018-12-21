#!/usr/bin/env python3
def verify(x):
    if x == 'r' or x == 's' or x == 'p':
        return x
    else:
        print ('Please choose a valid character')


def playerOne():
    pl1 = str(input('Player One: Rock (r) Paper (p) or Scissors (s)?'))
    verify(pl1)
    return pl1


def playerTwo():
    pl2 = str(input('Player Two: Rock (r) Paper (p) or Scissors (s)?'))
    verify(pl2)
    return pl2


p1 = playerOne()

p2 = playerTwo()


def rochambeau(p1, p2):
    if p1 == p2:
        print('Draw')
    elif p1 == 'r' and p2 == 's':
        print('Player one wins, Rock Crushes Scissors')
    elif p2 == 'r' and p1 == 's':
        print('Player two wins, Rock Crushes Scissors')
    elif p1 == 's' and p2 == 'p':
        print('Player one wins, Scissors cut Paper')
    elif p2 == 's' and p1 == 'p':
        print('Player two wins, Scissors cut paper')
    elif p1 == 'r' and p2 == 'p':
        print('Player two wins, Paper covers Rock')
    elif p2 == 'r' and p1 == 'r':
        print('Player one wins, Paper Covers Rock')


rochambeau(p1, p2)

