# Ex1 - Dictionary or object
# studentList [
#   {'id': 1, 'name': 'dara', 'age': 20},
#   {'id': 2, 'name': 'kaka', 'age': 20},
#   {'id': 3, 'name': 'bopha', 'age': 12},
#   {'id': 4, 'name': 'chompa', 'age': 40},
#   {'id': 5, 'name': 'chompey', 'age': 30},
#   {'id': 6, 'name': 'romdul', 'age': 60},
# ]

#1 - who is younger in list
# studentList = [
#   {'id': 1, 'name': 'dara', 'age': 10},
#   {'id': 2, 'name': 'kaka', 'age': 20},
#   {'id': 3, 'name': 'bopha', 'age': 12},
#   {'id': 4, 'name': 'chompa', 'age': 40},
#   {'id': 5, 'name': 'chompey', 'age': 8},
#   {'id': 6, 'name': 'romdul', 'age': 60},
# ]
# minAge = studentList[0]['age']
# studentName = ""
# for list in studentList:
#     if list['age'] <= minAge:
#         minAge = list['age']
#         studentName = list['name']
# print(studentName)


#2 - who  is older in list
# studentList = [
#   {'id': 1, 'name': 'dara', 'age': 10},
#   {'id': 2, 'name': 'kaka', 'age': 20},
#   {'id': 3, 'name': 'bopha', 'age': 12},
#   {'id': 4, 'name': 'chompa', 'age': 90},
#   {'id': 5, 'name': 'chompey', 'age': 8},
#   {'id': 6, 'name': 'romdul', 'age': 60},
# ]
# maxAge = studentList[0]['age']
# studentName = ""
# for list in studentList:
#     if list['age'] >= maxAge:
#         maxAge = list['age']
#         studentName = list['name']
# print(studentName)



#3 - how many student has the same age
# studentList = [
#   {'id': 1, 'name': 'dara', 'age': 10},
#   {'id': 2, 'name': 'kaka', 'age': 10},
#   {'id': 3, 'name': 'bopha', 'age': 12},
#   {'id': 4, 'name': 'chompa', 'age': 10},
#   {'id': 5, 'name': 'chompey', 'age': 8},
#   {'id': 6, 'name': 'romdul', 'age': 60},
# ]
# count = 0 
# age = studentList[0]['age']
# for list in studentList:
#   if list['age'] == age:
#     count += 1
# print(str(count) + " students have same age")



#4 - how many student older than "kaka"
# studentList = [
#   {'id': 1, 'name': 'dara', 'age': 10},
#   {'id': 2, 'name': 'kaka', 'age': 20},
#   {'id': 3, 'name': 'bopha', 'age': 72},
#   {'id': 4, 'name': 'chompa', 'age': 30},
#   {'id': 5, 'name': 'chompey', 'age': 8},
#   {'id': 6, 'name': 'romdul', 'age': 60},
# ]
# age = 0
# count = 0
# for list in studentList:
#     if list['name'] == 'kaka':
#         age = list['age']
# for list in studentList:
#     if list['age'] > age:
#         count += 1
# print(count)



#5 - remove student name "romdul" from the list
# studentList = [
#   {'id': 1, 'name': 'dara', 'age': 10},
#   {'id': 2, 'name': 'kaka', 'age': 20},
#   {'id': 3, 'name': 'bopha', 'age': 12},
#   {'id': 4, 'name': 'chompa', 'age': 40},
#   {'id': 5, 'name': 'chompey', 'age': 8},
#   {'id': 6, 'name': 'romdul', 'age': 60},
# ]
# index = None
# for i in range(len(studentList)):
#     if studentList[i]['name'] == "romdul":
#         index = i
# studentList.pop(index)
# print(studentList)