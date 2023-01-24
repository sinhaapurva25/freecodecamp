import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv(r'Data Analysis With Python\boilerplate-sea-level-predictor\epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    lingress_output = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = [i for i in range(1880, 2051)]
    y = [(lingress_output[0] * x[i] + lingress_output[1]) for i in range(0, len(x))]
    # x = np.array([i for i in range(1880, 2050)])
    # y = lingress_output[0] * x + lingress_output[1]
    print(y)

    # Create second line of best fit
    # lingress_output = linregress(df['Year'][df['Year'] >= 2000], df['CSIRO Adjusted Sea Level'][df['Year'] >= 2000])
    lingress_output = linregress(df['Year'][df['Year'] >= 2000], df['CSIRO Adjusted Sea Level'][df['Year'] >= 2000])
    x_2 = np.array([i for i in range(2000, 2051)])
    y_2 = [(lingress_output[0] * x_2[i] + lingress_output[1]) for i in range(0, len(x_2))]
    # x_2 = np.array([i for i in range(1880, 2050)])
    # y_2 = lingress_output[0] * x_2 + lingress_output[1]

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.plot(x, y, label='best fit line')
    plt.plot(x_2, y_2, label='second best fit line')
    plt.tight_layout()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
