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
  formattedTime = str(formattedHrs) + ':' + str(formattedMins)

  print('Hr:', intHr)
  print('Min:', intMin)
  print('AM/PM:', startDay)
  print('Start time is ', militaryMin, 'minutes past midnight.')
  print('Total duration is', totalDur, 'minutes.')
  print('The end time is', endTime, 'minutes after midnight.')
  print('Or:', formattedTime)
  #return new_time

print(add_time("3:30 PM", "2:12"))