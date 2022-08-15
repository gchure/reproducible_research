## `figures`

All figures containing data should be stored here, preferably labeled with a descriptive file name that also points to the correct figure, e.g. `Fig1_power_spectrum.py`. 

Figure scripts should not perform any data processing, data generation, or inference whenever possible. This maintains a separation between each layer of the scientific method in a clear and reproducible way. Keeping figure generation separate from other parts of the scientific pipeline allows for simple modification of figures, such as correcting axis labels, without needing to rerun the processing and analysis steps.
