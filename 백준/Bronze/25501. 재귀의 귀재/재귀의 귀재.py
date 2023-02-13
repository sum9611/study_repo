test_case = int(input())
test_case_list = []

for i in range(test_case):
    test_case_list.append(input())
    

def recursion(s, l, r, cnt):
    if l >= r: return 1, cnt
    elif s[l] != s[r]: return 0, cnt
    else: return recursion(s, l+1, r-1, cnt+1)

def isPalindrome(s):
    cnt = 1
    return recursion(s, 0, len(s)-1, cnt)


for i in test_case_list:
    print(isPalindrome(i)[0], isPalindrome(i)[1])

