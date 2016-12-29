from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
sense.set_rotation(180)


T = [255, 0, 0]
H = [0, 255, 0]

while True:
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    msg = "temp: {:.2f}, humidity: {:.2f}".format(round(temp, 1), round(humidity, 1))
    print msg
    sense.show_message("{}".format(round(temp, 1)), text_colour=T)
    sense.show_message("{}".format(round(humidity, 1)), text_colour=H)
