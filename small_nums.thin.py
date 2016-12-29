# 4 x 4 numbers
from sense_hat import SenseHat
import time
s = SenseHat()

O = [0, 0, 0]
A = [255, 0, 0]
B = [0, 255, 0]
C = [0, 0, 255]
D = [124, 124, 124]

DB = [
  O,O,O,O,
  O,O,O,O,
  O,O,O,O,
  O,O,O,O    
]

D1 = [
  O,A,A,A,
  O,O,A,A,
  O,O,A,A,
  O,O,A,A 
]

D2 = [
  O,B,B,B,
  O,O,B,B,
  O,B,B,O,
  O,B,B,B    
]

D3 = [
  O,C,C,C,
  O,O,C,C,
  O,O,O,C,
  O,C,C,C  
]

D4 = [
  O,D,O,D,
  O,D,O,D,
  O,D,D,D,
  O,O,O,D    
]

D5 = [
  O,A,A,A,
  O,A,A,O,
  O,O,A,A,
  O,A,A,A    
]

D6 = [
  O,B,O,O,
  O,B,B,B,
  O,B,O,B,
  O,B,B,B    
]

D7 = [
  O,C,C,C,
  O,O,O,C,
  O,O,C,O,
  O,O,C,O    
]

D8 = [
  O,D,D,O,
  O,D,D,D,
  O,D,O,D,
  O,D,D,D    
]

D9 = [
  O,A,A,A,
  O,A,O,A,
  O,A,A,A,
  O,O,O,A    
]

D0 = [
  O,O,B,O,
  O,B,O,B,
  O,B,O,B,
  O,O,B,O    
]

s.clear()

while True:
  image = []
  image[0:7] = D1[0:4] + D2[0:4]
  image[8:15] = D1[4:8] + D2[4:8]
  image[16:23] = D1[8:12] + D2[8:12]
  image[24:31] = D1[12:16] + D2[12:16]

  image[32:39] = D3[0:4] + D4[0:4]
  image[40:47] = D3[4:8] + D4[4:8]
  image[48:55] = D3[8:12] + D4[8:12]
  image[56:63] = D3[12:16] + D4[12:16]

  print ("{}".format(len(image)))
  s.set_pixels(image)
  time.sleep(2)

  image = []
  image[0:7] = D5[0:4] + D6[0:4]
  image[8:15] = D5[4:8] + D6[4:8]
  image[16:23] = D5[8:12] + D6[8:12]
  image[24:31] = D5[12:16] + D6[12:16]

  image[32:39] = D7[0:4] + D8[0:4]
  image[40:47] = D7[4:8] + D8[4:8]
  image[48:55] = D7[8:12] + D8[8:12]
  image[56:63] = D7[12:16] + D8[12:16]

  print ("{}".format(len(image)))
  s.set_pixels(image)
  time.sleep(2)

  image = []
  image[0:7] = D9[0:4] + D0[0:4]
  image[8:15] = D9[4:8] + D0[4:8]
  image[16:23] = D9[8:12] + D0[8:12]
  image[24:31] = D9[12:16] + D0[12:16]

  image[32:39] = DB[0:4] + DB[0:4]
  image[40:47] = DB[4:8] + DB[4:8]
  image[48:55] = DB[8:12] + DB[8:12]
  image[56:63] = DB[12:16] + DB[12:16]

  print ("{}".format(len(image)))
  s.set_pixels(image)
  time.sleep(2)
