import pickle

class ModelLocator(object):
    def __init__(self, *args):
        pass

    def load_model(self, category, algorithm):
        '''A partir do codigo do produto, identifica a categoria. Deve ser carregado um modelo
        que é a combinação entre a categoria e o algoritmo
        '''
        return self.deserialize('arima')

    def deserialize(self, model_name):
        with open(f'${model_name}.plk', 'rb') as handle:
            model = pickle.load(handle)
        return model

    def predict(self, category, algorithm, cycles_or_date):
        model = self.load_model(category, algorithm)
        #NECESSARIO CONSTRUIR O MODELO(Carregar dataset, filtrar categoria)
        #Serão criadas N classes(uma pra cara algoritmo) e cada uma chamar seu respectivo método:
        #predict(sarimax), get_prediction(arima) ou make_future_dataframe(prophet), dentro de um método predict
        return model.predict(cycles_or_date)
        