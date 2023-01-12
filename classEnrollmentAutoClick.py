import pyautogui
import datetime

import time
from datetime import datetime
from typing import Final

INITIAL_TIMESTAMP: Final[float] = time.time()
INITIAL_TIMESTAMP_PERF_COUNTER: Final[float] = time.perf_counter()

# modify to what time you want
hour = 7  

def get_timestamp_now() -> datetime:
    dt_sec = time.perf_counter() - INITIAL_TIMESTAMP_PERF_COUNTER
    return datetime.fromtimestamp(INITIAL_TIMESTAMP + dt_sec)

while True:
  currentTime = get_timestamp_now()
  if currentTime.hour >= hour:
    width, height = pyautogui.size()

    # change pixel numbers to where you want to click
    enrollLocationWidth = 1800
    enrollLocationHeight = 350
    pyautogui.click(enrollLocationWidth, enrollLocationHeight)
    break