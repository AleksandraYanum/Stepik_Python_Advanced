from datetime import date, time, datetime, timedelta


data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]

total_minutes = 0

for start_time_str, end_time_str in data:
    start_time = datetime.strptime(start_time_str, "%H:%M")
    end_time = datetime.strptime(end_time_str, "%H:%M")
    
    time_difference = end_time - start_time
    total_minutes += time_difference.total_seconds() // 60
