import subprocess

num_folds = 10  # The number of folds


# customize your model_path and output_base_dir
model_path = ""
output_base_dir = ""
train_file = "dataset/ner_data.json"
label_column_name = "ner_tags"

for fold in range(num_folds):
    cmd = [
        "python", "run_ner.py",
        "--model_name_or_path", model_path,
        "--output_dir", output_base_dir,
        "--fold", str(fold),
        "--label_column_name", label_column_name,
        "--train_file", train_file,
        "--do_train",
        "--do_predict",
        "--overwrite_output_dir", "True",
        "--num_train_epochs", "15",
        "--seed", "42",
        "--per_device_train_batch_size", "16",
        "--gradient_accumulation_steps", "2",
        "--learning_rate", "2e-5",
        "--text_column_name", "words"
    ]

    print(f"Running fold {fold}...")
    subprocess.run(cmd, check=True)