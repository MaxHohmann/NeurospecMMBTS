"""
This module provides code for communicating with the
MMBT-S Trigger Box (NEUROSPEC).

The class supports:
- Opening serial connection to the trigger box
- Sending digital event markers (triggers)
- Closing serial connection to the trigger box
- Listing available serial ports for setup


Version:    1.1
Date:       26/05/2026  
Author:     Maximilian Hohmann
            mhohmann@dpz.eu
            maximilian.hohmann@stud.uni-goettingen.de
"""


import serial
import serial.tools.list_ports


class MMBTS:

    def __init__(self):

        self.ser = None  # placeholder

        print(f"MMBT-S\t: Assigned object ({self})")


    # ----------------------
    # OPEN PORT
    # ----------------------
    def open_port(self, port):

        # check port input
        if port is None or port == "":
            raise ValueError("MMBT-S\t: No port defined!")

        self.ser = serial.Serial(
            port        = port, # change port accordingly
            baudrate    = 9600  # default
        )

        self.ser.write(bytes([0]))
        self.ser.setRTS(False)
        self.ser.setDTR(False)

        print(f"MMBT-S\t: Opened port ({port})")

            
    # ----------------------
    # SEND TRIGGER
    # ----------------------
    def send_trigger(self, value):

        # check for port object
        if self.ser is None or not self.ser.is_open:
            raise RuntimeError("MMBT-S\t: No open port found!")
        
        # check trigger value
        if value < 0 or value > 255:
            raise ValueError("MMBT-S\t: Trigger out of range!")

        self.ser.write(bytes([value]))


    # ----------------------
    # CLOSE PORT
    # ----------------------
    def close_port(self):

        # check for port object
        if self.ser is None or not self.ser.is_open:
            raise RuntimeError("MMBT-S\t: No open port found!")
        
        port = self.ser.port

        self.ser.write(bytes([0]))
        self.ser.close()

        print(f"MMBT-S\t: Closed port ({port})")


    # ----------------------
    # SHOW AVAILABLE PORTS
    # ----------------------
    @staticmethod
    def show_ports():

        ports = serial.tools.list_ports.comports()

        print("MMBT-S\t: Display list of available ports")
        for p in ports:
            print(p.device, p.description)

