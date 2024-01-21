"""
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
"""
import matplotlib.pyplot as plt
import pandas as pd


def read_csv(file_name):
    """
    Reads a CSV file into a pandas DataFrame.
    :param file_name: Name of the CSV file to read.
    :return: DataFrame created from the CSV file.
    """
    return pd.read_csv(file_name)


def calculate_and_print_averages(df):
    """
    Calculates and prints the average number of delays and cancellations.
    :param df: DataFrame containing flight data.
    """
    avg_delays = df['Delayed'].mean()
    avg_cancellations = df['Cancelled'].mean()
    print(f"Average delays: {avg_delays:.2f}")
    print(f"Average cancellations: {avg_cancellations:.2f}")


def create_line_plot(df):
    """
    Creates a line plot for the number of delayed and cancelled flights.
    :param df: DataFrame containing flight data.
    """
    plt.plot(df['Month'], df['Delayed'], label='Delays', color='blue', marker='o')
    plt.plot(df['Month'], df['Cancelled'], label='Cancellations', color='red', marker='o')
    plt.xlabel('Months', fontsize=10)
    plt.ylabel('Number of flights', fontsize=10)
    plt.title('Flight status at LAX', fontsize=14)
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.savefig('output_fig.png')
    plt.show()


def main():
    """
    Main function to execute the script.
    """
    file_name = input("Enter the CSV file name: ")
    df = read_csv(file_name)
    calculate_and_print_averages(df)
    create_line_plot(df)


if __name__ == "__main__":
    main()
