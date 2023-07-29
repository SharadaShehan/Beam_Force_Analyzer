# Desktop-Software-for-Civil-Engineering-Applications
<p>
  This Python program is a numerical analysis tool designed to calculate and visualize bending moment and shear force diagrams for a given beam structure. The program uses numerical integration to obtain the general polynomial coefficients for bending moment values. These coefficients are then employed to construct continuous polynomial functions representing bending moment distribution along the beam's length.

In detail, the program follows these steps:
<ul>
<li>
Integration and Polynomial Coefficients: The input data is integrated to compute the bending moment polynomial coefficients in a general format. These coefficients are obtained by dividing the data points by appropriate scaling factors, resulting in a set of continuous polynomial functions describing the bending moment distribution.
</li>
<li>
Accurate Intercept Calculation: The bending moment polynomial functions are modified to ensure accurate intercepts at specified positions along the beam. This involves calculating the change in values between adjacent positions and adjusting the coefficients accordingly to achieve the desired intercepts.
</li>
<li>
Plotting Shear Forces and Bending Moments Graphs: Using the calculated polynomial coefficients and positions, the program utilizes the matplotlib library to graphically represent the shear forces and bending moments diagrams. These diagrams visually depict the variations in shear force and bending moment along the beam's length.
</li>
<li>
Graphical User Interface (GUI) Implementation: The program employs the tkinter library to create a user-friendly GUI. The GUI facilitates user interaction with the plotted diagrams by incorporating sliders and spinboxes. Users can adjust the position and values of shear forces and bending moments, enabling exploration of the beam's behavior under different loading conditions.
</li>
<li>
Length Setting and Configuration: A settings window is provided to enable users to input the length value for the beam structure, which influences the calculations and visualizations.
</li>
<li>
Component Organization: Various frames and classes are defined to compartmentalize and present different aspects of the GUI. These components handle elements like supports, loads, couples, and distributions, providing a structured layout for the user interface.
</li>
<li>
Go To Graphs: A "Go To Graphs" button initiates the visualization process, activating a function (error_check0) responsible for displaying the bending moment and shear force diagrams based on the user's input and preferences.
</li>
</ul>
</p>
<br>

<p float="left">
<img src="https://github.com/Sharada001/Desktop-Software-for-Civil-Engineering-Applications/blob/e8c2ba7f644ccef36266905ef44b7392d16fadff/ScreenShots/2.JPG"  width="45%" height="50%" style="float: left; display: inline;">
<img src="https://github.com/Sharada001/Desktop-Software-for-Civil-Engineering-Applications/blob/03a7297036434601f3204cc9003b5f53cb1ade63/ScreenShots/2-1.JPG"  width="45%" height="50%" style="float: left; display: inline;">
</p>

<p float="left">
<img src="https://github.com/Sharada001/Desktop-Software-for-Civil-Engineering-Applications/blob/03a7297036434601f3204cc9003b5f53cb1ade63/ScreenShots/3.JPG"  width="45%" height="30%">
<img src="https://github.com/Sharada001/Desktop-Software-for-Civil-Engineering-Applications/blob/03a7297036434601f3204cc9003b5f53cb1ade63/ScreenShots/3-1.JPG"  width="45%" height="30%">
</p>

<br><br>
<p float="left">
<img src="https://github.com/Sharada001/Desktop-Software-for-Civil-Engineering-Applications/blob/03a7297036434601f3204cc9003b5f53cb1ade63/ScreenShots/4.JPG"  width="45%" height="30%">
<img src="https://github.com/Sharada001/Desktop-Software-for-Civil-Engineering-Applications/blob/03a7297036434601f3204cc9003b5f53cb1ade63/ScreenShots/4-1.JPG"  width="45%" height="30%">
</p>

<p float="left">
<img src="https://github.com/Sharada001/Desktop-Software-for-Civil-Engineering-Applications/blob/03a7297036434601f3204cc9003b5f53cb1ade63/ScreenShots/5.JPG"  width="45%" height="30%">
<img src="https://github.com/Sharada001/Desktop-Software-for-Civil-Engineering-Applications/blob/03a7297036434601f3204cc9003b5f53cb1ade63/ScreenShots/5-1.JPG"  width="45%" height="30%">
  </p>
<p align="center">
<img src="https://github.com/Sharada001/Desktop-Software-for-Civil-Engineering-Applications/blob/03a7297036434601f3204cc9003b5f53cb1ade63/ScreenShots/5-3.JPG"  width="45%" height="30%">
</p>
