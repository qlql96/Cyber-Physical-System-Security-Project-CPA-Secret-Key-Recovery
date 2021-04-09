# CZ4055 Cyber Physical System Security Project

Given a set of power traces (in a csv file format as captured in the lab), a **Correlation Power Analysis (CPA) program** is developed in Java for this project to implement CPA on the given traces to extract the key. A **Python script** is also written to visualize the output of the CPA program by plotting two types of graphs (Plot 1 and Plot 2). 

## Author - **Tong Qi Long (U1822422C)**



## Prerequisite:

1. Installed with Java
2. Installed with Python3, Python pandas library and Python matplolib library


## Get Started:
1. Unzip the CZ4055_Project.rar
3. Place your waveform.csv file in the same directory as CPASecretKeyRecovery.jar executable file.

### Run Correlation Power Analysis (CPA) program (CPASecretKeyRecovery.jar)

1. Open your terminal/command prompt and navigate to the directory of the CPASecretKeyRecovery.jar file.
2. In the terminal/command prompt, type in "java -jar CPASecretKeyRecovery.jar" to run the program.
3. plot1Data.csv and plot2Data.csv are the output of the program and can be found in the same directory. 
4. After each successful recovery of the 16 bytes of key, type in the original secret 16 bytes of key to the program. The program will compare the extracted key and the original key.

### Run Visualization Python Script (plotCPA.py)
1. Open your terminal/command prompt and navigate to the directory of the plotCPA.py (should be in the same direcotry as CPASecretKeyRecovery.jar file.)
2. In the terminal/command prompt, type in "python3 plotCPA.py" to run the program
3. plot1.png and plot2.png are the output of the script and are saved in the same directory. It will take around 1 mins to export the 2 graphs due to large number of data points. 
