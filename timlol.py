import whisper,os
from faster_whisper import WhisperModel
# model = WhisperModel("whisper-large-v2-ct2")
model = WhisperModel("large-v2", device="cuda", compute_type="auto")
result = model.transcribe("C:\\Users\\userx\\Desktop\\PROJECTS\\war\milooyim.wav")

with open("timlool.txt",'a') as f:
    for i in result[0]:
        print(i[4])
        f.write(i[4]+"\n")

'''

                        ####################### SETUP ##########################

# pip install -U openai-whisper OR pip install faster-whisper

# Uninstall pytorch

# pip3 uninstall torch torchvision torchaudio
# pip 3 cache purge
# Install cuda-python and Torch cuda
# pip install cuda-python

# To install pytorch you can choose your version from the pytorch website https://pytorch.org/ see INSTALL PYTORCH section

# pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
# # import whisper

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
