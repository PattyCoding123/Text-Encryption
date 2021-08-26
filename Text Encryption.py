# Patrick Ducusin

def transposeText(s):

    #initializing
    encryptedFirst = '' 
    encryptedSecond = '' 
    encryptedThird = ''
    finalText = ''
    
    #To break the string into multiple substrings, start by doing a for loop from 0 to len(string) since indices go from 0 to length - 1 and range does the same thing.
    #The for loop will keep repeating until no more substrings of length n can be made.
    #Next, make the step (interval) equal to the amount of characters you want in a substring. In this case, we want 3 characters in each substring.

    for i in range(0,len(s),3):
        subString = list(s[i:i+3]) #The subString variable will be assigned to a list of the different substrings that cane from the main string.
                                   #This will make the substring start at j and go to j+3. This will have characters j, j+1, and j+2 in the substring.

        for index,character in enumerate(subString):
            if(index == 2): #For the third character in the substring, it will be assigned to encryptedFirst
                encryptedFirst += subString[index]

            elif(index == 1): #For the second character in the substring, it will be assigned to encryptedSecond
               encryptedSecond += subString[index]

            elif(index == 0): #For the first character in the substring, it will be assigned to encryptedThid
                encryptedThird += subString[index]

        finalText = encryptedFirst + encryptedSecond + encryptedThird
        #The final encrypted message will be constructed by putting all the final characters to the front, then adding the second character of each string next.
        #Finally, the first character in each string are added last to the final encrypted message.

    print(s,'->',finalText)

transposeText('ABCDEFGHI')
transposeText('JACK IN THE BOX')    
                
                                        
