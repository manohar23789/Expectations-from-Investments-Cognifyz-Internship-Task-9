import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset
df = pd.read_csv("Data_set 2 - Copy.csv")

# Step 2: Display all column names
print("Column Names:")
print(df.columns.tolist())

# Step 3: Display the Expectations column
print("\nExpectations from Investments:")
print(df["Expect"])

# Step 4: Count the frequency of each expectation
expectation_counts = df["Expect"].value_counts()

print("\nFrequency of Investment Expectations:")
print(expectation_counts)

# Step 5: Calculate the percentage of participants
total_participants = expectation_counts.sum()

percentage = (expectation_counts / total_participants) * 100

# Step 6: Create a summary table
summary = pd.DataFrame({
    "Expectation": expectation_counts.index,
    "Number of Participants": expectation_counts.values,
    "Percentage": percentage.values.round(2)
})

print("\nSummary of Investment Expectations:")
print(summary)

# Step 7: List and describe the common expectations
print("\nCommon Expectations from Investments:")

for index, row in summary.iterrows():
    print(
        f"{index + 1}. {row['Expectation']} - "
        f"{row['Number of Participants']} participants "
        f"({row['Percentage']}%)"
    )

# Step 8: Identify the most common expectation
most_common_expectation = expectation_counts.idxmax()
highest_frequency = expectation_counts.max()

print("\nMost Common Investment Expectation:")
print(most_common_expectation)

print("Number of Participants:")
print(highest_frequency)

# Step 9: Create a bar chart
plt.figure(figsize=(8, 5))

expectation_counts.plot(kind="bar")

plt.title("Expectations from Investments")
plt.xlabel("Investment Expectation")
plt.ylabel("Number of Participants")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()