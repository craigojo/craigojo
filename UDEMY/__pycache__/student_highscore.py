# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇

highest_score = 0

for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"high score = {highest_score}")

# number_of_students = 0
# for student in student_heights:
#   number_of_students += 1

# print(f"number of students = {number_of_students}")

# average_height = round(total_height / number_of_students)
# print(f"average height = {average_height}")