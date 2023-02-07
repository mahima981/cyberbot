import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hey,I am CyberBot.!How can I help you?', ['hello', 'hi', 'hey', 'sup', 'heyo'], required_words=['hello'])
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('Currently,I am limited to 5 malwares. 1.Viruses 2.Worms 3.ransomware 4.bots 5.Trojan horses.', ['could', 'you', 'please','explain','malwares'], required_words=['could', 'malwares'])
    response('A computer virus infects devices and replicates itself across systems. Viruses require human intervention to propagate. Once users download the malicious code onto their devices -- often delivered via malicious advertisements or phishing emails -- the virus spreads throughout their systems. Viruses can modify computer functions and applications; copy, delete and steal data', ['viruses'], required_words=['viruses'])
    response('A computer worm self-replicates and infects other computers without human intervention. This malware inserts itself in devices via security vulnerabilities or malicious links or files. ', ['Worms'], required_words=['Worms'])
    response('Ransomware encrypts files or devices and forces victims to pay a ransom in exchange for reentry.', ['ransomware'], required_words=['ransomware'])
    response('A bot is a self-replicating malware that spreads itself to other devices, creating a network of bots, or a botnet. Once infected, devices perform automated tasks commanded by the attacker.', ['bots'], required_words=['bots'])
    response('A Trojan horse is malicious software that appears legitimate to users. Trojans rely on social engineering techniques to invade devices. Once inside a device .the Trojan payload or malicious code is installed, which is responsible for facilitating the exploit. Trojans give attackers backdoor access to a device, perform keylogging, install viruses or worms, and steal data.', ['trojan horses'], required_words=['trojan horses'])
    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))