# Terminal-Based Chatbot

This Python script creates a simple chatbot using the OpenAI API. The chatbot uses a conversational model to interact with users in a chat-like format.

## Requirements

- Python 3.x
- OpenAI API key

## Installation

### Create and Activate a Virtual Environment

#### Windows

Create:

```bash
python -m venv env
```

Activate:

```bash
env\Scripts\activate
```

#### Mac / Linux

Create:

```bash
python3 -m venv env
```

Activate:

```bash
source env/bin/activate
```

### Install Dependencies

To install the required packages, run:

```bash
pip install -r requirements.txt
```

### Obtain an OpenAI API Key

1. Create a free account or log in at [OpenAI](https://beta.openai.com/signup/).
2. Retrieve your API key from the [API section](https://platform.openai.com/account/api-keys) in your OpenAI account.

### Set Environment Variable

#### macOS/Linux:

Set your API key as an environment variable:

```bash
export OPENAI_API_KEY=YOUR_API_KEY
```

#### Windows:

```bash
set OPENAI_API_KEY=YOUR_API_KEY
```

## Running the Chatbot

### Navigate to the Project Directory

```bash
cd Terminal-Based-Chatbot
```

### Start the Chatbot

#### Windows

```bash
python chatbot.py
```

#### Mac / Linux

```bash
python3 chatbot.py
```

Begin chatting by typing your messages and pressing Enter. Type `quit` to end the conversation.

## Customization

### Model

Change the language model in `chatbot.py` (line 15):

```python
model="gpt-3.5-turbo"  # Replace with whichever model you want to use
```

## Additional Notes

- **API Costs**: Be aware that OpenAI API calls incur costs. Monitor your usage and review the pricing plans at [OpenAI Pricing](https://beta.openai.com/pricing).
- **Experiment with Models**: Explore different language models to find the one that best suits your needs.
- **Tailor Prompts**: Customize the conversation flow by modifying the initial prompts and user inputs.

## Contributing

Contributions are welcome! Feel free to fork the repository, make your changes, and submit a pull request.

---
