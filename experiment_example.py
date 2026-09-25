# ---------------------------------------------------------
# EXPERIMENT EXAMPLE
# ---------------------------------------------------------
"""
Short example script on how to use the MMBTS functions within 
an experiment. Experiment contains a short loop over trials in
different conditions.


Date    :   25/09/2026
Author. :   Maximilian Hohmann
            maximilian.hohmann@stud.uni-goettingen.de
            https://github.com/MaxHohmann
"""



# ----- SETUP ---------------------------------------------

import time
from mmbts import MMBTS



# ----- SETTINGS ------------------------------------------

# set debugging mode
debugging = True        # simulate port, check trigger values
# debugging = False       # for running the experiment


# trial parameters
n_trials    = 5         # number of trials
ITI_time    = 3         # inter trial interval 


# trigger values
TRIGGERS = {

    # trial
    "trial_start":      10,
    "trial_end":        11,

    "event_01":         20,
    "event_02":         21,
    "event_03":         22,
    "event_04":         23,
    "event_05":         24,


    # data recording
    "stream_start":     254,
    "stream_stop":      255,
}



# ----- START EXPERIMENT ----------------------------------

print("---=== START EXPERIMENT ===---")


# open serial port
MMBTS.show_ports()                  # show available ports

mmbt = MMBTS()
mmbt.open_port("COM5", debugging)   # open port in predefined mode

time.sleep(3.0)



# ----- TRIAL LOOP ----------------------------------------

for trial in range(1, n_trials + 1):

    print(f"-----> TRIAL ({trial}/{n_trials}) <-----")


    # start data recording
    mmbt.send_trigger(TRIGGERS['stream_start'])
    time.sleep(0.5)


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

    elif trial == 4:
        mmbt.send_trigger(TRIGGERS['event_04'])

    elif trial == 5:
        mmbt.send_trigger(TRIGGERS['event_05'])

    time.sleep(5.0)


    # end trial
    mmbt.send_trigger(TRIGGERS['trial_end'])
    time.sleep(0.5)


    # stop data recording
    mmbt.send_trigger(TRIGGERS['stream_stop'])

    print(f"TRIAL completed...")


    # break
    time.sleep(ITI_time)



# ----- EXIT EXPERIMENT -----------------------------------

print("---=== COMPLETED EXPERIMENT ===---")


# close serial port
mmbt.close_port()

