This is the code and result of Yinghao's project.

In the pretraining folder, you can find the script `run_mlm.py` for pretraning. 
```
python run_mlm.py \
    --model_name_or_path=BASE_MODEL_NAME \
    --output_dir=OUTPUT_DIR \
    --do_train \
    --do_eval \
    --validation_split_percentage=VALIDATION_SPLIT \
    --train_file=PATH_TO_CORPUS \
    --per_device_train_batch_size=TRAIN_BATCH_SIZE \
    --per_device_eval_batch_size=EVAL_BATCH_SIZE \
    --gradient_accumulation_steps=GRAD_ACCUM_STEPS \
    --learning_rate=LEARNING_RATE \
    --num_train_epochs=EPOCHS \
    --save_total_limit=MAX_CKPT \
    --save_strategy=steps \
    --save_steps=SAVE_INTERVAL \
    --line_by_line \
    --max_seq_length=MAX_SEQ_LEN \
    --eval_strategy=steps \
    --eval_steps=EVAL_INTERVAL \
    --fp16
```

In the fine-tune folder, the results are saved under each sub folder.

In terms of NER, there are two folders: Romanian and Spanish. 


Code 

```
├── README.md
├── fine_tune
│         ├── NER
│         │    ├── romanian
│         │    │         ├── evaluate_NER.ipynb
│         │    │         ├── mbert
│         │    │         ├── mbert-nl-clin
│         │    │         ├── mbert-nl-ro
│         │    │         ├── mbert-ro-bio
│         │    │         └── script
│         │    │             ├── README.md
│         │    │             ├── dataset
│         │    │             ├── run_ft.py
│         │    │             └── run_ner.py
│         │    └── spanish
│         │              ├── evaluate_NER.ipynb
│         │              ├── mbert
│         │              │         └── cantemist-ner
│         │              │             └── result
│         │              ├── mbert-nl-clin
│         │              │         └── cantemist-ner
│         │              │             └── result
│         │              ├── bsc_bio_ehr_es
│         │              │         └── cantemist-ner
│         │              │             └── result
│         │              └── script
│         │                    ├── README.md
│         │                    ├── ner.sh
│         │                    └── run_ner.py
│         └── hiv_classification               
│                   ├── evaluation_hiv_classification.ipynb
│                   └── result                     
│                        ├── mbert
│                        ├── mbert-nl-bio
│                        └── mbert-nl-clin
└── pretrain
    ├── pretrain_corpus
    └── run_mlm.py
        
```
