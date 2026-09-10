
def get_quiz_question(df):
    sample = df.sample(1).iloc[0]
    correct = sample['english']
    others = df[df['english'] != correct]['english']
    others = others.sample(min(2, len(others))).tolist()
    options = [correct] + others
    random.shuffle(options)
    return sample, correct, options