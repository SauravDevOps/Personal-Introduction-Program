# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 21:45:56 2026

@author: dell
"""

#Personal Introduction Program
#Input the data
name = input("What is your name? ")
age = input("How old are you? ")
city = input("Where are you from? ")

hobbies = [] #empty list 

print("\nWhat are your Hobbies/Interests? (type done when finished)")
while True:
    hobby = input(" ")
    if hobby.lower() == "done":
        break
    hobbies.append(hobby)

#Displaying Information with a message
print("\n-----------------------------------------")
print(f"👋 Hello {name}!")
print(f"You are {age} years old and live in {city}.")

print("\n🎯 Your hobbies are:")
for h in hobbies:
    print(f" - {h}")

print("\n✨ Welcome! Great to have you here. ✨")
print("-----------------------------------------")

    

