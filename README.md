# LLM Translator

LLM Translator, is a demo language translation solution. Powered by Django and Langchain, it seamlessly integrates leading LLMs like ChatGPT, Gemini Pro, and LLAMA2. This app ensures unparalleled translation accuracy and fluency. Say goodbye to language barriers and hello to natural, human-like conversations.

![A screenshot of the app.](/images/sample.png "A screenshot of the app.")

## Project Setup

1. Copy the Dotenv file.
```sh
cp .env.example .env
```

2. Populate all the fields.
```sh
APP_PORT=80
APP_KEY= # Can be any string.

# OPENAI example
LLM_TYPE=openai
LLM_API_KEY=sk-*
LLM_MODEL_NAME=gpt-3.5-turbo

# or

# GOOGLE example
LLM_TYPE=google
LLM_API_KEY=AI*
LLM_MODEL_NAME=gemini-pro

# or

# OLLAMA example
LLM_TYPE=ollama
LLM_API_BASE='http://to-ollama-container:11434'
LLM_MODEL_NAME=llama2

```

3. Install and run the app.
```sh
docker-compose up -d --build
```

## Security Notice
This app is designed to protect against malicious prompt injection. It's always a good idea to exercise caution and follow best practices when copying the code to your application. By being diligent and careful, you can ensure your app is secure and free from potential vulnerabilities.
