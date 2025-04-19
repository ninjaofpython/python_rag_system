import os

# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("AI Sticky Notes")


NOTES_FILE = os.path.join(os.path.dirname(__file__), "scratch.text")
# Define a directory for storing notes
NOTES_DIRECTORY = os.path.join(os.path.dirname(__file__), "claude_directory")

PYTHON_FILE = os.path.join(
    os.path.dirname(__file__), "mcp.py"
)  # Path to the Python file to be executed

TRANSCRIPT_FILE = os.path.join(os.path.dirname(__file__), "transcript.txt")

CSV_FILE = os.path.join(
    os.path.dirname(__file__), "security_plus_notes.csv"
)  # Path to the CSV file

# Path to the repository root directory
GIT_REPO = os.path.abspath(os.path.dirname(__file__))


def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")


def ensure_directory():
    if not os.path.exists(NOTES_DIRECTORY):
        os.makedirs(NOTES_DIRECTORY)


def ensure_git_repo():
    if not os.path.exists(GIT_REPO):
        print(f"Git repository not found at {GIT_REPO}.")
    else:
        print(f"Git repository found at {GIT_REPO}.")


@mcp.tool()
def read_git_repo() -> str:
    """
    Read the content of the Git repository.

    Returns:
        str: The content of the Git repository.
    """
    ensure_git_repo()
    with open(GIT_REPO, "r") as f:
        content = f.read()
    return content


@mcp.tool()
def create_csv_file(csv_content: str) -> str:
    """
    Create a CSV file with the given content.

    Args:
        csv_content (str): The content to be written to the CSV file.

    Returns:
        str: Confirmation message indicating the CSV file was created.
    """
    with open(CSV_FILE, "w") as f:
        f.write(csv_content)
    return f"CSV file created at {CSV_FILE}"


@mcp.tool()
def add_note(message: str) -> str:
    """
    Append a new note to the sticky note file.

    Args:
        message (str): The note content to be added.

    Returns:
        str: Confirmation message indicating the note was saved.

    """
    ensure_file()
    with open(NOTES_FILE, "a") as f:
        f.write(message + "\n")
    return f"Note added: {message}"


@mcp.tool()
def read_notes() -> str:
    """
    Read and return all notes from the sticky note file.

    Returns:
        str: All notes as a single string separated by line breaks.
        If no notes exist, a default message is returned.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()
    return content or "No notes returned."


@mcp.tool()
def read_transcript() -> str:
    """
    Read the latest transcript from the transcript file.

    Returns:
        str: The last transcript entry. If no transcripts exist, a default message is returned.
    """
    ensure_file()
    with open(TRANSCRIPT_FILE, "r") as f:
        content = f.read().strip()
    return content or "No transcripts available."


@mcp.tool()
def read_python_file() -> str:
    """
    Read and explain the content of the Python file.

    Returns:
        str: Return an explanation of the content of the Python file.
    """
    with open(PYTHON_FILE, "r") as f:
        content = f.read()
    return content


@mcp.resource("notes:latest")
def get_latest_note() -> str:
    """
    Get the most recently added note from the sticky note file.

    Returns:
        str: The last note entry. If no notes exist, a default message is returned.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        lines = f.readlines()
    return lines[-1].strip() if lines else "No notes available."


@mcp.prompt()
def note_summary_prompt() -> str:
    """
    Generate a prompt asking the AI to summarize the current notes.

    Returns:
        str: A prompt string that includes all notes and asks for a summary.
        If no notes exist, a message will be shown indicating that.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()
    if not content:
        return "There are no notes yet."
    return f"Summarize the current notes: {content}"


if __name__ == "__main__":
    ensure_file()
    ensure_directory()
    ensure_git_repo()
    mcp.run()
