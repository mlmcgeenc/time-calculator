def test_func (start, duration):
  startTime, startMeridian = start.split()
  startHr, startMin = startTime.split(':')
  durHr, durMin = duration.split(':')

  sumMin = int(startMin) + int(durMin)
  addHr = 0
  halfDayCount = 0
  while sumMin > 60:
    sumMin = sumMin - 60
    addHr = addHr + 1
  sumHr = int(startHr) + int(durHr) + addHr
  while sumHr > 12:
    sumHr = sumHr - 12
    halfDayCount = halfDayCount + 1
  dayCount = int(halfDayCount/2)

  if dayCount == 0:
    dayOutput = ''
  elif dayCount == 1:
    dayOutput = ' the next day.'
  else:
    dayOutput = str(dayCount) + ' days later.'
  
  if (dayCount % 2) == 0:
    endDay = startMeridian
  else:
    if startMeridian == 'AM':
      endDay = 'PM'
    else:
      endDay = 'AM'

  print('Start Meridian:', startMeridian)
  print('End Time:', str(sumHr) + ':' + str(sumMin) + ' ' + endDay + ' ' + dayOutput)
  result = 'In testing'
  return result

print(test_func("10:45 PM", "72:30"))