This folders include the scripts for Spanish NER datasets.

The ner.sh is creating automatically fine-tune the select model by using 10-fold cross-validation, which you can set the selected model name, model output path, etc.
The run_ner.py is the script for fine-tuning the model.

```
bash ner.sh [model_name] [dataset_name] [seed]
```
