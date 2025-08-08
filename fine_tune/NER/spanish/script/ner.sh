#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

model_name=$1
dataset_name=$2
seed=$3

for fold in {0..9}
do
    output_dir=output/model-$model_name/dataset-$dataset_name/fold-$fold/seed-$seed
    mkdir -p $output_dir

    python3 $SCRIPT_DIR/ner/run_ner.py \
        --model_name_or_path $model_name \
        --dataset_name $dataset_name \
        --fold $fold \
        --do_train \
        --do_eval \
        --do_predict \
        --per_device_train_batch_size 4 \
        --gradient_accumulation_steps 4 \
        --num_train_epochs 10 \
        --save_strategy no \
        --overwrite_output_dir \
        --seed $seed \
        --report_to none \
        --return_entity_level_metrics True \
        --logging_dir $output_dir/tb \
        --output_dir $output_dir 2>&1 | tee $output_dir/train.log
done
