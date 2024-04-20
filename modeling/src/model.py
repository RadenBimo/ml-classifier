from transformers import BertModel, BertTokenizer, DistilBertModel, DistilBertTokenizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, matthews_corrcoef
import numpy as np
import torch
import pandas as pd
from typing import Any, Dict, List, Callable, Optional, Tuple, Union
from torch.utils.data import DataLoader, TensorDataset
from tqdm import tqdm

def batch_tokenize_data(tokenizer, texts,max_length=512, batch_size=100):
    """
    Tokenize and batch the dataset
    """
    # Tokenize the text data
    tokenized = tokenizer(texts, max_length=max_length,padding=True, truncation=True, return_tensors="pt")
    
    # Create a dataset from tensors
    dataset = TensorDataset(tokenized['input_ids'], tokenized['attention_mask'], tokenized['token_type_ids'])
    
    # Create a DataLoader
    return DataLoader(dataset, batch_size=batch_size, shuffle=False)


def get_cls_hidden_state_batches(data_loader, model):
    """
    get cls hidden value by running the choosen BERT model in batches dataset
    """
    model.eval()
    outputs = []
    total_batches = len(data_loader)
    processed_batches = 0
    
    with torch.no_grad():
        for input_ids, attention_mask, token_type_ids in tqdm(data_loader, desc="Processing batches"):
            inputs = {
                'input_ids': input_ids,
                'attention_mask': attention_mask,
                'token_type_ids': token_type_ids
            }
            output = model(**inputs)

            # Accessing the last hidden state
            outputs.append(output.last_hidden_state)

            remaining_batches = total_batches - processed_batches
    
    # Concatenating the results across batches
    return torch.cat(outputs, dim=0)

def calculate_classification_metrics(
    y_true: np.array,
    y_pred: np.array,
    average: Optional[str] = None,
    return_df: bool = True,
) -> Union[Dict[str, float], pd.DataFrame]:
    """
    Computes f1, precision, recall, precision, kappa, accuracy, and support

    Args:
        y_true: The true labels
        y_pred: The predicted labels
        average: How to average multiclass results

    Returns:
        Either a dataframe of the performance metrics or a single dictionary
    """
    labels = unique_labels(y_true, y_pred)

    # get results
    precision, recall, f_score, support = sk_metrics.precision_recall_fscore_support(
        y_true, y_pred, labels=labels, average=average
    )

    kappa = sk_metrics.cohen_kappa_score(y_true, y_pred, labels=labels)
    accuracy = sk_metrics.accuracy_score(y_true, y_pred)

    # create a pandas DataFrame
    if return_df:
        results = pd.DataFrame(
            {
                "class": labels,
                "f_score": f_score,
                "precision": precision,
                "recall": recall,
                "support": support,
                "kappa": kappa,
                "accuracy": accuracy,
            }
        )
    else:
        results = {
            "f1": f_score,
            "precision": precision,
            "recall": recall,
            "kappa": kappa,
            "accuracy": accuracy,
        }

    return results

def compare_model(
    y_preds: Dict[str,np.array],
    y_test: np.array
):
    """
    Computes f1, precision, recall, precision, kappa, accuracy, and support

    Args:
        y_preds: The predicted labels
        y_true: The true labels

    Returns:
        dataframe of the models performance metrics 
    """

    results= pd.DataFrame(columns=["Model",'Accuracy', 'Precision', 'Recall', 'F1 Score', 'MCC'])

    data_list = []
    for model, y_pred in y_preds.items():
        metrics = {}
        metrics["Model"] = model
        metrics['Accuracy'] = accuracy_score(y_test, y_pred)
        metrics['Precision'] = precision_score(y_test, y_pred, average='weighted')
        metrics['Recall'] = recall_score(y_test, y_pred, average='weighted')
        metrics['F1 Score'] = f1_score(y_test, y_pred, average='weighted')
        metrics['MCC'] = matthews_corrcoef(y_test, y_pred)
        data_list.append(metrics)
    
    return pd.concat([results, pd.DataFrame(data_list)], ignore_index=True)

