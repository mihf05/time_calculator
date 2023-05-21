def add_time(start, duration, day=''):
  start_time, am_pm = start.split()
  start_hours, start_minutes = start_time.split(':')

  duration_hours, duration_minutes = duration.split(':')

  # convert hours to 24 format 
  start_hours = int(start_hours)
  if (start == '12:00 AM'):
    start_hours = 0
  elif (start == '12:00 PM'):
    start_hours = 12
  elif (am_pm == 'PM'):
    start_hours += 12

  # sum hours and minutes
  hours = int(start_hours) + int(duration_hours)
  minutes = int(start_minutes) + int(duration_minutes)
  
  #convert minutes to hours
  hours += minutes // 60
  minutes = minutes % 60
  minutes = str(minutes).rjust(2, "0")

  # calculate day of week
  days_of_week = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
  if (day != ''):
    day = day.lower()
    day = days_of_week.index(day)
    day += hours // 24
    day = day % 7
    day = days_of_week[day]
    day = day.capitalize()
    day = f', {day}'

  #calculate how many days later
  days_later = ''
  if (hours // 24 == 1):
    days_later = ' (next day)'
  elif (hours // 24 != 0):
    days_later = f' ({hours // 24} days later)'

  # convert hours back to 12 format
  hours = hours % 24
  if (hours == 0):
    am_pm = 'AM'
    hours = 12
  elif (hours < 12):
    am_pm = 'AM'
  elif (hours == 12):
    am_pm = 'PM'
  else:
    am_pm = 'PM'
    hours -= 12

  new_time = f'{hours}:{minutes} {am_pm}{day}{days_later}'

  return new_time