import time
import datetime

today = datetime.datetime.now()
seconds = time.time()
print(f'Seconds since January 1, 1970: {seconds:,.4f} '
      f'or {seconds:.2e} in scientific notation')
print(today.strftime("%b %d %Y"))
