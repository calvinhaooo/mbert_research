import os
import shutil

base_dir = "."
results_dir = os.path.join(base_dir, "result")

os.makedirs(results_dir, exist_ok=True)

for fold in range(10):
    fold_name = f"fold-{fold}"
    src_file = os.path.join(base_dir, fold_name, "seed-42", "predict_results.json")
    dst_file = os.path.join(results_dir, f"predict_fold_{fold}_results.json")

    if os.path.exists(src_file):
        shutil.copyfile(src_file, dst_file)
        print(f"Copied: {src_file} → {dst_file}")
    else:
        print(f"Missing: {src_file}")
