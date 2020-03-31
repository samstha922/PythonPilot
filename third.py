# #----------writing and reading files
# fp=open('testfile.txt','w')
# fp.write('My anme is sam.I study in class 12 laskfjkdslhjdskfjdsalfkjadsflkjdaslkj sdafkjdasjfkdsajflk  sflsadf  sdfljladskfj  ldsfkjkladsjflkdas')
# fp.close()

#-----------writing in file
import sys
import os.path

if os.path.exists('testfile2.txt'):
    # sys.exit('exists'+str(os.path.exists('testfile2.txt')))
    fp=open('testfile2.txt','a')
    textcontent = input('Enter the content to write in your existing file:')
    # fp.write(textcontent+'\n')

    while not textcontent:
        print('Error!!!Need to add something into the file')
        textcontent = input('Enter the content to write in file:')
    ## sys.exit('safd:{0}'.format(str(fp)))  ##die equivalent in python; for type oconversion: 'safd:'+sty(fp) also can be done

    fp.write(textcontent+'\n')
    text_add=input('Wanna add contents below it?(Y/N)')
    if text_add == 'Y' or text_add=='y':
        print('Enter the words to append:')
        textcontent=input()
        fp.write(textcontent+'\n')
    elif text_add == 'N' or text_add=='n':
        print('Good Bye')
    else:
        while text_add == 'Y' or text_add == 'N' or text_add == 'y' or text_add == 'n':
            print('Invalid input. Please enter again')
else:
    fp = open('testfile2.txt', 'w')

fp.close()

# #---reading from a file
# fp=open('testfile.txt','r')
# text=fp.read()
# lines=text.split('\n') #??????????????
# fp.close()
# print(text)