def evaluate_grade(name,score,/,*,passing_score=50):
    if score >= passing_score:
        print(f'{name} passed the exam.')
    else:
        print(f'{name} failed the exam.')
