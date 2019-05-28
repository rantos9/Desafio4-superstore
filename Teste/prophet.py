#Importando o Prophet
from fbprophet import Prophet
#import pickle

#Chama a função do prophet
def prophet(timeseries,steps):
    timeseries=timeseries.reset_index()
    #Renomeando o dataframe para o Prophet
    timeseries= timeseries.rename(columns= { "Order Date":"ds" , "Sales": "y" })
    # Instanciando o modelo e Fitando
    my_model = Prophet(interval_width=0.95) #pickle.load(open("prophet,pkl","rb"))
    my_model.fit(timeseries)
    # Escolhendo a quande de cycles para a prediçao
    future_dates = my_model.make_future_dataframe(periods=int(steps), freq='MS')
    # Executando a predição do modelo
    forecast = my_model.predict(future_dates)
    return forecast