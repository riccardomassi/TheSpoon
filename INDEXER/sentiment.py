from transformers import AutoModelForSequenceClassification, AutoTokenizer, TextClassificationPipeline
from transformers import pipeline


#Return the float value in range [-1.0,1.0] corresponding to the parsed sentiment 
def parseSentiment(content,classifier):
    
    sentiment = classifier(content)

    return sentiment[0].get('label')
#Generates a classifier
    
def generateClassifier():
    model_name = "SamLowe/roberta-base-go_emotions"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return TextClassificationPipeline(model=model,tokenizer=tokenizer, task="text-classification")
