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
#from sarimax import sarimax
#from arima import arima
#from prophet import prophet
from pylab import rcParams
from statsmodels.tsa.stattools import adfuller

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

# Plota o Y para uma análise visual do faturamento por mês
y.plot(figsize=(15, 6))
plt.show()
print('\n') # Pular a linha para o s graficos não ficarem encavalados

# Plota os graficos de tendencia, sasonalidade e Residual
rcParams['figure.figsize'] = 18, 8
decomposition = sm.tsa.seasonal_decompose(y, model='additive')
fig = decomposition.plot()
plt.show()
print('\n') # Pular a linha para o s graficos não ficarem encavalados

#Prepara uma função para o teste DICKEY-FULLER
def test_stationarity(timeseries):
    
    #Determing rolling statistics
    rolmean = timeseries.rolling(12).mean()
    rolstd = timeseries.rolling(12).std()

    #Plot rolling statistics:
    orig = plt.plot(timeseries, color='blue',label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)
    
#     Perform Dickey-Fuller test:
    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print(dfoutput)

# Executa o teste
adfuller(y)

#Analisa a estacionaridade
test_stationarity(y)

# Roda modelo de previsão de vendas (Forecasting)
#pred = results.get_prediction(start=pd.to_datetime('2017-01-01'), dynamic=False)
#pred_ci = pred.conf_int()

ax = y['2014':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))

ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)

ax.set_xlabel('Date')
ax.set_ylabel('Sales')
plt.legend()
plt.show()

# Mensura o MSE do modelo de predição
y_forecasted = pred.predicted_mean
y_truth = y['2017-01-01':]
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))

#Printa o RMSE do modelo
print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))

# Printa a previsão para um período maior eo seu intervalo de confiança
pred_uc = results.get_forecast(steps=100)
pred_ci = pred_uc.conf_int()

ax = y.plot(label='observed', figsize=(14, 7))
pred_uc.predicted_mean.plot(ax=ax, label='Forecast')
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.25)
ax.set_xlabel('Date')
ax.set_ylabel('Furniture Sales')

plt.legend()
plt.show()





