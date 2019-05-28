#Define a funçao do arima 
import statsmodels.api as sm
import pandas as pd
def arima(timeseries,steps):
    mod=sm.tsa.ARIMA(timeseries, order=(2, 1,0))
    results = mod.fit()
    pred = results.get_prediction(start=('2017-01-01'), dynamic=False)
    pred_ci = pred.conf_int()
    return pred_ci