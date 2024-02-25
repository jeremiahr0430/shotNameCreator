# def shotNameCreator():
#     name = input('put shot number in')
#     fullName = 'MNF'+
def insert_underscores(input_string):
    result = ''
    for i, char in enumerate(input_string):
        if i > 0 and i % 3 == 0:
            result += '_'
        result += char
    result = 'MNF_'+ result
    return result

original_string = input('put shot number here: ')
modified_string = insert_underscores(original_string)

# Write the modified string to a file
with open('output_file.txt', 'a') as file:
    file.write(modified_string + '\n')

print(f"Modified string: {modified_string}")
print("Result written to output_file.txt")

print(modified_string)
