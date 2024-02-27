import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create list of the years (x) to predict later.
    year_predict1 = pd.Series(range(1880, 2051, 1));
    year_predict2 = pd.Series(range(2000, 2051, 1));

    # Extract the year values to be inputted as the x.
    Year = df['Year']
    Recent_Year = df['Year'][df['Year']>=2000]

    # Extract the sea level values to be inputted as the y.
    Recent_Level = df['CSIRO Adjusted Sea Level'][df['Year']>=2000]

    # Create scatter plot
    scatter = plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='lightsteelblue', s=8)
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Create first line of best fit
    reg_predict1 = linregress(Year, df['CSIRO Adjusted Sea Level'])
    level_predict1 = reg_predict1.intercept + reg_predict1.slope * year_predict1
    plt.plot(year_predict1, level_predict1,'-', color='red', linewidth=1)

    # Create second line of best fit
    reg_predict2 = linregress(Recent_Year, Recent_Level)
    level_predict2 = reg_predict2.intercept + reg_predict2.slope * year_predict2
    plt.plot(year_predict2, level_predict2, '--',  color='purple', linewidth=1)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()