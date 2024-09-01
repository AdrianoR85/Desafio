from datetime import datetime,timedelta, date
from random import randint
import json

# 1. Generate a list of revenues
def generate_revenues(days: int, min_value: int, max_value: int) -> list:
  revenues = []
  for i in range(days):
    day = (date(2024,8,1) - timedelta(days=-i))
    value = float(randint(min_value, max_value)) if day.weekday() < 5 else 0
    revenue = {
      'date': day.strftime('%Y-%m-%d'),
      'revenue': value
    }
    revenues.append(revenue)
  return revenues

# Generate 31 days of revenues with random values between 10,000 and 50,000
revenues = generate_revenues(31, 10000, 50000)

# enues to a JSON file
with open('revenues.json', 'w') as f:
  json.dump(revenues, f)