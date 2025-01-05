from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, File
import logging
import requests

logging.basicConfig(level=logging.ERROR)

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
API_KEY: Final[str] = os.getenv('API_KEY')

# Bot setup
intents: Intents = Intents.default()
intents.message_content = True # NOQA
client: Client = Client(intents=intents)

def generate_image(prompt: str) -> str:
    """
    Generate an image using the Stable Diffusion API and return the file path.
    """
    url = "https://api.stability.ai/v2beta/stable-image/generate/sd3"
    headers = {
        "authorization": f"Bearer {API_KEY}",
        "accept": "image/*",
    }
    data = {
        "prompt": prompt,
        "output_format": "jpeg",
    }

    response = requests.post(url, headers=headers, files={"none": ''}, data=data)

    if response.status_code == 200:
        file_path = f"./{prompt.replace(' ', '_')}.jpeg"
        with open(file_path, 'wb') as file:
            file.write(response.content)
        return file_path
    else:
        logging.error(f"Stable Diffusion API Error: {response.json()}")
        raise Exception(f"Error generating image: {response.json()}")

# Message functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        await message.channel.send('No message provided.')
        return

    if message.embeds:
        await message.channel.send("The message contains embeds that might interfere.")
        return

    if message.attachments:
        await message.channel.send("The message contains attachments that might interfere.")
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        # Check if the message starts with !gen
        if user_message.startswith("!gen"):
            prompt = user_message[5:]  # Extract the prompt after "!gen "
            if not prompt:
                await message.channel.send("Please provide a prompt for image generation.")
                return

            # Call the generate_image function
            try:
                image_path = generate_image(prompt)
                await message.channel.send(file=File(image_path))
            except Exception as e:
                await message.channel.send(f"Error generating image: {e}")
                logging.error("Error in image generation", exc_info=True)
        else:
            await message.channel.send("Unrecognized command. Use `!gen <prompt>` to generate an image.")
    except Exception as e:
        logging.error("An error occurred", exc_info=True)
        await message.channel.send("An unexpected error occurred. Please try again later.")

@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()
