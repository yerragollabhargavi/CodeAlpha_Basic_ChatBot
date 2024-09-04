#importing nlp library called spacy
import spacy 
from nltk.corpus import wordnet

nlp=spacy.load("en_core_web_sm")
#Function to preprocess text using spaCy
def preprocess_text(text):
    doc=nlp(text)
    tokens=[token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return tokens 
#function to get synonyms using NLTK's WordNet
def get_synonyms(word):
    synonyms=set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return synonyms
#basic rule-based response function
def respond_to_input(text):
    preprocessed_text=preprocess_text(text)
    reponse=""
    if any(word in preprocessed_text for word in ["hello","hi","hii","hey"]):
        response="Hello! How can I assit you ? Iam chat bot"

    elif any(word in preprocessed_text for word in["how","are","feeling"]):
        response="I'm just a bunch of code, but I'm here assist you"

    elif "synonym" in preprocessed_text:
        for word in preprocessed_text:
            if word!="synonymn":
                synonyms=get_synonyms(word)
                response=f"synonyms for '{word}' are :{','.join(synonyms)}"
                break

    else:
        response="I'm not sure how to respond to that.Can you rephrase?"
    return response


if __name__=="__main__":
    text=input("You: ")
    bot_response=respond_to_input(text)
    print(f"Bot:{bot_response}")
