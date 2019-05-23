#Importando o Prophet
from fbprophet import Prophet

#Chama a função do prophet
def prophet(timeseries):
    #Renomeando o dataframe para o Prophet
    data=data.rename(columns= { "Order Date":  "ds","Sales": "y"})

    # Instanciando o modelo e Fitando
    my_model = Prophet(interval_width=0.95)
    my_model.fit(data)
    
    # Escolhendo a quande de cycles para a prediçao
    future_dates = my_model.make_future_dataframe(periods=cycles, freq='MS')

    # Executando a predição do modelo
    forecast = my_model.predict(future_dates)

    # Plotando a saida das predições
    my_model.plot(forecast,uncertainty=True) # Necessario o comando print ?

    # PLota a decomposição do Forecast
    my_model.plot_components(forecast)
    
    return forecast 