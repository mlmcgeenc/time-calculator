"3:30 PM", "2:12"

import re
import math
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
  formattedHrs = math.floor(endTimeHrs)
  formattedMins = int(math.fmod(endTime, 60))

  meridianFlip = 0
  while endTime > 720:
    endTime = endTime - 720
    meridianFlip = meridianFlip + 1
    continue

  if (meridianFlip % 2) == 0:
    endDay = startDay[0]
  else:
    if startDay[0] == 'AM':
      endDay = 'PM'
    else:
      endDay = 'AM'

  new_time = str(formattedHrs) + ':' + str(formattedMins) + ' ' + str(endDay)

  print('Hr:', intHr)
  print('Min:', intMin)
  print('Start Meridian:', startDay)
  print('Start time is ', militaryMin, 'minutes past midnight.')
  print('Total duration is', totalDur, 'minutes.')
  print('The end time is', endTime, 'minutes after midnight.')
  print('Or:', new_time)
  return new_time

print(add_time("2:05 AM", "12:00"))