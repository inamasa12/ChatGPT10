import openai, os

openai.api_key = os.environ["OPEN_API_KEY"]

def call_chatgpt(prompt, debug=False):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{'role': 'user', 'content': prompt}]
    )
    
    if debug: print(response)

    content = response.choices[0]['message']['content']
    return content

pet_names = call_chatgpt('ペットの名前を5つ考えて', debug=True)
print(pet_names)
