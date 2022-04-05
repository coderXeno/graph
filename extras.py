x =   {
  "type": "line",
  "data": {
    "labels": [
      new Date("2022-03-17T16:12:35.27Z"),
      new Date("2022-03-17T16:12:30:04Z"),
      new Date("2022-03-17T16:12:25:30Z"),
      new Date("2022-03-17T16:12:20:28Z"),
      new Date("2022-03-17T16:12:15:28Z"),
      new Date("2022-03-17T16:12:10:27Z"),
    ],
    "datasets": [
      {
        "label": "My First dataset",
        "backgroundColor": "rgba(255, 99, 132, 0.5)",
        "borderColor": "rgb(255, 99, 132)",
        "fill": false,
        "data": [
          1,1,1,1,1,1
        ]
      },
      {
        "label": "My Second dataset",
        "backgroundColor": "rgba(54, 162, 235, 0.5)",
        "borderColor": "rgb(54, 162, 235)",
        "fill": false,
        "data": [
          0,0,0,0,0,0
        ]
      },
    ]
  },
  "options": {
    "title": {
      "text": "Chart.js Time Scale"
    },
    "scales": {
      "xAxes": [{
        "type": "time",
        "time": {
          "parser": "MM/DD/YYYY HH:mm",
        },
        "scaleLabel": {
          "display": true,
          "labelString": "Date"
        }
      }],
      "yAxes": [{
        "scaleLabel": {
          "display": true,
          "labelString": "value"
        }
      }]
    }
  }
}

y = {
  type: 'progressBar',
  data: {
    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
    datasets: [{
      label: "Dataset 1",
      data: [100,100,100,100,100,0,100],
      backgroundColor: [
        "#32a852",
        "#3295a8",
        "#cc1ad9",
        "#de238a",
        "#ded523",
        "#ded523",
        "#571994",
      ]
    }]
  },
  options: {
    plugins: {
      datalabels:{ display: true },
      responsive: true,
      progressbarlabel: {
        labels: [
          {
            "text": "\nCPU LOAD",
            "color": "#fc03f4",
            "font": {
              "size": "25"
            },
          },{
            "text": "\nUSED SPACE",
            "color": "#fc036b",
            "font": {
              "size": "25"
            },
          },{
            "text": "\nUSED SWAP SPACE",
            "color": "#5d42f5",
            "font": {
              "size": "25"
            },
          },{
            "text": "\nRAM",
            "color": "#f0fc03",
            "font": {
              "size": "25"
            },
          }
        ]
      }
    }
  }
}

z = {
  "type": 'bar',
  "data": {
    "labels": ['2022-03-28,16:20:58', '2022-03-28,16:21:36', '2022-03-28,16:22:14', '2022-03-28,16:22:58', '2022-03-28,16:23:41', '2022-03-28,16:24:33', '2022-03-28,16:25:09', '2022-03-28,16:25:52', '2022-03-28,16:26:36', '2022-03-28,16:27:19', '2022-03-28,16:28:03', '2022-03-28,16:28:48', '2022-03-28,16:29:30', '2022-03-28,16:30:22', '2022-03-28,16:30:58', '2022-03-28,16:31:40', '2022-03-28,16:32:24', '2022-03-28,16:33:10', '2022-03-28,16:33:51', '2022-03-28,16:34:38', '2022-03-28,16:35:18', '2022-03-28,16:36:02', '2022-03-28,16:36:45', '2022-03-28,16:37:29', '2022-03-28,16:38:12', '2022-03-28,16:38:56', '2022-03-28,16:39:40', '2022-03-28,16:40:44', '2022-03-28,16:41:13', '2022-03-28,16:41:50', '2022-03-28,16:42:34', '2022-03-28,16:43:17', '2022-03-28,16:44:01', '2022-03-28,16:44:50', '2022-03-28,16:45:29'],
    "datasets": [
      {
        "label": 'Dataset 1',
        "backgroundColor": 'rgba(255, 99, 132, 0.5)',
        "borderColor": 'rgb(255, 99, 132)',
        "borderWidth": 1,
        "data": [1.6245, 0.4178, 0.5451, 0.3551, 0.5755, 8.2891, 1.0338, 0.4941, 0.4838, 0.4164, 0.6674, 2.4483, 0.471, 6.0762, 2.0154, 0.3668, 0.4384, 2.9053, 0.5154, 1.5101, 0.5991, 0.4231, 0.505, 0.441, 0.3637, 0.359, 0.4563, 6.7079, 0.3842, 0.3383, 0.4237, 0.4285, 0.4182, 1.0586, 1.1112],
      }
    ],
  },
  "options": {
    "title": {
      "display": "true",
      "text": 'Bar Chart',
    },
    "plugins": {
      "datalabels": {
        "display":false,
        "anchor": 'center',
        "align": 'center',
        "color": '#666',
        "font": {
          "weight": 'normal',
        }
      }
    }
  }
}

a = {'type': 'bar', 'data': {'labels': ['2022-03-28,14:58:02', '2022-03-28,14:58:46', '2022-03-28,14:59:29', '2022-03-28,15:00:13', '2022-03-28,15:00:57', '2022-03-28,15:01:40', '2022-03-28,15:02:24', '2022-03-28,15:03:10', '2022-03-28,15:03:51', '2022-03-28,15:04:35', '2022-03-28,15:05:18', '2022-03-28,15:06:02', '2022-03-28,15:06:45', '2022-03-28,15:07:30', '2022-03-28,15:08:15', '2022-03-28,15:08:56', '2022-03-28,15:09:39', '2022-03-28,15:10:23', '2022-03-28,15:11:10', '2022-03-28,15:11:50', '2022-03-28,15:12:33', '2022-03-28,15:13:17', '2022-03-28,15:14:01', '2022-03-28,15:14:45', '2022-03-28,15:15:28', '2022-03-28,15:16:13', '2022-03-28,15:16:55', '2022-03-28,15:17:38', '2022-03-28,15:18:22', '2022-03-28,15:19:06', '2022-03-28,15:19:49', '2022-03-28,15:20:33', '2022-03-28,15:21:23', '2022-03-28,15:22:04', '2022-03-28,15:22:45', '2022-03-28,15:23:27', '2022-03-28,15:24:10', '2022-03-28,15:24:54', '2022-03-28,15:25:37', '2022-03-28,15:26:21', '2022-03-28,15:27:05', '2022-03-28,15:27:48', '2022-03-28,15:28:32', '2022-03-28,15:29:15', '2022-03-28,15:29:59', '2022-03-28,15:30:42', '2022-03-28,15:31:26', '2022-03-28,15:32:10', '2022-03-28,15:32:53', '2022-03-28,15:33:43', '2022-03-28,15:34:21', '2022-03-28,15:35:05', '2022-03-28,15:35:47', '2022-03-28,15:36:31', '2022-03-28,15:37:14', '2022-03-28,15:37:57', '2022-03-28,15:38:41', '2022-03-28,15:39:25', '2022-03-28,15:40:10', '2022-03-28,15:40:52', '2022-03-28,15:41:35', '2022-03-28,15:42:19', '2022-03-28,15:43:08', '2022-03-28,15:43:46', '2022-03-28,15:44:30', '2022-03-28,15:45:13', '2022-03-28,15:45:57', '2022-03-28,15:46:40', '2022-03-28,15:47:27', '2022-03-28,15:48:08', '2022-03-28,15:48:51', '2022-03-28,15:49:39', '2022-03-28,15:50:25', '2022-03-28,15:51:06', '2022-03-28,15:51:45', '2022-03-28,15:52:29', '2022-03-28,15:53:12', '2022-03-28,15:53:56', '2022-03-28,15:54:40', '2022-03-28,15:55:23', '2022-03-28,15:56:09', '2022-03-28,15:56:50', '2022-03-28,15:57:34', '2022-03-28,15:58:17', '2022-03-28,15:59:00', '2022-03-28,15:59:44', '2022-03-28,16:00:45', '2022-03-28,16:01:13', '2022-03-28,16:01:55', '2022-03-28,16:02:38', '2022-03-28,16:03:22', '2022-03-28,16:04:05', '2022-03-28,16:04:49', '2022-03-28,16:05:32', '2022-03-28,16:06:16', '2022-03-28,16:06:59', '2022-03-28,16:08:04', '2022-03-28,16:08:30', '2022-03-28,16:09:11', '2022-03-28,16:09:54', '2022-03-28,16:10:37', '2022-03-28,16:11:21', '2022-03-28,16:12:05', '2022-03-28,16:12:48', '2022-03-28,16:13:32', '2022-03-28,16:14:15', '2022-03-28,16:14:59', '2022-03-28,16:15:42', '2022-03-28,16:16:26', '2022-03-28,16:17:09', '2022-03-28,16:17:53', '2022-03-28,16:18:36', '2022-03-28,16:19:20', '2022-03-28,16:20:05'], 'datasets': [{'label': 'Dataset 1', 'backgroundColor': 'rgba(255, 99, 132, 0.5)', 'borderColor': 'rgb(255, 99, 132)', 'borderWidth': 1, 'data': [0.538, 0.3874, 0.3927, 0.8625, 1.1191, 0.4182, 0.3963, 2.1034, 0.403, 0.5123, 0.5322, 0.5519, 0.3524, 1.686, 3.3597, 0.4999, 0.4121, 0.3812, 3.9266, 0.4129, 0.3491, 0.4048, 0.4963, 0.8545, 0.373, 1.6278, 0.518, 0.4733, 0.4692, 0.5613, 0.4771, 0.5058, 1.2469, 4.226, 2.0715, 0.4673, 0.4766, 0.5339, 0.3998, 0.4936, 1.1203, 0.3541, 0.5984, 0.4374, 0.4076, 0.341, 0.5078, 0.5209, 0.4513, 6.8378, 0.3942, 2.4927, 0.564, 0.5028, 0.4476, 0.3502, 0.4469, 0.6651, 0.4641, 0.8077, 0.3655, 0.5695, 5.7481, 0.4118, 0.8666, 0.6044, 0.4582, 0.5285, 3.7807, 0.6724, 0.3532, 0.7303, 0.6445, 5.2568, 0.4187, 0.8849, 0.4524, 0.3921, 0.5865, 0.6049, 3.4105, 0.4075, 0.6244, 0.3939, 0.4554, 0.3528, 1.06, 0.9642, 0.4859, 0.4127, 0.4608, 0.4468, 0.7096, 0.4102, 0.5088, 0.4304, 1.6191, 3.7208, 1.0153, 0.4622, 0.5933, 0.3587, 0.5013, 0.4763, 0.5422, 0.3947, 0.5599, 0.4328, 0.6298, 0.6076, 0.4506, 0.4479, 0.3935, 1.8597]}]}, 'options': {'title': {'display': 'true', 'text': 'Bar Chart'}, 'plugins': {'datalabels': {'display': false, 'anchor': 'center', 'align': 'center', 'color': '#666', 'font': {'weight': 'normal'}}}}}