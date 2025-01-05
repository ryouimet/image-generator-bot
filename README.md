# Discord Image Generator Bot

This is a Discord bot that generates images using the Stable Diffusion API based on user prompts. The bot listens for messages in your Discord server and responds with an image generated from the provided text prompt using the `!gen <prompt>` command.

## Prerequisites

Before you begin, make sure you have the following:

1. **Python 3.13+** installed on your system. 
2. **Discord Bot Token**: You need to create a Discord bot and get its token from the [Discord Developer Portal](https://discord.com/developers/applications).
3. **Stable Diffusion API Key**: Sign up on [Stability AI](https://platform.stability.ai/) to get an API key for generating images.

## Setup

Follow these steps to set up and run the bot:

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/ryouimet/discord-image-generator-bot.git
cd discord-image-generator-bot
```

### 2. Install the Required Python Packages

Install the necessary Python libraries using `pip`:

```bash
pip install discord.py requests python-dotenv
```

Alternatively, if you have a `requirements.txt` file, you can install dependencies with:

```bash
pip install -r requirements.txt
```

### 3. Set Up the Environment Variables

Create a `.env` file in the project's root directory to store your sensitive information (e.g., Discord bot token and Stable Diffusion API key).

The `.env` file should look like this:

```env
DISCORD_TOKEN=your_discord_bot_token
API_KEY=your_stable_diffusion_api_key
```

### 4. Run the Bot

Run the bot using Python:

```bash
python image-generator-bot.py
```

The bot will now start, and you should see a message in your terminal when it is logged in and ready to use.

### Usage

Once the bot is running, you can use the following command to generate images:

`!gen <prompt>`


For example:

`!gen A futuristic cityscape at sunset`


The bot will respond with an image generated from the prompt.


