import pickle

def sarimax(category, steps = 6):
    model = pickle.load(open(category+".pkl","rb"))
    pred_uc = model.get_forecast(steps = steps)
    return pred_uc.conf_int()