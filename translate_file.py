#-*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------#
#Note: Translation rule - double every consonant and place an occurrence of “o” in between.
#For example, the string “this is fun” is translated into the string “tothohisos isos fofunon”.
#This python script takes in a file name from user and creates another file containing translation.
#-----------------------------------------------------------------------------------------------#
 

#creates a prompt like environment
prompt = "$ "
print "Please enter file you want to translate.."

#Takes in a valid existing filename
file_name = raw_input(prompt)
open_file = open(file_name)
file_data = open_file.read()
translated_data = file_data

#consonant array
con = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

#for all values in consonants if exist in s
for ch in con:
    if ch in translated_data:
       
        #replacement according to rule
        translated_data = translated_data.replace(ch,ch+'o'+ch)


#create a new file to store translation
new_file = open('translated_'+file_name,'w')
for i in translated_data:
   new_file.write(i)


if new_file:
    print "File translated_"+file_name+" created"
#close all filehandles
open_file.close()
new_file.close

