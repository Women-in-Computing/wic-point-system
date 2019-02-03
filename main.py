import csv

# The dictionary that will hold all of the member points
member_points = {}  # type: dict

#############################################
## PART 1: ATTENDANCE TO REGULAR WIC EVENT ##
#############################################

input_file = csv.DictReader(open("../checkin-forms/intro-to-tech.csv"))

for row in input_file:
    email = row["Email Address"]
    if email in member_points:
        member_points[email] += 1
    else:
        member_points[email] = 1
    print("\n")

for key, value in member_points.items():
    print("{}: {}".format(key, value))
    print("\n")
