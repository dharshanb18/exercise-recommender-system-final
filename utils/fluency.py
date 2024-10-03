import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import detect_silence

def analyze_audio_pauses(audio_file):

    audio = AudioSegment.from_file(audio_file)

    # Detect silence
    silence_threshold = -50 
    silence_duration_ms = 700 
    silences = detect_silence(audio, min_silence_len=silence_duration_ms, silence_thresh=silence_threshold)

    #number of pauses
    pause_count = len(silences)

    pause_durations = [(start / 1000, end / 1000) for start, end in silences]  # Convert to seconds

    return pause_count, pause_durations

def calculate_score(pause_count, sentence):
    word_count = len(sentence.split())  # Count words in the provided sentence

    if word_count == 0:
        return 0
    
    if pause_count == 0:
        return 100
    elif pause_count == 1:
        return 90
    elif pause_count == 2:
        return max(75, 100 - (pause_count * 10) - (word_count // 5))
    else:
        # For more than 2 pauses, decrease score more aggressively
        return max(0, 100 - (pause_count * 10) - (word_count // 5))

def analyze_fluency(sentence, audio_file):
    pause_count, pause_durations = analyze_audio_pauses(audio_file)
    score = calculate_score(pause_count, sentence)
    remarks = f"Pause durations (start, end in seconds): {pause_durations}"
    return score, remarks

# # Example usage
# audio_file_path = r"C:\Users\DHARSHAN BALAJI\Downloads\Recording.wav"
# sentence = "This will give us an idea of overall well-being of the human nation."

# # Get fluency score and remarks
# score, remarks = analyze_fluency(sentence, audio_file_path)
# print(f"Score: {score}/100")
# print(f"Remarks: {remarks}")
