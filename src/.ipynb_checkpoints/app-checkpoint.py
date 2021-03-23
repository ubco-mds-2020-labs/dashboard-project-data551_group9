import dash
import numpy as np
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import altair as alt
from vega_datasets import data

alt.data_transformers.disable_max_rows()
hr = pd.read_csv("../data/raw/analysis.csv")
hr1 = hr[["education_level", "training_hours", "gender"]]
hr1 = hr1.dropna()
bins = pd.Series(np.linspace(hr1.training_hours.min()-1, hr1.training_hours.max(), 11)).tolist()
label = pd.Series(np.arange(1,11,1))
hr1["train_level"] = pd.cut(hr.training_hours, bins = bins, labels = label.tolist()).astype(str)
hr1["education_level"].replace("Graduate", "Bachelor", inplace = True)

hr2 = hr[["relevent_experience", "company_size", "training_hours"]].fillna("no experience")
hr2 = hr2.replace("10/49", "10-49")

hr3 = hr[["city_development_index", "last_new_job", "target"]]
hr3 = hr3.dropna()
hr3["city_development_index"] = hr3.city_development_index.round(2)

hr4 = hr[["education_level", "major_discipline", "experience", "target"]].fillna("None")
hr4.experience.replace("<1",0, inplace=True)
hr4.experience.replace(">20",21, inplace=True)
bins_4 = [-1, 7, 14, 21, 28]
lab_4 = ["Limit Experienced(between (0,7] years)", "Medium Experienced(between (7,14] years)", "Experienced(between (14,21] years)", "Missing information"]
hr4.experience.replace("None",23, inplace = True)
sli = hr4.experience.astype(int)
hr4["experience_level"] = pd.cut(sli, bins = bins_4, labels = lab_4)
hr4["education_level"].replace("Graduate", "Bachelor", inplace = True)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

colors = {
    'background': '#dedede',
    'text': '#7FDBFF'
}

server = app.server

app.layout = dbc.Container([
    html.Br(),
    dcc.Tabs(id='tabs', value='tab-1', children=[
        dbc.Tab([
            html.Br(),
            html.Br(),
            dbc.Row([
                    html.H1("HR Analytics on Training")], 
                    justify="center", align="center"),
            html.Br(),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    html.Label([
                        dcc.Markdown('''
                            **PLEASE SELECT EDUCATION LEVELS:**
                        '''),
                        dcc.Dropdown(options = [
                            {'label': col, 'value': col} for col in hr1.education_level.unique()
                        ], value = "Bachelor", placeholder = "Please enter", clearable = False,
                        style={'width': '400px'}, id = "dropdown1")]),
                    html.Br(),
                    html.Label([
                        html.Br(),
                        dcc.Dropdown(options = [
                            {'label': col, 'value': col} for col in hr1.education_level.unique()
                        ], value = "Masters", placeholder = "Please enter", clearable = False, 
                        style={'width': '400px'}, id = "dropdown2")])
                    ], md = 5),
                dbc.Col([
                    html.Iframe(
                        id='chart1',
                        style={'border-width': '0', 'width': '125%', 'height': '500px'}),
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    html.Label([
                        dcc.Markdown('''
                            **PLEASE SELECT PREVIOUS COMPANY SIZE:**
                        '''),
                        dcc.RadioItems(id = "radio_items", options = [
                            {'label': ' ' + i, 'value': i} for i in [hr2.company_size.unique()[0], hr2.company_size.unique()[2], hr2.company_size.unique()[6], hr2.company_size.unique()[1], hr2.company_size.unique()[7], hr2.company_size.unique()[8], hr2.company_size.unique()[5], hr2.company_size.unique()[4], hr2.company_size.unique()[3]]
                        ], value = "50-99", labelStyle={'display': 'block'})])
                ], md = 5),
                dbc.Col([
                    html.Iframe(
                    id='chart2',
                    style={'border-width': '0', 'width': '150%', 'height': '700px'}),
                ])
            ])
        ], label = "HR PERSPECTIVE"),
        dbc.Tab([
            html.Br(),
            html.Br(),
            dbc.Row([
                    html.H1("Advertising Analytics on Job Change")], 
                    justify="center", align="center"),
            html.Br(),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    html.Label([
                        dcc.Markdown('''
                            **PLEASE SELECT CITY DEVELOPMENT LEVEL RANGE:**
                        '''),
                        dbc.Card([
                            html.Br(),
                            dcc.RangeSlider(id = "rangeslider1", 
                                min = hr3.city_development_index.min(),
                                max = hr3.city_development_index.max()+0.01,
                                step = 0.05,
                                value = [hr3.city_development_index.min(), hr3.city_development_index.min()+0.25])
                            ], color = "#ffd699", style={'width': '400px', 'height': '38px', 'justify-content': 'center'})
                    ]),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Label([
                        dcc.Markdown('''
                            **PLEASE SELECT LAST JOB SERVING Year:**
                        '''),
                        dcc.Dropdown(options = [
                            {'label': col, 'value': col} for col in [hr3.last_new_job.unique()[2], hr3.last_new_job.unique()[0], hr3.last_new_job.unique()[5], hr3.last_new_job.unique()[4], hr3.last_new_job.unique()[3], hr3.last_new_job.unique()[1]]
                        ], value = "never", placeholder = "Please enter", clearable = False, 
                        style={'width': '400px'}, id = "dropdown4")]),
                    html.Br(),
                    html.Br(),
                    html.Label([
                        dcc.Dropdown(options = [
                            {'label': col, 'value': col} for col in [hr3.last_new_job.unique()[2], hr3.last_new_job.unique()[0], hr3.last_new_job.unique()[5], hr3.last_new_job.unique()[4], hr3.last_new_job.unique()[3], hr3.last_new_job.unique()[1]]
                        ], value = "1", placeholder = "Please enter", clearable = False, 
                        style={'width': '400px'}, id = "dropdown5")]),
                ], md = 5),
                dbc.Col([
                    html.Iframe(
                    id='chart3',
                    style={'border-width': '0', 'width': '150%', 'height': '500px'}),
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    html.Label([
                        dcc.Markdown('''
                            **PLEASE SELECT EXPERIENCE LEVEL:**
                        '''),
                        dcc.Dropdown(options = [
                            {"label": i, "value": i} for i in hr4.experience_level.unique()
                        ], value = "Missing information", placeholder = "Please enter", clearable = False,
                        style={'width': '400px'}, id = "dropdown3")
                    ])
                ], md = 5),
                dbc.Col([
                    html.Iframe(id='chart4',
                    style={'border-width': '0', 'width': '150%', 'height': '600px'})
                ])
            ])
        ], label = "ADVERTISING PERSPECTIVE"),
    ], colors={
        "border": "grey",
        "primary": "gery",
        "background": "#ccf2ff",
    })
])

@app.callback(
    Output("chart1", "srcDoc"),
    Input("dropdown1", "value"),
    Input("dropdown2", "value"))

def plot_chart1(edu, edu2):
    click = alt.selection_multi(fields=["education_level"])
    chart = alt.Chart(hr1[(hr1.education_level == edu) | (hr1.education_level == edu2)]).mark_bar().encode(
        alt.X('count()', title = "Total Count"),
        alt.Y("train_level", title = "Train Level", sort = label.iloc[::-1].astype(str).tolist()),
        alt.Color("education_level"),
        opacity=alt.condition(click, alt.value(0.9), alt.value(0.2))
    ).properties(
    width = 450,
    height = 400)

    chart = alt.layer(chart).configure_axis(
        labelFontSize=16, titleFontSize=20).configure_legend(labelFontSize=16, titleFontSize=16) 
    chart = chart.add_selection(click)
    return chart.to_html()

@app.callback(
    Output("chart2", "srcDoc"),
    Input("radio_items", "value"))

def plot_chart2(size):
    brush = alt.selection_interval(encodings=['x'])
    chart = alt.Chart(hr2[hr2.company_size == size]).transform_density(
        'training_hours', 
        groupby=['company_size'],
        as_=['training_hours', 'density'],
    ).mark_area(
        opacity=0.5
    ).encode(
        alt.X('training_hours', title = "Training Hours", axis=alt.Axis(format='~s', labelFontSize=16, titleFontSize=20)),
        alt.Y('density:Q', title = "Hours Density", axis=alt.Axis(labelFontSize=16, titleFontSize=20)),
        alt.Color('company_size:N', legend=alt.Legend(title='Company Size', labelFontSize=16, titleFontSize=16))
    ).properties(
                width = 450,
                height = 400
    )
    full = chart.properties(height=80).add_selection(brush)
    detail = chart.encode(alt.X('training_hours', title = "Training Hours", axis=alt.Axis(labelFontSize=16, titleFontSize=20), scale=alt.Scale(domain=brush)))
    
    chart = detail & full
    return chart.to_html()

@app.callback(
    Output("chart3", "srcDoc"),
    Input("rangeslider1", "value"),
    Input("dropdown4", "value"),
    Input("dropdown5", "value"))

def plot_chart3(range_val, last_job, last_job2):
    click = alt.selection_multi(fields=["last_new_job"])
    chart = alt.Chart(hr3[(hr3.city_development_index > range_val[0]) & (hr3.city_development_index < range_val[1]) & ((hr3.last_new_job == last_job) | (hr3.last_new_job == last_job2))]).mark_bar(
                opacity=0.8).encode(
                alt.X("mean(target)", title = "Change Percentage"),
                alt.Y("city_development_index:O", scale=alt.Scale(zero=False), title = "City Development Level"),
                alt.Color("last_new_job", legend=alt.Legend(title = "Last Job Serving Year")),
                opacity=alt.condition(click, alt.value(0.9), alt.value(0.2))).properties(
                width = 450,
                height = 400
            )
    chart = alt.layer(chart).configure_axis(
        labelFontSize=16, titleFontSize=20).configure_legend(labelFontSize=16, titleFontSize=16) 
    chart = chart.add_selection(click)
    return chart.to_html()

@app.callback(
    Output("chart4", "srcDoc"),
    Input("dropdown3", "value")
)

def plot_chart4(level):
    chart = alt.Chart(hr4[hr4.experience_level == level]).mark_point().encode(
                alt.X("education_level", title = "Educaiton Level"),
                alt.Y("major_discipline", title = "Major Discipline"),
                alt.Size("mean(target)", legend = alt.Legend(title = "Change Job Ratio")),
                alt.Color("mean(target)"),
                fill = "mean(target)",
            ).properties(
                width = 400,
                height = 400
            )
    chart = alt.layer(chart).configure_axis(
        labelFontSize=16, titleFontSize=20).configure_legend(labelFontSize=16, titleFontSize=16) 
    return chart.to_html()

if __name__ == "__main__":
    app.run_server(debug = True)