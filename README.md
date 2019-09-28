# Classification and Named Entity Recognition

## Description 

- `Train a deep learning model on a question dataset to classify them and also extract entities.`

## Requirements

- `python3`
- `pip3 install -r requirements.txt`



## Run

- `To train classification : python -W ignore train.py`
- `To predict user input data : python -W ignore run_sample_predict.py `


## Result

### Validation Data
```
        Validation accuracy : 0.8256
```
### Test Data
```
        Test accuracy :  0.8249

               precision    recall  f1-score   support

        DESC       0.70      0.90      0.79       238
        ENTY       0.80      0.69      0.74       265
         HUM       0.94      0.82      0.87       236
         LOC       0.85      0.88      0.86       153
         NUM       0.94      0.88      0.91       182

    accuracy                           0.82      1074
   macro avg       0.84      0.83      0.83      1074
weighted avg       0.84      0.82      0.83      1074

```
### Sample Output
```
        INPUT :  What caused the death of Bob Marley ?
        OUTPUT: 
                {'category': 'DESC',
                 'entites': {'PER': {'end': 35, 'name': 'Bob Marley', 'start': 25}}}

```
