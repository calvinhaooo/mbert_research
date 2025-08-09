This is the code and result of Yinghao's project.

In the pretraining folder, you can find the script for pretraning.

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
