#Name: Tanay Garg, Date: 29/10/2025, Project Title: Daily Calorie Tracker CLI

print("Many students want a quick and simple way to monitor their daily calorie intake. " \
"This mini project aims to help them build a Python-based CLI (Command Line Interface) tool " \
"where they can log their meals and keep track of total calories consumed, " \
"compare against a personal daily limit, and save session logs for future tracking.")


total_meals=int(input("Enter the total no. of meals you want to enter:"))
M=[]
C=[]
for i in range(total_meals):
    meal=input("Enter the name of the meal:")
    calorie_amount=int(input("Enter the total no. of calories of that meal:"))
    M.append(meal)
    C.append(calorie_amount)

sum=0
for i in range(len(C)):
    sum+=C[i]

avg= sum/total_meals

daily=int(input("Enter your daily total calories limit:"))

if daily<sum:
    print("WARNING!! Your total calories intake is more than your total daily limit!")
else:
    print("SUCCESS! Your total calories intake is under your total daily limit!")

print("Meal Name\tCalories")
print("-------------------------")
print(f"{M[0]}\t{C[0]}")
for i in range(1,total_meals):
    print(f"{M[i]}\t\t{C[i]}")
print(f"Total:\t\t{sum}")
print(f"Average:\t{avg}")

report=input("You want to save the report(yes/no)?:")
date=input("Enter today's date:")
if report=="yes":
    f=open("calorie_log.txt","w")
    f.write(f"{date}\n")
    f.write("Meal Name\tCalories\n")
    f.write("-------------------------\n")
    f.write(f"{M[0]}\t{C[0]}\n")
    for i in range(1,total_meals):
        f.write(f"{M[i]}\t\t{C[i]}\n")
    f.write(f"Total:\t\t{sum}")
    f.write(f"Average:\t{avg}")
    if daily<sum:
        f.write("STATUS: WARNING!! Your total calories intake is more than your daily limit!")
    else:
        f.write("STATUS: SUCCESS! Your total calories intake in under your total daily limit!")
    print("UPLOAD COMPLETED!")
else:
    pass