import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../data/global_semiconductor_market.csv")

plt.figure(figsize=(8,5))

plt.plot(
    df["Year"],
    df["Market_Size_USD_Billion"],
    marker='o',
    linewidth=2
)

plt.title("Global Semiconductor Market Size (2020–2024)")
plt.xlabel("Year")
plt.ylabel("Market Size (USD Billion)")
plt.grid(True)

for x, y in zip(df["Year"], df["Market_Size_USD_Billion"]):
    plt.text(x, y + 8, f"{y:.1f}", ha="center", fontsize=9)

plt.tight_layout()

plt.savefig("../charts/global_market_growth.png", dpi=300)

plt.show()
