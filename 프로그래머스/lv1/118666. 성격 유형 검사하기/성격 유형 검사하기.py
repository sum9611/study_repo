
# 1번 지표	라이언형(R), 튜브형(T)
# 2번 지표	콘형(C), 프로도형(F)
# 3번 지표	제이지형(J), 무지형(M)
# 4번 지표	어피치형(A), 네오형(N)

def solution(survey, choices):
    dict = {'R' : 0, 'T': 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    score = [3, 2, 1, 0, 1, 2, 3]
    answer = ''
    for i,j in zip(survey, choices):
        if j-1 < 3: 
            dict[i[0]] += score[j-1]
        elif j -1 > 3:
            dict[i[1]] += score[j-1]
            
    if dict['R'] >= dict['T']:
        answer += 'R'
    else:
        answer += 'T'
        
    if dict['C'] >= dict['F']:
        answer += 'C'
    else:
        answer += 'F'
        
    if dict['J'] >= dict['M']:
        answer += 'J'
    else:
        answer += 'M'
        
    if dict['A'] >= dict['N']:
        answer += 'A'
    else:
        answer += 'N'
    
        
    return answer