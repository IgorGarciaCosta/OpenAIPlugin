import openai
import requests
import shutil


def make_image(size: str, prompt: str, api_key: str):
    openai.api_key = api_key
    # client = openai.OpenAI()

    response = openai.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size=size,
        quality="standard",
        n=1,)

    return response.data[0].url

    # response = openai.Image.create(prompt=prompt, n=1, size=size)
    # return response["data"][0]["url"]


def download_image(url: str, filepath: str, filename: str):
    res = requests.get(url, stream=True)

    full_filepath = filepath + "Images/" + filename + ".png"

    if (res.status_code == 200):
        with open(full_filepath, 'wb') as f:
            shutil.copyfileobj(res.raw, f)


def get_image(api_key: str, size: str, prompt: str, filename: str, filepath: str):

    image_url = make_image(size, prompt, api_key)
    download_image(image_url, filepath, filename)
