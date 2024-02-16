import os, openai

openai.api_key=os.getenv('OPEN_API_KEY')

models=openai.Model.list()

for model in models['data']:
    print('-', model['id'])