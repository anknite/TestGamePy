#-*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------#
#Note: Translation rule - double every consonant and place an occurrence of “o” in between.
#For example, the string “this is fun” is translated into the string “tothohisos isos fofunon”.
#This python script takes in a string from user and prints its translation.
#-----------------------------------------------------------------------------------------------#
 
#creates a prompt like environment
prompt = "> "
print "Enter a string"

#takes in user input
user_string = raw_input(prompt)
translated_string = user_string

#consonants array
con=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

#for all values in consonants if exist in s
for ch in con:
    if ch in translated_string:

        #replacement according to rule
        translated_string = translated_string.replace(ch,ch+'o'+ch)

print user_string
print translated_string


