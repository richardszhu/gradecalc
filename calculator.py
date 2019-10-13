"""
Final Grade Calculator that considers weighted categories and point totals.
Built out of necessity for my own high school and university's grading systems.
Terminal-based UI

Made by Richard Zhu
Improved version utilizing abstract data types
"""

from category_type import *

def start(): #Introduction to the calculator
    global final_category_inputted, category_num, total_class_percent
    final_category_inputted = False
    total_class_percent = 0
    class_cats = []
    category_num = 1
    fp = 0

    start_text()

    while total_class_percent < 100 and None not in class_cats:
        current_category = cat()
        if final_points(current_category) > 0:
            fp = final_points(current_category)
        total_class_percent += weight(current_category)
        class_cats += [current_category]
        category_num += 1
    dg = find_desired_grade()
    needed_grade = calculate(class_cats, dg)
    print("***You need a {0}/{1} for a {2} in the class.***".format(needed_grade, fp, dg ))
    print("")
    restart()

def error():
    print("ERROR: Your input does not make sense (Negative points, categories add up to over 100 percent, etc)")
    restart()

def restart():
    print("Type restart to restart or q to quit")
    answer = input()
    if answer[0] == "r":
        start()
    #if answer[0] == 'q'
        #return None

def calculate(class_cats, desired_grade_percent ):
    pn = points_needed(class_cats, desired_grade_percent)
    return pn

def cat():
    w = find_weight()
    tp = find_total_points()
    p = find_points()
    fp = 0
    if not final_category_inputted:
        fp = find_final_category()

    return category(w, p, tp, fp)

def find_weight():
    print("Category " + str(category_num) + ": What percentage of the total grade is this category worth?")
    answer = float(input())
    if answer <= 0 or answer + total_class_percent > 100 :
        return error()
    return answer

def find_total_points():
    print("Category " + str(category_num) + ": How many TOTAL points are in this category already?")
    answer = float(input())
    if answer < 0:
        return error()
    return answer

def find_points():
    print("Category " + str(category_num) + ": How many points have you EARNED in this category so far?")
    answer = float(input())
    if answer < 0:
        return error()
    return answer

def find_final_category():
    print("Category " + str(category_num) + ": Is the FINAL contained in this category? ('yes' or 'no')")
    answer = input()
    if answer[0] == 'y':
        return find_final_points()
    elif answer[0] == 'n':
        return 0
    else:
        return error()

def find_final_points():
    final_category_inputted = True
    print("How many points is the final worth?")
    answer = float(input())
    if answer < 0:
        return error()
    return answer

def find_desired_grade():
    print("What is your desired grade?")
    answer = float(input())
    return answer

def start_text():
    print(" ")
    print(" ")
    print(" ")
    print("Final Grade Calculator:")
    print("Follow the instructions carefully to find out what grade you need on an assignment/exam to maintain a certain grade.")
    print("---------------------------------------------------------------------------------------------")


start()
