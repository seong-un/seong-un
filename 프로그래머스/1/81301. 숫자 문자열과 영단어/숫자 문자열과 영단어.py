def solution(s):
    answer = ''
    number = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    string = ''
    for i in s:
        string += i
        if string in number:
            answer += str(number.index(string))
            string = ''
        if string.isdigit():
            answer += string
            string = ''
    return int(answer)