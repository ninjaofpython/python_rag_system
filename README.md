# Python RAG System

A Python-based Retrieval Augmented Generation (RAG) system that provides tools for note-taking, file management, content processing, and interaction with AI models.

## Overview

This system implements a Retrieval Augmented Generation (RAG) framework using the FastMCP server to expose various tools that allow AI assistants to:

- Create and manage notes
- Read and process Python files
- Access transcript information
- Work with CSV data
- Interact with Git repositories

The system is designed to provide AI models with access to external data sources, enhancing their ability to provide relevant and contextual responses.

## Features

- **Note Management**: Add, read, and retrieve notes stored in a central location
- **File Processing**: Read and analyze Python files for context
- **Transcript Access**: Read transcript data for conversational context
- **CSV File Handling**: Create and manage CSV files
- **Git Repository Integration**: Read Git repository contents

## Core Components

### Tools

The system provides several tools that can be invoked by AI assistants:

1. **`add_note(message)`**: Append a new note to the sticky note file
2. **`read_notes()`**: Read all notes from the sticky note file
3. **`get_latest_note()`**: Retrieve the most recent note
4. **`read_transcript()`**: Read the latest transcript
5. **`read_python_file()`**: Read and explain Python file contents
6. **`create_csv_file(csv_content)`**: Create a CSV file with provided content
7. **`read_git_repo()`**: Read Git repository contents

### Resources

- **`notes:latest`**: A resource that provides access to the most recent note

### Prompts

- **`note_summary_prompt()`**: Generates a prompt asking the AI to summarize the current notes

## File Structure

- **`mcp.py`**: Main Python file with tool implementations
- **`scratch.text`**: Storage file for notes
- **`transcript.txt`**: File containing transcript data
- **`security_plus_notes.csv`**: CSV file for data storage
- **`claude_directory/`**: Directory for storing notes and other data

## Setup and Usage

1. Ensure all dependencies are installed:
   ```
   pip install fastmcp
   ```

2. Run the server:
   ```
   python mcp.py
   ```

3. The AI assistant can now use the exposed tools to interact with the system

## Integration with AI Models

This system is designed to work with AI models like Claude that support tool use. The FastMCP server exposes the tools that the AI can invoke during conversations to fetch relevant information or store user inputs.

## Requirements

- Python 3.6+
- FastMCP library

## License

[MIT License](LICENSE)
