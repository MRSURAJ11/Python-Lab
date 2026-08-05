## single quote string

# name='Ritika'
# print(name)

##double quote string 
# message="Hello World"
# print(message)

##triple quote string 
# address = """Kolhapur,
# Maharashtra,
# India"""
# print(address)

# ##1.string length 
# string=input("Enter a string:")
# count=0
# for ch in string:
#     count+=1
# print("length of the string is",count)

##2.Character Count 
## Count the number of vowels, consonants, digits, spaces, and special characters in a given string. 

# string=input("Enter a string:")
# vowels = consonants = digits = spaces = special = 0
# for ch in string:
#     if ch.lower() in "aeiou":
#         vowels += 1
#     elif ch.isalpha():
#         consonants += 1
#     elif ch.isdigit():
#         digits += 1
#     elif ch.isspace():
#         spaces += 1
#     else:
#         special += 1

# print("Vowels:", vowels)
# print("Consonants:", consonants)
# print("Digits:", digits)
# print("Spaces:", spaces)
# print("Special Characters:", special)

##3.Reverse a String 
##Reverse the given string without using built-in reverse functions.
 # string=input("Enter a string:")
# reverse=""

# for ch in string:
#     reverse=ch+reverse
# print("reversed string",reverse)

##4.Palindrome Check 
##Check whether the entered string is a palindrome.

# string=input("Enter a string:")
# reverse=""
# for ch in string:
#     reverse=ch+reverse
# if string==reverse:
#         print("palindrome")
# else:
#         print("not palindrome") 

##5.Uppercase and Lowercase Count 
##Count the number of uppercase and lowercase letters in a string. 
# string=input("Enter a string")
# uppercase=0
# lowercase=0
# for ch in string:
#     if ch.isupper():
#         uppercase+=1
#     elif ch.islower():
#         lowercase+=1
# print("uppercase letters",uppercase)
# print("lowercase letters",lowercase)

##6.Replace Characters 
##Replace all occurrences of a given character with another character.

# string=input("Enter a string:")
# old=input("Enter a character to replace:")
# new=input("Enter the new character:")
# result=""
# for ch in string:
#     if ch==old:
#         result+=new
#     else:
#         result+=ch
# print("updated string:",result)

##7.Remove Spaces 
##Remove all spaces from the input string. 
# string = input("Enter a string: ")

# result = ""

# for ch in string:
#     if ch != " ":
#         result += ch

# print("String without spaces:", result)

# string = input("Enter a string: ")
# char = input("Enter the character to find: ")

# count = 0

# for ch in string:
#     if ch == char:
#         count += 1

# print("Frequency of", char, "is:", count)

##9.First and Last Character 
##Print the first and last character of a string
# string = input("Enter a string: ")
# print("First character:", string[0])
# print("Last character:", string[-1])

##10.ASCII Values 
##Display each character of a string along with its ASCII value.
# string=input("Enter a string:")
# for ch in string:
#     print(ch,":",ord(ch))

##11 count word 
##count the total no.of words in sentence
# sentence=input("Enter a string:")
# words=sentence.split()
# print("total no.of words",len(words))

##12.Longest Word 
##a.Find the longest word in a given sentence. 

# string=input("Enter a string:")
# words=string.split()
# longest=words[0]
# for word in words:
#     if len(word) > len(longest):
#         longest=word
# print("longest word in sentence is",longest)        

##13.Shortest Word 
##a.Find the shortest word in a sentence.
 
# string=input("Enter a string:")
# words=string.split()
# shorest=words[0]
# for word in words:
#     if len(word) < len(shorest):
#         shorest=word
# print("shorest word in sentence is",shorest) 

##14.Title Case 
##a.Convert the first letter of every word to uppercase.

# string=input("Enter a string:")
# words = string.split()
# result=" "
# for word in words:
#     result += word[0].upper() + word[1:]+""
#     print("Title case:",result)

##15.Duplicate Characters 
##a.Print all duplicate characters in a string

# string=input("Enter a string:")
# for ch in string:
#     if string.count(ch)>1:
#         print(ch)

##16.Character Frequency 
##a.Display the frequency of every character in a string. 
# string=input("Enter a string:")
# printed=""
# for ch in string:
#     if ch not in printed:
#      print(ch,":",string.count(ch))
#     printed+=ch

##17.Anagram Check 
##a.Check whether two strings are anagrams

# string1=input("Enter a string:")
# string2=input("Enter a string:")

# if sorted(string1) == sorted(string2):
#     print("Anagram")
# else:
#     print("Not Anagram")

##18.Remove Duplicate Characters 
##a.Remove duplicate characters while maintaining the original order. 

# string=input("Enter a string:")
# result=""
# for ch in string:
#     if ch not in result:
#         result+=ch
# print("string after removing the duplicates:",result)

##19.Substring Search 
##a.Check whether a given substring exists in the main string. 
# string=input("Enter a  main string:")
# substring=input("Enter a substring:")
# if substring in string:
#  print("substring found")
# else:
#    print("substring not found")

##20.Count Occurrences of a Word 
##a.Count how many times a specific word appears in a sentence. 
# sentence=input("Enter a sentence:")
# word=input("Enter the word to count:")
# count=sentence .split().count(word)
# print("Number of word occured in string:",count)

##21.Password Validator
#Minimum 8 characters 
#At least one uppercase letter 
#One lowercase letter 
#One digit 
#One special character

# password = input("Enter a password: ")

# uppercase = 0
# lowercase = 0
# digit = 0
# special = 0

# for ch in password:
#     if ch.isupper():
#         uppercase += 1
#     elif ch.islower():
#         lowercase += 1
#     elif ch.isdigit():
#         digit += 1
#     else:
#         special += 1

# if len(password) >= 8 and uppercase >= 1 and lowercase >= 1 and digit >= 1 and special >= 1:
#     print("Valid Password")
# else:
#     print("Invalid Password")

##22.Run-Length Encoding
#●Compress a string by counting consecutive repeated characters. 
#●Example:
#Input: aaabbccccd
#Output: a3b2c4d1

# string=input("Enter a string:")
# count=1
# for i in range(len(string) - 1):
#     if string[i] == string[i + 1]:
#         count += 1
#     else:
#         print(string[i], count, end="")
#         count = 1

# print(string[-1], count)

##23.String Compression 
##●Compress repeated characters and return the original string if compression does not reduce the length
# s=input("Enter a string:")
# compressed=""
# count=1
# for i in range(len(s) - 1):
#     if s[i] == s[i + 1]:
#         count += 1
#     else:
#         compressed = compressed + s[i] + str(count)
#         count = 1

# compressed = compressed + s[-1] + str(count)

# if len(compressed) < len(s):
#     print("Compressed String:", compressed)
# else:
#     print("Original String:", s)

#24.Most Frequent Character 
#●Find the character with the highest frequency. 

# s = input("Enter a string: ")

# max_char = s[0]
# max_count = s.count(s[0])

# for ch in s:
#     if s.count(ch) > max_count:
#         max_count = s.count(ch)
#         max_char = ch

# print("Most Frequent Character:", max_char)
# print("Frequency:", max_count)

##25.Second Most Frequent Character 
#●Find the second most frequently occurring character. 

# s = input("Enter a string: ")

# first_char = ""
# second_char = ""
# first_count = 0
# second_count = 0

# for ch in s:
#     count = s.count(ch)

#     if count > first_count:
#         second_count = first_count
#         second_char = first_char

#         first_count = count
#         first_char = ch

#     elif count > second_count and ch != first_char:
#         second_count = count
#         second_char = ch

# print("Second Most Frequent Character:", second_char)
# print("Frequency:", second_count)

##26.Caesar Cipher 
##●Encrypt and decrypt a message using the Caesar Cipher algorithm

# text = input("Enter a message: ")
# shift = int(input("Enter shift value: "))

# encrypted = ""

# for ch in text:
#     if ch.isalpha():
#         encrypted = encrypted + chr(ord(ch) + shift)
#     else:
#         encrypted = encrypted + ch

# print("Encrypted Message:", encrypted)

# decrypted = ""

# for ch in encrypted:
#     if ch.isalpha():
#         decrypted = decrypted + chr(ord(ch) - shift)
#     else:
#         decrypted = decrypted + ch

# print("Decrypted Message:", decrypted)

##27.Email Validator 
##●Validate whether a given email address follows a valid format. 

# text = input("Enter a message: ")
# shift = int(input("Enter shift value: "))

# encrypted = ""

# for ch in text:
#     if ch.isalpha():
#         encrypted = encrypted + chr(ord(ch) + shift)
#     else:
#         encrypted = encrypted + ch

# print("Encrypted Message:", encrypted)

# decrypted = ""

# for ch in encrypted:
#     if ch.isalpha():
#         decrypted = decrypted + chr(ord(ch) - shift)
#     else:
#         decrypted = decrypted + ch

# print("Decrypted Message:", decrypted)

#28.Word Frequency Dictionary 
#●Count the frequency of every word in a paragraph. 

# para = input("Enter a paragraph: ")

# words = para.split()

# freq = {}

# for word in words:
#     if word in freq:
#         freq[word] += 1
#     else:
#         freq[word] = 1

# print("Word Frequency:")

# for word in freq:
#     print(word, ":", freq[word])

#29.Sentence Reversal 
#●Reverse the order of words in a sentence without changing the words themselves. 
#●Example:
#●Input: Python is easy
#Output: easy is Python

# s = input("Enter a sentence: ")

# words = s.split()

# reverse_words = words[::-1]

# result = " ".join(reverse_words)

# print("Reversed Sentence:", result)

##30.String Rotation 
#●Check whether one string is a rotation of another. 

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("String is a rotation.")
else:
    print("String is not a rotation.")



