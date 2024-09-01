import json

# Return the mean revenue from the list of revenues
def mean_revenue(revenues: list) -> float:
  total = 0
  count = 0
  for revenue in revenues:
    if revenue['revenue'] != 0:
      total += revenue['revenue']
      count += 1
  
  return total / count

# Read the revenues from the json file
with open('revenues.json', 'r') as f:
  revenues = json.load(f)
  min_value = revenues[0]['revenue']
  max_value = revenues[0]['revenue']
  mean = mean_revenue(revenues)
  days = 0

  # Find the min, max and days with revenue above mean
  for revenue in revenues: 
    if revenue['revenue'] != 0:

      if min_value > revenue['revenue']:
        min_value = revenue['revenue']
      
      if max_value < revenue['revenue']:
        max_value = revenue['revenue']

      if revenue['revenue'] > mean:
        days += 1

  print(f'Min revenue: {min_value:.2f}')
  print(f'Max revenue: {max_value:.2f}')
  print(f'Days with revenue above mean: {days} days')



