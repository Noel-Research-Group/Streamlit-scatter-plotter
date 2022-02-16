"""
Demo on using Streamlit for plotting data

D.Pintossi
2022-02-16
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import random


# Create mockup data
def f(t):
    return t**2 + t + 3 * (random.random() - 1)


x = np.linspace(0, 10, 5000)
y = f(x)
df = pd.DataFrame({
    'x': x,
    'y': y,
})
df.to_csv('mockup_data.csv', index=False)


# Set up the plot
st.title('Scatter-plotter')

# Add axis titles
plt.xlabel('Optical path length [cm]')
plt.ylabel('Transmittance [%]')

# Set font for plots
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 14

# Set custom color palette based on hex codes
# form coolors.co (should be fine for color-blind people)
red_orange_color_wheel = '#f6511d'
jet = '#343434'
space_cadet = '#2f3061'
naples_yellow = '#ffe66d'
queen_pink = '#d6c3c9'

# Set linewidth
plt.rcParams['axes.linewidth'] = 1.5

# Set up the figure object and define its size
cm = 1/2.54  # this is just to convert inches into cm
fig = plt.figure(figsize=(12*cm, 12*cm))

# Add axes to the figure object
#  1.25:1 aspect ratio is the default one in Origin
ax = fig.add_axes([0, 0, 1.25, 1])

# Customize geometry of the ticks
L1 = 6    # major tick length
W1 = 1.5  # major tick width
L2 = 4    # minor tick length
W2 = 1.5  # minor tick width
ax.xaxis.set_tick_params(which='major', size=L1, width=W1)
ax.xaxis.set_tick_params(which='minor', size=L2, width=W2)
ax.yaxis.set_tick_params(which='major', size=L1, width=W1)
ax.yaxis.set_tick_params(which='minor', size=L2, width=W2)

# Add data series
ax.plot(data["Length [cm]"], data["T [%] @ 0.0001 M"],
        color=queen_pink, label="0.1 mM")

# Set limits of the axes
ax.set_xlim(0, 25)
ax.set_ylim(-0.4, 100)

# Set major/minor ticks locations on the axes
# x-axis
ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1))
# y-axis
ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(20))
ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(10))

# Set axes titles
ax.set_xlabel('Optical path length [cm]', labelpad=10, fontweight='bold')
ax.set_ylabel('Transmittance [%]', labelpad=10, fontweight='bold')

# Create labels
ax.annotate('0.1 mM', xy=(15,76), color=queen_pink, ha='center')

# Save plot as PDF and PNG (600 dpi)
plt.savefig('Origin-like plot.pdf', bbox_inches='tight')
plt.savefig('Origin-like plot.png', dpi=600, bbox_inches='tight')