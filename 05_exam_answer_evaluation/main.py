def evaluate_answers(key, answers):
    correct = incorrect = unanswered = 0
    for i in range(len(key)):
        if answers[i] == "":
            unanswered += 1
        elif answers[i] == key[i]:
            correct += 1
        else:
            incorrect += 1
    score = correct - 0.25 * incorrect
    print("\nEXAM RESULT")
    print("Correct answers:", correct)
    print("Incorrect answers:", incorrect)
    print("Unanswered:", unanswered)
    print(f"Final score: {score:.2f} out of {len(key)}")

print("EXAM ANSWER EVALUATOR")
try:
    count = int(input("Enter number of questions: "))
    if count <= 0:
        print("Number of questions must be positive.")
    else:
        key = []
        answers = []
        print("Enter the answer key (A/B/C/D):")
        for i in range(count):
            value = input(f"Correct answer for Q{i+1}: ").strip().upper()
            while value not in ["A", "B", "C", "D"]:
                value = input("Enter A, B, C or D: ").strip().upper()
            key.append(value)
        print("Enter student's answers. Press Enter if unanswered.")
        for i in range(count):
            value = input(f"Student answer for Q{i+1}: ").strip().upper()
            while value not in ["", "A", "B", "C", "D"]:
                value = input("Enter A, B, C, D or blank: ").strip().upper()
            answers.append(value)
        evaluate_answers(key, answers)
except ValueError:
    print("Please enter a valid whole number.")
