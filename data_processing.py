sentence1 = input("Please enter a sentence: ")
sentence1_formatted = sentence1.strip().upper()
print(sentence1_formatted)

paragraph1 = input("Please enter a paragraph: ")
paragraph1_formatted = (paragraph1.strip().capitalize().count(" ")+1)
print(f"the paragraph has {paragraph1_formatted} words. ")

string = input("Please enter a string: ")
string_formatted = (string.strip().isdigit())
print(string_formatted)

string2 = input("Please enter another string: ")
string2_formatted = (string2.strip())
print(string2_formatted)



def initials(name):
    return '.'.join(x[0] for x in name.strip().split()).upper()

name = input("Please enter your full name: ")
name_formatted = (initials(name))
print(f"Your initials are: {initials(name)} ")


string3 = len(input("Please enter one more string: "))
print(f"The length of your string is: {string3}")
