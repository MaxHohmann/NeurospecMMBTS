# ---------------------------------------------------------
# MMBTS
# ---------------------------------------------------------
"""
This module provides code for using the MMBT-S Trigger Box 
(NEUROSPEC) to send trigger to EEG systems.

The class supports:
- opening serial connection to the trigger box
- sending digital event markers (triggers)
- closing serial connection to the trigger box
- listing available serial ports for setup

Debugging mode:
In debugging mode no port is openend or closed and no triggers
are send. Trigger values are still validated, so experiment 
scripts can be run without actual connection to hardware while
trigger errors are still caught.


Version:    1.1.3
Date:       23/09/2026  
Author:     Maximilian Hohmann
            mhohmann@dpz.eu
            maximilian.hohmann@stud.uni-goettingen.de
"""


import serial
import serial.tools.list_ports


# byte value used for reset
RESET_TRIGGER = bytes([0])


class MMBTS:

    # -----------------------------------------------------
    # INITIALIZE
    # -----------------------------------------------------
    def __init__(self):

        # initiate with placeholders
        self.ser        = None
        self.debugging  = False

        print(f"MMBT-S\t: assigned object ({self})")



    # -----------------------------------------------------
    # OPEN PORT
    # -----------------------------------------------------
    def open_port(self, port=None, debugging=False):
        """
        # set mode for all subsequent calls:
        # debugging = True  : no port connection
        # debugging = False : connect to serial port
        """
        
        self.debugging = debugging


        if self.debugging:

            # no real connection
            self.ser = None

            print(f"MMBT-S\t: [debugging] simulate opened port")
            return


        # check port input
        if port is None or port == "":
            raise ValueError("no port defined!")


        # open port
        try:
            self.ser = serial.Serial(
                port        = port,     # port name
                baudrate    = 9600      # default
            )

            # default settings
            self.ser.write(RESET_TRIGGER)
            self.ser.setRTS(False)
            self.ser.setDTR(False)

            print(f"MMBT-S\t: opened port ({port}) [debugging={self.debugging}]")
   
        except serial.SerialException:
            raise ValueError(f"Could not open port ({port})!") from None



    # -----------------------------------------------------
    # VALIDATE TRIGGER
    # -----------------------------------------------------
    @staticmethod
    def _validate_trigger(value=None):
 
        # check trigger value
        if value is None:
            raise ValueError("no trigger value defined!")
 
        # check trigger format
        if not isinstance(value, int):
            raise TypeError(f"trigger value must be integer ({type(value)})")
 
        # only accept triggers within range (0 to 255)
        if not (0 <= value <= 255):
            raise ValueError(f"trigger value out of range ({value})!")
 
        return value



    # -----------------------------------------------------
    # SEND TRIGGER
    # -----------------------------------------------------
    def send_trigger(self, value=None):

        if self.debugging:

            # validate trigger values
            value = self._validate_trigger(value)

            # continue without hardware
            print(f"MMBT-S\t: [debugging] simulate sent trigger! ({value})")
            return
        

        # send trigger
        try:
            self.ser.write(bytes([value]))

        except (serial.SerialException, AttributeError, TypeError):
            raise ConnectionError(f"could not send trigger! ({value})!") from None   



    # -----------------------------------------------------
    # CLOSE PORT
    # -----------------------------------------------------
    def close_port(self):

        if self.debugging:

            # no port to close
            self.ser = None

            print("MMBT-S\t: [debugging] simulate closed port")
            return
        

        # check for opened port
        if self.ser is None or not self.ser.is_open:
            raise ConnectionError("no open port found!")


        port = self.ser.port


        # close port
        try:            
            self.ser.write(RESET_TRIGGER)   # reset trigger
            self.ser.close()                # close port

            print(f"MMBT-S\t: closed port ({port})")

        except serial.SerialException:
            raise ValueError(f"could not close port ({port})!") from None



    # -----------------------------------------------------
    # SHOW AVAILABLE PORTS
    # -----------------------------------------------------
    @staticmethod
    def show_ports():
        """
        Print device names od all available serial ports.
        """

        ports = serial.tools.list_ports.comports()

        print("MMBT-S\t: list of available ports")
        for p in ports:
            print(f"\t- {p.device}")

        return

