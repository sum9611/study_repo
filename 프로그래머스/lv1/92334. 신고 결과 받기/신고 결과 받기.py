def solution(id_list, report, k):
    id_dict = {}
    report_dict = {}
    answer = []   
    for id in id_list:
        id_dict[id] = []
        report_dict[id] = 0
        
    for r in report :
        user, target = r.split(' ')
        if target not in id_dict[user]:
            id_dict[user].append(target)
            report_dict[target] += 1
            
    for i in id_dict:
        cnt = 0
        for j in id_dict[i]:
            if report_dict[j] >= k:
                cnt += 1
        answer.append(cnt)
            
    
    
  
    return answer