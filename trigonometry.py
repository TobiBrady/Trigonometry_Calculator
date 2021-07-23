#this is a trigonometry calculator that will calculate the parameters of a triangle based on the minmum input

#inporting the required math functions
from math import sin, cos, tan, asin, acos, atan, radians, degrees

#trigonomic functions
#sin_opposite
def sin_opposite(angle, hypotenuse):
    angle = radians(angle)
    result = sin(angle) * hypotenuse
    return result
#sin_hypotenuse
def sin_hypotenuse(angle, opposite):
    angle = radians(angle)
    result = opposite / sin(angle)
    return result
#sin_angle
def sin_angle(opposite, hypotenuse):
    opposite = float(opposite)
    result = asin(opposite / hypotenuse)
    result = degrees(result)
    return result

#cos_adjacent
def cos_adjacent(angle, hypotenuse):
    angle = radians(angle)
    result = cos(angle) * hypotenuse
    return result
#cos_hypotenuse
def cos_hypotenuse(angle, adjacent):
    angle = radians(angle)
    result = adjacent / cos(angle)
    return result
#cos_angle
def cos_angle(adjacent, hypotenuse):
    adjacent = float(adjacent)
    result = acos(adjacent / hypotenuse)
    result = degrees(result)
    return result

#tan_opposite
def tan_opposite(angle, adjacent):
    angle = radians(angle)
    result = tan(angle) * adjacent
    return result
#tan_adjacent
def tan_adjacent(angle, opposite):
    angle = radians(angle)
    result = opposite / tan(angle)
    return result
#tan_angle
def tan_angle(opposite, adjacent):
    opposite = float(opposite)
    result = atan(opposite / adjacent)
    result = degrees(result)
    return result

#sin_rule_side
def sinrule_side(angle_1, example_side, example_angle):
    angle_1 = radians(angle_1)
    example_angle = radians(example_angle)
    result = (example_side / sin(example_angle)) * sin(angle_1)
    return result
#sin_rule_angle
def sinrule_angle(side_1, example_side, example_angle):
    example_angle = radians(example_angle)
    result = asin((sin(example_angle) / example_side) * side_1)
    result = degrees(result)
    return result

#cos_rule_side
def cosrule_side(side1, side2, angle_1):
    angle_1 = radians(angle_1)
    result = ((side1 ** 2) + (side2 ** 2) - (2 * side1 * side2 * cos(angle_1))) ** 0.5
    return result
#cos_rule_angle
def cosrule_angle(side1, side2, side_1):
    side_1 = float(side_1)
    result = acos(((side1 ** 2) + (side2 ** 2) - (side_1 ** 2)) / (2 * side1 * side2))
    result = degrees(result)
    return result

#non-trigonomic functions
#determines if the input can be converted into a float
def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

#determines if the value inputed for a side is valid
def input_side():
    side = raw_input("Input a numerical side length or leave blank: ")
    while True:
        if isfloat(side):
            side = float(side)
            break
        elif len(side) == 0:
            side = None
            break
        else:
            side = raw_input("Invalid entry, please try again: ")
    return side

#determines if the value inputed for an angle is valid
def input_angle():
    angle = raw_input("Input an angle in degrees or leave blank: ")
    while True:
        if isfloat(angle):
            angle = float(angle)
            break
        elif len(angle) == 0:
            angle = None
            break
        else:
            angle = raw_input("Invalid entry, please try again: ")
    return angle

#counts the number of valid parameters that have been provided
def valid_inputs(lst):
    numerical_inputs = []
    for item in lst:
        if not item == None:
            numerical_inputs.append(item)
    return numerical_inputs

#counts the number of parameters that have been provided
def complete_input_check(lst):
    count = 0
    for item in lst:
        if not item == None:
            count += 1
    return count

#counts the number of angle parameters provided
def angle_input_count(lst,lst2):
    angle_inputs = []
    for item in lst:
        if item in lst2:
            angle_inputs.append(item)
    return len(angle_inputs)

#counts the number of side parameters provided
def side_input_count(lst,lst2):
    side_inputs = []
    for item in lst:
        if item in lst2:
            side_inputs.append(item)
    return len(side_inputs)

#begining of interface
print
print "Trigonometry Calculator"

#asking the user if the triangle of interest is a right angled triangle
print
print "Are you processing a right angled triangle?"
triangle_type = raw_input("Type Yes or No, if you are unsure type No: ")
triangle_type = triangle_type.lower()

#chacking the validity of the answer to the previous question and re-asking the if not
valid_triangle = 0
triangle_type_inputs = ["no", "yes"]
while valid_triangle == 0:
    if triangle_type in triangle_type_inputs:
        if triangle_type == "yes":
            print
            print "Right Angled Triangle Selected"
        elif triangle_type == "no":
            print
            print "Right Angled Triangle Not Selected"
        valid_triangle += 1
    else:
        print
        triangle_type = raw_input("Invalid entry. Type yes or no, if you are unsure leave blank: ")
        triangle_type.lower()

#the process for triangles that do not have a right angle
if triangle_type == "no":

    print
    print "You will now be asked to input the known parameters of your triangle."
    print "please ensure that you enter at least three values including at lest one side."

    #user input
    while True:

        print
        print "Input the known side lengths of your triangle"
        print
        print "Side a Length"
        side_a = input_side() #25
        print
        print "Side b Length"
        side_b = input_side() #43
        print
        print "Side c Length"
        side_c = input_side() #45

        print
        print "Input the known angles of your triangle"
        print
        print "Angle A"
        angle_a = input_angle() #33
        print 
        print "Angle B"
        angle_b = input_angle() #69.5
        print
        print "Angle C"
        angle_c = input_angle() #77.5

        #generation of the required lists to check inputs
        all_inputs_one = [side_a, side_b, side_c, angle_a, angle_b, angle_c]
        new_list_one = valid_inputs(all_inputs_one)
        possible_side_inputs_one = [side_a, side_b, side_c]

        #input checking
        if complete_input_check(all_inputs_one) >= 3 and side_input_count(new_list_one, possible_side_inputs_one) >= 1:
            break
        else:
            print
            print "Not enough values to complete the calculation."
            print "Ensure that you enter at least 3 values including 1 side."
    
    #trigonomic expression loop for non right angled triangles
    while not len(new_list_one) == 6:

        #angles up to 180
        if angle_a in new_list_one and angle_b in new_list_one and angle_c not in new_list_one:
            angle_c = 180 - (angle_a + angle_b)
            new_list_one.append(angle_c)

        elif angle_b in new_list_one and angle_c in new_list_one and angle_a not in new_list_one:
            angle_a = 180 - (angle_b + angle_c)
            new_list_one.append(angle_a)

        elif angle_c in new_list_one and angle_a in new_list_one and angle_b not in new_list_one:
            angle_b = 180 - (angle_a + angle_c)
            new_list_one.append(angle_b)

        #sin rule
        elif side_a in new_list_one and angle_a in new_list_one:

            if side_b in new_list_one and angle_b not in new_list_one:
                angle_b = sinrule_angle(side_b, side_a, angle_a)
                new_list_one.append(angle_b)

            elif angle_b in new_list_one and side_b not in new_list_one:
                side_b = sinrule_side(angle_b, side_a, angle_a)
                new_list_one.append(side_b)

            elif side_c in new_list_one and angle_c not in new_list_one:
                angle_c = sinrule_angle(side_c, side_a, angle_a)
                new_list_one.append(angle_c)

            elif angle_c in new_list_one and side_c not in new_list_one:
                side_c = sinrule_side(angle_c, side_a, angle_a)
                new_list_one.append(side_c)

        elif side_b in new_list_one and angle_b in new_list_one:

            if side_a in new_list_one and angle_a not in new_list_one:
                angle_a = sinrule_angle(side_a, side_b, angle_b)
                new_list_one.append(angle_a)

            elif angle_a in new_list_one and side_a not in new_list_one:
                side_a = sinrule_side(angle_a, side_b, angle_b)
                new_list_one.append(side_a)

            elif side_c in new_list_one and angle_c not in new_list_one:
                angle_c = sinrule_angle(side_c, side_b, angle_b)
                new_list_one.append(angle_c)

            elif angle_c in new_list_one and side_c not in new_list_one:
                side_c = sinrule_side(angle_c, side_b, angle_b)
                new_list_one.append(side_c)

        elif side_c in new_list_one and angle_c in new_list_one:

            if side_a in new_list_one and angle_a not in new_list_one:
                angle_a = sinrule_angle(side_a, side_c, angle_c)
                new_list_one.append(angle_a)

            elif angle_a in new_list_one and side_a not in new_list_one:
                side_a = sinrule_side(angle_a, side_c, angle_c)
                new_list_one.append(side_a)

            elif side_b in new_list_one and angle_b not in new_list_one:
                angle_b = sinrule_angle(side_b, side_c, angle_c)
                new_list_one.append(angle_b)

            elif angle_b in new_list_one and side_b not in new_list_one:
                side_b = sinrule_side(angle_b, side_c, angle_c)
                new_list_one.append(side_b)
        
        #cos rule
        elif side_a in new_list_one and side_b in new_list_one and side_c in new_list_one:

            if angle_a not in new_list_one:
                angle_a = cosrule_angle(side_b, side_c, side_a)
                new_list_one.append(angle_a)

            elif angle_b not in new_list_one:
                angle_b = cosrule_angle(side_a, side_c, side_b)
                new_list_one.append(angle_b)

            elif angle_c not in new_list_one:
                angle_c = cosrule_angle(side_a, side_b, side_c)
                new_list_one.append(angle_c)

        elif angle_a in new_list_one and side_b in new_list_one and side_c in new_list_one:
            side_a = cosrule_side(side_b, side_c, angle_a)
            new_list_one.append(side_a)

        elif angle_b in new_list_one and side_a in new_list_one and side_c in new_list_one:
            side_b = cosrule_side(side_a, side_c, angle_b)
            new_list_one.append(side_b)

        elif angle_c in new_list_one and side_a in new_list_one and side_b in new_list_one:
            side_c = cosrule_side(side_a, side_b, angle_c)
            new_list_one.append(side_c)

    #result printing
    print
    print "Side Lengths"
    print "a: " + str(round(side_a, 3))
    print "b: " + str(round(side_b, 3))
    print "c: " + str(round(side_c, 3))
    print
    print "Angle Sizes in Degrees"
    print "A: " + str(round(angle_a, 3))
    print "B: " + str(round(angle_b, 3))
    print "C: " + str(round(angle_c, 3))
    print

    #result checking
    if angle_a + angle_b + angle_c > 181 or angle_a + angle_b + angle_c < 179:
        print "Looks like the angles are a bit off, try doing your calculations again."
    print "End of Program!"
    print

#process for right angled triangles
elif triangle_type == "yes":

    print
    print "You will now be asked to input the known parameters of your triangle."
    print "Ensure that you enter at least two values including at lest one side."

    #user input
    while True:
        
        print
        print "Input the angle of interest if known."
        print
        print "Angle of Interest"
        subject_angle = input_angle()
        other_angle = None

        print 
        print "Input the known side lengths of your right angled triangle."
        print
        print "Opposite Side Length"
        opposite_side = input_side() #4
        print
        print "Adjacent Side Length"
        adjacent_side = input_side() #3
        print
        print "Hypotenuse Side Length"
        hypotenuse_side = input_side() #5

        #generation of required lists to check input
        all_inputs_two = [opposite_side, adjacent_side, hypotenuse_side, subject_angle]
        new_list_two = valid_inputs(all_inputs_two)
        possible_side_inputs_two = [opposite_side, adjacent_side, hypotenuse_side]

        #input checking
        if side_input_count(new_list_two, possible_side_inputs_two) >= 1 and new_list_two >= 2:
            break
        else:
            print
            print
            print "Not enough values to complete the calculation."
            print "Ensure you are entering at least one angle and one side."

    #trigononic expression loop for right angled triangles
    while not len(new_list_two) == 5:

        if subject_angle in new_list_two and other_angle not in new_list_two:
            other_angle = 180 - (subject_angle + 90)
            new_list_two.append(other_angle)

        elif hypotenuse_side in new_list_two:

            if adjacent_side in new_list_two and subject_angle not in new_list_two:
                subject_angle = cos_angle(adjacent_side, hypotenuse_side)
                new_list_two.append(subject_angle)

            elif subject_angle in new_list_two and adjacent_side not in new_list_two:
                adjacent_side = cos_adjacent(subject_angle, hypotenuse_side)
                new_list_two.append(adjacent_side)

            elif opposite_side in new_list_two and subject_angle not in new_list_two:
                subject_angle = sin_angle(opposite_side, hypotenuse_side)
                new_list_two.append(subject_angle)

            elif subject_angle in new_list_two and opposite_side not in new_list_two:
                opposite_side = sin_opposite(subject_angle, hypotenuse_side)
                new_list_two.append(opposite_side)

        elif adjacent_side in new_list_two:

            if opposite_side in new_list_two and subject_angle not in new_list_two:
                subject_angle = tan_angle(opposite_side, adjacent_side)
                new_list_two.append(subject_angle)

            elif subject_angle in new_list_two and opposite_side not in new_list_two:
                opposite_side = tan_opposite(subject_angle, adjacent_side)
                new_list_two.append(opposite_side)

            elif subject_angle in new_list_two and hypotenuse_side not in new_list_two:
                hypotenuse_side = cos_hypotenuse(subject_angle, adjacent_side)
                new_list_two.append(hypotenuse_side)

        elif opposite_side in new_list_two:

            if subject_angle in new_list_two and hypotenuse_side not in new_list_two:
                hypotenuse_side = sin_hypotenuse(subject_angle, opposite_side)
                new_list_two.append(hypotenuse_side)

            elif subject_angle in new_list_two and adjacent_side not in new_list_two:
                adjacent_side = tan_adjacent(subject_angle, opposite_side)
                new_list_two.append(adjacent_side)

    #result printing
    print
    print "Side Lengths"
    print "Opposite:   " + str(round(opposite_side, 3))
    print "Adjacent:   " + str(round(adjacent_side, 3))
    print "Hypotenuse: " + str(round(hypotenuse_side, 3))
    print
    print "Angle Sizes in Degrees"
    print "Right Angle:   " + str(90.000)
    print "Subject Angle: " + str(round(subject_angle, 3))
    print "Other Angle:   " + str(round(other_angle, 3))
    print

    #result checking
    if subject_angle + other_angle < 89 or subject_angle + other_angle > 91:
        print "Looks like the angles are a bit off, try doing your calculations again."
    elif opposite_side >= hypotenuse_side or adjacent_side >= hypotenuse_side:
        print "Looks like the side lengths are a bit off, try doing your calculations again."
    print "End of Program!"
    print