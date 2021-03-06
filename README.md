## KuttyPy Interactive Playground [ Microcontroller Training Utility ]

[![PyPI version](https://badge.fury.io/py/kuttyPy.svg)](https://badge.fury.io/py/kuttyPy)
[![Documentation Status](https://readthedocs.org/projects/kuttypy/badge/?version=latest)](https://kuttypy.readthedocs.io/en/latest/?badge=latest)

![Screenshot](/docs/images/main.gif?raw=true "Recording of the User Interface")

---
The kuttyPy (/kʊtipʌɪ/) Microcontroller training utility allows live manipulation of the registers in microcontrollers via a connected computer containing its python library.  setReg and getReg function calls act as debugging and monitoring tools, and combined with Python's visualization and analytical utilities, this approach has immense pedagogical potential for beginners to the microcontroller world. 

The kuttyPy hardware is an ATMEGA32 microcontroller development board developed by the [ExpEYES](http://expeyes.in) project, and is currently supported by this software. It contains the kuttyPy firmware, but can also be used to run other programs via its bootloader.

---
## What can I use it for?
+ It's an atmega32 development board with a bootloader supporting the 'arduino' protocol
+ The bootloader also allows real-time manipulation of registers through commmands sent via the serial port.
+ This is done by the associated Python library and companion GUI
    + You can monitor every input
    + Toggle every output
    + Deal with Peripherals such as PWMs and Counters
    + View ADC readings via an analog gauge
    + Scan for sensors connected to the I2C Bus
    + Monitor readings from sensors [TSL2561 luminosity, and MPU6050 IMU supported]
+ Compile code to hex with the avr-gcc compiler
+ Upload hex via the built-in uploader
+ Rapidly prototype and debug educational projects. For example, you can verify ADC input values before handing over control to the uploaded hex file which will likely have very limited debugging capabilities.
+ Learn how registers are the key to microcontroller operation, as opposed to the Arduino ecosystem which prefers obfuscation of these details underneath abstraction layers.

## Python library and Graphical utility

### 7 channel voltmeter [ 0-5000mV without analog frontend ]
![Screenshot](/docs/images/voltmeter.gif?raw=true "Voltmeter")

### Monitor I2C Sensors
Supports I2C sensors: Luminosity Example. | Video recording
---|---
![sensor](https://user-images.githubusercontent.com/19327143/52988950-5c64f580-3427-11e9-8516-d6708ef2532b.gif) | ![ezgif com-optimize](https://user-images.githubusercontent.com/19327143/52989158-2bd18b80-3428-11e9-9b26-21f21f8fe99a.gif)

+ Scan for Sensors
+ Click to monitor via analog gauge
+ List of I2C sensors supported thus far (Minimal data logging. Configuration options via the graphical utility might be incomplete)
  + MPU6050 3 Axis Accelerometer, 3 axis Angular velocity (Gyro)
  + TSL2561 Luminosity measurements
  + BMP280 Pressure and Temperature sensor
  + MCP4725 Single channel DAC
  + PCA9685 PWM controller
  + MLX90614 Passive IR

Programming library and examples : [READ THE DOCS](https://kuttypy.readthedocs.io/en/latest/)

![Screenshot](/docs/images/mpu6050.gif?raw=true "6 DOF inertial measurement unit MPU6050")

### Plotting ADC values using matplotlib
![Screenshot](/docs/images/code.gif?raw=true "Recording of the ADC logging example")

![Screencast](/docs/images/monitor.gif?raw=true "Monitor your code!")

Hall Sensor|Servo Motor
---|---
![Screencast](/docs/images/hall_sensor.webp?raw=true "Hall sensor!") | ![Screencast](/docs/images/servo_motor.webp?raw=true "Hall sensor!")

Plug and play various accessories such as this Hall Sensor, & servo motor.

### Simple blink.py example
![Screenshot](/docs/images/blink.gif?raw=true "Write Python code to blink all of PORT D")

![Screencast](/docs/images/monitor.gif?raw=true "Monitor your code!")

Monitor your code's activity while it executes

![Screencast](/docs/images/custom_registers.gif?raw=true "Add Register widgets, twiddle bits, and see what happens!")

Add custom register blocks, twiddle bits, and observe!
In this demo, the ADC is read by first setting the bits in the ADCSRA(control and status register), then reading back ADCL(8LSB)+ADCH(2MSB), and also checking the new status of ADCSRA after the operation.

## C Code compilation and uploading

### Seamless switching between the KuttyPy monitor, and user uploaded hex file.
---
The KuttyPy monitor code is part of the bootloader. This allows users to upload their own Hex files without losing the training utility features.

![App Switching](/docs/images/switch.gif?raw=true "App Switching")

This example shows how to skip back and forth to an LED scanning code (which also prints letters to the serial port) written in C and uploaded.

In the animation, after fiddling a little with the PWM controls on the monitor, the 'user app' button is clicked. This triggers the following:
+ Within a few ten milliseconds the user uploaded hex file starts executing
+ The console turns into a serial monitor, and shows any text sent by the user uploaded hex.

The user can switch back to the monitoring utility in a snap!

![Screencast](/docs/images/pov_display.webp?raw=true "POV display!")

A persistence of vision display made with C code! Write text in thin air using 8 LEDs on PORTB.

### Installing on Ubuntu
+ sudo apt-get install python3 python3-pyqt5 python3-serial
---
+ python3 KuttyPyGUI.py

### Installing on windows.
+ This code can be run from source, provided python3 and pyqt5 are installed.
+ [Download Bundled Installer](https://drive.google.com/uc?export=download&id=1giJuDNIql8X5oaIcOLFACXD05-hmkBAy)



License: MIT



---
Developed by Jithin B.P @CSpark Research, 2018.  
Special thanks to Georges Khazanadar for Debianizing efforts.
