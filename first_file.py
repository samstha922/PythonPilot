# foods=['bacon', 'cheese','pork', 'ham']
# for f in foods[:2]:
#     print (f)
#     print (len(f))

# for s in range(4,10,2):
#     print (s)

# while loop
# sam=5
# while sam<10:
#     print(sam)
#     sam += 1
#--------------------------------------------------------------------------------------
# magic=26;
# # check if magic number is present
# print('bucky',9)
# for n in range(50):
#     if n is magic:
#         print(n,'is the magic number')
#         break
#     else:
#         print(n)
#--------------------------------------------------------------------------

# numberToken=[2,15,19,8]
# print('Available numbers are:\n')
# #print(numberToken)
# for n in range(1,20):
#     if n in numberToken:
#         continue        #skips whatever after the loop but keeps going with the loop without breaking loop
#     print(n)

#----function
# def pork():
#     print('sam is cool')
# def bitcoin_to_usd(btc):
#     amount=btc*527
#     print(amount)
#
# #pork()
# bitcoin_to_usd(3.85)
# bitcoin_to_usd(38)
# bitcoin_to_usd(100)

# ---------------fxn with multiple return values IMP (need to brainstorm)-------------------

# def allowed_dating_age(my_age):
#     girls_age=my_age/2 + 7
#     girls_max_age= my_age+7
#     return {'girls_age':girls_age, 'girls_max_age':girls_max_age}   #stored values in list
#
#
# my_min_limit=allowed_dating_age(24)['girls_age']
# my_max_limit=allowed_dating_age(24)['girls_max_age']
# print('My girl\'s min. age limit is:',my_min_limit,'and max age limit is:', my_max_limit)
#


##---------------default values-----
# def get_gender(sex='unknown'):  # default value is unknown in sex
#     if sex is 'm':
#         sex='male'
#     elif sex is 'f':
#         sex='female'
#     print (sex)
# get_gender('m')
# get_gender('f')
# get_gender()

# #----var scope
#
# a=78
# def corn():
#     print(a)
# def fudge():
#     print(a)
#
# corn()
# fudge()

# #------- keyword arg
# def dumb_sentence(name='bucky', action='ate',item='tuna'):
#     print(name, action, item)
#
# dumb_sentence() #takes default args
# dumb_sentence('sally','works','gently')   #overrides arguments
# dumb_sentence(item='awesome', action='is')   #override specific arguments

# flexible number of args

##-----concatenating different datatypes
# s=19//7
##use format or can also use ',' or 'f'
# print('string is:{}'.format(s))


##-----if and elseif
# age =30
# if age<21:
#     print('21-')
#     #check 'and' keyword ahere
# elif age<24 and age>=21:
#     print('24- and 21+')
# else:
#     print('24+')

##--returning a value from fxn
# def age(girl):
#     if girl<18:
#         x= 'teen'
#         return x
#     elif girl>=18 and girl <30:
#         x='suitable'
#         return x
#     else:
#         x= 'old'
#         return x
# y=age(54)
# print(y)

# #----flexible number of arguments
# #*args means flexible no. of argumaents
# def total_no(*args):
#         total=0
#         for a in args:
#             total+=a
#         print (total)
#
# total_no(13)
# total_no(1231,1321,16544,456)

# #-------unpacking arguments
# def health_calc(age, apple_ate, cigs_packed):
#       answer= (100-age)+(apple_ate*3.3)-(cigs_packed*2)
#       print('YOur health rating is',answer)
#
# buckys_data=[27,20,9]
# # unpacking the arguments down
# health_calc(*buckys_data)
# # same as above code thus above reduces the below code
# # health_calc(buckys_data[0],buckys_data[1],buckys_data[2])


# # -------------sets {} curly bracket are sets
# groceries={'cereal','beer','milk','rice','lotion'}
# print (groceries)
#
# if 'milk' in groceries:
#     print('u already have milk')
# else:
#     print('u need milk')

# -----------------data dictionary: are unordered key value paits in python

# classmates = {'Tony':'cool but smily', 'Emma':'sits behind', 'Lucy':'asks for ppl'}
# print(classmates['Tony'])
# # k and v are syntax with items also a keyword
# for k,v in classmates.items():
#     print(k+v)

