#Define a funçao do arima 
import statsmodels.api as sm
def arima(timeseries):
    mod = sm.tsa.ARIMA(timeseries, order=(2, 1,0))
    results = mod.fit()
    #pred = results.get_prediction(start=pd.to_datetime('2017-01-01'), dynamic=False)
    #pred_ci = pred.conf_int()
    return results