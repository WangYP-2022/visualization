# Data Visualization Course - Executable Code Examples
# Based on the presentation slides

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Example 1: Basic scatter plot (similar to Life Expectancy visualization)

# Create sample data similar to the life expectancy example
np.random.seed(42)
continents = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
colors = ['#3498db', '#e67e22', '#2ecc71', '#e74c3c', '#9b59b6']

# Generate sample data
data = []
for i, continent in enumerate(continents):
    n_countries = np.random.randint(20, 40)
    gdp = np.random.lognormal(8, 1.5, n_countries)
    life_exp = 50 + 15 * np.log(gdp) + np.random.normal(0, 3, n_countries)
    life_exp = np.clip(life_exp, 40, 85)
    
    for j in range(n_countries):
        data.append({
            'continent': continent,
            'gdp_per_capita': gdp[j],
            'life_expectancy': life_exp[j],
            'population': np.random.lognormal(15, 2),
            'color': colors[i]
        })

df = pd.DataFrame(data)

# Create the visualization
plt.figure(figsize=(12, 8))
for continent, color in zip(continents, colors):
    continent_data = df[df['continent'] == continent]
    plt.scatter(
        continent_data['gdp_per_capita'],
        continent_data['life_expectancy'],
        s=continent_data['population'] / 1e6,
        alpha=0.6,
        c=color,
        label=continent,
        edgecolors='white',
        linewidth=0.5
    )

plt.xlabel('GDP per capita (2000 dollars)', fontsize=12)
plt.ylabel('Life Expectancy (years)', fontsize=12)
plt.title('Life Expectancy v. Per Capita GDP, 2007', fontsize=14, fontweight='bold')
plt.xscale('log')
plt.legend(title='Continent', loc='lower right')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('life_expectancy_gdp.png', dpi=300, bbox_inches='tight')
plt.show()

# Example 2: Line chart with multiple series

# Create sample sales data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
desktops = [80, 45, 25, 20, 10, 5]
laptops = [30, 25, 35, 50, 45, 55]
tablets = [10, 15, 20, 35, 60, 95]

plt.figure(figsize=(10, 6))
plt.plot(months, desktops, marker='o', linewidth=2, label='Desktops')
plt.plot(months, laptops, marker='o', linewidth=2, label='Laptops')
plt.plot(months, tablets, marker='o', linewidth=2, label='Tablets')

plt.xlabel('Month', fontsize=12)
plt.ylabel('Units Sold', fontsize=12)
plt.title('Product Sales by Month', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('sales_line_chart.png', dpi=300, bbox_inches='tight')
plt.show()

# Example 3: Demonstrating aspect ratio effects (from slide 21)

# Generate exponential data
x = np.linspace(0, 8, 100)
y = np.exp(x / 2)

# Create two plots with different aspect ratios
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Tall, narrow plot
ax1.plot(x, y, linewidth=2, color='#2c3e50')
ax1.set_xlabel('x', fontsize=11)
ax1.set_ylabel('Value', fontsize=11)
ax1.set_title('Narrow Aspect Ratio\n(Emphasizes steepness)', fontsize=12)
ax1.grid(True, alpha=0.3)
ax1.set_aspect(0.002)

# Wide plot
ax2.plot(x, y, linewidth=2, color='#2c3e50')
ax2.set_xlabel('x', fontsize=11)
ax2.set_ylabel('Value', fontsize=11)
ax2.set_title('Wide Aspect Ratio\n(De-emphasizes steepness)', fontsize=12)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('aspect_ratio_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

# Example 4: Bar chart

years = ['1972', '1974', '1976', '1978', '1980', '1982 est.']
costs = [50, 75, 125, 175, 250, 300]

plt.figure(figsize=(10, 6))
bars = plt.bar(years, costs, color='#c0392b', alpha=0.7, edgecolor='black')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Total Campaign Expenditures (millions)', fontsize=12)
plt.title('House and Senate Campaign Costs', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3, axis='y')

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'${int(height)}M',
             ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('campaign_costs.png', dpi=300, bbox_inches='tight')
plt.show()

# Example 5: Creating a basic plot with customization (teaching example)

# Simple example for beginners
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o', linestyle='-', color='blue', linewidth=2, markersize=8)
plt.xlabel('X Values', fontsize=12)
plt.ylabel('Y Values', fontsize=12)
plt.title('Simple Line Plot Example', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('simple_example.png', dpi=300, bbox_inches='tight')
plt.show()

print("All visualizations have been created and saved!")
print("\nFiles created:")
print("1. life_expectancy_gdp.png")
print("2. sales_line_chart.png")
print("3. aspect_ratio_comparison.png")
print("4. campaign_costs.png")
print("5. simple_example.png")

# Slide deck 02 - Matplotlib visualization examples

import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(613)

# Generate sample data
x = np.arange(50)
y = np.random.randint(0, 100, 50)

# Basic scatter plot
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y)

# Basic bar chart
fig, ax = plt.subplots(figsize=(5, 3))
ax.bar(x, y)

# Basic line plot
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y)

# Histogram with labels
fig, ax = plt.subplots(figsize=(5, 3))
ax.hist(y)
ax.set_title('Total growth over time')
ax.set_ylabel('Total growth')
ax.set_xlabel('Years since start')

# Define custom fonts
font1 = {'family': 'sans-serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'monospace', 'color': 'green', 'size': 14}

# Line plot with custom fonts
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y)
ax.set_title('Total growth over time', fontdict=font1)
ax.set_ylabel('Total growth', fontdict=font2)
ax.set_xlabel('Years since start', fontdict=font2)

# Line plot with left-aligned title
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y)
ax.set_title('Total growth over time', fontdict=font1, loc='left')
ax.set_ylabel('Total growth', fontdict=font2)
ax.set_xlabel('Years since start', fontdict=font2)

# Scatter plot with custom marker and color
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y, marker='*', color='indigo')
fig.show()

# Line plot with markers and dashed line
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y, marker='*', color='indigo', linestyle='--', linewidth=2)
fig.show()

# Line plot with hex color code
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y, marker='*', color='#7425b9', linestyle='--', linewidth=2)
fig.show()

# Line plot with custom marker styling
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y, marker='*', markersize=12, color='#7425b9', 
        linestyle='--', linewidth=2, 
        markeredgecolor='#fa9359', markerfacecolor='#fa9359')

# Add vertical gridlines
ax.grid(axis='y')

# Add styled gridlines
ax.grid(axis='y', color='blue', linewidth=2, linestyle='-.')

# Slide deck 05 - Advanced Matplotlib: Legends, Annotations, and Styling

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import PIL
import requests

# Generate sample data
np.random.seed(613)
x = np.arange(50)
y1 = np.random.randint(0, 100, 50)
y2 = np.random.randint(0, 100, 50)

# Basic multi-line plot
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y1)
ax.plot(x, y2)
fig.show()

# Multi-line plot with basic legend
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y1, label="Person 1")
ax.plot(x, y2, label="Person 2")
ax.legend(loc='lower right')
fig.show()

# Legend with custom styling
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y1, label="Person 1")
ax.plot(x, y2, label="Person 2")
ax.legend(loc='lower right',
          frameon=True,      # Add frame around legend
          fontsize=12,       # Change font size
          ncol=2,            # Two-column layout
          shadow=True)       # Add shadow effect
fig.show()

# Legend positioned outside plot area
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y1, label="Person 1")
ax.plot(x, y2, label="Person 2")
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
fig.show()

# Scatter plot with text annotation
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y1, label="Person 1")
ax.scatter(x, y2, label="Person 2")
ax.legend(loc='lower right')
ax.text(10, 95, "This value is important!")
fig.show()

# Text annotation with custom styling
ax.text(10, 95, "This value is important!",
        ha='center',       # Horizontal alignment
        color='red',       # Font color
        size=20)           # Font size
fig.show()

# Demonstrating different coordinate systems
fig, ax = plt.subplots()
ax.axis([0, 10, 0, 10])
ax.text(1, 5, ". Data:(1, 5)", transform=ax.transData)
ax.text(0.5, 0.1, ". Axes:(0.5, 0.1)", transform=ax.transAxes)
ax.text(0.2, 0.2, ". Figure:(0.2, 0.2)", transform=fig.transFigure)

# Corrected spacing in coordinate labels
ax.text(1, 5, ". Data: (1, 5)", transform=ax.transData)
ax.text(0.5, 0.1, ". Axes: (0.5, 0.1)", transform=ax.transAxes)
ax.text(0.2, 0.2, ". Figure: (0.2, 0.2)", transform=fig.transFigure)

# Annotation with arrow
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y1, label="Person 1")
ax.scatter(x, y2, label="Person 2")
ax.legend(loc='lower right')
ax.annotate('This is important!', xy=(10, 95), xytext=(20, 94),
            arrowprops=dict(facecolor='black'))
fig.show()

# Annotation with custom arrow style
ax.annotate('This is important!',
            xy=(10, 95), xytext=(20, 94),
            arrowprops=dict(arrowstyle="wedge", color="hotpink"))
fig.show()

# Hide axis ticks and labels
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y1, label="Person 1")
ax.scatter(x, y2, label="Person 2")
ax.legend(loc='lower right')
ax.yaxis.set_major_locator(plt.NullLocator())      # Remove y-axis ticks
ax.xaxis.set_major_formatter(plt.NullFormatter())  # Remove x-axis labels

# Limit number of x-axis ticks
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y1, label="Person 1")
ax.scatter(x, y2, label="Person 2")
ax.legend(loc='lower right')
ax.xaxis.set_major_locator(plt.MaxNLocator(3))  # Maximum 3 ticks

# Set x-axis ticks at regular intervals
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y1, label="Person 1")
ax.scatter(x, y2, label="Person 2")
ax.legend(loc='lower right')
ax.xaxis.set_major_locator(plt.MultipleLocator(5))  # Tick every 5 units

# Rotate x-axis labels
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y1, label="Person 1")
ax.scatter(x, y2, label="Person 2")
ax.legend(loc='lower right')
plt.xticks(rotation=45, ha='right')

# Custom axis label with font styling
font1 = {'family': 'serif', 'color': 'indigo'}
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y1, label="Person 1")
ax.scatter(x, y2, label="Person 2")
ax.legend(loc='lower right')
plt.xlabel('Shiny New X Axis!', fontsize=18, fontdict=font1)

# View available plot styles
plt.style.available

# Apply 'fivethirtyeight' style
plt.style.use('fivethirtyeight')

# Plot with applied style
plt.style.use('fivethirtyeight')
np.random.seed(613)
x = np.arange(50)
y1 = np.random.randint(0, 100, 50)
y2 = np.random.randint(0, 100, 50)
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y1)
ax.plot(x, y2)
fig.show()

# Slide deck 06 - Subplots, Multiple Plots, Error Bars, and Images

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import PIL
import requests

# Generate sample data
np.random.seed(613)
x1 = np.arange(50)
y1 = np.random.randint(0, 75, 50)
x2 = np.array(["Luffy", "Zoro", "Nami", "Usopp", "Sanji"])
y2 = np.array([110, 180, 240, 99, 220])

# Create empty figure with single subplot
fig, ax = plt.subplots(figsize=(5, 3))

# Create figure with 2 subplots (1 row, 2 columns)
fig, (ax1, ax2) = plt.subplots(ncols=2,
                                nrows=1,
                                figsize=(7, 3))

# Plot different data in each subplot
fig, (ax1, ax2) = plt.subplots(ncols=2,
                                nrows=1,
                                figsize=(7, 3))
ax1.scatter(x1, y1)
ax2.bar(x2, y2)
fig.show()

# Create mosaic layout (custom subplot arrangement)
fig, someaxes = plt.subplot_mosaic([['ax1', 'ax3'],
                                     ['ax2', 'ax3']],
                                    figsize=(7, 4))

# Populate mosaic subplots with different plot types
fig, someaxes = plt.subplot_mosaic([['ax1', 'ax3'],
                                     ['ax2', 'ax3']],
                                    figsize=(7, 4))
someaxes["ax1"].scatter(x1, y1)
someaxes["ax2"].bar(x2, y2)
someaxes["ax3"].plot(x1, y1)
plt.show()

# Add labels to mosaic subplots (may overlap without layout adjustment)
fig, someaxes = plt.subplot_mosaic([['ax1', 'ax3'],
                                     ['ax2', 'ax3']],
                                    figsize=(7, 4))
someaxes["ax1"].scatter(x1, y1)
someaxes["ax2"].bar(x2, y2)
someaxes["ax3"].plot(x1, y1)
someaxes["ax1"].set_xlabel('A Big Label', fontsize=18)
someaxes["ax2"].set_xlabel('Another Label', fontsize=18)
someaxes["ax3"].set_xlabel('Label 2: 2 Fast 2 Furious', fontsize=18)

# Use constrained layout to prevent label overlap
fig, someaxes = plt.subplot_mosaic([['ax1', 'ax3'],
                                     ['ax2', 'ax3']],
                                    figsize=(7, 4),
                                    layout="constrained")
someaxes["ax1"].scatter(x1, y1)
someaxes["ax2"].bar(x2, y2)
someaxes["ax3"].plot(x1, y1)
someaxes["ax1"].set_xlabel('A Big Label', fontsize=18)
someaxes["ax2"].set_xlabel('Another Label', fontsize=18)
someaxes["ax3"].set_xlabel('Label 2: 2 Fast 2 Furious', fontsize=18)

# Prepare data for overlapping plots
x = np.array(["Luffy", "Zoro", "Nami", "Usopp", "Sanji"])
y1 = np.array([110, 180, 240, 99, 220])
y2 = np.array([170, 100, 90, 120, 50])

# Overlay bar and line plots on same axes
fig, ax = plt.subplots(figsize=(7, 3))
ax.bar(x, y1, color="indigo")
ax.plot(x, y2, color="red")

# Calculate standard deviation for error bars
y2_sd = np.std(y2)

# Basic line plot (for comparison)
fig, ax = plt.subplots(figsize=(7, 3))
ax.plot(x, y2, color="red")

# Add basic error bars to plot
ax.errorbar(x,            # x values
            y2,           # y values
            yerr=y2_sd,   # error values
            fmt="none")   # no marker/line (only error bars)

# Customize error bar appearance
fig, ax = plt.subplots(figsize=(7, 3))
ax.plot(x, y2, color="red")
ax.errorbar(x,
            y2,
            yerr=y2_sd,
            fmt="none",
            ecolor="indigo",    # Error bar color
            elinewidth=4,       # Error bar line width
            capsize=6,          # Cap width
            capthick=4)         # Cap thickness

# Show error bars at intervals (every 2nd point)
ax.errorbar(x,
            y2,
            yerr=y2_sd,
            fmt="none",
            ecolor="indigo",
            elinewidth=4,
            capsize=6,
            capthick=4,
            errorevery=2)       # Show every 2nd error bar

# Download and load image from URL
from PIL import Image
import requests
from io import BytesIO

response = requests.get('https://upload.wikimedia.org/wikipedia/en/c/cb/Monkey_D_Luffy.png')
image_file = BytesIO(response.content)
image = Image.open(image_file)

# Create plot with space for image
fig, ax = plt.subplots(figsize=(7, 3))
ax.plot(x, y2, color="red")

# Add axes for image overlay (using figure coordinates)
ax_image = fig.add_axes([0.1,   # x position (0-1 range)
                         0.11,  # y position (0-1 range)
                         0.15,  # width
                         0.35]) # height

# Display image in overlay axes
fig, ax = plt.subplots(figsize=(7, 3))
ax.plot(x, y2, color="red")
ax_image = fig.add_axes([0.1, 0.11, 0.15, 0.35])
ax_image.imshow(image)
ax_image.axis('off')  # Hide image axes








