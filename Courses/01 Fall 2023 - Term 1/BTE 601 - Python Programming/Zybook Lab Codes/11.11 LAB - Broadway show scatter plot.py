'''
11.11 LAB: Broadway show scatter plot
The Broadway dataset contains data for Broadway shows' Capacity (percentage of the theatre filled) and Gross Potential (maximum amount that can be earned) for multiple shows in a specific month and year.

Given a CSV file name read from user input, write a program that performs the following tasks:

Read in the CSV file as a dataframe.
Insert a new column labelled "Size" at the end of the dataframe. The "Size" column contains values in column "Gross Potential" divided by 2.
Output the dataframe using the print() function.
Create a scatter plot of "Gross Potential" vs "Capacity" with the following marker styling parameters:
markers: 'x'
color: orange
size: values in column "Size"
Add the x-label ("Capacity", fontsize = 10), y-label ("Gross Potential", fontsize = 10), and title ("Gross Potential vs Capacity", fontsize = 16) to the figure.
Add gridlines to the figure using '--' as linestyle.
Save the figure as output_fig.png.

Input and Output Example
Ex: If the input is:
broadway_jul_2000.csv

the output using the print() function should be:

     Date.Month  Date.Year  Capacity  Gross Potential  Size
0             7       2000        36               25  12.5
1             7       2000        47               28  14.0
2             7       2000        46               28  14.0
3             7       2000        63               30  15.0
4             7       2000        49               31  15.5
..          ...        ...       ...              ...   ...
122           7       2000       100               97  48.5
123           7       2000       100               97  48.5
124           7       2000       100               98  49.0
125           7       2000       100               98  49.0
126           7       2000        97              121  60.5

[127 rows x 5 columns]

and the output figure (saved in output_fig.png) is:

A figure containing a scatter plot of Gross Potential vs Capacity of the Broadway dataset. The size of each mark is proportional to the value of the Gross Potential.
'''
import matplotlib.pyplot as plt
import pandas as pd

file = input()

# Read in CSV file as a dataframe
df = pd.read_csv(file)

# Insert a column to the dataframe as the last column
# Label the column "Size", which contains half the values in column "Gross Potential"
df['Size'] = df['Gross Potential'] / 2

# Output dataframe
print(df)

# Create scatter plot
plt.scatter(df['Capacity'], df['Gross Potential'], c='orange', s=df['Size'], marker='x')

# Add axis labels and title
plt.xlabel('Capacity', fontsize=10)
plt.ylabel('Gross Potential', fontsize=10)
plt.title('Gross Potential vs Capacity', fontsize=16)

# Add gridlines
plt.grid(True, linestyle='--', linewidth=0.5)

# Save figure as output_fig.png
plt.savefig('output_fig.png')
plt.show()