#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install dash
#!pip install pandas


# In[2]:


# importing necessary libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px


# In[3]:


# df = pd.read_csv("/Users/kennethlau/Desktop/IAT_project/IAT_2/IAT2/IAT/Datasets/nutrition/all_nutrition.csv")
# income = pd.read_csv("/Users/kennethlau/Desktop/IAT_project/IAT_2/IAT2/IAT/Datasets/map/income_per_state.csv")
# obesity = pd.read_csv("/Users/kennethlau/Desktop/IAT_project/IAT_2/IAT2/IAT/Datasets/map/obesity_per_state.csv")
# population = pd.read_csv("/Users/kennethlau/Desktop/IAT_project/IAT_2/IAT2/IAT/Datasets/map/population_per_state.csv")
# number_bk = pd.read_csv("/Users/kennethlau/Desktop/IAT_project/IAT_2/IAT2/IAT/Datasets/locations/burgerking_locations.csv")
# number_chick = pd.read_csv("/Users/kennethlau/Desktop/IAT_project/IAT_2/IAT2/IAT/Datasets/locations/chick-fil-a_locations.csv")
# number_mcdonalds = pd.read_csv("/Users/kennethlau/Desktop/IAT_project/IAT_2/IAT2/IAT/Datasets/locations/mcdonalds_locations.csv")
# number_starbucks = pd.read_csv("/Users/kennethlau/Desktop/IAT_project/IAT_2/IAT2/IAT/Datasets/locations/starbucks_locations.csv")
# number_subway = pd.read_csv("/Users/kennethlau/Desktop/IAT_project/IAT_2/IAT2/IAT/Datasets/locations/subway_locations.csv")
# foodo = pd.read_csv("/Users/kennethlau/Desktop/IAT_project/IAT_2/IAT2/IAT/Datasets/nutrition/all_nutrition.csv")
# drinko = pd.read_csv("/Users/kennethlau/Desktop/IAT_project/IAT_2/IAT2/IAT/Datasets/nutrition/all_nutrition.csv")
# df_ind = pd.read_csv("/Users/kennethlau/Desktop/IAT_project/IAT_2/IAT2/IAT/Datasets/map/state_indicators.csv")

# df = pd.read_csv("/Users/srijeevsarkar/Desktop/IAT/Datasets/nutrition/all_nutrition.csv")
# income = pd.read_csv("/Users/srijeevsarkar/Desktop/IAT/Datasets/map/income_per_state.csv")
# obesity = pd.read_csv("/Users/srijeevsarkar/Desktop/IAT/Datasets/map/obesity_per_state.csv")
# population = pd.read_csv("/Users/srijeevsarkar/Desktop/IAT/Datasets/map/population_per_state.csv")
# number_bk = pd.read_csv("/Users/srijeevsarkar/Desktop/IAT/Datasets/locations/burgerking_locations.csv")
# number_chick = pd.read_csv("/Users/srijeevsarkar/Desktop/IAT/Datasets/locations/chick-fil-a_locations.csv")
# number_mcdonalds = pd.read_csv("/Users/srijeevsarkar/Desktop/IAT/Datasets/locations/mcdonalds_locations.csv")
# number_starbucks = pd.read_csv("/Users/srijeevsarkar/Desktop/IAT/Datasets/locations/starbucks_locations.csv")
# number_subway = pd.read_csv("/Users/srijeevsarkar/Desktop/IAT/Datasets/locations/subway_locations.csv")
# foodo = pd.read_csv("/Users/srijeevsarkar/Desktop/IAT/Datasets/nutrition/all_nutrition.csv")
# drinko = pd.read_csv("/Users/srijeevsarkar/Desktop/IAT/Datasets/nutrition/all_nutrition.csv")
# df_ind = pd.read_csv("/Users/srijeevsarkar/Desktop/IAT/Datasets/map/state_indicators.csv")

df = pd.read_csv("https://raw.githubusercontent.com/srijeev-ds/IAT/main/Datasets/nutrition/all_nutrition.csv")
income = pd.read_csv("https://raw.githubusercontent.com/srijeev-ds/IAT/main/Datasets/map/income_per_state.csv")
obesity = pd.read_csv("https://raw.githubusercontent.com/srijeev-ds/IAT/main/Datasets/map/obesity_per_state.csv")
population = pd.read_csv("https://raw.githubusercontent.com/srijeev-ds/IAT/main/Datasets/map/population_per_state.csv")
number_chick = pd.read_csv("https://raw.githubusercontent.com/srijeev-ds/IAT/main/Datasets/locations/chick-fil-a_locations.csv")
number_mcdonalds = pd.read_csv("https://raw.githubusercontent.com/srijeev-ds/IAT/main/Datasets/locations/mcdonalds_locations.csv")
number_starbucks = pd.read_csv("https://raw.githubusercontent.com/srijeev-ds/IAT/main/Datasets/locations/starbucks_locations.csv")
number_subway = pd.read_csv("https://raw.githubusercontent.com/srijeev-ds/IAT/main/Datasets/locations/subway_locations.csv")
foodo = pd.read_csv("https://raw.githubusercontent.com/srijeev-ds/IAT/main/Datasets/nutrition/all_nutrition.csv")
drinko = pd.read_csv("https://raw.githubusercontent.com/srijeev-ds/IAT/main/Datasets/nutrition/all_nutrition.csv")
df_ind = pd.read_csv("https://raw.githubusercontent.com/srijeev-ds/IAT/main/Datasets/map/state_indicators.csv")
number_bk = pd.read_csv("https://raw.githubusercontent.com/srijeev-ds/IAT/main/Datasets/locations/burgerking_locations.csv")



available_indicators = df_ind['Indicator Name'].unique()
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
path = ["Restaurant", "Category", "Items"]
# merging datasets
xf = pd.merge(income, obesity, on=['State'])
master = pd.merge(xf, population, on=['State'])
rest1 = pd.merge(number_bk,number_chick, on=['State'])
rest2 = pd.merge(rest1,number_mcdonalds, on=['State'])
rest3 = pd.merge(rest2,number_starbucks, on=['State'])
rest4 = pd.merge(rest3,number_subway, on=['State'])
rest = rest4

# dictionary to add state codes to the dataframes
master.rename(columns={'Average Income (in K)': 'Income', 'Percent of obesities': 'Obesity', 'Population (July)': 'Population'}, inplace=True)
state_2 = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

state_2 = {state: abbrev for abbrev, state in state_2.items()}

df_new = pd.DataFrame(list(state_2.items()),columns = ['State Code','State'])

final = pd.merge(master,df_new,on=['State'])

rest = pd.merge(rest,df_new,on=['State'])

is_sandwich =  foodo['Category']=="Sandwich"
sando = foodo[is_sandwich]
is_drink =  drinko['Category']=="Drink"
drink = drinko[is_drink]


# In[4]:


# App layout 
app.layout = html.Div([

    html.H1("Fast Food Analysis Notebook", style={'text-align': 'center'}),
    html.Br(),
    html.H4("Explore the relationship between fast-food prices and nutrition/Compare items by price/nutrition",style={'text-align': 'center'}),
    #html.H4("Compare menu items by price/nutritional value",style={'text-align': 'center'}),
    #html.H4("Items can also be compared on nutritional value ",style={'text-align': 'center'}),
    #html.H5("How to use: Select options from dropdown for restaurant and metrics. Use hover to select/zoom in on items",style={'text-align': 'center'}),
    
    dcc.Dropdown(id='dpdn2', value=['burgerking', 'mcdonalds', 'starbucks'], multi=True,
                 options=[{'label': x, 'value': x} for x in
                          df.Restaurant.unique()]),
    dcc.Dropdown(id='dpdn3', value= 'Cost (USD)', multi=False,
                 options=[
                     {"label": "Fat", "value": 'Fat (g)'},
                     {"label": "Carbs", "value": 'Carbs (g)'},
                     {"label": "Sugar", "value": 'Sugar (g)'},
                     {"label": "Sodium", "value": 'Sodium (g)'},
                     {"label": "Cost (USD)", "value": 'Cost (USD)'},
                     {"label": "Protein", "value": 'Protein (g)'}],),
    html.Div([
        dcc.Graph(id='pie-graph', figure={}, className='five columns'),
        dcc.Graph(id='my-graph', figure={}, clickData=None, hoverData=None, # I assigned None for tutorial purposes. By defualt, these are None, unless you specify otherwise.
                  config={
                      'staticPlot': False,     # True, False
                      'scrollZoom': True,      # True, False
                      'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
                      'showTips': False,       # True, False
                      'displayModeBar': True,  # True, False, 'hover'
                      'watermark': True,
                      # 'modeBarButtonsToRemove': ['pan2d','select2d'],
                        },
                  className='seven columns'
                  )
    ]),
    
    html.Br(),
    html.H4("Compare sandwiches",style={'text-align': 'center'}),
    #html.H4("The grouped bar charts facilitate nutritional comparisons",style={'text-align': 'center'}),
    #html.H5("How to use: Select values from drop down. You can select specific metrics by clicking on the legend",style={'text-align': 'center'}),
    #html.Br(),
    #html.H2("Compare your favourite sandwiches - nutrition",style={'text-align': 'center'}),
    #html.H3("use options for sandwiches, hover to select/zoom, legend to filter by nutritonal component",style={'text-align': 'center'}),
    
    html.Div([
    html.Div([
        
    html.Div([    
    dcc.Dropdown(id="opt1",
                 options=[{'label': x, 'value': x} for x in sando.Items.unique()],
                 multi=False,
                 value="SW - Spicy Italian Sandwich",
                 style={'width': "115%"}),],className="two columns"),
        
    html.Div([    
    dcc.Dropdown(id='opt2', value="McD - McDouble", multi=False,
                 options=[{'label': x, 'value': x} for x in
                          sando.Items.unique()],
                          style={'width': "115%"}),],className="two columns"),
                          
    html.Div([                      
    dcc.Dropdown(id='opt3', value="McD - Big Mac", multi=False,
                 options=[{'label': x, 'value': x} for x in
                          sando.Items.unique()],
                          style={'width': "115%"}),],className="two columns"),
        
    html.Div([    
    dcc.Dropdown(id='opt4', value="SB - Ham & Swiss Panini", multi=False,
                 options=[{'label': x, 'value': x} for x in
                          sando.Items.unique()],
                          style={'width': "115%"}),],className="two columns"),
        
    html.Div([    
    dcc.Dropdown(id='opt5', value="SB - Chicken Caprese", multi=False,
                 options=[{'label': x, 'value': x} for x in
                          sando.Items.unique()],
                          style={'width': "115%"}),],className="two columns"),
    html.Br(),    
        
    ],className="rows"),
        
    
]),
    html.Br(),
    
    
    html.Div([
        
    html.Br(),
    html.H4("Compare drinks",style={'text-align': 'center'}),
    #html.H3("use options for drinks, hover to select/zoom, legend to filter by nutritonal component",style={'text-align': 'center'}),
    html.Div([
    html.Div([
    dcc.Dropdown(id='dpt1', value="McD - Vanilla Shake", multi=False,
                 options=[{'label': x, 'value': x} for x in
                          drink.Items.unique()]
                  ,style={'width': "115%"},
                ) ], className="two columns"),
        
    html.Div([        
    dcc.Dropdown(id='dpt2', value="McD - Mocha", multi=False,
                 options=[{'label': x, 'value': x} for x in
                          drink.Items.unique()]
                 ,style={'width': "115%"},
                ) ], className="two columns"),
    html.Div([
    dcc.Dropdown(id='dpt3', value="SB - Cinnamon Dolce Crème", multi=False,
                 options=[{'label': x, 'value': x} for x in
                          drink.Items.unique()]
                                 ,style={'width': "115%"},
                ) ], className="two columns"),
    html.Div([
    dcc.Dropdown(id='dpt4', value="SB - London Fog Tea Latte", multi=False,
                 options=[{'label': x, 'value': x} for x in
                          drink.Items.unique()]
                                 ,style={'width': "115%"},
                ) ], className="two columns"),
    html.Div([
    dcc.Dropdown(id='dpt5', value="SB - Skinny Mocha", multi=False,
                 options=[{'label': x, 'value': x} for x in
                          drink.Items.unique()]
                                 ,style={'width': "115%"}, 
                ) ], className="two columns"),
        ], className="row"),
    
    #dcc.Graph(id='drink_map', figure={}),
    
    
]),
    html.Div([
    html.Div([
    dcc.Graph(id='sando_map', figure={}),],className="six columns"),
    html.Div([
    dcc.Graph(id='drink_map', figure={}),],className="six columns"),
    ],className="rows"),
    
    
#     html.Div([dcc.Graph(id="sunburst",style= {'height': 800},figure=px.sunburst(df, path=path, values="Cost (USD)")),])
    
    html.H4("Explore the relationship between income/poverty/population and the number of fast food restaurants",style={'text-align': 'center'}),
    #html.H4("The bar charts account for income/poverty/population and fast food representation",style={'text-align': 'center'}),
    #html.H4("The choropleth map shows the number of restaurants in each state and info on income/poverty/population",style={'text-align': 'center'}),
    #html.H5("How to use: Select values from drop down. You can hover over any element for information",style={'text-align': 'center'}),
    html.Br(),
    
    html.Div([
    html.Div([
          dcc.Dropdown(id="select_category",
                 options=[
                     {"label": "Income per state", "value": 'Income'},
                     {"label": "Obesity per state", "value": 'Obesity'},
                     {"label": "Population per state", "value": 'Population'}],
                 multi=False,
                 value="Income",
                 style={'width': "80%"}
                 )
    ],className="five columns"),
     
    html.Div([
    dcc.Dropdown(id="select_restaurant",
                 options=[
                     {"label": "McDonalds", "value": 'Number of McDonalds'},
                     {"label": "Burger King", "value": 'Number of Buger King'},
                     {"label": "Subway", "value": 'Number of Subway'},
                     {"label": "Starbucks", "value": 'Number of Starbucks'},
                     {"label": "Chick-fil-A", "value": 'Number of Chick-fil-A'}],
                 multi=False,
                 value="Number of McDonalds",
                 style={'width': "80%"}
                 )],className="five columns"),
    ], className="row"),
    
    html.Br(),
    html.Div(id='output_container', children=[]),
    html.Br(),
    html.Div([
    html.Div([
            dcc.Graph(id='plot_map', figure={})
        ], className="six columns"),

    html.Div([
            dcc.Graph(id='plot_map_2', figure={})
        ], className="six columns"),
        ], className="row"),
        dcc.Graph(id='fast_food_map', figure={}, clickData=None, hoverData=None,
              config={
                      'staticPlot': False,     # True, False
                      'scrollZoom': True,      # True, False
                      'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
                      'showTips': False,       # True, False
                      'displayModeBar': True,  # True, False, 'hover'
                      'watermark': True,
                      # 'modeBarButtonsToRemove': ['pan2d','select2d'],
                        },),
    
    html.H4("Explore the relationship between income/poverty/population in each state over the years",style={'text-align': 'center'}),
    #html.H4("The main line chart accounts for a comparison for each state. The subplots show how the selected values changed over time",style={'text-align': 'center'}),
    #html.H5("How to use: Select values from drop down. You can hover over any element/drag the time slider to update all visualizations",style={'text-align': 'center'}),
    html.Br(),
    html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='crossfilter-xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='Income'
            ),
            dcc.RadioItems(
                id='crossfilter-xaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ],
        style={'width': '49%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='crossfilter-yaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='Population'
            ),
            dcc.RadioItems(
                id='crossfilter-yaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'})
    ], style={
        'borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)',
        'padding': '10px 5px'
    }),

    html.Div([
        dcc.Graph(
            id='crossfilter-indicator-scatter',
            hoverData={'points': [{'customdata': 'Texas'}]}
        )
    ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([
        dcc.Graph(id='x-time-series'),
        dcc.Graph(id='y-time-series'),
    ], style={'display': 'inline-block', 'width': '49%'}),

    html.Div(dcc.Slider(
        id='crossfilter-year--slider',
        min=df_ind['Year'].min(),
        max=df_ind['Year'].max(),
        value=df_ind['Year'].max(),
        marks={str(year): str(year) for year in df_ind['Year'].unique()},
        step=None
    ), style={'width': '49%', 'padding': '0px 20px 20px 20px'})
]),
    
    html.Br(),
    html.H4("Summary of menu items - distribution across categories and price",style={'text-align': 'center'}),
    #html.H4("The proportions are based on price",style={'text-align': 'center'}),
    #html.H5("How to use: Click on restaurant to open categories and items. You can hover over the item for price",style={'text-align': 'center'}),
    dcc.Graph(id="sunburst",style= {'height': 800},figure=px.sunburst(df, path=path, values="Cost (USD)")),
    

])


# In[ ]:


@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='dpdn2', component_property='value'),
    Input(component_id='dpdn3', component_property='value')
)
def update_graph(rest_chosen, ten):
    dff = df[df.Restaurant.isin(rest_chosen)]
    mystring2 = b = f'{ten}'
    fig = px.bar(data_frame=dff, x='Items', y=mystring2, color='Restaurant',  color_discrete_sequence=px.colors.qualitative.Antique)
#     print(fig)
    return fig


# Dash version 1.16.0 or higher
@app.callback(
    Output(component_id='pie-graph', component_property='figure'),
    Input(component_id='my-graph', component_property='hoverData'),
    Input(component_id='my-graph', component_property='clickData'),
    Input(component_id='my-graph', component_property='selectedData'),
    Input(component_id='dpdn2', component_property='value')
)


def update_side_graph(hov_data, clk_data, slct_data, rest_chosen):
    if clk_data is None:
        dff2 = df[df.Restaurant.isin(rest_chosen)]
        dff2 = dff2[dff2.Items == 'BK - Bacon Double Cheeseburger']
        test1 = dff2[['Protein (g)','Fat (g)', 'Carbs (g)', 'Sugar (g)', 'Sodium (g)']]
        test2 = test1.values.tolist() 
        test3= test2[0]
        test4 =test1.iloc[0].values.tolist()
        labels = ['Protein (g)','Fat (g)', 'Carbs (g)', 'Sugar (g)', 'Sodium (g)']
#         print(test3)

        colors1 = {'Protein (g)': 'red',
          'Fat (g)': 'pink',
          'Carbs (g)': 'orange',
          'Sugar (g)': 'lightgreen',
          'Sodium (g)': 'darkgreen'}
        fig2 = px.bar(x=labels, y=test4,labels =dict(x="Nutritional Component", y="Value"),color = labels,    color_discrete_map=colors1,
                      title='Nutrition')
        return fig2
    else:
#         print(f'hover data: {hov_data}')
        # print(hov_data['points'][0]['customdata'][0])
        # print(f'click data: {clk_data}')
        # print(f'selected data: {slct_data}')
        dff2 = df[df.Restaurant.isin(rest_chosen)]
        labels = ['Protein (g)','Fat (g)', 'Carbs (g)', 'Sugar (g)', 'Sodium (g)']
        hov_year = clk_data['points'][0]['x']
        dff2 = dff2[dff2.Items == hov_year]
        test1 = dff2[['Protein (g)','Fat (g)', 'Carbs (g)', 'Sugar (g)', 'Sodium (g)']]
        test2 = test1.values.tolist() 
        test3= test2[0]
        test4 =test1.iloc[0].values.tolist()
        #print(test3)
        colors1 = {'Protein (g)': 'red',
          'Fat (g)': 'pink',
          'Carbs (g)': 'orange',
          'Sugar (g)': 'lightgreen',
          'Sodium (g)': 'darkgreen'}
        fig2 = px.bar(x=labels, y=test4,color = labels,labels =dict(x="Nutritional Component", y="Value"),color_discrete_map=colors1, title=f'Nutrition: {hov_year}')
        return fig2

#
@app.callback(
    Output(component_id='fast_food_map', component_property='figure'),
    Input(component_id='select_category', component_property='value'),
    Input(component_id='select_restaurant',component_property='value')
)
def update_graph2(option_slctd,option_slctd_2):
    
    dfff = final.copy()
    figg = px.choropleth(
        data_frame=dfff,
        locationmode='USA-states',
        locations='State Code',
        scope="usa",
        color=option_slctd,
        color_continuous_scale="Viridis",
#         template='plotly_dark'
    )

    dfff2 = rest.copy()

    figg2 = px.scatter_geo(
         data_frame=dfff2,
         locationmode='USA-states',
         scope="usa",
         locations="State Code",
         size=option_slctd_2,
         template='plotly_dark',
                       )
    figg.add_trace(
        figg2.data[0]
    )
    
    return figg

@app.callback(
    Output(component_id='plot_map', component_property='figure'),
    Output(component_id='plot_map_2', component_property='figure'),
    Input(component_id='fast_food_map', component_property='hoverData'),
    Input(component_id='fast_food_map', component_property='clickData'),
    Input(component_id='fast_food_map', component_property='selectedData'),
    Input(component_id='select_category', component_property='value'),
    Input(component_id='select_restaurant',component_property='value')
)

def update_side_graph2(hov_data, clk_data, slct_data, option_slctd,option_slctd_2):
    if hov_data is None:
        dfff = final.copy()
        boom = rest.copy()
        mfig1 = px.bar(dfff,x='State Code',y=option_slctd, height = 450,color="State Code",
                      color_discrete_map={'AL': 'Blue',
    'AK': 'Blue',
    'AZ': 'Blue',
    'AR': 'Blue',
    'CA': 'Blue',
    'CO': 'Blue',
    'CT': 'Blue',
    'DE': 'Blue',
    'DC': 'Blue',
    'FL': 'Blue',
    'GA': 'Blue',
    'HI': 'Blue',
    'ID': 'Blue',
    'IL': 'Blue',
    'IN': 'Blue',
    'IA': 'Blue',
    'KS': 'Blue',
    'KY': 'Blue',
    'LA': 'Blue',
    'ME': 'Blue',
    'MD': 'Blue',
    'MA': 'Blue',
    'MI': 'Blue',
    'MN': 'Blue',
    'MS': 'Blue',
    'MO': 'Blue',
    'MT': 'Blue',
    'NE': 'Blue',
    'NV': 'Blue',
    'NH': 'Blue',
    'NJ': 'Blue',
    'NM': 'Blue',
    'NY': 'Blue',
    'NC': 'Blue',
    'ND': 'Blue',
    'OH': 'Blue',
    'OK': 'Blue',
    'OR': 'Blue',
    'PA': 'Blue',
    'RI': 'Blue',
    'SC': 'Blue',
    'SD': 'Blue',
    'TN': 'Blue',
    'TX': 'Blue',
    'UT': 'Blue',
    'VT': 'Blue',
    'VA': 'Blue',
    'WA': 'Blue',
    'WV': 'Blue',
    'WI': 'Blue',
    'WY': 'Blue'})
        mfig2 = px.bar(boom,x='State Code',y=option_slctd_2, height = 450,color="State Code",
                      color_discrete_map={'AL': 'Blue',
    'AK': 'Blue',
    'AZ': 'Blue',
    'AR': 'Blue',
    'CA': 'Blue',
    'CO': 'Blue',
    'CT': 'Blue',
    'DE': 'Blue',
    'DC': 'Blue',
    'FL': 'Blue',
    'GA': 'Blue',
    'HI': 'Blue',
    'ID': 'Blue',
    'IL': 'Blue',
    'IN': 'Blue',
    'IA': 'Blue',
    'KS': 'Blue',
    'KY': 'Blue',
    'LA': 'Blue',
    'ME': 'Blue',
    'MD': 'Blue',
    'MA': 'Blue',
    'MI': 'Blue',
    'MN': 'Blue',
    'MS': 'Blue',
    'MO': 'Blue',
    'MT': 'Blue',
    'NE': 'Blue',
    'NV': 'Blue',
    'NH': 'Blue',
    'NJ': 'Blue',
    'NM': 'Blue',
    'NY': 'Blue',
    'NC': 'Blue',
    'ND': 'Blue',
    'OH': 'Blue',
    'OK': 'Blue',
    'OR': 'Blue',
    'PA': 'Blue',
    'RI': 'Blue',
    'SC': 'Blue',
    'SD': 'Blue',
    'TN': 'Blue',
    'TX': 'Blue',
    'UT': 'Blue',
    'VT': 'Blue',
    'VA': 'Blue',
    'WA': 'Blue',
    'WV': 'Blue',
    'WI': 'Blue',
    'WY': 'Blue'})
        #ec = dfff.loc[dfff['State Code'] == 'MT']
        #mfig1.add_traces(px.bar(ec,x='State Code', y=option_slctd, color='State'))
        mfig1.update_layout(font=dict(
        family="Times New Roman",
        size=8,
        color="Black"
    ),showlegend=False)
        mfig2.update_layout(font=dict(
        family="Times New Roman",
        size=8,
        color="Black"
    ),showlegend=False)

        return mfig1,mfig2
    else:
        hov_new = hov_data['points']
        list1 = []
        for dic in hov_new:
            for key in dic:
                list1.append(dic[key])
        # list1 is a collection of data from the hover
        #print(list1)
        state_code = list1[-2]
        #dfff2 = final.copy()
        #boom2 = rest.copy()
        #xc = dfff2.loc[dfff2['State Code'] == state_code]
        #xc2 = boom2.loc[boom2['State Code'] == state_code]

        #mfig1 = px.bar(xc,x='State Code',y=option_slctd, height = 450)
        #mfig2 = px.bar(xc2,x='State Code',y=option_slctd_2, height = 450)
        
        ###
        dfff2 = final.copy()
        boom2 = rest.copy()
        mfig1 = px.bar(dfff2,x='State Code',y=option_slctd, height = 450,color="State Code",
                      color_discrete_map={'AL': 'Blue',
    'AK': 'Blue',
    'AZ': 'Blue',
    'AR': 'Blue',
    'CA': 'Blue',
    'CO': 'Blue',
    'CT': 'Blue',
    'DE': 'Blue',
    'DC': 'Blue',
    'FL': 'Blue',
    'GA': 'Blue',
    'HI': 'Blue',
    'ID': 'Blue',
    'IL': 'Blue',
    'IN': 'Blue',
    'IA': 'Blue',
    'KS': 'Blue',
    'KY': 'Blue',
    'LA': 'Blue',
    'ME': 'Blue',
    'MD': 'Blue',
    'MA': 'Blue',
    'MI': 'Blue',
    'MN': 'Blue',
    'MS': 'Blue',
    'MO': 'Blue',
    'MT': 'Blue',
    'NE': 'Blue',
    'NV': 'Blue',
    'NH': 'Blue',
    'NJ': 'Blue',
    'NM': 'Blue',
    'NY': 'Blue',
    'NC': 'Blue',
    'ND': 'Blue',
    'OH': 'Blue',
    'OK': 'Blue',
    'OR': 'Blue',
    'PA': 'Blue',
    'RI': 'Blue',
    'SC': 'Blue',
    'SD': 'Blue',
    'TN': 'Blue',
    'TX': 'Blue',
    'UT': 'Blue',
    'VT': 'Blue',
    'VA': 'Blue',
    'WA': 'Blue',
    'WV': 'Blue',
    'WI': 'Blue',
    'WY': 'Blue',
    state_code: 'Red'
    })
        mfig2 = px.bar(boom2,x='State Code',y=option_slctd_2, height = 450,color="State Code",
                      color_discrete_map={'AL': 'Blue',
    'AK': 'Blue',
    'AZ': 'Blue',
    'AR': 'Blue',
    'CA': 'Blue',
    'CO': 'Blue',
    'CT': 'Blue',
    'DE': 'Blue',
    'DC': 'Blue',
    'FL': 'Blue',
    'GA': 'Blue',
    'HI': 'Blue',
    'ID': 'Blue',
    'IL': 'Blue',
    'IN': 'Blue',
    'IA': 'Blue',
    'KS': 'Blue',
    'KY': 'Blue',
    'LA': 'Blue',
    'ME': 'Blue',
    'MD': 'Blue',
    'MA': 'Blue',
    'MI': 'Blue',
    'MN': 'Blue',
    'MS': 'Blue',
    'MO': 'Blue',
    'MT': 'Blue',
    'NE': 'Blue',
    'NV': 'Blue',
    'NH': 'Blue',
    'NJ': 'Blue',
    'NM': 'Blue',
    'NY': 'Blue',
    'NC': 'Blue',
    'ND': 'Blue',
    'OH': 'Blue',
    'OK': 'Blue',
    'OR': 'Blue',
    'PA': 'Blue',
    'RI': 'Blue',
    'SC': 'Blue',
    'SD': 'Blue',
    'TN': 'Blue',
    'TX': 'Blue',
    'UT': 'Blue',
    'VT': 'Blue',
    'VA': 'Blue',
    'WA': 'Blue',
    'WV': 'Blue',
    'WI': 'Blue',
    'WY': 'Blue',
     state_code: 'Red'})
        mfig1.update_layout(font=dict(
        family="Times New Roman",
        size=8,
        color="Black"
    ),showlegend=False)
        mfig2.update_layout(font=dict(
        family="Times New Roman",
        size=8,
        color="Black"
    ),showlegend=False)
        
        
        
        return mfig1,mfig2



@app.callback(
    Output(component_id='sando_map', component_property='figure'),
    Input(component_id='opt1', component_property='value'),
    Input(component_id='opt2', component_property='value'),
    Input(component_id='opt3', component_property='value'),
    Input(component_id='opt4', component_property='value'),
    Input(component_id='opt5', component_property='value'),
)


def group_graph(choice1,choice2,choice3,choice4,choice5):
    
    
    labels = [choice1,choice2,choice3,choice4,choice5]
    
    a = sando[sando["Items"]==choice1]
    protein_a = a.iloc[0][5]
    fat_a = a.iloc[0][6]
    carb_a = a.iloc[0][7]
    sugar_a= a.iloc[0][8]
    sodium_a = a.iloc[0][9]
    
    b = sando[sando["Items"]==choice2]
    protein_b = b.iloc[0][5]
    fat_b = b.iloc[0][6]
    carb_b = b.iloc[0][7]
    sugar_b= b.iloc[0][8]
    sodium_b = b.iloc[0][9]
    
    c = sando[sando["Items"]==choice3]
    protein_c = c.iloc[0][5]
    fat_c = c.iloc[0][6]
    carb_c = c.iloc[0][7]
    sugar_c= c.iloc[0][8]
    sodium_c = c.iloc[0][9]
    
    d = sando[sando["Items"]==choice4]
    protein_d = d.iloc[0][5]
    fat_d = d.iloc[0][6]
    carb_d = d.iloc[0][7]
    sugar_d = d.iloc[0][8]
    sodium_d = d.iloc[0][9]
    
    e = sando[sando["Items"]==choice5]
    protein_e = e.iloc[0][5]
    fat_e = e.iloc[0][6]
    carb_e = e.iloc[0][7]
    sugar_e = e.iloc[0][8]
    sodium_e = e.iloc[0][9]

    
    sfig = go.Figure(data=[
    go.Bar(name='Protein', x=labels, y=[protein_a,protein_b,protein_c,protein_d,protein_e],marker={'color': 'red'}),
    go.Bar(name='Fat', x=labels, y=[fat_a,fat_b,fat_c,fat_d,fat_e],marker={'color': 'pink'}),
    go.Bar(name='Carbs', x=labels, y=[carb_a,carb_b,carb_c,carb_d,carb_e],marker={'color': 'orange'}),
    go.Bar(name='Sugar', x=labels, y=[sugar_a,sugar_b,sugar_c,sugar_d,sugar_e],marker={'color': 'lightgreen'}),
    go.Bar(name='Sodium', x=labels, y=[sodium_a,sodium_b,sodium_c,sodium_d,sodium_e],marker={'color': 'darkgreen'})
    ])
    
    sfig.update_layout(barmode='group')
    sfig.update_layout(title_text='Sandwich comparison')
    return sfig


@app.callback(
    Output(component_id='drink_map', component_property='figure'),
    Input(component_id='dpt1', component_property='value'),
    Input(component_id='dpt2', component_property='value'),
    Input(component_id='dpt3', component_property='value'),
    Input(component_id='dpt4', component_property='value'),
    Input(component_id='dpt5', component_property='value'),
)

def group_graph(choice1,choice2,choice3,choice4,choice5):
    labels = [choice1,choice2,choice3,choice4,choice5]
    a = drink[drink["Items"]==choice1]
    protein_a = a.iloc[0][5]
    fat_a = a.iloc[0][6]
    carb_a = a.iloc[0][7]
    sugar_a= a.iloc[0][8]
    sodium_a = a.iloc[0][9]
    
    b = drink[drink["Items"]==choice2]
    protein_b = b.iloc[0][5]
    fat_b = b.iloc[0][6]
    carb_b = b.iloc[0][7]
    sugar_b= b.iloc[0][8]
    sodium_b = b.iloc[0][9]
    
    c = drink[drink["Items"]==choice3]
    protein_c = c.iloc[0][5]
    fat_c = c.iloc[0][6]
    carb_c = c.iloc[0][7]
    sugar_c= c.iloc[0][8]
    sodium_c = c.iloc[0][9]
    
    d = drink[drink["Items"]==choice4]
    protein_d = d.iloc[0][5]
    fat_d = d.iloc[0][6]
    carb_d = d.iloc[0][7]
    sugar_d = d.iloc[0][8]
    sodium_d = d.iloc[0][9]
    
    e = drink[drink["Items"]==choice5]
    protein_e = e.iloc[0][5]
    fat_e = e.iloc[0][6]
    carb_e = e.iloc[0][7]
    sugar_e = e.iloc[0][8]
    sodium_e = e.iloc[0][9]

    
    dfig = go.Figure(data=[
    go.Bar(name='Protein', x=labels, y=[protein_a,protein_b,protein_c,protein_d,protein_e],marker={'color': 'red'}),
    go.Bar(name='Fat', x=labels, y=[fat_a,fat_b,fat_c,fat_d,fat_e],marker={'color': 'pink'}),
    go.Bar(name='Carbs', x=labels, y=[carb_a,carb_b,carb_c,carb_d,carb_e],marker={'color': 'orange'}),
    go.Bar(name='Sugar', x=labels, y=[sugar_a,sugar_b,sugar_c,sugar_d,sugar_e],marker={'color': 'lightgreen'}),
    go.Bar(name='Sodium', x=labels, y=[sodium_a,sodium_b,sodium_c,sodium_d,sodium_e],marker={'color': 'darkgreen'})
    ])
    
    dfig.update_layout(barmode='group')
    dfig.update_layout(title_text='Drink comparison')
    return dfig

@app.callback(
    dash.dependencies.Output('crossfilter-indicator-scatter', 'figure'),
    [dash.dependencies.Input('crossfilter-xaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-yaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-xaxis-type', 'value'),
     dash.dependencies.Input('crossfilter-yaxis-type', 'value'),
     dash.dependencies.Input('crossfilter-year--slider', 'value')])
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type,
                 year_value):
    df_indf = df_ind[df_ind['Year'] == year_value]

    fig = px.scatter(x=df_indf[df_indf['Indicator Name'] == xaxis_column_name]['Value'],
            y=df_indf[df_indf['Indicator Name'] == yaxis_column_name]['Value'],
            hover_name=df_indf[df_indf['Indicator Name'] == yaxis_column_name]['State Name']
            )

    fig.update_traces(customdata=df_indf[df_indf['Indicator Name'] == yaxis_column_name]['State Name'])

    fig.update_xaxes(title=xaxis_column_name, type='linear' if xaxis_type == 'Linear' else 'log')

    fig.update_yaxes(title=yaxis_column_name, type='linear' if yaxis_type == 'Linear' else 'log')

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    return fig


def create_time_series(df_indf, axis_type, title):

    fig = px.scatter(df_indf, x='Year', y='Value')

    fig.update_traces(mode='lines+markers')

    fig.update_xaxes(showgrid=False)

    fig.update_yaxes(type='linear' if axis_type == 'Linear' else 'log')

    fig.add_annotation(x=0, y=0.85, xanchor='left', yanchor='bottom',
                       xref='paper', yref='paper', showarrow=False, align='left',
                       bgcolor='rgba(255, 255, 255, 0.5)', text=title)

    fig.update_layout(height=225, margin={'l': 20, 'b': 30, 'r': 10, 't': 10})

    return fig


@app.callback(
    dash.dependencies.Output('x-time-series', 'figure'),
    [dash.dependencies.Input('crossfilter-indicator-scatter', 'hoverData'),
     dash.dependencies.Input('crossfilter-xaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-xaxis-type', 'value')])
def update_y_timeseries(hoverData, xaxis_column_name, axis_type):
    state_name = hoverData['points'][0]['customdata']
    df_indf = df_ind[df_ind['State Name'] == state_name]
    df_indf = df_indf[df_indf['Indicator Name'] == xaxis_column_name]
    title = '<b>{}</b><br>{}'.format(state_name, xaxis_column_name)
    return create_time_series(df_indf, axis_type, title)


@app.callback(
    dash.dependencies.Output('y-time-series', 'figure'),
    [dash.dependencies.Input('crossfilter-indicator-scatter', 'hoverData'),
     dash.dependencies.Input('crossfilter-yaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-yaxis-type', 'value')])
def update_x_timeseries(hoverData, yaxis_column_name, axis_type):
    df_indf = df_ind[df_ind['State Name'] == hoverData['points'][0]['customdata']]
    df_indf = df_indf[df_indf['Indicator Name'] == yaxis_column_name]
    return create_time_series(df_indf, axis_type, yaxis_column_name)

if __name__ == "__main__":
    app.run_server(host = '127.0.0.1');


# In[ ]:




