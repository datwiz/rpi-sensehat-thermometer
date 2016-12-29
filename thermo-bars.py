from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
# sense.set_rotation(270)

t_max = 50
t_min = 0

h_min = 0
h_max = 100

x_min = 0
x_max = 3

y_min = 0
y_max = 7

while True:
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    print("temp: %.2f, humidity: %.2f" % (round(temp, 1), round(humidity, 1)))
    temp = int( ((y_max - y_min + 1) * (temp - t_min) / (t_max - t_min)) + y_min )
    humidity = int( ((y_max - y_min + 1) * (humidity - h_min) / (h_max - h_min)) + y_min )
    print(" scaled> t: %d, h: %d" % (temp, humidity))

    for x in range(x_min, x_max + 1):
        for y in range(y_min, temp):
            sense.set_pixel(x, y_max - y, 255, 0, 0)
        for y in range(temp, y_max + 1):
            sense.set_pixel(x, y_max - y, 0, 0, 0)

    for x in range(x_max + 1, 8):
      for y in range(y_min, humidity):
        sense.set_pixel(x, y_max - y, 0, 255, 0)
      for y in range(humidity, y_max + 1):
        sense.set_pixel(x, y_max - y, 0, 0, 0)
