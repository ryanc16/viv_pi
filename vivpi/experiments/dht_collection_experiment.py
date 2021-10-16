import threading
from time import sleep
import math
from datetime import datetime
import grovepi
from vivpi.utils.denoise import eliminateNoise

from vivpi.utils.stats import Stats

sensor = 4  # The Sensor goes on digital port 4.
# temp_humidity_sensor_type
blue = 0    # The Blue colored sensor.
white = 1   # The White colored sensor.

filtered_temperature = [] # here we keep the temperature values after removing outliers
filtered_humidity = [] # here we keep the filtered humidity values after removing the outliers

lock = threading.Lock() # we are using locks so we don't have conflicts while accessing the shared variables
event = threading.Event() # we are using an event so we can close the thread as soon as KeyboardInterrupt is raised

# function for processing the data
# filtering, periods of time, yada yada
def readingValues():
  seconds_window = 10 # after this many second we make a record
  values = []

  while not event.is_set():
    counter = 0
    while counter < seconds_window and not event.is_set():
      temp = None
      humidity = None
      try:
          [temp, humidity] = grovepi.dht(sensor, blue)

      except IOError:
          print("we've got IO error")

      if math.isnan(temp) == False and math.isnan(humidity) == False:
          values.append({"temp" : temp, "hum" : humidity})
          counter += 1
      #else:
          #print("we've got NaN")

      sleep(1)

    lock.acquire()
    filtered_temperature.append(Stats.mean(eliminateNoise([x["temp"] for x in values])))
    filtered_humidity.append(Stats.mean(eliminateNoise([x["hum"] for x in values])))
    lock.release()

    values = []

def Main():
  # here we start the thread
  # we use a thread in order to gather/process the data separately from the printing proceess
  data_collector = threading.Thread(target = readingValues)
  data_collector.start()

  while not event.is_set():
    if len(filtered_temperature) > 0: # or we could have used filtered_humidity instead
      lock.acquire()

      # here you can do whatever you want with the variables: print them, file them out, anything
      temperature = filtered_temperature.pop()
      humidity = filtered_humidity.pop()
      print('{},{:.01f},{:.01f}' .format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), temperature, humidity))

      lock.release()

    # wait a second before the next check
    sleep(1)

  # wait until the thread is finished
  data_collector.join()

if __name__ == "__main__":
  try:
    Main()

  except KeyboardInterrupt:
    event.set()