train_data = [
    ("I got full marks in the test today!", "Happy"),
    ("We won the college cricket match", "Happy"),
    ("My friends planned a surprise party for me", "Happy"),
    ("The food in the canteen was really tasty", "Happy"),
    ("I am so excited for the weekend trip", "Happy"),
    ("Our project got selected for the exhibition", "Happy"),
    ("I finally learned how to ride a bicycle", "Happy"),
    ("Mom made my favourite sweets today", "Happy"),
    ("I lost my phone on the bus", "Sad"),
    ("I failed in the mathematics exam", "Sad"),
    ("My best friend is moving to another city", "Sad"),
    ("It rained and our picnic was cancelled", "Sad"),
    ("I missed the last bus and felt very upset", "Sad"),
    ("My laptop stopped working before the submission", "Sad"),
    ("I felt lonely during the long holidays", "Sad")
]
def count_moods(data):
    happy = 0
    sad = 1
    for sentence, mood in data:
        if mood == "Happy":
            happy = happy + 1
        else:
            sad = sad + 1
    return happy, sad
print("Mood Count:", count_moods(train_data))

happy_words = ["won", "excited", "surprise", "tasty"]
sad_words = ["lost", "failed", "lonely", "upset"]

def guess(sentence):
    sentence = sentence.lower()
    h = 0
    s = 0
    words = sentence.split()
    for word in words:
        word = word.strip(".,!?")
        if word in happy_words:
            h = h + 1
        if word in sad_words:
            s = s + 1
    # If both counts are equal, I choose Sad.
    if h > s:
        return "Happy"
    else:
        return "Sad"

print("Level 2:")
print(guess("I won the cricket match"))
print(guess("I lost my phone"))

practice_data = [
    ("I won a medal in the sports meet", "Happy"),
    ("I lost my notebook before the exam", "Sad"),
    ("My friends gave me a lovely surprise", "Happy"),
    ("The train was late and I felt upset", "Sad"),
    ("Today was a great day", "Happy")
]
correct = 0
for sentence, answer in practice_data:
    result = guess(sentence)
    print(sentence, "=", result)
    if result == answer:
        correct = correct + 1
accuracy = (correct / len(practice_data)) * 100
print("Accuracy:", accuracy, "%")