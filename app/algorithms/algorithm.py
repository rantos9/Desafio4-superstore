import abc

class TimeSeriesAlgorithm(abc.ABC):

    @abc.abstractmethod
    def predict(self, params_input):
        '''
        Método a ser implementado pelas classes filhas
        '''
        return 'Implementacao do predict'
