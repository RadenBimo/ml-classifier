#model
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.svm import LinearSVC
from transformers import AutoTokenizer, AutoModel



if ___name__== "___main___":

    #innitiate Tokenizer
    tokenizer = AutoTokenizer.from_pretrained("indobenchmark/indobert-base-p1")
    model = AutoModel.from_pretrained("indobenchmark/indobert-base-p1")

    # Create data loaders
    train_loader = batch_tokenize_data(tokenizer, X_train.tolist())
    val_loader = batch_tokenize_data(tokenizer, X_test.tolist())
    
    # Process training and validation data
    hidden_train = process_batches(train_loader, model)
    hidden_val = process_batches(val_loader, model)



