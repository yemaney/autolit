from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from dataclasses import dataclass

@dataclass()
class Autolitpred:
    
    numeric_features: list  
    categorical_features: list
    numeric_transformer: list
    categorical_transformer: list
    predictor: object

    
    
    def pipline(self):
        
        if (len(self.numeric_features) > 0) and ( len(self.categorical_features) > 0):
                  
            numeric_transformer = make_pipeline(*self.numeric_transformer)
            categorical_transformer = make_pipeline(*self.categorical_transformer)
            preprocessor = make_column_transformer(*[(numeric_transformer, self.numeric_features), 
                                                    (categorical_transformer, self.categorical_features)])
        
        elif (len(self.numeric_features) == 0) and ( len(self.categorical_features) > 0):              
            categorical_transformer = make_pipeline(*self.categorical_transformer)
            preprocessor = make_column_transformer(*[(categorical_transformer, self.categorical_features)])
           
        else:
            numeric_transformer = make_pipeline(*self.numeric_transformer)
            preprocessor = make_column_transformer(*[(numeric_transformer, self.numeric_features)])
   


        pipeline = make_pipeline(*[preprocessor, self.predictor])
        return pipeline