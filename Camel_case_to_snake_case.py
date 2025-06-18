"""Converting a camel case sentence to snake case sentence"""
#out: My_Name_Is_Archana

sentence="MyNameIsArchana"
for char in sentence[1:]:
    if char.isupper():
        sentence=sentence.replace(char,"_"+char)
print(sentence)
