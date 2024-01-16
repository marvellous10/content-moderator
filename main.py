from dotenv import load_dotenv
import os
from azure.ai.contentsafety import ContentSafetyClient
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import HttpResponseError
from azure.ai.contentsafety.models import AnalyzeTextOptions

def analyzeText(user_text):
    load_dotenv()
    # Make Connection
    key = os.getenv("CONTENT_SAFETY_KEY")
    endpoint = os.getenv("CONTENT_SAFETY_ENDPOINT")
    
    #Create Client for connection
    client = ContentSafetyClient(endpoint, AzureKeyCredential(key=key))
    
    #Request
    request = AnalyzeTextOptions(text=str(user_text))
    
    #Analyze Text
    try:
        response = client.analyze_text(request)
    except HttpResponseError as e:
        print("Couldnt analyze text")
        if e.error:
            print(f"Error code: {e.error.code}")
            print(f"Error message: {e.error.message}")
            raise
        print(e)
        raise
    if response.categories_analysis:
        for category in response.categories_analysis:
            print(f"{category.category}: {category.severity}")
        

    
user_text = input("Write a text here: ")

analyzeText(user_text=user_text)