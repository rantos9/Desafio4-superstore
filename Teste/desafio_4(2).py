#Executando os imports
import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd
import statsmodels.api as sm
import matplotlib
#%matplotlib inline
#import sarimax
#from arima import arima
#from prophet import prophet

#Executando parametros de plot
matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'

#Lendo o dataset e criando o dataframe
df = pd.read_excel("./data/Sample - Superstore.xls")

#Preparando função de preparação da Time Series
def prepare_time_series (data):
    cols = ['Row ID', 'Order ID', 'Ship Date', 'Ship Mode', 'Customer ID', 'Customer Name', 'Segment', 'Country', 'City','State', 'Postal Code',
 'Region', 'Product ID', 'Category', 'Sub-Category', 'Product Name', 'Quantity', 'Discount', 'Profit']
    data.drop(cols, axis=1, inplace=True)
    data = data.sort_values('Order Date')
    data = data.groupby('Order Date')['Sales'].sum().reset_index()
    data = data.set_index('Order Date')
    return data

#Preparando função de filtro do dataframe pela categoria escolida 
def filter_by_category(category):
    return df.loc[df['Category'] == category]
#Executando filtro standard
data = filter_by_category('Office Supplies')

#Executando a função de Time Series
prepare_time_series(data)

#Plotando o Grafico do faturamento pelo tempo
plt.plot(data)

#  Joga para Y a Time Series organizada pela média mensal
y = data['Sales'].resample('MS').mean()

# Roda modelo de previsão de vendas (Forecasting)
pred = results.get_prediction(start=pd.to_datetime('2017-01-01'), dynamic=False)
pred_ci = pred.conf_int()
print(pred_ci)