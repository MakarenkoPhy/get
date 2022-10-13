import RPi.GPIO as gpio
import time
import matplotlib.pyplot as plt

dac = [26, 19, 13, 6, 5, 11, 9, 10]

measure =[]

comp = 4

troyka = 17

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
gpio.setup(comp, gpio.IN)
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)

def decbin(n):
    return [int(bit) for bit in bin(n)[2:].zfill(8)]

def adc():
    vlt = 0
    for i in range(8):
        gpio.output(dac, decbin(vlt + 2**(7-i)))
        time.sleep(0.001)
        if(gpio.input(comp) == 1):
            vlt += 2**(7-i)
    return vlt

start_time = time.time()

count=0
c1=0

try:
    while(1):
        vlt = adc()
        res = ", Напряжение {outvlt:.2f} В"
        print(vlt, res.format(outvlt=vlt*3.3/256))
        count=count+1
        measure.append("{0:.2f}".format(vlt*3.3/256))
        if(vlt>=245):
            gpio.output(troyka, 0)
            c1=c1+1
        if(vlt<=15 and c1>0):
            with open('settings.txt', 'w', encoding="utf-8") as g:
                g.write(str("{0:.2f}".format(count/(time.time()-start_time))))
                g.write('\n')
                g.write('0.01')
                measure_str=[str(item) for item in measure]
                with open('data.txt', 'w', encoding="utf-8") as f:
                    f.write("\n".join(measure_str))
                plt.plot(measure)
                plt.show()
                break
            



except ValueError:
    print("Не числовое значение")

finally: 
    for j in range(8):
        gpio.output(dac[j],0)
        gpio.cleanup()


