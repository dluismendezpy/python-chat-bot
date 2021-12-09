""" Luis Fernando Mendez Aquino 2019-8304 """
import re
import random
from questions import data


def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


def message_probability(user_message, recognized_words, single_response=False, required_word=None):
    if required_word is None:
        required_word = []
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob = {}

    def response(bot_response, list_of_words, single_response=False, required_words=None):
        if required_words is None:
            required_words = []
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    for i in data:
        response(i['answer'], i['keys'], required_words=i['required_words'], single_response=i['single_response'])

    best_match = max(highest_prob, key=highest_prob.get)
    # print(highest_prob)

    return unknown() if highest_prob[best_match] < 1 else best_match


def unknown():
    response = [
        '¿Puedes repetirlo?',
        'Lo siento, no estoy seguro de lo quieres decir',
        'Búscalo en google a ver que tal'][random.randrange(3)]
    return response


if __name__ == '__main__':
    while True:
        print(f"Bot: {get_response(input('You: '))}")
