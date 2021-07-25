# pipeline imports
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer, make_column_selector

# preprocessors
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

# classifiers
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

# regressors
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

# selection 
from sklearn.feature_selection import SelectKBest, mutual_info_classif, mutual_info_regression
from sklearn.model_selection import GridSearchCV, train_test_split


class Autopipe():
    
    def __init__(self, df, y) -> None:
        self.df = df
        self.y = y
    
    
    def clf_pipeline(self):
        """Class method used to create a simple classification pipeline, and gridsearchs for the best combination
        of feature preprocessing, selections and model selection, hyperparameter tuning

        Returns:
            gridsearch: outcome of custom sklearn classification pipeline gridsearch
            X_train: Validation set of predictor variables
            y_train: Validation set of target variables
        """
        
        
        
        
        
        df = self.df
        y = self.y
        
        
        
        numeric_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer()),
            ('scaler', StandardScaler())
        ])
        

        categorical_transformer = OneHotEncoder(handle_unknown="ignore")
        
        
        preprocessor  = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, make_column_selector(dtype_include='number')),
                ('cat', categorical_transformer, make_column_selector(dtype_include=object))
            ]
        )


        clf = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('selector', SelectKBest(mutual_info_classif, k=5)),
            ('classifier', LogisticRegression())
        ])
        
        
        X = df.drop(y, axis=1)
        y = df[y]
        
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=20, random_state=42)
        

        param_grid = [
            {'preprocessor__num__imputer__strategy': ['mean', 'median']},
            {'selector__k': [2, 3, 5, 7]},
            {'classifier': [RandomForestClassifier()],
            'classifier__criterion': ['gini', 'entropy']},
            {'classifier': [SVC()],
            'classifier__kernel': ['linear', 'poly', 'rbf', 'sigmoid']},
            {'classifier': [KNeighborsClassifier()],
            'classifier__n_neighbors': [2, 3, 4],
            'classifier__weights': ['uniform', 'distance']}
        ]
        
        
        grid_search = GridSearchCV(clf, param_grid, cv=3, verbose=2)
        
        
        grid_search.fit(X_train, y_train)
        
        return grid_search, X_test, y_test
    
    
    
    def reg_pipeline(self):
        """Class method used to create a simple regression pipeline, and gridsearchs for the best combination
        of feature preprocessing, selections and model selection, hyperparameter tuning

        Returns:
            gridsearch: outcome of custom sklearn regression pipeline gridsearch
            X_train: Validation set of predictor variables
            y_train: Validation set of target variables
        """       
        
        
        
        
        
        df = self.df
        y = self.y
        
        
        
        numeric_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer()),
            ('scaler', StandardScaler())
        ])
        

        categorical_transformer = OneHotEncoder(handle_unknown="ignore")
        
        
        preprocessor  = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, make_column_selector(dtype_include='number')),
                ('cat', categorical_transformer, make_column_selector(dtype_include=object))
            ]
        )


        clf = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('selector', SelectKBest(mutual_info_regression, k=5)),
            ('classifier', LinearRegression())
        ])
        
        
        X = df.drop(y, axis=1)
        y = df[y]
        
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=20, random_state=42)
        

        param_grid = [
            {'preprocessor__num__imputer__strategy': ['mean', 'median']},
            {'selector__k': [2, 3, 5, 7]},
            {'classifier': [RandomForestRegressor()],
            'classifier__criterion': ['mse', 'mae']},
            {'classifier': [SVR()],
            'classifier__kernel': ['linear', 'poly', 'rbf', 'sigmoid']}
        ]
        
        
        grid_search = GridSearchCV(clf, param_grid, cv=3, verbose=2)
        
        
        grid_search.fit(X_train, y_train)
        
        return grid_search, X_test, y_test
