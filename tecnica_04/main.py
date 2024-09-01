import json
from pathlib import Path

file_path = "MonthlyRevenueByDistributor.json"

with open(file_path, 'r') as file:
  data = json.load(file) # Load the JSON data

  total_revenue = sum(item['revenue'] for item in data) # Calculate the total revenue

  percent_by_state = {} # Dictionary to store the percentage of total revenue for each state

  # Calculate the percentage of total revenue for each state and store it in the dictionary
  for item in data:
    state = item['state']
    revenue = item['revenue']
    percent = (revenue / total_revenue) * 100
    percent_by_state[state] = round(percent,2)

  # Show the results
  for state, percent in percent_by_state.items():
    print(f"State: {state.upper()}: {percent}%")



