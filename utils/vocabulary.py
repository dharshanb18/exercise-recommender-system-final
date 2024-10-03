import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display, Markdown

# Function to evaluate a sentence and extract score and remark
def evaluate_sentence(sentence):
    print("exercise on vocabulary")
    genai.configure(api_key="AIzaSyA8Wsh5G0Coz5Mx1-FDcmX0I5uGrwcr6gc")

    prompt = f"This is my sentence: '{sentence}'. I need a score out of 100 and a remark, just a few words like 'suggest this word can be this word'. in the format score:<just the score like 50,70>, remark:<remark>"

    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    response = model.generate_content(prompt)
    response_text = response.text
    print("response", response_text)

    score = None
    remark = None
    #we need to extract score and remark from response
    if 'score:' in response_text.lower():
        score = response_text.split('score:')[-1].strip().split()[0].rstrip(',')

    if 'remark:' in response_text.lower():
        remark = response_text.split('remark:')[-1].strip()

    print(f"Score: {score}")
    print(f"Remark: {remark}")

    return score, remark


# sentence = input("Enter a sentence: ")
# score, remark = evaluate_sentence(sentence)

# # Print the score and remark
# print(f"Score: {score}")
# print(f"Remark: {remark}")
