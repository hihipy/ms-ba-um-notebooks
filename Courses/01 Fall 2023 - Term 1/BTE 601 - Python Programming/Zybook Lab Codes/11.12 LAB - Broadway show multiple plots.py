'''
11.12 LAB: Broadway show multiple plots
Given two CSV files containing data for Broadway shows' Capacity (percentage of the theatre filled) and Gross Potential (maximum amount that can be earned) for multiple shows in a specific month:

Read in each CSV file as dataframes.
Print each dataframe individually with a separate print function, one print function per dataframe.
Generate an image containing two scatter subplots comparing that month's Capacity and Gross Potential.
The main title of the image should be "Capacity vs. Gross Potential", with each subplot's title being the month and year, respectively (i.e. "July 2002").
The left subplot should be July's, with the right subplot being December's.
The x-axis should be "Gross Potential" with the y-axis being "Capacity".

Input and Output Example

Ex. If the input is:
broadway_jul_2002.csv
broadway_dec_2002.csv

The output using the print functions should be:

     Month  Year  Capacity  Gross Potential
0        7  2002        39               22
1        7  2002        34               23
2        7  2002        46               29
3        7  2002        38               29
4        7  2002        40               30
..     ...   ...       ...              ...
99       7  2002        97               92
100      7  2002        99              108
101      7  2002        99              109
102      7  2002        99              109
103      7  2002        99              109

[104 rows x 4 columns]
     Month  Year  Capacity  Gross Potential
0       12  2002        30               20
1       12  2002        28               20
2       12  2002        25               24
3       12  2002        58               25
4       12  2002        31               26
..     ...   ...       ...              ...
128     12  2002        91              102
129     12  2002        98              109
130     12  2002       100              110
131     12  2002       100              111
132     12  2002        99              112

[133 rows x 4 columns]

and the output figure (saved in subplots.png) is:
An image containing two scatter plots comparing a particular month's capacity versus gross potential. Each mark is proportional to the value of the Gross Potential.

'''
import matplotlib.pyplot as plt
import pandas as pd

# Get input files 
file1 = input()
file2 = input()

# Read in .csv files as dataframes
df1 = pd.read_csv(file1)  
df2 = pd.read_csv(file2)

# Print each dataframe  
print(df1)
print(df2)

# Create subplots with 1 row, 2 columns
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5)) 

# Plotting for first dataframe (left subplot)
axes[0].scatter(df1['Gross Potential'], df1['Capacity'], color='blue', alpha=0.5)
axes[0].set_title(f"{df1['Month'].iloc[0]} {df1['Year'].iloc[0]}")  
axes[0].set_xlabel("Gross Potential")
axes[0].set_ylabel("Capacity")
axes[0].grid(True, linestyle='--', linewidth=0.5)

# Plotting for second dataframe (right subplot) 
axes[1].scatter(df2['Gross Potential'], df2['Capacity'], color='red', alpha=0.5)
axes[1].set_title(f"{df2['Month'].iloc[0]} {df2['Year'].iloc[0]}")
axes[1].set_xlabel("Gross Potential")
axes[1].set_ylabel("Capacity")
axes[1].grid(True, linestyle='--', linewidth=0.5)

# Set main title  
fig.suptitle("Capacity vs. Gross Potential")  

# Adjust layout 
plt.tight_layout()  

# Save figure 
plt.savefig('subplots.png')

# Show plot
plt.show()