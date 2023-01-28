# -*- coding: utf-8 -*-
"""
Created on %(Date: 26 Jan 2023)s

@author: %(Nativida Barlow)s
Python Version 3.11.1
SDEV 220 Spring 2023
Assignment: M02 Lab - Case Study: if...else and while
Program Description:  This is program collects student name and grade
information using if and else to determine if they made the Dean's list or the Honor Roll.
"""

student_first_name = ""
student_last_name = ""
gpa = float


student_last_name = input("What is the student's last name? ")

if student_last_name == "ZZZ":
    print("Error, the last name you entered cannot be 'ZZZ'.  Please re-enter last name. ")


student_first_name = input("What is the student's first name? ")
print("Retrieving records for " + student_first_name + " " + student_last_name + ".  Please stand by...")

gpa = float(input("What is " + student_first_name + "'s GPA? "))

if gpa >= 3.5:
    print(student_first_name + " " + student_last_name + " is on the Dean's List.")
    
elif gpa >= 3.25:
    print(student_first_name + " " + student_last_name + " made the Honor Roll.")
    
else:
    print(student_first_name + " " + student_last_name + " did not make the Dean's List or the Honor Roll.")
        
    




