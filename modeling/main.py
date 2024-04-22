#model
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.svm import LinearSVC
from sklearn.preprocessing import  LabelEncoder
from transformers import AutoTokenizer, AutoModel

from src.model import *
from src.preprocessing import *


tokenizer = AutoTokenizer.from_pretrained("indobenchmark/indobert-base-p1")
model = AutoModel.from_pretrained("indobenchmark/indobert-base-p1")

class Preprocessing:

    def __init__(self,df):
        self.X = df["text"].values
        self.labels = df['Category'].values

    #def clean_data(self):
    #    self.X = batch_clean(self.X)
    #    self.labels = batch_clean(self.labels)
    
    def split_data(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.labels, test_size=0.2, random_state=42)

    def tokenizing(self):
        self.train_loader = batch_tokenize_data(tokenizer, self.X_train.tolist())
        self.val_loader = batch_tokenize_data(tokenizer, self.X_test.tolist())

    def encoding(self):
        self.encoder = LabelEncoder()
        self.y_train_ = self.encoder.fit_transform(self.y_train)
        self.y_test_ = self.encoder.transform(self.y_test)
    
    def get_data(self):
        return self.train_loader, self.val_loader, self.y_train_, self.y_test_
    

class Modeling:
    models= {
        "rf": RandomForestClassifier(),
        "xgb": XGBClassifier(),
        "svm": LinearSVC()
    }

    def __init__(self,train_loader,val_loader,y_train_,y_test_,**kwargs):
        self.train_loader = train_loader
        self.val_loader = val_loader
        self.y_train_ = y_train_
        self.y_test_ = y_test_

    def get_hidden_clf(self):
        self.cls_train = get_cls_hidden_state_batches(self.train_loader, model)[:,0,:]
        self.cls_val = get_cls_hidden_state_batches(self.val_loader, model)[:,0,:]
        print(self.cls_train)
        print(self.cls_val)

    def train_models(self):
        for key, model in self.models.items():
            model.fit(self.cls_train,self.y_train_)

    def evaluate_models(self):
        preds = {key: model.predict(self.cls_val) for key,model in self.models.items()}
        models_score = compare_model(preds,self.y_test_)
        self.scores(models_score.to_json(orient='records'))

    def get_models():
        return self.models

def save_model(client_id,product_id,models):
    model_path = {}
    for key,model in models.items():
        path = f"./model_library/{client_id}/{product_id}"
        os.makedirs(path, exist_ok=True)
        pickle.dump(model, open(os.path.join(path, f"{key}.pkl"), 'wb'))
        model_path[key]= os.path.join(path, f"{key}.pkl")

    return models_path
    

def create_model():
    preprocess = Preprocessing()
    preprocess.split_data()
    preprocess.tokenizing()
    preprocess.encoding()

    modeling = Modeling(**vars(preprocess))
    print(vars(preprocess).keys())
    modeling.get_hidden_clf()
    modeling.train_models()
    return modeling.models, modeling.scores