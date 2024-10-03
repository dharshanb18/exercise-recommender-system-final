import textwrap
import google.generativeai as genai
from IPython.display import display, Markdown
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import os
import urllib.parse

# format the text as Markdown as I did run this is colab a few times
def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def download_images(query):
    query_encoded = urllib.parse.quote(query)
    url = f'https://www.google.com/search?hl=en&tbm=isch&q={query_encoded}'

    os.makedirs('downloaded_images', exist_ok=True)

    try:
        htmldata = urlopen(url)
        soup = BeautifulSoup(htmldata, 'html.parser')
        images = soup.find_all('img')

        # Limit to top 5 images
        downloaded_images = []
        for index, item in enumerate(images[:5]):  # Get only the first 5 images
            img_url = item.get('src')

            # Handle relative URLs
            if img_url and img_url.startswith('/'):
                img_url = url + img_url

            if img_url:  # Check if the URL is valid
                try:
                    # Create a filename based on the index
                    filename = os.path.join('downloaded_images', f'image_{index + 1}.jpg')
                    urlretrieve(img_url, filename)
                    downloaded_images.append(filename)
                    print(f'Downloaded {filename}')
                except Exception as e:
                    print(f'Failed to download {img_url} - {e}')
        return downloaded_images
    except Exception as e:
        print(f'Failed to open URL {url} - {e}')
        return []

#this function will generate grammar exercise
def grammar_que(details):
    print("Exercise for grammar")
    
    interest = details.split(',')[-1]  
    print(f"Scraping images related to: {interest}")
    
    downloaded_images = download_images(interest)

    genai.configure(api_key="your api")

    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            #print(m.name)
            pass

    model = genai.GenerativeModel('gemini-1.5-flash-8b-exp-0924')

    prompt = f"Generate a single intermediate level grammar fill-in-the-blanks question using gaps for grammatical words such as Articles, Prepositions, Conjunctions, Pronouns, Auxiliary Verbs, Determiners, or Interjections. Relate the question to a general interest of this person '{details}', avoiding focus on specific personal details like age or name. Use 1 or 2 blanks to represent missing grammatical words, and ensure it tests common grammatical knowledge. Example: This ____ a popular sitcom, and many people ____ fans of the show. ____ has been on air for many years, and it still ____ watched by millions."

    response = model.generate_content(prompt)
    fill_up_text = response.text
    print(fill_up_text)

    question = fill_up_text.strip()
    return question

# validate the answer's grammar and provide feedback
def validate_grammar(question, answers):
    filled_question = question.replace("____", answers)  # Insert answers directly

    prompt = f"""
    Please evaluate the following sentence for grammar and fluency:

    Question: "{question}"
    Answers: "{answers}"

    Insert the answers into the question to check grammar and fluency. If the sentence is grammatically correct and natural, give a score of 100 and a short, positive remark, reply only this "score:<score just that number like 50 or 70>, remarks:<remarks few words>".
    """

    model = genai.GenerativeModel('gemini-1.5-flash-002')
    response = model.generate_content(prompt)

    response_text = response.text
    print(response_text)  # Debugging purposes

    score_line = None
    remarks_line = None

    if 'score:' in response_text.lower():
        try:
            # Split by comma and clean up whitespace
            parts = response_text.split(',')
            score_line = parts[0].split(':')[1].strip()  # Get score
            remarks_line = parts[1].split(':')[1].strip()  # Get remarks
            score_line = int(score_line)  # Convert score to integer
        except (ValueError, IndexError):
            # Handle any parsing errors gracefully
            return "There was an error processing the score and remarks."

    if score_line is None or remarks_line is None:
        return "The response format was not as expected."

    return score_line, remarks_line

# if __name__ == "__main__":
#     details = "age 21, usa, like sports"
    
#     question = grammar_que(details)  # Get fill-up question from the first function
#     answers = input("Enter your answers in the form of a string (e.g., 'is, is, on'): ")

#     # Call the function to validate your answers and get feedback
#     score_line, remarks_line = validate_grammar(question, answers)

#     # Print the extracted score and remarks
#     print("Score:", score_line)
#     print("Remarks:", remarks_line)
