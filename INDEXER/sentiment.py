from transformers import AutoModelForSequenceClassification, AutoTokenizer, TextClassificationPipeline
from transformers import pipeline


#Return the float value in range [-1.0,1.0] corresponding to the parsed sentiment 
def parseSentiment(content,classifier):
    
    sentiment = classifier(content)

    if sentiment[0].get('label') == 'positive':
        return sentiment[0].get('score')
    elif sentiment[0].get('label') == 'negative':
        return -sentiment[0].get('score')
    else:
        return 0

#Generates a classifier
    
def generateClassifier():
    model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_Fast = False)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return TextClassificationPipeline(model=model,tokenizer=tokenizer, task="text-classification")