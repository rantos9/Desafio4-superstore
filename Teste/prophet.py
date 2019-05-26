#Importando o Prophet
from fbprophet import Prophet

#Chama a função do prophet
def prophet(timeseries):
    timeseries=timeseries.reset_index()
    #Renomeando o dataframe para o Prophet
    timeseries= timeseries.rename(columns= { "Order Date":"ds" , "Sales": "y" })
    # Instanciando o modelo e Fitando
    my_model = Prophet(interval_width=0.95)
    my_model.fit(timeseries)
    # Escolhendo a quande de cycles para a prediçao
    future_dates = my_model.make_future_dataframe(periods=36, freq='MS')
    # Executando a predição do modelo
    futuro=future_dates
    forecast = my_model.predict(future_dates)
    return forecast, futuro 