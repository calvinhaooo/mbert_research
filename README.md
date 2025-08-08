This is the code and result of Yinghao's project.

In the pretraining folder, you can find the script for pretraning.

In the fine-tune folder, the results are saved under each sub folder.

The HIV classification results are across three models. mbert, mbert-nl-bio and mbert-nl-clin.

In terms of NER, there are two folders: Romanian and Spanish.

Note: The results of Pharmaconer and the visualization of LIME, and embedding analysis are still in the platform. Need approval to be downloaded.

Missing points(all finished but its in the mydre platform):

1. The romanian experiment lacks of entity-level analysis and embedding analysis.
2. The Spanish NER lacks of Pharmaconer updated results, with embedding analysis.
3. The HIV classification lacks of the LIME analysis.


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
│         │              ├── bsc_bio_ehr_es
│         │              │         └── cantemist-ner
│         │              │             └── result
│         │              ├── evaluate_NER.ipynb
│         │              ├── mbert
│         │              │         └── cantemist-ner
│         │              │             └── result
│         │              ├── mbert-nl-clin
│         │              │         └── cantemist-ner
│         │              │             └── result
│         │              └── script
│         │                    ├── README.md
│         │                    ├── ner.sh
│         │                    └── run_ner.py
│         └── hiv_classification
│             ├── evaluation_hiv_classification.ipynb
│             ├── mbert
│             ├── mbert-nl-bio
│             └── mbert-nl-clin
└── pretrain
    ├── pretrain_corpus
    └── run_mlm.py
        
```