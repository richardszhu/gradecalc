"""
Final Grade Calculator CLI that considers weighted categories and point totals.
Built out of necessity for my own high school and university's grading systems.
Terminal-based UI

Made by Richard Zhu
Improved version utilizing abstract data types
"""

from category_type import *

class Category:
    def __init__(self, category_percent_sum, final_category, i):
        self.percent = float(input(f"What percentage is category #{i} weighted?"))
        if self.percent <= 0:
            raise ValueError("Weight of category must be positive")
        if category_percent_sum + self.percent > 100:
            raise ValueError("Weight of categories sums to over 100%")

        self.existing_points = float(input("How many points have been assigned in this category?"))
        if self.existing_points < 0:
            raise ValueError("Points assigned must be non-negative")

        self.achieved_points = float(input("How many points have you gotten in this category?"))

        if not final_category:
            if category_percent_sum + self.percent == 100:
                self.contains_final = True
            else:
                self.contains_final = input("Does this category have the final exam? [y/n]")[0].lower() == "y"
        else:
            self.contains_final = False

        self.final_points = float(input("How many points is the final exam worth?")) if self.contains_final else 0
        if self.final_points < 0:
            raise ValueError("Points assigned must be non-negative")
        if self.final_points + self.percent == 0:
            raise ValueError("Weight of category must be positive")


def start():
    try:
        any(print() for _ in range(3))

        category_percent_sum = 0
        final_category = None
        cats = []
        i = 1
        while category_percent_sum < 100:
            cat = Category(category_percent_sum, final_category, i)
            category_percent_sum += cat.percent
            if cat.contains_final:
                final_category = cat
            cats.append(cat)
            i += 1

        if not final_category:
            raise ValueError("No final exam category")

        desired_grade = float(input("What is your desired grade in the class?"))

        other_cat_totals = sum(cat.achieved_points * cat.percent / cat.existing_points for cat in cats if cat is not final_category)
        needed = (desired_grade - other_cat_totals) * (final_category.existing_points + final_category.final_points) / final_category.percent - final_category.achieved_points
        print(f"***You need a {needed}/{final_category.final_points} for a {desired_grade} in the class.***")
    except Exception as e:
        print(e)


print("Richard's Final Grade Calculator CLI")
start()
while True:
    response = input("Type q to quit, or enter to restart")
    if not response or response[0].lower() != "q": 
        start()
    else:
        break