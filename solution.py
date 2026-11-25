# Case Study 66: Student Academic Risk Classification

def classify_students(names, academic_averages, attendance, lab_scores):
    if not (len(names) == len(academic_averages) == len(attendance) == len(lab_scores)):
        raise ValueError("All student lists must have equal lengths.")

    for values in (academic_averages, attendance, lab_scores):
        for value in values:
            if value < 0 or value > 100:
                raise ValueError("All marks and percentages must be between 0 and 100.")

    report = []
    counts = {"High Risk": 0, "Medium Risk": 0, "Low Risk": 0, "No Risk": 0}

    for index in range(len(names)):
        factors = []
        if academic_averages[index] < 40:
            factors.append("Low academic average")
        if attendance[index] < 75:
            factors.append("Low attendance")
        if lab_scores[index] < 40:
            factors.append("Low laboratory score")

        number_of_risks = len(factors)
        if number_of_risks == 3:
            category = "High Risk"
        elif number_of_risks == 2:
            category = "Medium Risk"
        elif number_of_risks == 1:
            category = "Low Risk"
        else:
            category = "No Risk"

        counts[category] += 1
        report.append((names[index], category, factors))

    return report, counts


def main():
    names = ["Aarav", "Sara", "Ibrahim", "Meera", "Kabir"]
    academics = [35, 55, 38, 72, 65]
    attendance = [68, 70, 82, 90, 78]
    labs = [30, 35, 32, 85, 55]
    report, counts = classify_students(names, academics, attendance, labs)

    print("STUDENT ACADEMIC RISK REPORT")
    print("-" * 58)
    for name, category, factors in report:
        reason = ", ".join(factors) if factors else "No risk factors"
        print(f"{name:12} {category:12} | {reason}")
    print("-" * 58)
    print("Category summary:")
    for category, count in counts.items():
        print(f"{category:12}: {count}")


if __name__ == "__main__":
    main()
