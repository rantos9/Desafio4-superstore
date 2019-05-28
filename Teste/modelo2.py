def modelo2(param_algorithm,param_category,param_cycles):
    #Executando os imports
    import warnings
    import itertools
    import numpy as np
    import matplotlib.pyplot as plt
    warnings.filterwarnings("ignore")
    import pandas as pd
    import statsmodels.api as sm
    from sarimax import sarimax
    from arima import arima
    from prophet import prophet
    import pickle
    #Preparando função de preparação da Time Series
    def prepare_time_series (data):
        cols = ['Row ID', 'Order ID', 'Ship Date', 'Ship Mode', 'Customer ID', 'Customer Name', 'Segment', 'Country', 'City','State','Postal Code','Region', 'Product ID', 'Category', 'Sub-Category', 'Product Name', 'Quantity', 'Discount', 'Profit']
        data.drop(cols, axis=1, inplace=True)
        data = data.sort_values('Order Date')
        data = data.groupby('Order Date')['Sales'].sum().reset_index()
        data = data.set_index('Order Date')
        return data
    steps=param_cycles
    #Preparando função de filtro do dataframe pela categoria escolida 
    def filter_by_category(param_category):
        return df.loc[df['Category'] == param_category]
    #selecionando o pickle file
        if param_category == "Office Supplies":
            pickle=pickle.load(open("Office Supplies.pkl","rb")
            return start
        elif param_category == "Technology":
            pickle=pickle.load(open("Technology.pkl","rb")
            return start
        else:
            pickle=pickle.load(open("Furniture.pkl","rb")    
            return start
    #Lendo o dataset e criando o dataframe
    df = pd.read_excel("./data/Sample - Superstore.xls",parse_dates=['Order Date'])
    #Executando filtro standard
    data = filter_by_category('Office Supplies')
    #Executando a função de Time Series
    prepare_time_series(data)
    #Joga para Y a Time Series organizada pela média mensal
    y = data #['Sales'].resample('M').mean()
    if param_algorithm == "arima":
        a = arima(y,steps,pickle)
        return a
    elif param_algorithm == "sarimax":
        s=sarimax(y,steps,pickle)
        return s
    else:
        p=prophet(y,steps,pickle)
        return p 
     