from arima import arima
from sarimax import sarimax
from prophet import prophet 
def modelo2(param_algorithm,param_category,param_cycles):
    steps=param_cycles
    if param_algorithm == "arima":
        a = arima(y,steps)
        return a
    elif param_algorithm == "sarimax":
        s=sarimax(y,steps)
        return s
    else:
        p=prophet(y,steps)
        return p 
     