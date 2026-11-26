print("STUDENT MARKS MATRIX ANALYSIS")
try:
    student_count = int(input("Enter number of students: "))
    subject_count = int(input("Enter number of subjects: "))
    if student_count <= 0 or subject_count <= 0:
        print("Students and subjects must be greater than zero.")
    else:
        names = []
        subject_names = []
        marks = []
        for j in range(subject_count):
            subject_names.append(input(f"Enter subject {j+1} name: "))
        for i in range(student_count):
            name = input(f"Enter student {i+1} name: ")
            names.append(name)
            row = []
            for j in range(subject_count):
                mark = float(input(f"Enter {subject_names[j]} marks for {name} (0-100): "))
                while mark < 0 or mark > 100:
                    print("Marks must be between 0 and 100.")
                    mark = float(input(f"Enter {subject_names[j]} marks: "))
                row.append(mark)
            marks.append(row)
        totals = []
        print("\nSTUDENT RESULTS")
        for i in range(student_count):
            total = sum(marks[i])
            totals.append(total)
            print(names[i], "Total:", total, "Average:", round(total / subject_count, 2))
        print("\nSUBJECT AVERAGES")
        for j in range(subject_count):
            average = sum(marks[i][j] for i in range(student_count)) / student_count
            print(subject_names[j], ":", round(average, 2))
        top = totals.index(max(totals))
        print("\nTop student:", names[top], "with", totals[top], "marks")
except ValueError:
    print("Please enter valid numeric marks and counts.")
