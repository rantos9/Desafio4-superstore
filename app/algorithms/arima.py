import statsmodels.api as sm
import itertools
from algorithms import algorithm

class Arima(TimeSeriesAlgorithm):
    def __init__(self, *args):
            pass
    
    def predict(self, cycles_or_date):
        return model.get_prediction(start=pd.to_datetime(cycles_or_date), dynamic=False)

    #Define a funçao do arima 
    def arima(self, timeseries):
        mod = sm.tsa.ARIMA(data, order=param)
        results = mod.fit()
        pred = results.get_prediction(start=pd.to_datetime('2017-01-01'), dynamic=False)
        return pred_ci = pred.conf_int()