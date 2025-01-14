import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in FCU checkings df
df = pd.read_csv("MSU_FCU_22_24_Checkings.csv")

# Convert dates to right format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Add trendline using linear regression
slope, intercept = np.polyfit(df['Date'].map(lambda x: x.toordinal()), df['New Balance'], 1)

# Plot data and trendline
plt.plot(df['Date'], df['New Balance'], label='New Balance')
plt.plot(df['Date'], slope * df['Date'].map(lambda x: x.toordinal()) + intercept, 'r--', label='Trend')
plt.xticks(rotation=45)
plt.title(label="Apollo Checking Account Over Time")
plt.legend()
plt.tight_layout()
plt.show()

##########################################################################################################

# Read in FCU savings df
df = pd.read_csv("MSU_FCU_22_24_Savings.csv")

# Convert dates to right format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df.columns
# Add trendline using linear regression
slope, intercept = np.polyfit(df['Date'].map(lambda x: x.toordinal()), df['New Balance'], 1)

# Plot data and trendline
plt.plot(df['Date'], df['New Balance'], label='New Balance')
plt.plot(df['Date'], slope * df['Date'].map(lambda x: x.toordinal()) + intercept, 'r--', label='Trend')
plt.xticks(rotation=45)
plt.title(label="Apollo Savings Account Over Time")
plt.legend()
plt.tight_layout()
plt.show()

##########################################################################################################

# Read in end of year df
df = pd.read_csv("MSU_FCU_EOY_Balances.csv")

# Group by 'Account Type' and plot each account's balance over time
for account_type in df['Account Type'].unique():
    account_data = df[df['Account Type'] == account_type]
    plt.plot(account_data['End of Year'], account_data['Balance'], marker='o', label=account_type)
    
# Calculate the total balance for each year
total_balance = df.groupby('End of Year')['Balance'].sum()

# Plot the total balance line
plt.plot(total_balance.index, total_balance, marker='s', linestyle='--', color='black', label='Total Balance')


# Add labels and title
plt.xlabel('Year')
plt.ylabel('Balance')
plt.title('Apollo Account Balances Over Time')

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Show legend
plt.legend(title="Account Type", fontsize = "small")

# Adjust layout to avoid clipping
plt.tight_layout()

# Show the plot
plt.show()