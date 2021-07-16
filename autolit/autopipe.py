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

    """Class used to create an sklearn pipeline for the streamlit app. 
    
    Args:
        numeric_features (list): list of numerical features from data to be used in the pipeline
        categorical_features (list): list of categorical features from data to be used in the pipeline
        numeric_transformer (list): list of sklearn API's used to preprocess the numerical data in the pipeline
        categorical_transformer (list): list of sklearn API's used to preprocess the categorical data in the pipeline
        predictor (sklearn object): sklearn algorithm used to predict at the end of the pipeline
    """
    
    
    def pipline(self):
        """USed to create the sklearn pipeline using the args passed to the class

        Returns:
            [pipeline]: [Sklearn pipeline of the data. Ready to be trained and evaluated.]
        """
        
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