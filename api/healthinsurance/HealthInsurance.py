import pickle
import pandas as pd
import numpy as np

class HealthInsurance(object):
    
    def __init__(self):
        self.path = '/home/jonas/Documentos/repos/health_insurance_cross_sell/parameter/'
        self.age_scaler                = pickle.load(open(self.path + 'age_scaler.pkl', 'rb'))
        self.annual_premium_scaler     = pickle.load(open(self.path + 'annual_premium_scaler.pkl', 'rb'))
        self.fe_encode_policy          = pickle.load(open(self.path + 'fe_encode_policy.pkl', 'rb'))
        self.target_encode_region_code = pickle.load(open(self.path + 'target_encode_region_code.pkl', 'rb'))
        self.target_encode_vehicle_age = pickle.load(open(self.path + 'target_encode_vehicle_age.pkl', 'rb'))
        self.vintage_scaler            = pickle.load(open(self.path + 'vintage_scaler.pkl', 'rb'))
    
    def data_cleaning(self, data):
        data.columns = data.columns.str.lower()
        
        return data
    
    def feature_engineering(self, data):
        # vehicle_age
        data['vehicle_age'] = data['vehicle_age'].apply(lambda x: 'less_than_1' if x == '< 1 Year' else 
                                                                'between_1_2' if x == '1-2 Year' else
                                                                'more_than_2')
        
        # age
        data['joviality'] = data['vintage'].apply(lambda x: 1 if x < 25 else 0)

        return data
    
    def data_preparation(self, data):
        
        ## annual premium
        data['annual_premium'] = self.annual_premium_scaler.transform(data[['annual_premium']].values)

        # age
        data['age'] = self.age_scaler.transform(data[['age']].values)

        # vintage 
        data['vintage'] = self.vintage_scaler.transform(data[['vintage']].values)

        # region_code
        data['region_code'] = data['region_code'].map(self.target_encode_region_code)

        # policy_sales_channel
        data['policy_sales_channel'] = data['policy_sales_channel'].map(self.fe_encode_policy)

        # vehicle_age
        data['vehicle_age'] = data['vehicle_age'].map(self.target_encode_vehicle_age)

        # gender
        data['gender'] = data['gender'].apply(lambda x: 1 if x == 'Male' else 0)

        # vehicle_damage -  One Hot Encoding (escolhido) / Frequency Encoding / Target Encoding / Weight Target Encoding
        data['vehicle_damage'] = data['vehicle_damage'].apply(lambda x: 1 if x == 'Yes' else 0)

        data = data.fillna(0)
        
        # colunas selecionadas    
        cols_selected = ['vintage', 'annual_premium', 'age', 'region_code', 'vehicle_damage', 'policy_sales_channel', 'previously_insured', 'vehicle_age', 'gender', 'driving_license', 'joviality']


        return data[cols_selected]

    def get_prediction(self, model, original_data, test_data):
        # model predition
        pred = model.predict_proba(test_data)
        
        # join prediction into original data
        original_data['score'] = pred[:, 1]
        
        return original_data.to_json(orient='records', date_format='iso') 
