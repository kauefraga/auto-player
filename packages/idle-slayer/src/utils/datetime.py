from datetime import datetime

def get_time_and_datetime():
  """Returns the current time and datetime formatted with strftime.
    @example ['12:30:50', '12.30-15.5.2023']
    @returns [time, datetime]
  """
  now = datetime.now()

  return [
    now.strftime('%H:%M:%S'),
    now.strftime('%H.%M-%d.%m.%Y')
  ]
