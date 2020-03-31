# #----modules (similar to templates in c) reusing fxn in different file
# # importing the file
# import second_module
# import random
# #second_module file ko fish fxn
# second_module.fish()
# # random number
# x= random.randrange(1,1000)
# print(x)


# # --------importing package from web
# import random
# import urllib.request
#
# def download_web_image(url):
#     name=random.randrange(1,2000)
#     full_name=str(name) + ".jpg"
#     urllib.request.urlretrieve(url,full_name)
#
#
# download_web_image("https://www.google.com.au/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")


# # ---------read and write files
# fw = open('sample.txt','w')
# fw.write('writing some stuff in text file\n I am stuffed')
# fw.write('I like bacon')
# fw.close()
#
# fr=open("sample.txt","r")
# text= fr.read()
# print (text)
# fr.close()



# #downloading files from web
#
# from urllib import request
# goog_url="http://samplecsvs.s3.amazonaws.com/SalesJan2009.csv"
#
# def data(csv_url):
#     response= request.urlopen(csv_url)
#     csv= response.read()
#     csv_str=str(csv)
#     lines=csv_str.split("\\n")
#     dest_url=r"google.com"
#     fx= open(dest_url,'w')
#     for line in lines:
#         fx.write(line + "\n")
#     fx.close()
#
# data(goog_url)

# #---------------checking out infinite loop with true in while
#
# while True:  # this is an infinite loop
#     command = input('Enter command:')
#     if len(command) == 0:  # no command - try again
#         continue  # goes to next loop (line 1)
#     elif command == 'exit':  # user exit
#         print('Goodbye')
#         break  # skips to line 10
#     else:
#         print(command)
# print('bye')

# #-------------------list comprehensions
# lines=['long','semester in last', 'long','last']
# trulines = [l for l in lines if l.find('last') > -1]
# print (trulines)


# ##-----separator
# print('one...', 'two...', 'three', sep='***')


