import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', header=0, sep=',')


    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data Points')

    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    x_pred = np.arange(1880, 2051, 1)
    y_pred = slope * x_pred + intercept
    plt.plot(x_pred, y_pred, color='red', label='Best Fit Line 1')

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    x_2000 = df_2000['Year']
    y_2000 = df_2000['CSIRO Adjusted Sea Level']
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(x_2000, y_2000)
    x_pred_2000 = np.arange(2000, 2051, 1)
    y_pred_2000 = slope_2000 * x_pred_2000 + intercept_2000
    plt.plot(x_pred_2000, y_pred_2000, color='green', label='Best Fit Line 2')


    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
