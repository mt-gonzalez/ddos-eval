import os
import shutil
from pathlib import Path
import kagglehub

raw_data_path = Path("./data/raw/")
raw_data_path.mkdir(parents=True, exist_ok=True)

try:
    kagglehub.dataset_download("aymenabb/ddos-evaluation-dataset-cic-ddos2019", output_dir=str(raw_data_path))
except FileExistsError:
    kagglehub.dataset_download("aymenabb/ddos-evaluation-dataset-cic-ddos2019", output_dir=str(raw_data_path), force_download=True)

temp_path = "./data/raw/.complete/"
if os.path.exists(temp_path) :
    shutil.rmtree(temp_path)

old_path = "./data/raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"
new_path = "./data/raw/CIC-DDos2019.csv"

try:
    os.rename(old_path, new_path)
    print("File successfully renamed.")
except FileNotFoundError:
    print("Error: The source file could not be found.")
except FileExistsError:
    print("Error: A file with the new name already exists.")