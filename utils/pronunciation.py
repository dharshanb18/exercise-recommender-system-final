import os
import librosa
import difflib
import pronouncing
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch

model_dir = r"C:\Users\DHARSHAN BALAJI\Downloads\objdetectioproject\grammar project\model weights\wav2vec2_processor"

if not os.path.exists(model_dir):
    raise FileNotFoundError(f"Model directory does not exist: {model_dir}")

try:
    processor = Wav2Vec2Processor.from_pretrained(model_dir)
    model = Wav2Vec2ForCTC.from_pretrained(model_dir)
    print("Model and processor loaded successfully.")
except Exception as e:
    raise RuntimeError(f"Failed to load model or processor: {e}")

def load_audio(file_path):
    speech, sr = librosa.load(file_path, sr=16000)
    return speech, sr

def transcribe_audio(file_path):
    speech, sr = load_audio(file_path)

    # Processing the speech
    input_values = processor(speech, return_tensors="pt", sampling_rate=sr).input_values
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)

    # Decoding the transcription
    transcription = processor.decode(predicted_ids[0])
    return transcription

def get_phonemes(word):
    # Get phonemes
    phoneme_list = pronouncing.phones_for_word(word.lower())
    if phoneme_list:
        return phoneme_list[0].split()
    return []

def compare_phonemes(reference_text, transcribed_text):
    ref_phonemes = [get_phonemes(word) for word in reference_text.split()]
    trans_phonemes = [get_phonemes(word) for word in transcribed_text.split()]

    errors = 0
    error_details = []

    for ref, trans in zip(ref_phonemes, trans_phonemes):
        # Compare phonemes for each word
        if ref != trans:
            errors += 1
            error_details.append(f"Pronunciation error: Expected {ref}, but got {trans}")

    return errors, error_details

# main function it incorporates all others
def check_pronunciation(file_path, reference_text):
    remarks = transcribe_audio(file_path)
    print(f"Transcribed Text: {remarks}")

    # Compare with the reference text
    errors, error_details = compare_phonemes(reference_text, remarks)
    print(f"Total pronunciation errors: {errors}")

    # Calculate score
    total_words = len(reference_text.split())
    score = max(0, (total_words - errors) / total_words * 100)
    print(f"Score: {score:.2f} / 100")
    return int(score),remarks

# # Example usage
# audio_path = r"C:\Users\DHARSHAN BALAJI\Downloads\Recording.wav"  # Replace with your audio file path
# reference_text = "AS I TOLD THAT IT WAS A VERY GOOD INFORMATION FOR world"  # Replace with your reference text

# check_pronunciation(audio_path, reference_text)
