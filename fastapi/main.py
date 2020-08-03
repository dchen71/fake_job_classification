from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer
from joblib import dump, load
import pandas as pd
import numpy as np
import os
import spacy
from tokenizer import tokenizer # Deal with cross pickle tokenization issues

app = FastAPI(title = "Ensemble Fake Job Classifier",
	description = "Classifies if a job is fake given company profile, job description, benefits description, and requirements.",
	version = "0.0.1")

# Prediction model using training data
def predict_svm(x_test, var):
  """
  Inputs:
  x_test: Validation/testing dataset
  var: Variable in training dataset to tokenize against

  Outputs:
  Predicted values
  """
  cv = load(os.path.join('models', 'cv_' + var + '.joblib'))
  svc = load(os.path.join('models', 'svc_' + var + '.joblib'))
  cv_preds = cv.transform(x_test)
  svc_preds = svc.predict(X = cv_preds)
  return(svc_preds)

# Ensemble model by summing predictions and using cutoff of 2 for these 4 classes
def predict_ensemble(x_test):
  """
  Inputs:
  x_test: Validation/testing dataset

  Outputs:
  Predicted value based on equally weighted predictions(n>2 = 1)
  """
  preds = np.zeros(4)
  preds[0] = predict_svm(x_test["company_profile"], "company_profile")
  preds[1] = predict_svm(x_test["description"], "description")
  preds[2] = predict_svm(x_test["benefits"], "benefits")
  preds[3] = predict_svm(x_test["requirements"], "requirements")
  return((int(preds.sum()) > 2) * 1) # Get the row based sums of predictions

# Heartbeat
@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Prediction GET endpoint
@app.get("/predict/")
async def predict_job(company_profile: str = None, requirements: str = None, benefits: str = None, description: str = None):
    x_test = pd.DataFrame({'company_profile': company_profile, 'requirements': requirements, 'benefits': benefits, 'description': description}, index=[0])
    pred = predict_ensemble(x_test)
    pred = "Real" if pred == 0 else "Fraudulent"
    return {"prediction": pred}