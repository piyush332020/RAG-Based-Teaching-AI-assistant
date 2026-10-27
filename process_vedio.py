#convert the vedios to mp3
import os
import subprocess #converts vedio to audio

files=os.listdir("vedios")


for file in files:

    tutorial_number=file.split("-")[0]
    file_name="-".join(file.split("-")[1:-1])
    print(tutorial_number + " "+ file_name)
    subprocess.run(["ffmpeg" , "-i",f"vedios/{file}",f"audios_mp3/{tutorial_number}_{file_name}.mp3"])
    
