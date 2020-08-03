# Fake Job Classification

## Introduction

The unemployment rate in the United States acording to the US Department of Labor as of June 2020 is at 11.1%¹. Although there are many factors causing contributing to the current unemployment rate, many people in the US and worldwide need to look for new jobs due to job loss and other financial hardships. As all of the job postings are done online now, most companies can directly post to job boards or have job data pulled from job aggregators. However, not all job postings are true job postings as some are fradulent job postings used to harvest data or other sensitive information towards desperate job seekers². Using the advances in natural learning processing, it should be possible to build a classifier to be able to detect potential fake jobs. This is an important task as many people will be applying for jobs online due to the current unemployment situation, and minimizing victims of scams due to fradulent job postings will be important for economic recovery.  

Using data gathered from the University of Aegean about various job postings from many different job sites, it should be possible to build some a classifer for potential fake job postings. Job posts typically are text rich with general job descriptions and typically some additional information such as telecommuting options and employment type. With all of these features, it should be possible to build a complex model using features from the job description using NLP or even more simple features with simplier models. This project will use three models and with the most simple model being the baseline model to compare against.  

1. Simple model using non-NLP features such as comparing correlations of job function to fraudulent postings  
2. Intermediate model using NLP tokenization features and modeling relationship of fraudent job postings using more traditional machine learning algorithms such as logistic regression or SVMs  
3. Complex model using state of the art transformer neural network models to predict fradulent job postings 

## Data Description
The dataset originally was downloaded from [kaggle](https://www.kaggle.com/shivamb/real-or-fake-fake-jobposting-prediction). The dataset hosted there is originally from the [University of Aegean](http://emscad.samos.aegean.gr/). This dataset is a publicly available dataset containing almost ~18,000 job ads with human classified fake jobs. This dataset is based on job ads published between 2012 and 2014. There are ~17000 true jobs and ~900 fake jobs in the dataset. The data was augmented using a variety of measures including synonymous adjectives and downsampling to deal with the class imbalances in the dataset.  


## System Requirements
NVIDIA GPU

## API
An API to serve the model can be found in the `fastapi` folder including instructions to run it.

## Models Tested
SVM
Logistic Regression
Random Forest
Roberta

## References

1. Bureau of Labor Statistics US Department of Labor. The Employment Situation - June 2020. Accessed 07/26/2020. https://www.bls.gov/news.release/pdf/empsit.pdf  
2. USC Career Center. Avoid Fradulent Job Postings. Accessed 07/26/2020. https://careers.usc.edu/students/find-a-job/avoid-fraudulent-job-postings/  
3. Rajapakse, Thilina. Simple Transformers - Introducing the Easiest Way To Use BERT, RoBERTa, XLNet, and XLM.Accessed 07/26/2020. https://towardsdatascience.com/simple-transformers-introducing-the-easiest-bert-roberta-xlnet-and-xlm-library-58bf8c59b2a3