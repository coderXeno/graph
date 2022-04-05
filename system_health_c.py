import csv

statuses = []
reqd_tasks = []

cpu_load = 0
total_space = 0
used_space = 0
clc_space = 0
percent_space = 0

total_ram = 0
used_ram = 0
clc_ram = 0
percent_ram = 0

total_swap_space = 0
used_swap_space = 0
clc_swap_space = 0
percent_swap_space = 0

with open("system_health.csv","r") as f:
    reader = csv.reader(f)
    
    rows = reader
    #print(list(rows)[0])
    lists = list(rows)

    cpu_load = float(lists[13][3].replace("%",""))

    total_space = float(lists[18][5].replace("GB",""))
    used_space = float(lists[19][5].replace("GB",""))
    
    clc_space = (used_space /total_space ) * 100
    percent_space = "{:.2f}".format(clc_space)

    total_ram = float(lists[21][6].replace("MB",""))
    used_ram = float(lists[22][6].replace("MB",""))
    
    clc_ram = (used_ram /total_ram ) * 100
    percent_ram = "{:.2f}".format(clc_ram)

    total_swap_space = float(lists[25][7].replace("MB",""))
    used_swap_space = float(lists[26][7].replace("MB",""))
    
    clc_swap_space = (used_swap_space /total_swap_space ) * 100
    percent_swap_space = "{:.2f}".format(clc_swap_space)

with open("system_health.csv","r") as f:
    readData = csv.reader(f)

    for line in readData:
        statuses.append(line[1])

    for item in statuses:
        if item == "CPU Load" or item == "Used Space" or item == "Used Ram" or item == "Used Swap Space":
            reqd_tasks.append(item)

    reqd_tasks.append('Total')
    
health_percentages = {
  "type": "horizontalBar",
  "data": {
    "labels": reqd_tasks,
    "datasets": [
      {
        "label": "Services Status",
        "backgroundColor": "rgba(255, 99, 132, 0.5)",
        "borderColor": "rgb(255, 99, 132)",
        "borderWidth": 1,
        "data": [
          cpu_load,
          percent_space,
          percent_ram,
          percent_swap_space,
          "100.0"
        ]
      },
    ]
  },
  "options": {
    "responsive": "true",
    "title": {
      "display": "true",
      "text": "Status of System Health"
    }
  }
}
system_resources_chart = "https://quickchart.io/chart?c={}".format(health_percentages)

healths = {
  "type": "doughnut",
  "data": {
    "datasets": [{
      "label": "cpu load",
      "data": [32.6, 100-32.6],
      "backgroundColor": [
        "rgba(0,0,0, 0.7)",
        "rgba(0, 0, 0, 0.3)"
      ],
      "textcolor":["#000","#000"],
      "borderWidth": 1,
    },{
      "label": "used space",
      "data": [44.65, 100-44.65],
      "backgroundColor": [
        "rgba(255, 99, 132, 1)",
        "rgba(0, 0, 0, 0.3)"
      ],
      "textcolor":["#000555","#555555"],
      "borderWidth": 1,
    },{
      "label": "used swap space",
      "data": [24.69, 100-24.69],
      "backgroundColor": [
        "rgba(255, 108, 200, 1)",
        "rgba(0,0,0,0.3)"
      ],
      "textcolor":["#000555","#555555"],
      "borderWidth": 1,
    },{
      "label": "used ram",
      "data": [58.10, 100-58.10],
      "backgroundColor": [
        "rgba(225, 99, 132, 1)",
        "rgba(0, 0, 0, 0.3)"
      ],
      "textcolor":["#000555","#555555"],
      "borderWidth": 1,
    }] 
  },
  "options": {
    "rotation": "Math.PI",
    "circumference": "Math.PI",
    "cutoutPercentage": 75,
    "plugins": {
      "datalabels": { "display": "false" },
      "doughnutlabel": {
        "labels": [
          {
            "text": "\nCPU LOAD",
            "color": "#000000",
            "font": {
              "size": "25"
            },
          },{
            "text": "\nUSED SPACE",
            "color": "#ff6384",
            "font": {
              "size": "25"
            },
          },{
            "text": "\nUSED SWAP SPACE",
            "color": "#ff6cc8",
            "font": {
              "size": "25"
            },
          },{
            "text": "\nUSED RAM",
            "color": "#e16384",
            "font": {
              "size": "25"
            },
          }
        ]
      }
    }		
  }
}

graphs = "https://quickchart.io/chart?c={}".format(healths)
print(graphs)