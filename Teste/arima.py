import statsmodels.api as sm
import itertools

#Define a funçao do arima 
def arima(timeseries):
    mod = sm.tsa.ARIMA(data, order=param)
    results = mod.fit()
    pred = results.get_prediction(start=pd.to_datetime('2017-01-01'), dynamic=False)
    return pred_ci = pred.conf_int()