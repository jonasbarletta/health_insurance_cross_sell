import pickle
import pandas as pd
from flask import Flask, request, Response
from healthinsurance.HealthInsurance import HealthInsurance
import numpy

path = '/home/jonas/Documentos/repos/health_insurance_cross_sell/'
model = pickle.load(open(path + 'model/lgbm_model.pkl', 'rb'))

# inicialização da API
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def health_insurance_predict():
    test_json = request.get_json()

    if test_json:  # se existir data
        if isinstance(test_json, dict): # se for uma única linha
            test_raw = pd.DataFrame(test_json, index=[0])
        
        else: # se for múltiplas linhas

            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())            
            
        # instanciando a Classe HealthInsurance
        pipeline = HealthInsurance()
        
        # limpeza dos dados
        df1 = pipeline.data_cleaning(test_raw)
        
        # feature engineering
        df2 = pipeline.feature_engineering(df1)
        
        # preparação dos dados
        df3 = pipeline.data_preparation(df2)
        
        # predição
        df_response = pipeline.get_prediction(model, test_raw, df3)
        
        return df_response
    
    else:
        return Response('{}', status=200, mimetype='application/json')
    
    
if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
