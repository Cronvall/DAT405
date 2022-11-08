import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors


def solution():
    gdp_data = pd.read_csv("./gdp2015.csv")
    life_expectancy = pd.read_csv("./life-expectancy.csv")
    xValues = []
    yValues = []

    life_expectancy.query("Year == 2015", inplace=True)

    # Place all points with relations in both tables in the plot.
    for i, rowI in gdp_data.iterrows():
        for j, rowJ in life_expectancy.iterrows():
            if rowJ['Code'] == rowI['Code']:
                xValues.append(rowI['GDP per capita'])
                yValues.append(rowJ['Life expectancy'])

    print(gdp_data['GDP per capita'].mean())
    print("Standard deviation ", gdp_data['GDP per capita'].std())
    c_map = colors.LinearSegmentedColormap.from_list("custom", ["#FA8564", "#58ED2D", "#2FF743", "#2FF7B5", "#2DEDE3"])
    # Drawing the plot
    plt.scatter(xValues, yValues, cmap=c_map, c=gdp_data['GDP per capita'][1:168], s= 25)
    plt.colorbar()
    plt.title("GDP per capita in relation to Life Expectancy")
    plt.xscale('log')
    plt.xlabel("GDP per capita (USD $)")
    plt.ylabel("Life expectancy (years)")
    plt.show()


if __name__ == '__main__':
    solution()
