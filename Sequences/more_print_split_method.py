sentence = "Lord Khorne, grant me your power that I might sweep this army " \
           "aside!"
print(sentence)

words = sentence.split()
print(words)
# split() returns a list
# Since we didn't provide any arguments to split(), it defaults to splitting
# strings using whitespaces

sentence2 = """Lord Khorne, grant\tme your power\tthat I might" \
            "sweep this army" \
            "aside!"""
words2 = sentence2.split(sep=",")
print(words2)
# Notice how Python considers the commas in the string as separators

numbers = "0,234,78,-1,-264,1,i,733,91"
print(numbers.split(","))