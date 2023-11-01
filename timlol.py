from faster_whisper import WhisperModel
import os,time


# FILE_NAME = "nuriel_gabay_18.10.23_part2"

model = WhisperModel("large-v2", device="cuda", compute_type="auto")

DIR_TO_SCAN = "Toomlal"
DIRS = os.walk(f"C:\\Users\\userx\\Desktop\\PROJECTS\\war\\{DIR_TO_SCAN}")
LS = [i for i in DIRS]
print(LS)
FILES = LS[0][2]
print(f"files: {FILES}")

def trans(file_name):
    result = model.transcribe(audio= f"C:\\Users\\userx\\Desktop\\PROJECTS\\war\\{DIR_TO_SCAN}\\{file_name}",
                            condition_on_previous_text=False,no_speech_threshold=0.4,
                            vad_filter=True,beam_size=7,patience=7,language='he')

    final_timlool = ""

    with open(f"war/{DIR_TO_SCAN}/{file_name.replace('.mp3','')}.txt",'a',encoding='utf-8') as f:
        for i in result[0]:
            print(i[4])
            final_timlool += str(i[4]) + "\n"
        # print(final_timlool)
        f.write(final_timlool)
    


for file in FILES:
    trans(file)





'''

                        ####################### SETUP ##########################

# pip install -U openai-whisper OR pip install faster-whisper

# Uninstall pytorch
# from faster_whisper import WhisperModel
# pip3 uninstall torch torchvision torchaudio
# pip 3 cache purge
# Install cuda-python and Torch cuda
# pip install cuda-python

# To install pytorch you can choose your version from the pytorch website https://pytorch.org/ see INSTALL PYTORCH section

# pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118



'''
# model = whisper.load_model("base")

# # load audio and pad/trim it to fit 30 seconds
# audio = whisper.load_audio("C:\\Users\\userx\\Desktop\\PROJECTS\\war\\abc1.mp3")
# audio = whisper.pad_or_trim(audio)

# # make log-Mel spectrogram and move to the same device as the model
# mel = whisper.log_mel_spectrogram(audio).to(model.device)

# # detect the spoken language
# _, probs = model.detect_language(mel)
# print(f"Detected language: {max(probs, key=probs.get)}")

# # decode the audio
# options = whisper.DecodingOptions()
# result = whisper.decode(model, mel, options)

# # print the recognized text
# print(result.text)


############ OPTIONAL ALTERNATIVE ########################


#### model = WhisperModel("whisper-large-v2-ct2")
# mod = whisper.load_model("large-v2",device="cuda")
# res = mod.transcribe(audio= "C:\\Users\\userx\\Desktop\\PROJECTS\\war\magav1.mp3")


# print(final_timlool)
    #f.write(final_timlool)
        # f.write("\n")

        # if prev != i[4]:
        #     print(i[4])
        #     f.write(str(i[4])+"\n")
        # prev = i[4]