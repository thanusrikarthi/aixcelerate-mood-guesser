# Mood Guesser

## Level 3: Testing

Accuracy on the 5 practice sentences: 80.0 %

1. Which sentence went wrong (or was closest to going wrong), and why?

   "Today was a great day" went wrong. The correct answer is Happy, but my program said Sad. None of its words are in my happy_words or sad_words lists, so both counts were 0. That is a tie, and my tie rule chooses Sad. The word "great" is a happy word, but it is not in my list.

2. One change that would make my program better:

   Let the program learn the clue words from the examples (word scores) instead of choosing only 4 words per list by hand. Then it would know many more words, such as "great", and would not have to answer Sad by default when it knows no words in the sentence.

## Learning questions

1. Total score of "good party today" and its mood:

   good = +2, party = +1, today = 0 (never seen). Total = +3, so the mood is Happy.

2. Total score of "bad exam day" and its mood:

   bad = -2, exam = 0, day = -1. Total = -3, so the mood is Sad.

3. Why did "exam" get a score of 0, and is that good or bad?

   "exam" appears once in a Happy sentence ("good exam") and once in a Sad sentence ("bad exam"), so +1 and -1 cancel out to 0. This is mostly good, because a word that appears equally in both moods gives no clue and should not push the answer either way. It can be bad if the data is very small, because the 0 may be only a coincidence.

4. Why is "not good" labelled Happy by this method, and how could it be fixed?

   The method scores each word separately and ignores word order and meaning. "good" is +2 and "not" is unseen (0), so the total is +2 (Happy). But "not" reverses the meaning of "good". A program could fix this by detecting negation words like "not" or "never" and flipping the score of the next word, or by scoring word pairs like "not good" together.
