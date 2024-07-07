import pip._vendor.requests as requests

class Question_Bank:

    def Get_Quiz(self):

        def __init__(self):
            pass

        quiz_bank = requests.get("https://opentdb.com/api.php?amount=10&difficulty=medium&type=boolean")
        print(f"quiz bank = {quiz_bank}")