def add_time(start, duration, dayName=''):
  startTime, meridian = start.split()
  startHr, startMin = startTime.split(':')
  durHr, durMin = duration.split(':')
  sumMin = int(startMin) + int(durMin)
  addHr = 0
  dayCount = 0
  week = {
    'monday': 1,
    'tuesday': 2,
    'wednesday': 3,
    'thursday': 4,
    'friday': 5,
    'saturday': 6,
    'sunday': 7
  }

  while sumMin > 60:
    sumMin = sumMin - 60
    addHr = addHr + 1
  sumHr = int(startHr) + int(durHr) + addHr
  while sumHr >= 12:
    sumHr = sumHr - 12
    if meridian == 'PM':
      meridian = 'AM'
      dayCount = dayCount + 1
    else:
      meridian = 'PM'
  if sumHr == 0:
    sumHr = 12

  if dayCount < 1:
    dayOutput = ''
  elif dayCount == 1:
    dayOutput = ' (next day)'
  else:
    dayOutput = ' (' + str(dayCount) + ' days later)'

  if dayName != '':
    weekDay = week[dayName.lower()]
    sumDays = weekDay + dayCount
    while sumDays > 7:
      sumDays = sumDays - 7
      continue
    for key, value in week.items():
      if sumDays == value:
        dayOfWeek = key
  else:
    dayOfWeek = ''
  
  finalString = str(sumHr) + ':' + ("{:02d}".format(sumMin)) + ' ' + meridian + dayOutput if dayOfWeek == '' else str(sumHr) + ':' + ("{:02d}".format(sumMin)) + ' ' + meridian + ', ' + dayOfWeek.capitalize() + dayOutput
  return finalString

print(add_time("11:40 AM", "0:25"))