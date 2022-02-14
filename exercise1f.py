# Create a basic function that returns True if the word 'elephant' is contained in the input string.
# Don't worry about edge cases like a punctuation being attached to the word dog, but do
# account for capitalization.


inputString = 'i am an Elephant'
target = 'elephant'


def contains_elephant(test_string, target_phrase):
    result = False
    if target_phrase in test_string.lower():
        result = True
    return result


print(contains_elephant(inputString, target))
