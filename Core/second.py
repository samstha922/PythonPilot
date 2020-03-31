# Python module index
# import first as f
# f.roll_a_dice(10)
# import calendar
# day=calendar.firstweekday()
# print('day'+str(day))
# # f.print_name("Sam")

# from student import Student
# student1 = Student("Jim","B.Tech",3.1, True)
# student2 = Student("Sam","B.B.A", 5, False)
# print(student2.major)

# from student import Student
# student1 = Student("Ram","BBA", 3.6, True)
# student2 = Student("Shyam", "BSW", 3.1, False)
# bool = student1.on_honor_role()
# if(bool == True):
#     print("On honor role")
# else:
#     print("Not on honor role")

# from Question import Question
# question_prompts = [
#     "What color is apple?",
#     "WHat color is banana?",
#     "WHat color is strawberry?"
# ]
#
# questions = [
#     Question(question_prompts[0], "red"),
#     Question(question_prompts[1], "yellow"),
#     Question(question_prompts[2], "red")
# ]
#
# def run_test(questions):
#     score = 0
#     for q in questions:
#         x = str(input(q.prompt))
#         if (x == q.answer):
#             score += 1
#     print("Your final score is "+str(score)+ " out of " + str(len(questions)))
#
# run_test(questions)
print ('sam')
# --------Inheritance---------------
from Core.student import *
# student1 = Student("Sam","BGA",,True)
# print(student1.on_honor_role())
teacher1 = Teacher('Sam',"BBA", "2.4", True)
print(teacher1.on_honor_role())

# print(teacher1.has_class())
# print(teacher1.on_honor_role())
'''Class Two'''
