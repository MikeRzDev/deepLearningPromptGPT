import openai
import os

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )

    return response.choices[0].message["content"]


def get_completion_as_stream(prompt, model="gpt-3.5-turbo"):
    print("Prompt:{promptText}".format(promptText=prompt))
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
        stream=True
    )
    answer = ""
    spinner = "|/-\\"
    print("Processing: ", end="")
    for index, chunk in enumerate(response):
        print("\rProcessing: [ " + spinner[index % len(spinner)] + " ]", end="")
        if chunk.choices[0].delta.get("content") is not None:
            answer += chunk.choices[0].delta.content

    print("\rAnswer:")
    return answer
