# POML Integration Examples

POML (Prompt Orchestration Markup Language), a powerful tool that brings structure, maintainability, and flexibility to advanced prompt engineering for Large Language Models (LLMs).  POML helps developers create clean, modular, and data-driven prompts with ease

Check out my YouTube video for a complete walkthrough of this code: https://youtu.be/qcrULZ02-Q0?si=ok-MXf2GmbLgKAli

Also refer to the official Microsoft doc https://microsoft.github.io/poml/latest/ to learn more about POML

This repository demonstrates how to integrate [POML](https://github.com/poml-lang/poml) with OpenAI and LangChain for conversational AI tasks using a POML template.

## Project Structure

- `POML_Integration_WithOpenAI.py` — Example using OpenAI's API with POML.
- `POML_Integration_WithLangChain.py` — Example using LangChain with POML.
- `example.poml` — Sample POML template for a teaching scenario.
- `photosynthesis_diagram.png` — Image referenced in the POML template.
- `.env` — Stores your OpenAI API key.
- `requirements.txt` — Python dependencies.

## Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/umianta/POML.git
   cd your-repo-name
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Add your OpenAI API key:**
   - Create a `.env` file in the project root:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

4. **Ensure `photosynthesis_diagram.png` is present in the root directory.**

## Usage

### OpenAI Integration

Run the script to generate a response using OpenAI's GPT-4 model:

```sh
python POML_Integration_WithOpenAI.py
```

### LangChain Integration

Run the script to generate a response using LangChain:

```sh
python POML_Integration_WithLangChain.py
```

## Example POML Template

See [`example.poml`](example.poml) for the template used in these examples.

