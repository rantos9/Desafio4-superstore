#Importando o Prophet
from fbprophet import Prophet
#Importando o Plotly
from plotly.offline import init_notebook_mode, iplot
from plotly import graph_objs as go
# Initialize plotly
init_notebook_mode(connected=True)

#Chama a função do prophet
def prophet(data):
    #Renomeando o dataframe para o Prophet
    data2=data.rename(columns= { "Order Date":  "ds",
                  "Sales": "y"})
    # Instanciando o modelo e Fitando
    my_model = Prophet(interval_width=0.95)
    my_model.fit(df)
    
    # Escolhendo a quande de cycles para a predicao
    future_dates = my_model.make_future_dataframe(periods=cycles, freq='MS')

    # Executando a predição do modelo
    forecast = my_model.predict(future_dates)

    # Plotando a saida das predições
    my_model.plot(forecast,uncertainty=True) # Necessario o comando print ?

    # PLota a decomposição do Forecast
    my_model.plot_components(forecast)
    
    # Define função para plotar o gráfico
    def plotly_df(data2, title=''):
        #"""Visualize all the dataframe columns as line plots."""
        common_kw = dict(x=df.index, mode='lines')
        data = [go.Scatter(y=data2[c], name=c, **common_kw) for c in data2.columns]
        layout = dict(title=title)
        fig = dict(data=data, layout=layout)
        iplot(fig, show_link=False)
        plotly_df(data2, title='Resultado das vendas')


return 




