from datetime import datetime, timedelta 
from dateutil.relativedelta import relativedelta
  
def exchange(date):
    yyyy = int(date.split('.')[0])
    mm = int(date.split('.')[1])
    dd = int(date.split('.')[2])  
    return yyyy,mm,dd
    
def solution(today, terms, privacies):
    dict = {}
    t_y, t_m, t_d = exchange(today)
    answer = []
    
    for i in terms:
        dict[i.split(' ')[0]] =i.split(' ')[1] 
    
    for i in range(len(privacies)):
        date = privacies[i].split(' ')[0]
        add_date = int(dict[privacies[i].split(' ')[1]])
        c_y, c_m, c_d = exchange(date)
        c_m += add_date     
        while c_m > 12:
            c_m -= 12
            c_y += 1

        c_d -= 1
        if c_d == 0:
            c_m -= 1
            c_d = 28
            if c_m == 0:
                c_m = 12
                c_y -= 1
        print(' ')
        print(t_y, t_m, t_d)
        print(c_y, c_m, c_d)
        # 비교 
        if t_y > c_y:
            answer.append(i + 1)
        elif t_y == c_y and t_m > c_m :
            answer.append(i + 1)
        elif t_y == c_y and t_m == c_m and t_d > c_d:
            answer.append(i + 1)
        


    return answer