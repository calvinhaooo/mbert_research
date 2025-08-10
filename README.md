This is the code and result of Yinghao's project.

In the fine-tune folder, the results are saved under each sub folder, which includes HIV classification and NER(Spanish, Romanian)

In terms of NER, there are two folders: Romanian and Spanish. You can find the entity_level_NER.ipynb and result_reasoning.ipynb in `Romanian` folder. This provides the results of Romanian NER. The script is under this folder `fine_tune/NER/romanian/script/README.md`


In Spanish, you can find the entity level discussion in evaluate_es_NER.ipynb nad embedding_analysis.ipynb. You can find the script for Spanish NER under this folder: `fine_tune/NER/spanish/script/README.md`



The structure of this project can be visualized as below:
```
├── README.md
├── fine_tune
│         ├── NER
│         │    ├── romanian
│         │    │         ├── evaluate_NER.ipynb
│         │    │         ├── entity_level_NER.ipynb
│         │    │         ├── result_reasoning.ipynb
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
│         │              ├── embedding_analysis.ipynb
│         │              ├── evaluate_es_NER.ipynb
│         │              ├── mbert
│         │              │         └── cantemist-ner
│         │              │             └── result
│         │              │         └── pharmaconer
│         │              │             └── result
│         │              ├── mbert-nl-clin
│         │              │         └── cantemist-ner
│         │              │             └── result
│         │              │         └── pharmaconer
│         │              │             └── result
│         │              ├── bsc_bio_ehr_es
│         │              │         └── cantemist-ner
│         │              │             └── result
│         │              │         └── pharmaconer
│         │              │             └── result
│         │              └── script
│         │                    ├── README.md
│         │                    ├── ner.sh
│         │                    └── run_ner.py
│         └── hiv_classification               
│                   ├── evaluation_hiv_classification.ipynb
│                   ├── lime_analysis.ipynb
│                   └── result                     
│                        ├── mbert
│                        ├── mbert-nl-bio
│                        └── mbert-nl-clin
└── pretrain
    └── run_mlm.py
        
```


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
