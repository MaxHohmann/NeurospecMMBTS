"""
Short example script on how to use the MMBTS functions
"""


from mmbts import MMBTS
import time


# ----- Setup -----

# Trigger Values
TRIGGERS = {
    # example events
    "event_01":       1,
    "event_02":       2,
    "event_03":       3,
    "trial_start":    254,
    "trial_end":      255,
}

# show availible ports
MMBTS.show_ports()

# open serial port
mmbt = MMBTS()
mmbt.open_port("COM5")

time.sleep(2.0)


# ----- Trial Loop -----
n_trials    = 3

for trial in range(1, n_trials+1):

    # start trial
    mmbt.send_trigger(TRIGGERS['trial_start'])

    time.sleep(1.0)


    # event onset
    if trial == 1:
        mmbt.send_trigger(TRIGGERS['event_01'])

    elif trial == 2:
        mmbt.send_trigger(TRIGGERS['event_02'])
        
    elif trial == 3:
        mmbt.send_trigger(TRIGGERS['event_03'])

    time.sleep(5.0)

    # end trial
    mmbt.send_trigger(TRIGGERS['trial_end'])

    time.sleep(3.0)


# close serial port
mmbt.close_port()

