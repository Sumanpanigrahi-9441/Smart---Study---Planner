from datetime import datetime

GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"




print(CYAN + "===== SMART STUDY PLANNER =====" + RESET)

subject = input("Enter Subject name: ")
exam_date = input("Enter Exam date (YYYY-MM-DD): ")
study_hours = float(input("Hours you can study daily: "))

today = datetime.today()
exam = datetime.strptime(exam_date, "%Y-%m-%d")

days_left = (exam - today).days

if days_left <= 0:
    print(RED + "Exam date already passed!" + RESET)
else:
    total_hours = days_left * study_hours

    print(BLUE + "\n----- STUDY PLAN -----" + RESET)
    print(GREEN + "Subject:" + RESET, subject)
    print(YELLOW + "Days Left:" + RESET, days_left)
    print(YELLOW + "Daily Study Hours:" + RESET, study_hours)
    print(YELLOW + "Total Available Study Hours:" + RESET, total_hours)

    print(CYAN + "\nRecommended Plan:" + RESET)
    print("40% Time -> Revision")
    print("40% Time -> New Topics")
    print("20% Time -> Practice Questions")

