import numpy as np
import pandas as pd
import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

app = Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('Carbon Intensity Indicator (CII) Calculator'),
            html.P('The IMO (International Maritime Organization) Carbon Intensity Indicator (CII) is a metric used to measure and control the carbon intensity of ships. It is part of the IMO\'s efforts to reduce greenhouse gas emissions from international shipping and improve the energy efficiency of vessels.')
        ])
    ]),
    dbc.Row([
        dbc.Col([html.H2('What is it?'),
                 html.P('The CII measures the carbon dioxide (CO2) emissions per transport work of a ship. Transport work is typically quantified as the amount of cargo (in tons) carried over a distance (in nautical miles). The CII is calculated annually for each ship, providing a measure of its carbon efficiency over a specified period.')
        ])
    ]),
    dbc.Row([
        dbc.Col([html.H2('CII Rating Systm'),
                 html.P('Ships are assigned a CII rating based on their calculated carbon intensity. The ratings range from A to E:'),
                 html.Ul([html.Li(letter) for letter in ['A (best performance)','B','C','D','E (worst performance)']]),
                 dcc.Markdown('''*Ships with a rating of D for three consecutive years or an E rating for one year must develop and implement a corrective action plan to improve their carbon intensity.*''')
        ])
    ]),
    dbc.Row([
        dbc.Col([html.H2('Benefits and Goals'),
                 html.P('The main goals of the CII are to:'),
                 dcc.Markdown('''
                              - Encourage shipowners and operators to adopt more energy-efficient technologies and practices. 
                              - Reduce the overall carbon footprint of the maritime industry.
                              - Contribute to the global effort to mitigate climate change by reducing greenhouse gas emissions from international shipping.
                              '''),
                html.P('The CII is a crucial part of the IMO\'s strategy to achieve a 40 percent reduction in carbon intensity by 2030 and a 70 percent reduction by 2050 compared to 2008 levels.')
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Row([]),
            dbc.Row([]),
            dbc.Row([])
        ]),
        dbc.Col()
    ])
])

if __name__ == '__main__':
    app.run(debug = True)