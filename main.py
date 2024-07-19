def isUnique(string):
    """ this checks if the string dosen't have reapeted characters """

    for i in range(len(string)):
        Unique_char = string[i]
        for char in range(1,len(string)):
            if(i==char):
                break;
            if string[char] == Unique_char and string[char] != " ":
                return False;
    return True;

def main():
    string = "abcdefg"
    print(isUnique(string))

main()