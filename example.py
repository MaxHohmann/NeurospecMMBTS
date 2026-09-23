# ---------------------------------------------------------
# EXAMPLE SCRIPT
# ---------------------------------------------------------
"""
Short example script on how to use the MMBTS functions within 
an experiment. Experiment contains a short loop over trials in
different conditions.

Author:     Maximilian Hohmann
            maximilian.hohmann@stud.uni-goettingen.de
            https://github.com/MaxHohmann
"""



# ----- SETUP ---------------------------------------------

import time
from mmbts import MMBTS     # custom code



# ----- SETTINGS ------------------------------------------

# set debugging mode
debugging = True            # simulate port, check trigger values
# debugging = False           # for running the experiment


# trial parameters
n_trials = 3


# trigger values
TRIGGERS = {
    # example events
    "event_01":       1,
    "event_02":       2,
    "event_03":       3,
    "trial_start":    254,
    "trial_end":      255,
}


# show available ports
MMBTS.show_ports()

time.sleep(5.0)



# ----- START EXPERIMENT ----------------------------------

print("---=== START EXPERIMENT ===---")

# open serial port
mmbt = MMBTS()
mmbt.open_port("COM5", debugging)   # open port in predefined mode

time.sleep(2.0)



# ----- TRIAL LOOP ----------------------------------------

for trial in range(1, n_trials + 1):

    print(f"-----> TRIAL ({trial}/{n_trials}) <-----")

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



# ----- EXIT EXPERIMENT -----------------------------------

print("---=== COMPLETED EXPERIMENT ===---")

# close serial port
mmbt.close_port()

