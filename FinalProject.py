import csv
import random

def main():
    name: str = input("Enter your name: ")
    while True:
        try:
            difficulty: str = input(f"Enter Difficulty level {name}: ").strip().lower()
            file: str = level(difficulty)
            score: int = generate_quiz(file)
            break
        except (ValueError , FileNotFoundError):
            print("Invalid Input!")
            continue
    print("\n\n\n=============================================================\n\n\n")
    print(f"\t\t{name.capitalize()} Your final score is: {score}")
    print("\n\n\n=============================================================")
    upload_score(score, name, difficulty)


def level(n: str) -> str:
    if n == "easy":
        return "easy.csv"
    elif n == "medium":
        return "medium.csv"
    elif n == "hard":
        return "hard.csv"
    else:
        raise ValueError("Invalid level")


def generate_quiz(file: str) -> int:
    score: int = 0
    with open(file) as f:
        reader= csv.DictReader(f)
        for row in reader:
            if ask_question(row):
                score += 1
    return score

def ask_question(row: dict) -> bool:
    print(row["question"])
    options: list = row["options"].split("|")
    random.shuffle(options)
    for i in range(1 , len(options) + 1):
        print(f"{i}){options[i-1]}" , end = " ")
    print()
    try:
        answer: int = int(input("\nEnter option Number (1,2,3,4): "))
        if options[int(answer)-1] == row["answer"]:
            print("Correct!!!\n")
            return True
        else:
            print(f"Wrong The correct answer is: {row['answer']}\n")
            return False
    except (ValueError , IndexError):
        print("Invalid Option! Question Skipped.")
        return False

def upload_score(score: int , name: str , difficulty: str) -> None:
    with open("result.txt" , "a") as f:
        f.write(f"{name} , {difficulty} , {score}\n")

if __name__ == "__main__":
    main()
