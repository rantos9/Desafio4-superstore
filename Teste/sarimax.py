import statsmodels.api as sm
import itertools

def tunning_SARIMAX_hyperparameters(timeseries):
    
    #Finds the best SARIMAX hyperparameters for a given timeseries 
    
    p = d = q = range(0, 2)
    pdq = list(itertools.product(p, d, q))
    seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
    AIC = 10**6
    for param in pdq:
        for param_seasonal in seasonal_pdq:
            try:
                mod = sm.tsa.statespace.SARIMAX(timeseries,
                                                order=param,
                                                seasonal_order=param_seasonal,
                                                enforce_stationarity=False,
                                                enforce_invertibility=False)
                results = mod.fit()
                if results.aic < AIC:
                    good_param = param
                    good_param_seasonal = param_seasonal
            except:
                continue
            
    return good_param, good_param_seasonal

#Ajusta os valores do SARIMAX para a melhor performace
tunning_SARIMAX_hyperparameters(y)
good_param, good_param_seasonal = tunn # Para que serve a variavel tunn ?

#Fita o modelo Sarimax para os valores do df
mod = sm.tsa.statespace.SARIMAX(y,
                                order=good_param,
                                seasonal_order=good_param_seasonal,
                                enforce_stationarity=False,
                                enforce_invertibility=False)

results = mod.fit()
#Printa os resultados do SARIMAX
print(results.summary().tables[1])