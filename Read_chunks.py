import requests
import os
import json
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

import joblib

def create_embeddings(text_list):
    r=requests.post("http://127.0.0.1:11434/api/embed",json={
        "model":"bge-m3",
        "input":text_list
    })
    print("Status:", r.status_code)
    print("Response:", r.text)
    embeddings=r.json()["embeddings"]
    return embeddings
# print(create_embeddings("my name is piyush"))

jsons=os.listdir("jsons")
my_dict=[]
chunk_id=0
for json_file in jsons:
    with open(f"jsons/{json_file}") as f:
        content =json.load(f)
    text = [c['text'] for c in content['chunks']]

    batch_size = 200

    for start in range(0, len(text), batch_size):

        end = min(start + batch_size, len(text))

        batch_text = text[start:end]

        print(f"Processing chunks {start + 1} to {end}")

        embedding = create_embeddings(batch_text)

        for i, emb in enumerate(embedding):

            chunk = content['chunks'][start + i]

            chunk['chunk_id'] = chunk_id
            chunk['embedding'] = emb

            my_dict.append(chunk)

            chunk_id += 1
df=pd.DataFrame.from_records(my_dict)
#save this dataframe df
joblib.dump(df,'embeddings.joblib')

# print("done")