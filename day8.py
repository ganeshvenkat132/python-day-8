import random
import pandas as pd
import numpy as np
import math

def generate_student_data(n):
    records = []

    for i in range(1, n + 1):
        marks = random.randint(0, 100)
        attendance = random.randint(0, 100)
        assignment = random.randint(0, 50)

        performance = (marks * 0.6 + assignment * 0.4) * math.log(attendance + 1)

        records.append((i, marks, attendance, assignment, performance))

    return records

def classify_students(data):
    categories = {
        "At Risk": [],
        "Average": [],
        "Good": [],
        "Top Performer": []
    }

    for record in data:
        student_id, marks, attendance, _, _ = record

        if marks < 40 or attendance < 50:
            categories["At Risk"].append(student_id)

        elif marks <= 70:
            categories["Average"].append(student_id)

        elif marks <= 90:
            categories["Good"].append(student_id)

        elif marks > 90 and attendance > 80:
            categories["Top Performer"].append(student_id)

    return categories


def analyze(data):
    df = pd.DataFrame(
        data,
        columns=["ID", "Marks", "Attendance", "Assignment", "Perf_Index"]
    )

    marks = df["Marks"]

    mean_marks = sum(marks) / len(marks)
    median_marks = np.median(marks)
    std_dev = np.std(marks)
    max_marks = max(marks)

    correlation = np.corrcoef(df["Marks"], df["Attendance"])[0][1]

    df["Normalized"] = [
        (x - min(marks)) / (max(marks) - min(marks))
        for x in marks
    ]

    unique_marks = set(marks)

    if std_dev < 15 and len(df[(df["Marks"] > 90) & (df["Attendance"] > 80)]) >= 2:
        insight = "Stable Academic System"

    elif len(df[df["Attendance"] < 50]) > 3:
        insight = "Critical Attention Required"

    else:
        insight = "Moderate Performance"

    return df, mean_marks, median_marks, std_dev, max_marks, correlation, insight

#main
n = int(input("Enter last digit of roll number: "))

data = generate_student_data(n)
categories = classify_students(data)

df, mean, median, std, max_m, corr, insight = analyze(data)

print("\nStudent details:\n")
print(df)

print("\nStudent categories:")
for key in categories:
    print(key, "->", categories[key])

print("\nBasic stats:")
print("Mean =", round(mean, 2))
print("Median =", median)
print("Std Dev =", round(std, 2))
print("Correlation =", round(corr, 3))

print("\nSome values:", (round(mean, 2), round(std, 2), max_m))

print("\nOverall remark:", insight)
