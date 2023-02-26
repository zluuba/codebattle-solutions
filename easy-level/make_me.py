# Create a function that changes specific words into emoticons. Given a sentence as a string,
# replace the words smile, grin, sad, shocked, bored and painful with their corresponding emoticons.
#
# Examples:
# "Make me :D"  == solution("Make me smile")
# "Make me :)"  == solution("Make me grin")
# "Make me :("  == solution("Make me sad")
# "Make me D:"  == solution("Make me shocked")
# "Make me (-_-)"  == solution("Make me bored")
# "Make me (>_<)"  == solution("Make me painful")


def solution(sentence: str) -> str:
    emoticons = {
        'smile': ':D', 'grin': ':)', 'sad': ':(',
        'shocked': 'D:', 'bored': '(-_-)', 'painful': '(>_<)'
    }

    emoticon_sentence = []
    for word in sentence.split():
        if word in emoticons:
            word = emoticons[word]
        emoticon_sentence.append(word)

    return ' '.join(emoticon_sentence)
