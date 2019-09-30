def category(weight, points, total_points, final_points=0):
    return [weight, points, total_points, final_points]

def weight(cat):
    return cat[0]
    #weight is the percent : so must divide by 100

def points(cat):
    return cat[1]

def total_points(cat):
    return cat[2] + final_points(cat)

def final_points(cat):
    return cat[3]

def is_final_cat(cat):
    return final_points(cat) > 0

#Category stuff done

def current_cat_percent(cat):
    return 100 * points(cat) / total_points(cat)

def class_point_sum(class_cats) :
    return sum([points(cat) * weight(cat) / 100 for cat in class_cats])

def class_total_point_sum(class_cats) :
    return sum([total_points(cat) * weight(cat) / 100 for cat in class_cats])

def current_class_percent(class_cats):
    return class_point_sum(class_cats) * 100 / class_total_point_sum(class_cats)

def points_needed(class_cats, desired_grade_percent):
    needed_point_sum = (desired_grade_percent / 100) * class_total_point_sum(class_cats)
    points_needed = needed_point_sum - class_point_sum(class_cats)
    return points_needed
