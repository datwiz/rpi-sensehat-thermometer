# 4 x 4 numbers
from sense_hat import SenseHat
import time
import subprocess
import re

s = SenseHat()

def digit_b(color):
  X = color
  O = [0, 0, 0]
  return [
    O,O,O,O,
    O,O,O,O,
    O,O,O,O,
    O,O,O,O    
  ]

def digit_1(color):
  X = color
  O = [0, 0, 0]
  return [
    O,X,X,X,
    O,O,X,X,
    O,O,X,X,
    O,O,X,X 
  ]

def digit_2(color):
  X = color
  O = [0, 0, 0]
  return [
    O,X,X,X,
    O,O,X,X,
    O,X,X,O,
    O,X,X,X    
  ]

def digit_3(color):
  X = color
  O = [0, 0, 0]
  return [
    O,X,X,X,
    O,O,X,X,
    O,O,O,X,
    O,X,X,X  
  ]

def digit_4(color):
  X = color
  O = [0, 0, 0]
  return [
    O,X,O,X,
    O,X,O,X,
    O,X,X,X,
    O,O,O,X    
  ]

def digit_5(color):
  X = color
  O = [0, 0, 0]
  return [
    O,X,X,X,
    O,X,X,O,
    O,O,X,X,
    O,X,X,X    
  ]

def digit_6(color):
  X = color
  O = [0, 0, 0]
  return [
    O,X,O,O,
    O,X,X,X,
    O,X,O,X,
    O,X,X,X    
  ]

def digit_7(color):
  X = color
  O = [0, 0, 0,]
  return [
    O,X,X,X,
    O,O,O,X,
    O,O,X,O,
    O,O,X,O    
  ]

def digit_8(color):
  X = color
  O = [0, 0, 0,]
  return [
    O,X,X,O,
    O,X,X,X,
    O,X,O,X,
    O,X,X,X    
  ]

def digit_9(color):
  X = color
  O = [0, 0, 0,]
  return [
    O,X,X,X,
    O,X,O,X,
    O,X,X,X,
    O,O,O,X    
  ]

def digit_0(color):
  X = color
  O = [0, 0, 0,]
  return [
    O,O,X,O,
    O,X,O,X,
    O,X,O,X,
    O,O,X,O    
  ]

def get_digit_map(digit, color):
  if digit == 0:
    return digit_0(color)
  elif digit == 1:
    return digit_1(color)
  elif digit == 2:
    return digit_2(color)
  elif digit == 3:
    return digit_3(color)
  elif digit == 4:
    return digit_4(color)
  elif digit == 5:
    return digit_5(color)
  elif digit == 6:
    return digit_6(color)
  elif digit == 7:
    return digit_7(color)
  elif digit == 8:
    return digit_8(color)
  elif digit == 9:
    return digit_9(color)
  else:
    return digit_b(color)

# compose an image of 2 upper digits and 2 lower digits
def compose_image(U1, U2, L1, L2):
  image = []
  image[0:7] = U1[0:4] + U2[0:4]
  image[8:15] = U1[4:8] + U2[4:8]
  image[16:23] = U1[8:12] + U2[8:12]
  image[24:31] = U1[12:16] + U2[12:16]
  
  image[32:39] = L1[0:4] + L2[0:4]
  image[40:47] = L1[4:8] + L2[4:8]
  image[48:55] = L1[8:12] + L2[8:12]
  image[56:63] = L1[12:16] + L2[12:16]
  return image

def display_thermostat(temp, humidity):
  upper_color = [255, 0, 0]
  lower_color = [0, 255, 0]

  U1 = get_digit_map(temp // 10, upper_color)
  U2 = get_digit_map(temp % 10, upper_color)
  L1 = get_digit_map(humidity // 10, lower_color)
  L2 = get_digit_map(humidity % 10, lower_color)
  s.set_pixels(compose_image(U1, U2, L1, L2))

# based on discussion from https://www.raspberrypi.org/forums/viewtopic.php?f=104&t=111457
def get_amb_temp():
  avg_sensor_temp = (s.get_temperature_from_humidity() + s.get_temperature_from_pressure()) / 2
  # cpu_temp_output = subprocess.check_output('vcgencmd measure_temp', shell=True)
  # TODO: need exception handling here if the call fails
  # cpu_temp = float(re.search('temp=(\d+\.\d+)\'C\\n', cpu_temp_output).group(1))
  # amb_temp = avg_sensor_temp - ((cpu_temp - avg_sensor_temp) / 2 )
  amb_temp = 0.0071*avg_sensor_temp*avg_sensor_temp + 0.86*avg_sensor_temp - 10.0 - 3
  return amb_temp

def get_amb_humidity():
  sensor_humidity = s.get_humidity()
  sensor_temp = s.get_temperature_from_humidity()
  amb_humidity = sensor_humidity * (2.5 - (0.029 * sensor_temp))
  return amb_humidity

# show two lines of 2 digit 4x4 numbers
def thermometer():
  while True:
    temp = int(get_amb_temp())
    humidity = int(get_amb_humidity())

    display_thermostat(temp, humidity)
    time.sleep(1)

thermometer()
