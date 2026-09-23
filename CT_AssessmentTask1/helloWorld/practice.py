import datetime

date = datetime.datetime.now()
print(date)

all_students_attendance = []

while True:
    user_input = int(input("Enter the amount of students attending "))
    
    if user_input == -1:
        break
    
    all_students_attendance.append(user_input)

count_over_25 = 0
for attendance in all_students_attendance:
    if attendance > 25:
        count_over_25 += 1

print("Attendance Report")
print("Highest attendance:", max(all_students_attendance))
print("Lowest attendance:", min(all_students_attendance))

average_attendance = sum(all_students_attendance)/len(all_students_attendance)
print("Average attendance:", average_attendance)

print("Number of attendances over 25:", count_over_25)

