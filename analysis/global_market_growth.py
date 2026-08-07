import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("global_semiconductor_market.csv")

# Create figure
plt.figure(figsize=(8, 5))

# Plot line
plt.plot(
    df["Year"],
    df["Market_Size_USD_Billion"],
    marker='o',
    linewidth=2.5,
    markersize=8
)

# Add data labels
for x, y in zip(df["Year"], df["Market_Size_USD_Billion"]):
    offset = 6 if x == 2020 else 4
    plt.text(
        x,
        y + offset,
        f"{y:.1f}",
        ha="center",
        fontsize=9
    )

# Title and labels
plt.title(
    "Global Semiconductor Market Size (2020–2024)",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Year", fontsize=11)
plt.ylabel("Market Size (USD Billion)", fontsize=11)

# Axis limits
plt.xlim(2019.8, 2024.2)
plt.ylim(400, 650)

# Show only integer years
plt.xticks(df["Year"])

# Horizontal gridlines only
plt.grid(axis="y", alpha=0.25)

# Remove top and right borders
ax = plt.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Source note
plt.figtext(
    0.99,
    0.01,
    "Source: Semiconductor Industry Association (SIA)",
    ha="right",
    fontsize=7,
    color="gray"
)

# Adjust layout
plt.tight_layout()

# Save high-resolution image
plt.savefig(
    "global_market_growth.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
