# NeurospecMMBTS

This repository contains Python functions to use the ([MMBT-S Trigger Box](https://www.neurospec.com/products/mmbt-s)) by **NEUROSPEC** to connect and send triggers to an EEG system. The Trigger Box serves as an USB-to-parallel port adapter, so that computers with serial port can be connected to EEG systems that usually require a parallel port. The Trigger Box appears as a serial COM port (installing the corresponding driver might be needed).



## Workflow to use the MMBT-S Trigger Box:

1. Define port object (once in the beginning of the experiment):
```python
mmbts = MMBTS()
```


2. Open port to MMBT-S (once in the beginning of the experiment):
```python
mmbts.open_port("COM5")
```


3. Send triggers to EEG system (during the experiment):
```python
mmbts.send_trigger(10)
```

    
4. Close port to MMBT-S (once at the end of the experiment):
```python
mmbts.close_port()
```


**Additionally**, you can get a list of availablee ports by using:
```python
MMBTS.show_ports()
```



## Requirements

- [Python (3.8+)](https://www.python.org/downloads/)
- [pySerial (3.5+)](https://pypi.org/project/pyserial/)



## References

Corresponding **MATLAB** functions for the Trigger Box can be found on the GitHub repository from **Dr. Niko Busch**:
https://github.com/nabusch/NeurospecTriggerBox

Details about using serial port in Python can be found on the documentation website for **pySerial**:
https://pyserial.readthedocs.io/en/latest/

