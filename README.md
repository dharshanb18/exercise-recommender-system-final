# exercise-recommender-system-final

**How to choose a category?**
As I consider previous 3 utterances each has 4 categories and each has feedback score 
as follows

Grammar_Score	Vocabulary_Score	Pronunciation_Score	Fluency_Score
80	80	80	80
60	85	75	80
75	75	85	75

The mean scores for each column are as follows:
•	Grammar Score: 71.67
•	Vocabulary Score: 80.00
•	Pronunciation Score: 80.00
•	Fluency Score: 78.33
Select the Minimum of the 4 category:
Grammar with 71.67



**Sample execution:**
Welcome to the Language Assessment System!
Enter your age: 21
Enter your country: India
Enter your interests: watching anime

Processing batch 1...
Selected category: Grammar_Score with average score: 71.66666666666667
Exercise for grammar
Scraping images related to:  Interest: watching anime
 ![image](https://github.com/user-attachments/assets/3d9f27ed-16b4-4c9d-af78-0696de75e18e)

Indian audiences are captivated by anime, a genre ____ often explores complex themes and compelling characters.  ____ the popularity of these shows, many viewers spend hours engrossed in the stories.

Enter your answers in the form of a string (e.g., 'is, is, on'): 'on, will'
Score: 70, Remarks: Slightly awkward phrasing

**I have failed here
Retake test**
Exercise for grammar
 ![image](https://github.com/user-attachments/assets/b8aab06f-68da-4f24-a5f7-11f7676aa424)

An Indian anime enthusiast enjoys watching various shows.  He often reflects ____ the different styles and plots.  He believes that ____ anime can be very thought-provoking, providing insights into different cultures.
Enter your answers in the form of a string (e.g., 'is, is, on'):    
Score: 95, Remarks: Minor word choice improvement needed
Exercise for Grammar Score completed with score 95, exceeding the threshold of 76.66666666666667.

Processing batch 2...
exercise on vocabulary
response score: 20, remark: suggest 'ate' be 'eating' 

Score: 20
Remark: suggest 'ate' be 'eating'
Exercise for Vocabulary_Score completed with score 95, exceeding the threshold of 25.0.

Processing batch 3...
Selected category: Fluency_Score with average score: 43.333333333333336
Fluency exercise
enter the fluency reference sentence that you are going to repeatThis is a big house
enter the audio file for fluency check C:\Users\DHARSHAN BALAJI\Downloads\objdetectioproject\grammar project\audio_samples\This-house-is-very-big_fluency_.wav
Exercise for Fluency_Score completed with score 95, exceeding the threshold of 48.333333333333336.

And so on until batch 10

My Exercise logs after execution:
1, Grammar, 70, Slightly awkward phrasing
1, Grammar, 95, Minor word choice improvement needed
2, Vocabulary, 20, suggest 'ate' be 'eating'
3, Fluency, 79, "Pause durations (start, end in seconds): [(0.0, 0.884), (3.463, 5.141)]"
4, Fluency, 80, "Pause durations (start, end in seconds): [(0.0, 0.887), (3.035, 3.989)]"
5, Fluency, 80, "Pause durations (start, end in seconds): [(0.0, 0.887), (3.035, 3.989)]"
6, Fluency, 79,"Pause durations (start, end in seconds): [(0.0, 0.884), (3.463, 5.141)]"
7, Fluency, 80,"Pause durations (start, end in seconds): [(0.0, 0.884), (3.463, 5.141)]"
8, Grammar, 100, Excellent flow and grammar
9, Grammar, 70, Slightly awkward
9, Grammar, 70, Slightly awkward
9, Grammar, 70, Slightly awkward
9, Grammar, 100, Excellent sentence.
10, Vocabulary, 70, "Suggest replacing ""taciturn"" with ""reserved"" or ""quiet""."

Here row 1,2 both are exercise 1 because I have failed to cross threshold so I have to retake same category exercise.
