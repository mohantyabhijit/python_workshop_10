# Create a function that counts the number of times the word "elephant" occurs in a string.
# Again ignore edge cases.

def count_occurrences(test_string, target_string):
    print(test_string.count(target_string))


test = "There are 2 elephants in this sentence. One is here - elephant, one is here - elephant. So there are 2 " \
       "elephants. Ok? Oh no"
target = 'elephant'
print("The sample sentence is : ", test)
print("We have to find occurrences of {}".format(target))
count_occurrences(test, target)
