import csv

cameras = []
smoke_camera_frames = []
outside_camera_1_frames = []
outside_camera_2_frames = []
office_camera_frames = []
hours = []

with open("frame_count.csv","r") as f:
    reader = csv.reader(f)

    next(reader)

    rows = reader
    #print(list(rows)[0])
    lists = list(rows)
    
    newlist1 = lists[0]
    smoke_camera_frames = newlist1[5:]

    newlist2 = lists[1]
    outside_camera_1_frames = newlist2[5:]

    newlist3 = lists[2]
    office_camera_frames = newlist3[5:]

    newlist4 = lists[3]
    outside_camera_2_frames = newlist4[5:]

with open("frame_count.csv","r") as f:
    readx = csv.reader(f)

    timings = next(readx)
    hourly = timings[5:]

smokeCameraData = {
    "type": 'bar',
    "data": {
        "labels": hourly,
        "datasets": [{
        "label": 'Smoke Camera',
        "data": smoke_camera_frames,
        }]
    },
    "options": {
        "legend": {
        "position": 'top',
        },
    },
}

smoke_chart = "https://quickchart.io/chart?c={}".format(smokeCameraData)

outside1CameraData = {
    "type": 'bar',
    "data": {
        "labels": hourly,
        "datasets": [{
        "label": 'Outside 1 Camera',
        "data": outside_camera_1_frames,
        }]
    },
    "options": {
        "legend": {
        "position": 'top',
        },
    },
}

outside_1_chart = "https://quickchart.io/chart?c={}".format(outside1CameraData)

outside2CameraData = {
    "type": 'bar',
    "data": {
        "labels": hourly,
        "datasets": [{
        "label": 'Outside 2 Camera',
        "data": outside_camera_2_frames,
        }]
    },
    "options": {
        "legend": {
        "position": 'top',
        },
    },
}

outside_2_chart = "https://quickchart.io/chart?c={}".format(outside2CameraData)

officeCameraData = {
    "type": 'bar',
    "data": {
        "labels": hourly,
        "datasets": [{
        "label": 'Office Camera',
        "data": office_camera_frames,
        }]
    },
    "options": {
        "legend": {
        "position": 'top',
        },
    },
}

office_chart = "https://quickchart.io/chart?c={}".format(officeCameraData)

a = {
  "type": "bar",
  "data": {
    "labels": hourly,
    "datasets": [
      {
        "label": "Dataset 2",
        "backgroundColor": "rgba(54, 162, 235, 0.5)",
        "borderColor": "rgb(54, 162, 235)",
        "borderWidth": 1,
        "data": office_camera_frames
      }
    ]
  },
  "options": {
    "responsive": "true",
    "legend": {
      "position": "top"
    },
    "title": {
      "display": "true",
      "text": "Chart.js Bar Chart"
    },
    "plugins": {
      "roundedBars": "true" 
    }
  }
}

#rounded
office_1_chart = "https://quickchart.io/chart?c={}".format(a)

b = {
  "type": 'line',
  "data": {
    "labels": hourly,
    "datasets": [
      {
        "label": 'Data',
        "steppedLine": "true",
        "data": office_camera_frames,
        "borderColor": 'rgb(255, 99, 132)',
        "fill": "true",
      },
    ],
  },
  "options": {
    "responsive": "true",
    "title": {
      "display": "true",
      "text": 'Stepped line',
    },
  },
}

#stepped line
office_2_chart = "https://quickchart.io/chart?c={}".format(b)

c = {
  "type": "bar",
  "data": {
    "labels": hourly,
    "datasets": [
      {
        "label": "Office Camera",
        "borderColor": "rgb(255, 99, 132)",
        "backgroundColor": "rgb(255, 99, 132)",
        "fill": "false",
        "data": office_camera_frames,
        "yAxisID": "y"
      },
      {
        "label": "Outside Camera 1",
        "borderColor": "rgb(54, 162, 235)",
        "backgroundColor": "rgb(54, 162, 235)",
        "fill": "false",
        "data": outside_camera_1_frames,
        "yAxisID": "y1"
      }
    ]
  },
  "options": {
    "stacked": "false",
    "title": {
      "display": "true",
      "text": "Systems"
    },
    "plugins": {
      "roundedBars": "true" 
    },
    "scales": {
      "yAxes": [
      {
        "id": "y",
        "type": "linear",
        "display": "true",
        "position": "left"
      }, 
      {
        "id": "y1",
        "type": "linear",
        "display": "true",
        "position": "right",
        "gridLines": {
          "drawOnChartArea": "false"
        }
      }
      ]
    }
  }
}

office_3_chart = "https://quickchart.io/chart?c={}".format(c)

d = {
  "type": "bar",
  "data": {
    "labels": hourly,
    "datasets": [
      {
        "type": "line",
        "label": "Office Camera",
        "borderColor": "rgb(54, 162, 235)",
        "borderWidth": 2,
        "fill": "false",
        "data": office_camera_frames
      },
      {
        "type": "bar",
        "label": "Outside Camera 1",
        "backgroundColor": "rgb(255, 99, 132)",
        "data": outside_camera_1_frames,
        "borderColor": "white",
        "borderWidth": 2
      },
    ]
  },
  "options": {
    "responsive": "true",
    "title": {
      "display": "true",
      "text": "Frame Rates"
    },
    "tooltips": {
      "mode": "index",
      "intersect": "true"
    }
  }
}

office_4_chart = "https://quickchart.io/chart?c={}".format(d)

f = {
  "type": "radar",
  "data": {
    "labels": hourly,
    "datasets": [
      {
        "backgroundColor": "rgba(255, 99, 132, 0.5)",
        "borderColor": "rgb(255, 99, 132)",
        "data": office_camera_frames,
        "label": "D0"
      },
      {
        "backgroundColor": "rgba(255, 159, 64, 0.5)",
        "borderColor": "rgb(255, 159, 64)",
        "data": outside_camera_1_frames,
        "label": "D1",
        "fill": "-1"
      }
    ]
  },
  "options": {
    "maintainAspectRatio": "true",
    "spanGaps": "false",
    "elements": {
      "line": {
        "tension": "0.000001"
      }
    },
    "plugins": {
      "filler": {
        "propagate": "false"
      },
      "samples-filler-analyser": {
        "target": "chart-analyser"
      }
    }
  }
}

office_5_chart = "https://quickchart.io/chart?c={}".format(f)

g = {
  "type": 'line',
  "data": {
    "labels": hourly,
    "datasets": [
      {
        "label": 'Outside 1 Camera',
        "borderColor": 'rgb(255, 99, 132)',
        "backgroundColor": 'rgba(255, 99, 132, .5)',
        "data": outside_camera_1_frames,
      },
      {
        "label": 'Office Camera',
        "borderColor": 'rgb(54, 162, 235)',
        "backgroundColor": 'rgba(54, 162, 235, .5)',
        "data": office_camera_frames,
      },
    ],
  },
  "options": {
    "responsive": "true",
    "title": {
      "display": "true",
      "text": 'Chart.js Line Chart - Stacked Area',
    },
    "tooltips": {
      "mode": 'index',
    },
    "hover": {
      "mode": 'index',
    },
    "scales": {
      "xAxes": [
        {
          "scaleLabel": {
            "display": "true",
            "labelString": 'Month',
          },
        },
      ],
      "yAxes": [
        {
          "stacked": "true",
          "scaleLabel": {
            "display": "true",
            "labelString": 'Value',
          },
        },
      ],
    },
  },
}

office_6_chart = "https://quickchart.io/chart?c={}".format(g)

h = {
  "type": 'bar',
  "data": {
    "labels": hourly,
    "datasets": [
      {
        "label": 'Office Camera',
        "backgroundColor": 'rgb(255, 99, 132)',
        "stack": 'Stack 0',
        "data": office_camera_frames,
      },
      {
        "label": 'Outside 1 Camera',
        "backgroundColor": 'rgb(54, 162, 235)',
        "stack": 'Stack 0',
        "data": outside_camera_1_frames,
      },
    ],
  },
  "options": {
    "title": {
      "display": "true",
      "text": 'Chart.js Bar Chart - Stacked',
    },
    "tooltips": {
      "mode": 'index',
      "intersect": "false",
    },
    "responsive": "true",
    "scales": {
      "xAxes": [
        {
          "stacked": "true",
        },
      ],
      "yAxes": [
        {
          "stacked": "true",
        },
      ],
    },
  },
}

office_7_chart = "https://quickchart.io/chart?c={}".format(h)

k = {
  "type": 'bar',
  "data": {
    "labels": hourly,
    "datasets": [{
      "label": 'Gradient example',
      "data": office_camera_frames,
      "backgroundColor": 'getGradientFillHelper("vertical", ["#36a2eb", "#a336eb", "#eb3639"])'
    }]
  }
}

office_8_chart = "https://quickchart.io/chart?c={}".format(k)
print(office_2_chart)