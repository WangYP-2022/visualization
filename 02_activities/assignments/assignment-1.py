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

# ============================================================================
# Example 5: Creating a basic plot with customization (teaching example)
# ============================================================================

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

