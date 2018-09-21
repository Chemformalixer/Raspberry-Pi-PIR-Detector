# IR Motion Recorder
Passive Infra Red motion detector recording code via Raspberry Pi and python

You can assembled and programmed raspberry pi and PIR motion detector with python to record motion with desired time intervals and stor in csv file.

Raspberry Pi:
https://www.raspberrypi.org/products/raspberry-pi-3-model-b/

PIR motion sensor:
https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/how-pirs-work

The GPIO (general purpose input/output) has to be in correct configuration with the PIR motion sensor.
Once running, it records the motion activity accessible to the PIR and logs the data with time into a csv file recording 1 (for motion detected) and 0 (for no motion detected) in desired time intervals. 
