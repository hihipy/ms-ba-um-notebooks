'''
11.10 LAB: Flight status (line plot)
The LAX dataset contains the flight status at the Los Angeles International Airport in a given year and has the following column labels: Month, Cancelled, Delayed, Diverted, and On Time.

Given a CSV file name read from user input, write a program that performs the following tasks:

Read in the CSV file as a dataframe.
Output the average of flight delays and the average of flight cancellations, with two digits after the decimal point. Follow the output format in the example below.
Create a lineplot of the number of flights delayed each month. Label the plot "Delays".
In the same figure, create another lineplot of the number of flights cancelled each month. Label the plot "Cancellations".
Add the x-label ("Months", fontsize = 10), y-label ("Number of flights", fontsize = 10), title ("Flight status at LAX", fontsize = 14), and a legend to the figure.
Save the figure as output_fig.png.

Input and Output Example

If the input is:
LAX_2004.csv

the output is:

Average delays: 3309.64
Average cancellations: 215.18
and the output figure (saved in output_fig.png) is:
A figure containing a lineplot of flight delays vs months and a lineplot of flight cancellations vs months.
'''
import matplotlib.pyplot as plt
import pandas as pd

file = input()

# Read in the CSV file as a dataframe
df = pd.read_csv(file)

# Print the average of flight delays and flight cancellations
avg_delays = df['Delayed'].mean()
avg_cancellations = df['Cancelled'].mean()
print(f"Average delays: {avg_delays:.2f}")
print(f"Average cancellations: {avg_cancellations:.2f}")

# Create a lineplot of flight delays vs months
plt.plot(df['Month'], df['Delayed'], label='Delays', color='blue', marker='o')

# In the same figure, create a lineplot of flight cancellations vs months
plt.plot(df['Month'], df['Cancelled'], label='Cancellations', color='red', marker='o')

# Add axis labels, title, and legend
plt.xlabel('Months', fontsize=10)
plt.ylabel('Number of flights', fontsize=10)
plt.title('Flight status at LAX', fontsize=14)
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Save figure as output_fig.png
plt.savefig('output_fig.png')
plt.show()