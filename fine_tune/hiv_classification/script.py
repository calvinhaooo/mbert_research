import pandas as pd
import random
from simpletransformers.classification import ClassificationModel, ClassificationArgs
import numpy as np
import os
from sklearn.metrics import classification_report
from scipy.special import softmax
import torch
from copy import deepcopy

cls_args = ClassificationArgs(num_train_epochs=5,
                              save_model_every_epoch=False,
                              save_eval_checkpoints=False,
                              save_steps=-1,
                              use_multiprocessing=False,
                              use_multiprocessing_for_evaluation=False,
                              sliding_window=True,
                              stride=0.8,
                              learning_rate=2e-5,
                              loss_type='focal',
                              loss_args={
                              'alpha': 0.8,
                              'gamma': 2,
                              'reduction': 'mean',
                              'ignore_index':-100,
                              },
                              max_seq_length=512,
                              overwrite_output_dir=True,
                              reprocess_input_data=True,
                              manual_seed=42,)

os.environ['TOKENIZERS_PARALLELISM'] = "false"

cls_args.logging_dir = 'logs'

test = pd.read_csv('dataset/test.csv')


test = test.rename(columns={'flag': 'labels'})

labels = test['labels'].to_numpy()

for fold in range(10):
    print(f"\n =========== fold {fold} ==========")

    
    model_args = deepcopy(cls_args)

    model_args.output_dir = f"model_name/fold_{fold}/"
    os.makedirs(model_args.output_dir, exist_ok = True)

    model = ClassificationModel(model_type='model_type', model_name='model_name', num_labels=2, use_cuda=True, args=model_args)
    train = pd.read_csv(f'dataset/cv_splits/fold_{fold}_train.csv')
    train = train.rename(columns={'flag': 'labels'})
    val = pd.read_csv(f'dataset/cv_splits/fold_{fold}_eva.csv')
    val = val.rename(columns={'flag': 'labels'})


    train_exc = train[train['labels'] == 0]
    train_inc = train[train['labels'] == 1]


    downsampled = train_exc.sample(n=len(train_inc), replace=False, random_state=24)
    print(f"The length of downsampled:",len(downsampled))
    train = pd.concat([downsampled, train_inc])

    train = train.sample(frac=1, random_state=24).reset_index(drop=True)

    model.train_model(train, eval_df = val)
    model.eval_model(test)
    model.args.sliding_window = False

    test_entries = test['text'].tolist()
    predictions, raw_output = model.predict(test_entries)
    probs = softmax(raw_output, axis = 1)
    probs_class1 = probs[:,1]
