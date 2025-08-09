---
library_name: transformers
license: apache-2.0
base_model: bert-base-multilingual-cased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: model_output_ro
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# model_output_ro

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4683
- Accuracy: 0.8954

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 5.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step  | Validation Loss | Accuracy |
|:-------------:|:------:|:-----:|:---------------:|:--------:|
| 1.1435        | 0.1914 | 500   | 0.8347          | 0.8234   |
| 0.9866        | 0.3828 | 1000  | 0.7380          | 0.8408   |
| 0.9251        | 0.5743 | 1500  | 0.6879          | 0.8504   |
| 0.8688        | 0.7657 | 2000  | 0.6606          | 0.8570   |
| 0.8492        | 0.9571 | 2500  | 0.6327          | 0.8633   |
| 0.8117        | 1.1485 | 3000  | 0.6011          | 0.8684   |
| 0.7849        | 1.3400 | 3500  | 0.5780          | 0.8715   |
| 0.7526        | 1.5314 | 4000  | 0.5760          | 0.8737   |
| 0.7465        | 1.7228 | 4500  | 0.5667          | 0.8741   |
| 0.7347        | 1.9142 | 5000  | 0.5537          | 0.8775   |
| 0.7185        | 2.1057 | 5500  | 0.5349          | 0.8822   |
| 0.7098        | 2.2971 | 6000  | 0.5217          | 0.8837   |
| 0.709         | 2.4885 | 6500  | 0.5155          | 0.8851   |
| 0.6898        | 2.6799 | 7000  | 0.5152          | 0.8853   |
| 0.6839        | 2.8714 | 7500  | 0.4977          | 0.8879   |
| 0.6721        | 3.0628 | 8000  | 0.4966          | 0.8882   |
| 0.6662        | 3.2542 | 8500  | 0.4887          | 0.8906   |
| 0.656         | 3.4456 | 9000  | 0.4841          | 0.8911   |
| 0.6563        | 3.6371 | 9500  | 0.4904          | 0.8902   |
| 0.65          | 3.8285 | 10000 | 0.4811          | 0.8925   |
| 0.6456        | 4.0199 | 10500 | 0.4713          | 0.8946   |
| 0.6326        | 4.2113 | 11000 | 0.4789          | 0.8929   |
| 0.6339        | 4.4028 | 11500 | 0.4752          | 0.8935   |
| 0.632         | 4.5942 | 12000 | 0.4712          | 0.8955   |
| 0.6241        | 4.7856 | 12500 | 0.4698          | 0.8941   |
| 0.6275        | 4.9770 | 13000 | 0.4673          | 0.8949   |


### Framework versions

- Transformers 4.49.0
- Pytorch 2.0.1+cu118
- Datasets 3.0.0
- Tokenizers 0.21.1
