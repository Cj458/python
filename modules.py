"""
ready-made code
"""
import random, turtle, time, math, webbrowser
from time import *




# webbrowser.open('https://alabugaais.ru')

user = int(input('Enter your year of birth: '))

t = asctime().split(' ')

year_now = int(t[-1])

print(year_now - user)
