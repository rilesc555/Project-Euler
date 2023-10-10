#returns number n or below with longest collatz sequence
def longestCollatz(n):
    answers = {1:1}
    longest = 1
    for i in range(2,n+1):
        if i in answers.keys():
            continue
        temp = i
        tempLength = 0
        while temp not in answers.keys():
            if temp%2 == 0:
                temp = temp/2
            else:
                temp = 3*temp + 1
            tempLength += 1
        answers[i] = tempLength + answers[temp]
        if answers[i] > answers[longest]:
            longest = i

    return longest
    

        