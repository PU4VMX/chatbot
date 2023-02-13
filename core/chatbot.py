import openai
OPENAI_API_KEY = '**************************'

openai.api_key = OPENAI_API_KEY
def sendAI(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Humano: {}".format(prompt),
    temperature=0.1,
    max_tokens=150,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0,
    stop=["Humano:"]
    )
    print(response['choices'][0]['text'].replace('Robô: ', ''))
    return response['choices'][0]['text'].replace('Robô: ', '')