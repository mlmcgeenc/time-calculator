def add_time(start, duration):
  startHr = re.findall("(\d+):", start)
  intHr = int(startHr[0])
  startMin = re.findall(":(\d+)", start)
  intMin = int(startMin[0])
  startDay = re.findall("(AM|PM)", start)

  if startDay == 'PM':
    militaryHr = (intHr * 60) + 720
  else:
    militaryHr = (intHr * 60)
  militaryMin = (militaryHr + intMin)

  durHr = re.findall("(\d+):", duration)
  intDurHr = int(durHr[0])
  durMin = re.findall(":(\d+)", duration)
  intDurMin = int(durMin[0])
  totalDur = (intDurHr * 60) + intDurMin

  endTime = militaryMin + totalDur
  endTimeHrs = endTime/60
  #formattedHrs = math.floor(endTimeHrs) - (meridianFlip * 12)
  formattedMins = int(math.fmod(endTime, 60))

  meridianFlip = 0
  while endTime > 720:
    endTime = endTime - 720
    meridianFlip = meridianFlip + 1
    continue

  if (meridianFlip/2) > 0:
    if (meridianFlip/2) <= 1:
      dayCount = 'next day'
    else:
      dayCount = str(meridianFlip) + ' days later'

  formattedHrs = math.floor(endTimeHrs) - (meridianFlip * 12)
  if formattedHrs == 0:
    displayHrs = 12
  else:
    displayHrs = formattedHrs

  if (meridianFlip % 2) == 0:
    endDay = startDay[0]
  else:
    if startDay[0] == 'AM':
      endDay = 'PM'
    else:
      endDay = 'AM'

  new_time = str(displayHrs) + ':' + str("{:02d}".format(formattedMins)) + ' ' + str(endDay) + ' ' + dayCount

  print('Start time is ', militaryMin, 'minutes past midnight.')
  print('Total duration is', totalDur, 'minutes.')
  print('The end time is', endTime, 'minutes after midnight.')
  return new_time

print(add_time("10:10 PM", "30:30"))