import whisper #convert audio to text
import json
import os

model = whisper.load_model("large-v2") # best model for transcript
audios=os.listdir("vedios_mp3")
for audio in audios:
    print(audio)
    number=audio.split("_")[0]
    title=audio.split("_")[1][:-4]
    # result=model.transcribe(audio="vedios_mp3/0_practise.mp3"
    result=model.transcribe(audio=f"vedios_mp3/{audio}",language="hi",task="translate",word_timestamps=False)

    chunks=[]
    for segment in result["segments"]:
        chunks.append({"number": number,"title":title,"start":segment["start"],"end":segment["end"],"text":segment["text"]})
    chunks_with_meta_data={"chunks":chunks,"text":result["text"]}
    print(chunks)
    with open(f"jsons/{title}.json","w") as f:
        json.dump(chunks_with_meta_data,f)

