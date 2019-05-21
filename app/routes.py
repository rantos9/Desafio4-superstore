from app import app
from flask import request, jsonify, abort, make_response, Response
from datetime import datetime

@app.route('/predict/time_series/<algorithim>', methods=['GET'])
def predict_by_category(algorithim):
    '''
    Metodo que executa a predicao do time_series, de acordo com algoritmo selecionado.
    Algorithim:
        ARIMA, SARIMAX, etc...
    Parâmetros URL Get:
        categoria
        data
    '''

    #Carregar lista de categorias da planilha
    category_list = ['cat1', 'cat2', 'cat3']

    param_date = get_date_parameter('date')
    param_category = request.args.get('category')
    if param_category not in category_list:
        abort(make_response(jsonify(message='Category is not valid'), 422))

    #Carregar Modelo e passar algorithm, category e date como parametros
    return  jsonify(f'Category: {param_category}, Data: {param_date}, Algorithm:{algorithim}'), 200

def get_date_parameter(name):
    try:
        #Procurar por uma solucao flask pra substituir o strip
        date_parameter = request.args.get(name).strip('\'"')
        return datetime.strptime(date_parameter, '%d/%m/%Y').date()
    except ValueError as v_error:
        print(v_error)
        abort(make_response(jsonify(message='Date is not valid'), 422))
    