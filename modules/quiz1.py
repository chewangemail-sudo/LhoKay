import random 
 
 
def get_quiz_question(df): 
    “””Return one random quiz question with 3 options.””” 
    Sample = df.sample(1).iloc[0]     Correct = sample[‘english’] 
 
    # Pick 2 wrong options from the dataset 
    Others = df[df[‘english’] != correct][‘english’] 
    Others = others.sample(min(2, len(others))).tolist() 
 Options = [correct] + others 
    Random.shuffle(options) 
 
    Return sample, correct, options 