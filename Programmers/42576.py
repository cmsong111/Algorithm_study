#1 try
def solution(participant, completion):
    completion_len = len(completion)
    
    for i in range(completion_len):
        if completion[i] in participant:
            temp = participant.index(completion[i])
            participant.pop(temp)
    
    answer = participant[0]
        
    return answer



#2 try
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    answer = participant.pop()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i] 
            break
   
    return answer

#3 try
def solution(phone_book):
    phone_book.sort()
    answer = True
    phone_book_len = len(phone_book)
        
    for i in range(phone_book_len-1):
        test = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][:test]:
            answer = False
            break
    
    return answer