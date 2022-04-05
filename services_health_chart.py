import csv
from numpy import number
import plotly.express as px

services = []
health = []
healthNumber = []

with open("services_health.csv",'r') as f:
    reader = csv.reader(f)

    next(reader)

    for line in reader:
        services.append(line[1])
        health.append(line[2])
    
    for item in health:
        if item == "Active":
            healthNumber.append(100)
        else:
            healthNumber.append(0)

healthData = {
  "type": 'bar',
  "data": {
    "labels": services,
    "datasets": [{
      "label": 'Active Services',
      "data": healthNumber,
    }]
  },
  "options": {
    "legend": {
      "position": 'top',
    },
  },
}

health_chart = "https://quickchart.io/chart?c={}".format(healthData)
print(health_chart)