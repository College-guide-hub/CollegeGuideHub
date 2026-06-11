import pandas as pd

faq = pd.read_csv("datasets/faq.csv")

def get_answer(question):

    question = question.lower()

    for _, row in faq.iterrows():

        if row["question"].lower() in question:
            return row["answer"]

    return None
