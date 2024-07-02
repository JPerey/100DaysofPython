import pip._vendor.requests as requests
def Get_Quiz():
    quiz_bank = requests.get("https://opentdb.com/api.php?amount=10&difficulty=medium&type=boolean")

    return quiz_bank