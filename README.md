# UART-Spectrum-Analyzer-for-Serial-Devices

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-yellow.svg?style=for-the-badge&logo=python)](https://python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-orange.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
![Depfu](https://img.shields.io/depfu/dwij2812/UART-Spectrum-Analyzer-for-Serial-Devices.svg?style=for-the-badge)

[![HitCount](http://hits.dwyl.io/dwij2812/UART-Spectrum-Analyzer-for-Serial-Devices.svg)](http://hits.dwyl.io/dwij2812/UART-Spectrum-Analyzer-for-Serial-Devices)


The following Script can be used to generate certain mathematical functions on a micro controller or FPGA Device connected in serial based on the configuration selected by the the user and collect realtime data of the signal as generated by the device for spectrum analysis.

## Screenshots of this application
!["A view of the UART-Spectrum-Analyzer Application running with realtime data from ZEDBoard"](https://github.com/dwij2812/UART-Spectrum-Analyzer-for-Serial-Devices/blob/master/UART-Spectrum-Analyzer-screenshot.png?raw=true)

## Features
1. Live plotting with Real-Time updates of all plots.
2. Hoverable markers and points can be marked on the plots during runtime.
3. Types of plots that can be plotted with this tool:
    - Received Signal
    - Normal FFT
    - Real-Time FFT
    - Magnitude Spectrum
    - Log Magnitude Spectrum
    - Discrete Cosine Transform
    - Phase Spectrum
    - Angle Spectrum
    - Discrete Sine Transform
    - Spectrogram of Signal
    - Periodogram of Signal (psd)
    - Power Spectral Density using Welch Normalization
        
4. Ability to adjust window size and plotting parameters anytime.

## Instructions to run this application
1. Make Sure Python3 is installed and added to PATH on your device. [Download Link for Python](https://www.python.org/downloads/).
2. Navigate to the project directory and run
    ```bash
    $ pip install -r requirements.txt
    ```
    *This will install all the dependencies needed to run this application.*

3. Install the Cypress USB2UART Drivers which enable UART connections between the computer and our ZED device. [Download Link for Cypress USB2UART Drivers](https://www.cypress.com/documentation/software-and-drivers/microsoft-certified-usb-uart-driver).
4. Open Xilinx SDK and load the hardware wrapper folder in it.
5. Use the program FPGA option in the toolbar and confirm to synthesize the logic fabric for the ZEDboard with ZYNQ 7000 series APSoC.
6. Once the ready light flashes on the ZEDboard Navigate to the left pane in Xilinx SDK and select the folder containing the source files.
7. Right Click on it and use Run As > Launch On Hardware (Use GDB) option and wait till the operation finishes.
8. Now our hardware is ready for use. Next we will now launch out python script.
9. For this run the following command from the root of the project directory
    ```bash
    $ python main.py
    ```
10. The Application will soon launch and you will get a popup window requesting the parameters of the wave. Once entered you may either choose to just view the live visualization or carry out analysis on the output waveforms.
11. The visualization options will yield a plot with all the computed parameters and keep updating in realtime as the data stream is constantly being recieved on the device from the ZEDboard.
12. The analysis option waits untill a specific number of points are recieved and evaluated by the system as entered by the user and then reveals the plot screen with all the computed graphs alongwith appropriate cursors that help in analyzing the plots with ease.
