import os
import pandas as pd
import numpy as np
from utils import grammar,vocabulary,pronunciation,fluency

def get_user_details():
    age = input("Enter your age: ")
    country = input("Enter your country: ")
    interests = input("Enter your interests: ")
    return age, country, interests

# Function to calculate the category with the least average score from the previous 3 batches
def select_exercise_category(batch_data):
    #average score for each category over the last 3 rows
    avg_scores = np.mean(batch_data, axis=0)
    least_category_index = np.argmin(avg_scores)
    categories = ['Grammar_Score', 'Vocabulary_Score', 'Pronunciation_Score', 'Fluency_Score']
    least_category = categories[least_category_index]
    return least_category, avg_scores[least_category_index]

# Function to log results in a CSV file
def log_exercise_result(exercise_number, category, score, remarks):
    # result_path = os.path.join("data", "exercise_res.csv")
    result_path = r'C:\Users\DHARSHAN BALAJI\Downloads\objdetectioproject\grammar project\data\exercise_res.csv'
    
    # Append results to the CSV file
    df = pd.DataFrame([[exercise_number, category, score, remarks]], 
                      columns=["Exercise Number", "Category", "Score", "Remarks"])
    df.to_csv(result_path, mode='a', header=not os.path.exists(result_path), index=False)


model_dir = r"C:\Users\DHARSHAN BALAJI\Downloads\objdetectioproject\grammar project\model weights\wav2vec2_processor"


def main():
    print("Welcome to the Language Assessment System!")
    
    # Get user details
    age, country, interests = get_user_details()
    details = f"Age: {age}, Country: {country}, Interest: {interests}"
    # Load data from utterance_data.xls
    data_path = r'C:\Users\DHARSHAN BALAJI\Downloads\objdetectioproject\grammar project\data\utterance_data.xlsx'
    df = pd.read_excel(data_path)

    # Process the data batch by batch (3 rows per batch, for 10 batches)
    num_batches = 10
    batch_size = 3
    threshold_offset = 5

    for batch_num in range(num_batches):
        print(f"\nProcessing batch {batch_num + 1}...")

        # Get the last 3 rows for the current batch
        start_row = batch_num * batch_size
        batch_data = df.loc[start_row:start_row + batch_size - 1, ['Grammar_Score', 'Vocabulary_Score', 'Pronunciation_Score', 'Fluency_Score']]
        
        # Select the category with the least average score
        category, avg_score = select_exercise_category(batch_data)
        print(f"Selected category: {category} with average score: {avg_score}")

        # Set threshold for stopping the exercise
        threshold = avg_score + threshold_offset

        # Continue the exercise for the selected category until score exceeds the threshold
        exercise_finished = False
        exercise_number = batch_num + 1

        while not exercise_finished:
            if category == 'Grammar_Score':  # Grammar exercise
                
                question=grammar.grammar_que(details=details)
                answers = input("Enter your answers in the form of a string (e.g., 'is, is, on'): ")

                score,remark = grammar.validate_grammar(question, answers)
                log_exercise_result(exercise_number, "Grammar", score, remark)

            elif category == 'Vocabulary_Score':  # Vocabulary exercise
                # print("vocabulary exercise")
                
                sentence=input("enter the sentence please for vocabulary check")
                score1,remark1=vocabulary.evaluate_sentence(sentence=sentence)
                log_exercise_result(exercise_number, "Vocabulary", score1, remark1)

            elif category == 'Pronunciation_Score':  # Pronunciation exercise
                print("Pronunciation exercise")
                pron_ref_sentence=input("enter the pronunciation reference sentence that you are going to repeat")
                pronun_filepath=input("enter the audio file for pronunciation check")
                score2,remark2=pronunciation.check_pronunciation(pronun_filepath,pron_ref_sentence)
                log_exercise_result(exercise_number, "Pronunciation", score2, remark2)

            elif category == 'Fluency_Score':  # Fluency exercise
                print("Fluency exercise")
                fluen_ref_sentence=input("enter the fluency reference sentence that you are going to repeat")
                pronun_filepath=input("enter the audio file for fluency check")
                score3,remark3=fluency.analyze_fluency(fluen_ref_sentence,pronun_filepath)
                log_exercise_result(exercise_number, "Fluency", score3, remark3)

            # Check if the score exceeds the threshold
            if score > threshold+5:
                print(f"Exercise for {category} completed with score {score}, exceeding the threshold of {threshold}.")
                exercise_finished = True

if __name__ == "__main__":
    main()
