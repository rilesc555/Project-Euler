import math
import threading
import time

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
    

def sum35(n):
    total = 0
    for i in range(1, n):
        if i%3 == 0 or i%5 == 0:
            total += i

    return total


'''Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
appended fibonaccis to solutions list and added the even ones until last fibonacci is over limit. Anser is 4613732'''

def dynamicFibonacciEvenSum(limit, fibonaccis = [0,1]):
    total = 0
    while fibonaccis[-1] < limit:
        fibonaccis.append(fibonaccis[-2] + fibonaccis[-1])
        if not fibonaccis[-1] % 2 and fibonaccis[-1] < limit:
            total += fibonaccis[-1]

    return total


# Brute force for 3. greatest prime factor of a number. could be optimized but got it
def primesUnder(n):
    primes = []
    for i in range(2, n):
        isPrime = True
        for prime in primes:
            if i % prime == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)

    return primes

def greatestPrimeFactor(n):
    primes = primesUnder(math.floor(math.sqrt(n)))
    i = -1
    while n % primes[i] != 0:
        i -= 1
    return primes[i]


# 4. find largest palindrome product of 2 3-digit numbers. Might have some unnecessary code, but it's quick
def largestPalindrome(n1, n2):
 
    largest = 0
    left, right = n1, n2 
    tested = []
    largestLeft, largestRight = 0, 0

    while True:
        if left < 100:
            break
        if right <= 99:
            right = n2
            left -= 1
            if left * right < largest:
                break
        if left * right < largest:
            left -= 1
            right = n2
            if left * right < largest:
                break
        if [left,right] in tested:
            print(left, right, "already in tested")
            right -= 1
            continue
        print(left, right)
        answer = left * right
        answerString = str(answer)
        tested.append([right, left])
        if isPalindrome(answerString):
            largest = max(largest, answer)
            print(answer, "is a palindrome")
            print("Current Largest is", largest)

            if largest == answer:
                largestLeft, largestRight = left, right
            left -= 1
            right = n2
            continue
        right -= 1

    return largest
        

def isPalindrome(word):
    stack = []

    for i in word:
        stack.append(i)

    for i in range(len(word) // 2):
        if word[i] != stack.pop():
            return False
        
    return True

# 5 smallest number divisible by all numbers from 1-20. We know 2520 is smallest number divisible by 1-20, 
# so keep checking multiples of that for being divisble by 11-20 until answer is found
def smallestProduct(n):
    factors = [i for i in range(20, 10, -1)]
    answer = 2520

    while True:
        good = False
        answer += 2520
        for i in factors:
            temp = answer % i
            if temp != 0:
                break
            if i == 11:
                good = True
        if good:
            return answer
                    

    return answer

def sumSquareDifference(n):
    total = 0

    sum = 1

    for i in range(2, n + 1):
        temp = i * sum
        total += 2 * (temp)
        sum += i

    print(total)




    
    
    

        