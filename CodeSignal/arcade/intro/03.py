def solution(inputString):
    return inputString == inputString[::-1]

# using slice() for variable "inputString"
# :: used to specify how a slice operation should work
# -1: reverse string
# check the first character to the last character of the string and second last one and so on