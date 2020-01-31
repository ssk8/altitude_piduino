import serial
import time
import csv

class Reading:
    def __init__(self, temperature, pressure, altitude, pres_sl, real_alt, now):
        self._temperature = temperature
        self._pressure = pressure
        self._altitude = altitude
        self._pres_sl = pres_sl
        self._real_alt = real_alt
        self._now = now

    def temperature(self):
        return float(self._temperature)

    def pressure(self):
        return float(self._pressure)

    def altitude(self):
        return float(self._altitude)
      
    def pres_sl(self):
        return float(self._pres_sl)

    def real_alt(self):
        return float(self._real_alt)

    def now(self):
        return time.mktime(self._now)

    def temperature_out(self):
        return f'Temp = {self._temperature}C'

    def pressure_out(self):
        return f'Press = {self._pressure}Pa'

    def altitude_out(self):
        return f'Alt = {self._altitude}m'
     
    def pres_sl_out(self):
        return f'Pres@SL = {self._pres_sl}Pa'

    def real_alt_out(self):
        return f'Real Alt= {self._real_alt}m'

    def now_out(self):
        return f'Time: {time.strftime("%H:%M:%S", self._now)}'
    
    def save_reading(self):
        with open('data.csv', 'a', newline='') as csvfile:
            data_write = csv.writer(csvfile, delimiter=',')
            data_write.writerow([self.now(), self.temperature(), self.pressure(), self.altitude(), self.pres_sl(), self.real_alt()])


class BMP180():
    def __init__(self):
        self.ser = serial.Serial(
                port='/dev/ttyACM0',
                baudrate=115200,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1
        )

    def get_reading(self):
        try:
            return Reading(*self.ser.readline().decode('utf-8').split(), time.localtime())
        except:
            return Reading(0,0,0,0,0, time.localtime())


def main(sensor):
    while True:
        reading = sensor.get_reading()
        print(f'{reading.now_out()} {reading.temperature_out()} {reading.altitude_out()}')
        reading.save_reading()


if __name__ == "__main__":
    bmp180 = BMP180()
    main(bmp180)
    