vowel=("a","e","i","o","u")
count = 0
count1 = 0 
user= input("enter sentence ")
i=0
while i<len(user):  
    if user[i] in vowel:  
        count = count + 1  
    elif (user[i] >= 'a' and user[i] <= 'z'):  
        count1 = count1 + 1
    i+=1  
print("vowel:",count) 
print("consonent:",count1)

#Vowel consonant count

user = input(" enter the name ")
vowels = 0
consonants = 0
for i in user:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
       or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1
 
print("number of vowels ", vowels)
print("number of consonats", consonants)