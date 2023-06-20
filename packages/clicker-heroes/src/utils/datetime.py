from datetime import datetime

def get_time_and_datetime():
  """Get the current time and datetime formatted with `strftime`.

  Example: ['12:30:50', '12.30-15.5.2023']

  Returns:
      list[str]: respectively, time and datetime
  """
  now = datetime.now()

  return [
    now.strftime('%H:%M:%S'),
    now.strftime('%H.%M-%d.%m.%Y')
  ]
