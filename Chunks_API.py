import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("WHISPER_API_KEY"))

# Ensure destination directory exists
os.makedirs("jsons", exist_ok=True)

audios = os.listdir("vedios_mp3")

for audio in audios:
    print(f"Processing: {audio}")
    number = audio.split("_")[0]
    title = audio.split("_")[1]  

    file_path = f"vedios_mp3/{audio}"

    # Call OpenAI API to translate speech into English text
    with open(file_path, "rb") as audio_file:
        result = client.audio.translations.create(
            model="whisper-1",
            file=audio_file,
            response_format="verbose_json",  # Required to get segment timestamps
        )

    chunks = []
    # Loop over translated segments
    for segment in result.segments:
        # segment objects use dot notation in the OpenAI Python SDK
        chunks.append(
            {
                "number": number,
                "title": title,
                "start": round(segment.start, 2),
                "end": round(segment.end, 2),
                "text": segment.text,
            }
        )

    chunks_with_meta_data = {"chunks": chunks, "text": result.text}

    # Save to JSON file
    with open(f"jsons/{title}.json", "w", encoding="utf-8") as f:
        json.dump(chunks_with_meta_data, f, indent=4)
