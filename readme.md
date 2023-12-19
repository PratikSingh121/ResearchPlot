# ResearchPlot

## Overview

The Research Assistant is a Python project that leverages the power of the LangChain library and the OpenAI API to conduct research on a given topic, keyword, question, or statement. The project aims to understand the user's scenario, ask relevant questions, and generate a Mermaid code, which is then converted into a flowchart for clear and concise representation of the research findings.

## Features

- Topic analysis and understanding.
- Intelligent question generation based on user input.
- Automatic generation of Mermaid code for a flowchart representation.
- Integration with the OpenAI API for enhanced natural language processing.

## Getting Started

### Prerequisites

Before running the project, ensure that you have an OpenAI API key. You can obtain one [here](https://platform.openai.com/api-keys). Additionally, make sure you have the required dependencies by installing them using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/langchain-research-assistant.git
   cd langchain-research-assistant
   ```

## Installation

1. **Clone the repository:**

   - Run the following command in your terminal:

     ```
     git clone https://github.com/your-username/langchain-research-assistant.git
     cd langchain-research-assistant
     ```

2. **Set up your OpenAI API key:**

   Obtain an OpenAI API key by following the steps below:

   - Visit [OpenAI's API Key page](https://platform.openai.com/api-keys).
   - Create an account or log in if you already have one.
   - Generate a new API key and copy it.

   Replace `YOUR_API_KEY` in the `.env` file with the API key you obtained.

   ```bash
   # .env
   OPENAI_API_KEY = 'YOUR_API_KEY'
   ```

3. **Run the main script:**

- Execute the following command in your terminal:

  ```
  python main.py
  ```

## Usage

1. Execute the main script.
2. Enter the topic, keyword, question, or statement when prompted.
3. The LangChain Research Assistant will analyze the input, generate relevant questions, and provide Mermaid code for a flowchart.
4. Visualize the flowchart to represent the research findings.
