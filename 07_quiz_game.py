QUESTIONS = [
    ("What is the capital of Bangladesh?", "dhaka"),
    ("Which language is this project written in?", "python"),
    ("What does CPU stand for? (3 words)", "central processing unit"),
    ("2 ** 5 = ?", "32"),
    ("Which data structure uses LIFO?", "stack"),
]

def main():
    score = 0
    for q, a in QUESTIONS:
        if input(q + " ").strip().lower() == a:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. Answer: {a}\n")
    print(f"Score: {score}/{len(QUESTIONS)}")

if __name__ == "__main__":
    main()
