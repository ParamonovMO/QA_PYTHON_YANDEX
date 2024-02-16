time = '1h 45m,360s,25m,30m 120s,2h 60s'

total_minutes = 0

time_list = time.replace(',', ' ').split(' ')

for time in time_list:
    if 'h' in time:
        hours = int(time.replace('h', ''))
        total_minutes += hours * 60
    
    if 'm' in time:
        minutes = int(time.replace('m', ''))
        total_minutes += minutes
   
    if 's' in time:
        seconds = int(time.replace('s', ''))
        total_minutes += int(seconds // 60)
 
print(f'Общее количество минут: {total_minutes}')