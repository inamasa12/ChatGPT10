import openai, os

openai.api_key = os.environ["OPEN_API_KEY"]

def completion(messages, temperature=1.0, debug=False):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=temperature
    )
    
    if debug: print(response)

    content = response.choices[0].message.content.strip()
    return content


if __name__ == '__main__':
    messages=[
        {'role': 'system', 'content': 'あなたは6面体のサイコロです。'},
        {'role': 'user', 'content': 'サイコロを振ってください。'}
    ]
    res = completion(messages, temperature=1.0)
    
    print(res)
