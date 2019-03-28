import csv
import os

# The dictionary that will hold all of the member points
member_points = {}  # type: dict

directory = os.fsencode("../checkin-forms")


def tallyPoints(input_file):
    for row in input_file:
        email = row["Email Address"]
        if email in member_points:
            member_points[email] += 1
        else:
            member_points[email] = 1


def addOutliers():
    # Mayli2020@u.northwestern.edu came to technical interview event
    # AND NSBE panel (2 points)
    member_points["mayli2020@u.northwestern.edu"] += 2


for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".csv"):
        print("Event: " + filename[:-4])
        input_file = csv.DictReader(open("../checkin-forms/" + filename))
        tallyPoints(input_file)

addOutliers()

with open("member_points.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    for key, value in member_points.items():
        writer.writerow([key, value])
