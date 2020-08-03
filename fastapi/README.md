# FastAPI

## Introduction

This houses a basic API for the fraudulent job classifcation model. The API will return back real or fake depending on the inputs given. There are 4 parameters that can be adjusted including the company profile and job description. 

## Requirements
The pipfile contains all of the library requirements needed to run this api server. Additionally, `scikit-learn` needs to be `0.22.2.post1` as the models were pickled using that version.

## How to run
    uvicorn main:app --reload

### Endpoints
    
    /predict
    	company_profile - Company profile
    	description - Job Description
    	benefits - Job Benefits
    	requirements - Requirements for Job

### How to submit queries
    localhost:8000/predict/?company_profile='quack quack'&description="moo"&benefits="pet a dog"&requirements="human"