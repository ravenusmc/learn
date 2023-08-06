import openai
from dotenv import dotenv_values 

config = dotenv_values(".env")
# print(config["OPENAI_API_KEY"])

openai.api_key = config["OPENAI_API_KEY"]
test = openai.Completion.create(model='text-davinci-003', prompt="Happy Birthday ")
print(test)