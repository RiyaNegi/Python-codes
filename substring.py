print("hey")
string = "micrrorometer"
small = "romea"

def is_valid(start_index, small, string):
    valid = True
    for i in range(len(small)):
        if small[i] != string[i + start_index]:
            valid = False
            break

    return valid

def is_substring(small, string):
    substring = False
    for start_index in range(len(string) - len(small) + 1):
        # print("Start index: ", start_index)
        substring = is_valid(start_index, small, string)
        if substring == True:
            return True
    return False

print(is_substring(small, string))
