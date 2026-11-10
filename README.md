# NeurospecMMBTS

This repository contains Python functions to use the [MMBT-S Trigger Box](https://www.neurospec.com/products/mmbt-s) by **NEUROSPEC** to connect and send triggers to an EEG system. The Trigger Box serves as an USB-to-parallel port adapter, so that computers with serial port can be connected to EEG systems that usually require a parallel port. The Trigger Box appears as a serial COM port (installing the corresponding driver might be needed).

<br>

## Workflow to use the MMBT-S Trigger Box

1. Define port object (once in the beginning of the experiment):
```python
mmbts = MMBTS()
```

2. Open port to MMBT-S (once in the beginning of the experiment):
```python
mmbts.open_port("COM5")                     # for running the experiment
mmbts.open_port("COM5", debugging=True)     # with predefined debugging mode
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
<br>

## Examples

**Demo Experiment**
```python
experiment_demo.py
```
- demonstrates how to use the MMBT-S Trigger Box within an experiment to send event triggers during an experiment.
<br>

**Extraction Notebook** 
```python
extraction_demo.ipynb
```
- demonstrates how to extract trigger events from BioSemi BDF data files using [MNE-Python](https://mne.tools/stable/index.html) and aggregate events into a trial-level dataset. 
<br>

**Example Data**
```python
NeurospecMMBTS/
│
└── example_data/
    ├── testdata_1024Hz_09112026.bdf
    ├── testdata_2048Hz_09112026.bdf
    └── testdata_512Hz_09112026.bdf
```
The folder `example_data` contains three data files recorded using the demo experiment at different sampling rates (512 Hz, 1024 Hz, and 2048 Hz).
<br>

## Requirements

- [Python (3.8+)](https://www.python.org/downloads/)
- [pySerial (3.5+)](https://pypi.org/project/pyserial/)

<br>

## References

Corresponding **MATLAB** functions for the Trigger Box can be found on the GitHub repository from **Dr. Niko Busch**: <br>
https://github.com/nabusch/NeurospecTriggerBox

Details about using serial port in Python can be found on the documentation website for **pySerial**: <br>
https://pyserial.readthedocs.io/en/latest/

Any further information about the MMBT-S Trigger Box can be found on the **NEUROSPEC** website: <br>
https://www.neurospec.com/products/mmbt-s

**YouTube** series on using the MMBT-S Trigger Box by **Neurospec**:
https://www.youtube.com/playlist?list=PLlqnpgURTieauXe2OMGoQrt98rZuPfOJJ

Information on the BDF file format by **BioSemi**:
https://www.biosemi.com/faq/file_format.htm

