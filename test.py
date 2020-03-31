# # calling and returning fxns
# def squareNumber(theNumber):
#     return theNumber * theNumber
# print("3 squared is {0}".format(squareNumber(3)))

# #------making a class
# class Vehicle:
#     wheel=4
#     def vehicleEngine(self):
#         return 'helloinside'
#
# veh = Vehicle()
# print('variable:{0}'.format(veh.wheel)+'\n'+'function_display:{}'.format(veh.vehicleEngine()))


#---------
input_string=input('Please enter the string:')
str_len= len(input_string)
print(str_len)
formatted_str=[]

# for i in range[:str_len]:
#     if(i % 2 == 0):
#         input_string[i].upper()
#         formatted_str+=input_string[i]
# print(formatted_str)


#--------------making a constructor

# class Company:
#     def __init__(self,name,num_employee,business_area):
#         self.name=name
#         self.num_employee=num_employee
#         self.business_area=business_area


# -----making a costructor
class Person:
    def __init__(self,first, last):
        self.firstname = first
        self.lastname = last
    def fullname(self):






# #-------------multiple assignmennts
# def findMinAndMax(list):
#     min=list[0]
#     max=list[0]
#     for value in list:
#         if(value<min):
#             min=value
#         if(value>max):
#             max=value
#     return min,max
#
# numbers=[10,22,66,32,12,77,9]
# min,max=findMinAndMax(numbers)
#
# print("lowest is {0}, highest is {1}".format(min,max))

# #-----multiple return types
# def giveMeBeatles():
#     return "John","Sam","Ramesh"
#
# beatles=giveMeBeatles()
#
# print(beatles[0])
# print(beatles[2])