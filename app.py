def test_func (start, duration, dayName):
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
  weekDay = week[dayName]

  while sumMin > 60:
    sumMin = sumMin - 60
    addHr = addHr + 1
  sumHr = int(startHr) + int(durHr) + addHr
  while sumHr >= 13:
    sumHr = sumHr - 12
    if meridian == 'PM':
      meridian = 'AM'
      dayCount = dayCount + 1
    else:
      meridian = 'PM'

  if dayCount < 1:
    dayOutput = ''
  elif dayCount == 1:
    dayOutput = 'the next day.'
  else:
    dayOutput = str(dayCount) + ' days later.'

  sumDays = weekDay + dayCount
  if weekDay < 7:
    for key, value in week.items():
      if sumDays == value:
        dayOfWeek = key
  else:
    while sumDays > 7:
      sumDays = sumDays - 7
      continue
    for key, value in week.items():
      if sumDays == value:
        dayOfWeek = key

  print('End Time:', str(sumHr) + ':' + ("{:02d}".format(sumMin)) + ' ' + meridian + ' ' + dayOutput + ' ' + dayOfWeek)
  result = 'In testing'
  return result

print(test_func("12:00 PM", "72:00", 'sunday'))