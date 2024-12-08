def pig_latinfy(sentence):
    words = sentence.split()
    new_sentence = [word[1:] + word[0] +"ay" for word in words]
    return " ".join(new_sentence)
sentence = input("Enter a sentence to be pig-latinfied: ")
new_sentence = pig_latinfy(sentence)
print(new_sentence)