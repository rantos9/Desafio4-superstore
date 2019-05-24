from flask import request, jsonify, abort, make_response
from app import app
from algorithms import ModelLocator

@app.route('/superstore/predict', methods=['GET'])
def timeseries_predict():
    '''
    Metodo que executa a predicao do time_series, de acordo com os parâmetros selecionados.
    algorithm:
        ARIMA, SARIMAX
    category:
        'Office Supplies', 'Furniture', 'Technology'
    cycles:
        Número de janelas a partir de 12/2017
    '''

    #Carregar lista de categorias da planilha
    category_list = ['Office Supplies', 'Furniture', 'Technology']
    algorithm_list = ['ARIMA', 'SARIMAX']

    param_algorithm = request.args.get('algorithm').strip('\'"')
    param_cycles = request.args.get('cycles', type=int)
    param_category = request.args.get('category').strip('\'"')
   
    if param_algorithm.upper() not in algorithm_list:
        abort(make_response(jsonify(message='Algorithm is not valid'), 422))

    if param_category not in category_list:
        abort(make_response(jsonify(message='Category is not valid'), 422))

    #Carregar Modelo e passar algorithm, category(OU PRODUTO) e date como parametros
    return jsonify(ModelLocator.predict(param_category, param_algorithm, param_cycles)), 200
    #return jsonify(f'Cat:{param_category},Cycles:{param_cycles},Algorithm:{param_algorithm}'),200

@app.route('/superstore/categories/<category_id>/products')
def products_by_category(category_id):
    '''
    Obtém a lista de códigos de produto por categoria
    '''
    return f'products_by_category {category_id}', 200

@app.route('/superstore/categories')
def categories():
    '''
    Obtém a lista de categorias
    '''
    return 'categories', 200
    