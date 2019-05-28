import pickle

def predict(category, periods = 6):
	model = pickle.load(open(category+".pkl","rb"))
	future_dates = model.make_future_dataframe(periods=int(periods), freq='MS')
	forecast = model.predict(future_dates)
	return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]