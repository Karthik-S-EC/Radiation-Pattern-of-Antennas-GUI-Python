# Radiation Pattern of Antennas Using GUI Python
Plot of Radiation Pattern of Different Antennas with the number of side lobes and their amplitudes

This is a Graphical user interface built using python, which gives the plot of different antennas with the amplitudes of sidelobes and the angles at which sidelobes occurs.

## Requirments (if any changes required or to do any changes)
Python:
1.  PyQt5: `pip install PyQt5`
2.  pyqtgraph:  `pip install pyqtgraph`
3.  Numpy:  `pip install numpy`
    
## Procedure to plot pattern
1. Run main_antenna_gui.py (if using python file to plot and vary).
2. Run Radiation Pattern.exe file to directly execute without any necessary installation of packages.
3. Select the number of antennas by varying the slider.
4. Select the type of antenna (eg. lambda/2 ==> lambda/x, select x), by varying the slider.
5. Select the type of Array 
    Broad-side Array: Maximum radiation in y direction
    End-fire Array  : Maximum radiation in x direction
    Scanning Array  : Maximum radiation in the required direction
6. If Scanning Array is selected, Enter the direction at which maximum radiation is required, Press enter to access the value.
7. Click on Plot to plot the radiation pattern of the details provided.
8. Click on Clear to clear the plot and values.
9. Check the null angles, sidelobe angles and corresponding sidelobe amplitude.
