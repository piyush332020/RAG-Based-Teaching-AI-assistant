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
    embeddings=r.json()["embeddings"]
    return embeddings
# print(create_embeddings("my name is piyush"))

jsons=os.listdir("jsons")
my_dict=[]
chunk_id=0
for json_file in jsons:
    with open(f"jsons/{json_file}") as f:
        content =json.load(f)
    text=[c['text'] for c in content['chunks']]
    embedding=create_embeddings(text)
    for i, chunk in enumerate(content['chunks']):
        chunk['chunk_id']=i
        chunk['embedding']=embedding[i]
        my_dict.append(chunk)
df=pd.DataFrame.from_records(my_dict)
#save this dataframe df
joblib.dump(df,'embeddings.joblib')

print("done")