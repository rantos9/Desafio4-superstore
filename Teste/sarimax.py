import pickle
import statsmodels.api as sm
def sarimax (timeseries,steps):
    #Fita o modelo Sarimax para os valores do df
    mod=sm.tsa.statespace.SARIMAX(timeseries,order=good_param,seasonal_order=good_param_seasonal,enforce_stationarity=False,enforce_invertibility=False)
    results = mod.fit()
    return results
