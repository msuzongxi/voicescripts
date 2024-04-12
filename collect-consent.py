import os
from datetime import datetime
import pandas as pd

uuids = []
src_folder = "/home/azureuser/projects/voice/consent/"
for f in os.listdir(src_folder):
    file_path = src_folder + f
    created_date = datetime.fromtimestamp(os.path.getctime(file_path))
    uuid = f.replace(".txt", "")
    if not f.endswith('.txt'):
        continue
    if created_date > datetime(2024, 3, 1):
        with open(file_path, 'r') as file:
            content = file.read().replace("\n", "").replace("\r", "")
            uuids.append([uuid, content])
df = pd.DataFrame(uuids, columns=["uuid", "qidx"])
df.to_csv(src_folder+"consent.csv", index=False)

