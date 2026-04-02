
score = 0
totalQuestions = 0
def showWelcome(playerName):
    print("==========================")
    print("  Japanese Vocabulary Quiz")
    print("  Welcome ", playerName)
    print("==========================")

# work bank - Japanese : English
wordBank = {
    "inu": "dog",
    "neko": "cat",
    "sakura": "cherryblossom",
    "hashi": "chopsticks",
    "mizu": "water",
    "hi": "fire",
    "sora": "sky",
    "yama": "mountain",
    "umi": "sea",
    "hana": "flower"
}

print("\n There are", len(wordBank), " words in today's quiz.")

def runQuiz(playerName):
    score = 0
    totalQuestions = 0

    for japaneseWord, correctAnswer in wordBank.items():
        totalQuestions += 1
        print("\nQuestion", totalQuestions, "of", len(wordBank))
        print("What does '", japaneseWord, "'mean in English?")

        playerAnswer = input("Your answer: ")

        if playerAnswer.lower() == correctAnswer:
            print("✓ Correct!")
            score += 1
        else:
            print("✗ Wrong! The answer was:", correctAnswer)
    showScore(playerName, score, totalQuestions)

def showScore(playerName, score, totalQuestions):
    percentage = (score / totalQuestions) * 100

    print("\n==========================")
    print("  Quiz Complete,", playerName)
    print("  Score:", score, "/", totalQuestions)
    print("\n==========================")

    if percentage == 100:
        print("  Perfect score! Incredible!")
    elif percentage >= 70:
        print("  Great Job, keep it up!")
    else:
        print(" Keep studying, you'll get there!")

    print("==========================")

def askReplay():
    replayAnswer = input("\nWould you like to play again? (yes/no): ")
    if replayAnswer.lower() == "yes":
        return True
    elif replayAnswer.lower() == "no":
        return False
    else:
        print("Please type 'yes' or 'no'.")
# beginning of main program

playerName = input("Enter your name:")
showWelcome(playerName)

while True:
    runQuiz(playerName)
    if askReplay() == false:
        print("\n Thanks for playing, ", playerName, "! keep studying your Japanese! 🎌")
        break