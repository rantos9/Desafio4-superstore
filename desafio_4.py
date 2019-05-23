#Executando o s imports
import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd
import statsmodels.api as sm
import matplotlib
#from sarimax import sarimax
#from arima import arima
#from prophet import prophet

#Executando parametros de plot
matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'

#Lendo o dataset e criando o dataframe
df = pd.read_excel("./data/Sample - Superstore.xls")
#Executando função de preparação da Time Series
def prepare_time_series (data):
    cols = ['Row ID', 'Order ID', 'Ship Date', 'Ship Mode', 'Customer ID', 'Customer Name', 'Segment', 'Country', 'City','State', 'Postal Code',
 'Region', 'Product ID', 'Category', 'Sub-Category', 'Product Name', 'Quantity', 'Discount', 'Profit']
    data.drop(cols, axis=1, inplace=True)
    data = data.sort_values('Order Date')
    data = data.groupby('Order Date')['Sales'].sum().reset_index()
    data = data.set_index('Order Date')

#Executando função de filtro do dataframe pela categoria escolida 
def filter_by_category(category):
    return df.loc[df['Category'] == category]

data = filter_by_category('Furniture')
prepare_time_series(data)
print(data.head())




