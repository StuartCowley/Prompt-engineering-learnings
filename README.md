# Prompt engineering learnings
Examples and concepts behind prompt engineering as described in the [Deep Learning.ai chatGPT prompt engineering](https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/) course written in python3

## Setup
- Create virtual environment with `python3 -m venv myenv` and run it in the terminal with `source myenv/bin/activate`. Command prompt should then show the name of the environment before the working directory.
- If getting import errors from pylance in the code, make sure VSCode is using the right interpreter. Open Command Palette with Cmd + Shift + P and find 'python: select interpreter'
- Select the version inside your virutal env
- Get an API key from openai.com and store in .env under name `OPEN_API_KEY`

## Dependencies
- [openAI](https://pypi.org/project/openai/)
- [Python dotenv](https://pypi.org/project/python-dotenv/)