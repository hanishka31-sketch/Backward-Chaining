# Student Academic Guidance - Backward Chaining

facts = {
    "CGPA_Above_7",
    "Attendance_Above_75",
    "No_Backlogs",
    "Completed_Mini_Project",
    "Solved_50_Coding_Problems"
}

rules = {
    "GoodAcademicPerformance": ["CGPA_Above_7", "Attendance_Above_75"],
    "StrongPracticalSkills": ["Completed_Mini_Project", "Solved_50_Coding_Problems"],
    "EligibleForPlacement": [
        "GoodAcademicPerformance",
        "No_Backlogs",
        "StrongPracticalSkills"
    ]
}

def backward(goal):
    print("Goal:", goal)

    if goal in facts:
        print(goal, "-> FACT")
        return True

    if goal in rules:
        for condition in rules[goal]:
            if not backward(condition):
                return False
        print(goal, "-> PROVED")
        return True

    print(goal, "-> NOT PROVED")
    return False


# Main
goal = "EligibleForPlacement"

result = backward(goal)

print("\nFinal Result:")
if result:
    print("Student is Eligible for Placement")
else:
    print("Student is Not Eligible for Placement")