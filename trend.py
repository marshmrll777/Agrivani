{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "7b54a8a7-929d-4080-8ad3-fe33460d21ea",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "line": {
          "color": "#2E7D32",
          "width": 3
         },
         "marker": {
          "size": 8
         },
         "mode": "lines+markers",
         "name": "Wheat",
         "type": "scatter",
         "visible": true,
         "x": [
          "2026-02-06T00:00:00.000000000",
          "2026-02-07T00:00:00.000000000",
          "2026-02-08T00:00:00.000000000"
         ],
         "y": {
          "bdata": "rkfhehQhqkDhehSuR06lQAAAAAAAqKZA",
          "dtype": "f8"
         }
        },
        {
         "line": {
          "color": "#6D4C41",
          "width": 3
         },
         "marker": {
          "size": 8
         },
         "mode": "lines+markers",
         "name": "Green Gram(Moong)(Whole)",
         "type": "scatter",
         "visible": false,
         "x": [
          "2026-02-06T00:00:00.000000000"
         ],
         "y": {
          "bdata": "AAAAAACIw0A=",
          "dtype": "f8"
         }
        },
        {
         "line": {
          "color": "#F9A825",
          "width": 3
         },
         "marker": {
          "size": 8
         },
         "mode": "lines+markers",
         "name": "Lentil(Masur)(Whole)",
         "type": "scatter",
         "visible": false,
         "x": [
          "2026-02-06T00:00:00.000000000"
         ],
         "y": {
          "bdata": "AAAAAABSvEA=",
          "dtype": "f8"
         }
        },
        {
         "line": {
          "color": "#558B2F",
          "width": 3
         },
         "marker": {
          "size": 8
         },
         "mode": "lines+markers",
         "name": "Jowar(Sorghum)",
         "type": "scatter",
         "visible": false,
         "x": [
          "2026-02-07T00:00:00.000000000",
          "2026-02-08T00:00:00.000000000"
         ],
         "y": {
          "bdata": "AAAAAAB4rkAAAAAAAHiuQA==",
          "dtype": "f8"
         }
        }
       ],
       "layout": {
        "annotations": [
         {
          "bgcolor": "rgba(255,255,255,0.95)",
          "bordercolor": "#C62828",
          "borderwidth": 2,
          "font": {
           "color": "#C62828",
           "size": 15
          },
          "showarrow": false,
          "text": "<b>📉 Price Decreasing</b>",
          "x": 0.99,
          "xref": "paper",
          "y": 0.85,
          "yref": "paper"
         }
        ],
        "height": 560,
        "hovermode": "x unified",
        "paper_bgcolor": "#F1F8E9",
        "plot_bgcolor": "#F9FFF7",
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermap": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermap"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "font": {
          "color": "#1B5E20",
          "size": 20
         },
         "text": "Wheat Market Price Trend",
         "x": 0.5,
         "xanchor": "center",
         "y": 0.98,
         "yanchor": "top"
        },
        "updatemenus": [
         {
          "bgcolor": "white",
          "bordercolor": "#4CAF50",
          "borderwidth": 1,
          "buttons": [
           {
            "args": [
             {
              "visible": [
               true,
               false,
               false,
               false
              ]
             },
             {
              "annotations": [
               {
                "bgcolor": "rgba(255,255,255,0.95)",
                "bordercolor": "#C62828",
                "borderwidth": 2,
                "font": {
                 "color": "#C62828",
                 "size": 15
                },
                "showarrow": false,
                "text": "<b>📉 Price Decreasing</b>",
                "x": 0.99,
                "xref": "paper",
                "y": 0.85,
                "yref": "paper"
               }
              ],
              "title": "Wheat Market Price Trend"
             }
            ],
            "label": "Wheat",
            "method": "update"
           },
           {
            "args": [
             {
              "visible": [
               false,
               true,
               false,
               false
              ]
             },
             {
              "annotations": [
               {
                "bgcolor": "rgba(255,255,255,0.95)",
                "bordercolor": "#6D6D6D",
                "borderwidth": 2,
                "font": {
                 "color": "#6D6D6D",
                 "size": 15
                },
                "showarrow": false,
                "text": "<b>➖ Stable</b>",
                "x": 0.99,
                "xref": "paper",
                "y": 0.85,
                "yref": "paper"
               }
              ],
              "title": "Green Gram(Moong)(Whole) Market Price Trend"
             }
            ],
            "label": "Green Gram(Moong)(Whole)",
            "method": "update"
           },
           {
            "args": [
             {
              "visible": [
               false,
               false,
               true,
               false
              ]
             },
             {
              "annotations": [
               {
                "bgcolor": "rgba(255,255,255,0.95)",
                "bordercolor": "#6D6D6D",
                "borderwidth": 2,
                "font": {
                 "color": "#6D6D6D",
                 "size": 15
                },
                "showarrow": false,
                "text": "<b>➖ Stable</b>",
                "x": 0.99,
                "xref": "paper",
                "y": 0.85,
                "yref": "paper"
               }
              ],
              "title": "Lentil(Masur)(Whole) Market Price Trend"
             }
            ],
            "label": "Lentil(Masur)(Whole)",
            "method": "update"
           },
           {
            "args": [
             {
              "visible": [
               false,
               false,
               false,
               true
              ]
             },
             {
              "annotations": [
               {
                "bgcolor": "rgba(255,255,255,0.95)",
                "bordercolor": "#6D6D6D",
                "borderwidth": 2,
                "font": {
                 "color": "#6D6D6D",
                 "size": 15
                },
                "showarrow": false,
                "text": "<b>➖ Price Stable</b>",
                "x": 0.99,
                "xref": "paper",
                "y": 0.85,
                "yref": "paper"
               }
              ],
              "title": "Jowar(Sorghum) Market Price Trend"
             }
            ],
            "label": "Jowar(Sorghum)",
            "method": "update"
           }
          ],
          "direction": "down",
          "x": 0.01,
          "y": 0.9
         }
        ],
        "xaxis": {
         "gridcolor": "#E0E0E0",
         "showgrid": true,
         "tickangle": -30,
         "tickformat": "%d %b %Y",
         "title": {
          "text": "Date"
         }
        },
        "yaxis": {
         "gridcolor": "#E0E0E0",
         "showgrid": true,
         "title": {
          "text": "Price (₹ per Quintal)"
         }
        }
       }
      },
      "image/png": "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"
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import plotly.graph_objects as go\n",
    "from sklearn.linear_model import LinearRegression\n",
    "df = pd.read_csv(\"market_trends_cleaned.csv\")\n",
    "\n",
    "# Convert date\n",
    "df['date'] = pd.to_datetime(df['date'])\n",
    "df['commodity'] = df['commodity'].str.strip()\n",
    "\n",
    "df = df.sort_values('date')\n",
    "\n",
    "# -----------------------------\n",
    "# 1. LOAD DATA\n",
    "\n",
    "# --------------------------------------------------\n",
    "# 1. LOAD YOUR DATASET\n",
    "# --------------------------------------------------\n",
    "data = {\n",
    "    \"commodity_group\": [\"Cereals\",\"Cereals\",\"Cereals\",\"Cereals\",\"Cereals\",\"Pulses\",\"Pulses\"],\n",
    "    \"commodity\": [\n",
    "        \"Jowar(Sorghum)\", \"Wheat\", \"Jowar(Sorghum)\",\n",
    "        \"Wheat\", \"Wheat\",\n",
    "        \"Green Gram(Moong)(Whole)\", \"Lentil(Masur)(Whole)\"\n",
    "    ],\n",
    "    \"date\": [\n",
    "        \"2026-02-08\",\"2026-02-08\",\"2026-02-07\",\n",
    "        \"2026-02-07\",\"2026-02-06\",\n",
    "        \"2026-02-06\",\"2026-02-06\"\n",
    "    ],\n",
    "    \"price\": [3900, 2900, 3900, 2727.14, 3344.54, 10000, 7250]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "df[\"date\"] = pd.to_datetime(df[\"date\"])\n",
    "df = df.sort_values(\"date\")\n",
    "\n",
    "commodities = df[\"commodity\"].unique().tolist()\n",
    "\n",
    "# --------------------------------------------------\n",
    "# 2. TREND DETECTION FUNCTION\n",
    "# --------------------------------------------------\n",
    "def detect_trend(series):\n",
    "    if len(series) < 2:\n",
    "        return \"➖ Stable\", \"#6D6D6D\"\n",
    "\n",
    "    X = np.arange(len(series)).reshape(-1, 1)\n",
    "    y = series.values.reshape(-1, 1)\n",
    "\n",
    "    model = LinearRegression()\n",
    "    model.fit(X, y)\n",
    "    slope = model.coef_[0][0]\n",
    "\n",
    "    epsilon = 0.01  # tolerance for stability\n",
    "\n",
    "    if slope > epsilon:\n",
    "        return \"📈 Price Increasing\", \"#2E7D32\"   # green\n",
    "    elif slope < -epsilon:\n",
    "        return \"📉 Price Decreasing\", \"#C62828\"   # red\n",
    "    else:\n",
    "        return \"➖ Price Stable\", \"#6D6D6D\"        # grey\n",
    "\n",
    "# --------------------------------------------------\n",
    "# 3. CREATE FIGURE\n",
    "# --------------------------------------------------\n",
    "fig = go.Figure()\n",
    "trend_info = []\n",
    "\n",
    "agri_colors = [\"#2E7D32\", \"#6D4C41\", \"#F9A825\", \"#558B2F\"]\n",
    "\n",
    "# --------------------------------------------------\n",
    "# 4. ADD ONE TRACE PER COMMODITY\n",
    "# --------------------------------------------------\n",
    "for i, commodity in enumerate(commodities):\n",
    "    df_c = df[df[\"commodity\"] == commodity]\n",
    "    trend_text, trend_color = detect_trend(df_c[\"price\"])\n",
    "    trend_info.append((trend_text, trend_color))\n",
    "\n",
    "    fig.add_trace(go.Scatter(\n",
    "        x=df_c[\"date\"],\n",
    "        y=df_c[\"price\"],\n",
    "        mode=\"lines+markers\",\n",
    "        name=commodity,\n",
    "        visible=True if i == 0 else False,\n",
    "        line=dict(width=3, color=agri_colors[i % len(agri_colors)]),\n",
    "        marker=dict(size=8)\n",
    "    ))\n",
    "\n",
    "# --------------------------------------------------\n",
    "# 5. DROPDOWN BUTTONS (NO REPEATS, NO BUGS)\n",
    "# --------------------------------------------------\n",
    "buttons = []\n",
    "\n",
    "for i, commodity in enumerate(commodities):\n",
    "    visible = [False] * len(commodities)\n",
    "    visible[i] = True\n",
    "\n",
    "    buttons.append(\n",
    "        dict(\n",
    "            label=commodity,\n",
    "            method=\"update\",\n",
    "            args=[\n",
    "                {\"visible\": visible},\n",
    "                {\n",
    "                    \"title\": f\"{commodity} Market Price Trend\",\n",
    "                    \"annotations\": [\n",
    "                        dict(\n",
    "                            text=f\"<b>{trend_info[i][0]}</b>\",\n",
    "                            xref=\"paper\",\n",
    "                            yref=\"paper\",\n",
    "                            x=0.99,\n",
    "                            y=0.85,\n",
    "                            showarrow=False,\n",
    "                            font=dict(size=15, color=trend_info[i][1]),\n",
    "                            bgcolor=\"rgba(255,255,255,0.95)\",\n",
    "                            bordercolor=trend_info[i][1],\n",
    "                            borderwidth=2\n",
    "                        )\n",
    "                    ]\n",
    "                }\n",
    "            ]\n",
    "        )\n",
    "    )\n",
    "\n",
    "# --------------------------------------------------\n",
    "# 6. LAYOUT (NO OVERLAP, FARMER FRIENDLY)\n",
    "# --------------------------------------------------\n",
    "fig.update_layout(\n",
    "    title=dict(\n",
    "        text=f\"{commodities[0]} Market Price Trend\",\n",
    "        x=0.5,\n",
    "        y=0.98,\n",
    "        xanchor=\"center\",\n",
    "        yanchor=\"top\",\n",
    "        font=dict(size=20, color=\"#1B5E20\")\n",
    "    ),\n",
    "\n",
    "    plot_bgcolor=\"#F9FFF7\",\n",
    "    paper_bgcolor=\"#F1F8E9\",\n",
    "\n",
    "    updatemenus=[dict(\n",
    "        buttons=buttons,\n",
    "        direction=\"down\",\n",
    "        x=0.01,\n",
    "        y=0.90,\n",
    "        bgcolor=\"white\",\n",
    "        bordercolor=\"#4CAF50\",\n",
    "        borderwidth=1\n",
    "    )],\n",
    "\n",
    "    xaxis=dict(\n",
    "        title=\"Date\",\n",
    "        tickangle=-30,\n",
    "        tickformat=\"%d %b %Y\",\n",
    "        showgrid=True,\n",
    "        gridcolor=\"#E0E0E0\"\n",
    "    ),\n",
    "\n",
    "    yaxis=dict(\n",
    "        title=\"Price (₹ per Quintal)\",\n",
    "        showgrid=True,\n",
    "        gridcolor=\"#E0E0E0\"\n",
    "    ),\n",
    "\n",
    "    hovermode=\"x unified\",\n",
    "    height=560,\n",
    "\n",
    "    annotations=[\n",
    "        dict(\n",
    "            text=f\"<b>{trend_info[0][0]}</b>\",\n",
    "            xref=\"paper\",\n",
    "            yref=\"paper\",\n",
    "            x=0.99,\n",
    "            y=0.85,\n",
    "            showarrow=False,\n",
    "            font=dict(size=15, color=trend_info[0][1]),\n",
    "            bgcolor=\"rgba(255,255,255,0.95)\",\n",
    "            bordercolor=trend_info[0][1],\n",
    "            borderwidth=2\n",
    "        )\n",
    "    ]\n",
    ")\n",
    "\n",
    "# --------------------------------------------------\n",
    "# 7. SHOW GRAPH\n",
    "# --------------------------------------------------\n",
    "fig.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "024230c7-d0be-47ea-bcb3-481a0fe31b6e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
