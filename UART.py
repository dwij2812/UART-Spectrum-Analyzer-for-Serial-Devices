from time import sleep
import serial
ser = serial.Serial('COM3', 115200) # Establish the connection on a specific port
counter = 32 # Below 32 everything in ASCII is gibberish
while(True):
     ##counter +=1
     ##ser.write(chr(counter).encode()) # Convert the decimal number to ASCII then send it to the Arduino
     ##ser.write("\n".encode())
     ##print("Python Sent: ",counter)
     ser.flush()
     print(ser.readline()) # Read the newest output from the Arduino
     ser.flush()
     sleep(.1) # Delay for one tenth of a second
     if counter == 255:
          counter = 32
