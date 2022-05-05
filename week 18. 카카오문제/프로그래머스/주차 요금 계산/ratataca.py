from collections import defaultdict

def calc_total_payment(time, fees):
    default_time, default_payment, per_time, per_payment = fees
    
    if time <= default_time:
        return default_payment
    
    result = 0
    result += default_payment
    result += ((time - default_time) // per_time) * per_payment
    
    return result
    
    

def total_time(clock):
    hour, minute = clock.split(":")
    return int(hour) * 60 + int(minute)

def solution(fees, records):
    parking_states = defaultdict(list)
    
    for record in records:
        time, number, state = record.split(" ")
        if state == 'IN':
            parking_states[number].append(total_time(time))
        elif state == 'OUT':
            parking_states[number].append(total_time(time))
    
    print(parking_states)
    answer = defaultdict(int)
    # in은 있는데 out은 없는 경우
    for key, value in parking_states.items():
        if len(value) % 2 == 1:
            parking_states[key].append(total_time('23:59'))
        result = 0
        for idx in range(0, len(value), 2):
            in_time = parking_states[number][idx]
            out_time = parking_states[number][idx + 1]
            
            result += calc_total_payment(out_time - in_time, fees)
            
        answer[key] = result
            
    
    print(answer)
    
    
    
    # 어떤 차량이 입차된 후에 출차된 내역이 없다면, 23:59에 출차된 것으로 간주
    
    return answer.values()