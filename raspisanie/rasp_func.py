from raspisanie import znamenatel, chislitel
import datetime

start_of_sem = datetime.datetime(2023, 2, 6).strftime('%W')
actual_week = datetime.datetime.now().strftime('%W')
week = (int(actual_week) - int(start_of_sem) + 1)
while (True):
  now = datetime.dateime.now().strfrime('%H')