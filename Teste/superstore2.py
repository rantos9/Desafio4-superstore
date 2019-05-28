from flask import Flask
from flask import request, jsonify, abort, make_response
from modelo2_ import modelo2_

app = Flask(__name__)
@app.route('/superstore/predict', methods=['POST','GET'])
def predict():
    param_category=request.args.get('category')
    param_cycles=request.args.get('cycles')
    param_algorithm=request.args.get('algorithm')
    results=modelo2_(param_algorithm,param_category,param_cycles)
    json_data = results.to_json()
    return json_data
    #Carregar Modelo e passar algorithm, category e date como parametros
    
    #jsonify({'category':param_category,'cycles': param_cycles,'algorithm':param_algorithm,'resultado':results}),200

@app.route('/superstore/predictor',methods=['POST', 'GET'])
def predictor():
    if request.method == 'POST':
        param_category=request.args.get('category')
        param_cycles=request.args.get('cycles')
        param_algorithm=request.args.get('algorithm')
        results=modelo2(param_algorithm,param_category,param_cycles)
        json_data = results.to_json()
        return json_data
        
    return'''<form method="POST">
    Steps <input type="text" name="cycles">
    Algoritimo<input type="text" name="algorithm">
    Categoria <input type="text" name="category">
    <input type="Submit">
    </form>'''

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
    return 'category_list' , 200 
if __name__ == "__main__":    app.run(debug=True)