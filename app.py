def test_func (start, duration):
  startTime, meridian = start.split()
  startHr, startMin = startTime.split(':')
  durHr, durMin = duration.split(':')
  sumMin = int(startMin) + int(durMin)
  addHr = 0
  dayCount = 0

  while sumMin > 60:
    sumMin = sumMin - 60
    addHr = addHr + 1
  sumHr = int(startHr) + int(durHr) + addHr
  while sumHr > 13:
    sumHr = sumHr - 12
    if meridian == 'PM':
      meridian = 'AM'
      dayCount = dayCount + 1
    else:
      meridian = 'PM'

  if dayCount < 1:
    dayOutput = ''
  elif dayCount == 1:
    dayOutput = ' the next day.'
  else:
    dayOutput = str(dayCount) + ' days later.'

  print('End Time:', str(sumHr) + ':' + ("{:02d}".format(sumMin)) + ' ' + meridian + ' ' + dayOutput)
  result = 'In testing'
  return result

print(test_func("12:00 PM", "2:00"))