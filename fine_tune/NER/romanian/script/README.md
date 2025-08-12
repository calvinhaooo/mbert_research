This folder includes the script for Romanian NER dataset

You can customize the model for fine-tuning by using 10-folds cross-validation, and the model output path.
The run_ner is the script for NER task. In addition, you can adjust the parameter of training.

```
python run_ft.py
```

Note: The path of dataset should be also changed in the run_ner.py if it is not dataset/ner_data.json

```
test_splits = datasets.load_dataset(path="json",
                                    data_files="dataset/ner_data.json",
                                    split=[f'train[{k}%:{k + 10}%]' for k in range(0, 100, 10)])
train_splits = datasets.load_dataset(path="json",
                                     data_files="dataset/ner_data.json",
                                     split=[f'train[:{k}%]+train[{k + 10}%:]' for k in range(0, 100, 10)])
```
