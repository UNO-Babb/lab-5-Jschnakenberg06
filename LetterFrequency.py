#LetterFrequency.py
#Name:
#Date:
#Assignment:

#This program will create a CSV file of frequencies based on a text file.
#Use Excel or similar spreadsheet software to visualize the frequencies of the CSV file.

import os

def countLetters(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()

    freq = [0] * 26 

    for letter in message:
        if letter in alpha:
            index = alpha.index(letter)
            freq[index] += 1
    
    output_lines = ["Letter,Count"]
    for i in range(26):
        print(alpha[i], ":", freq[i])
        output_lines.append(f"{alpha[i]},{freq[i]}")

    writeToFile("\n".join(output_lines))

def writeToFile(fileText):
    file_name = "letter_frequencies.csv"

    with open(file_name, 'w') as freqFile:
        freqFile.write(fileText)
    
    print("Letter frequencies saved to:", file_name)

def main():
    msg = input("Enter a message: ")
    countLetters(msg)

if __name__ == '__main__':
    main()