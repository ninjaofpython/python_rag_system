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


# If you want the absolute path, you can do:
TRANSCRIPT_FILE = os.path.join(os.path.dirname(__file__), "domain_4.txt")


CSV_FILE = os.path.join(
    os.path.dirname(__file__), "security_plus_notes_domain_4.csv"
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
def read_transcript() -> str:
    """
    Read the transcript text file from the transcript directory.

    Returns:
        str: Each txt file's text as a single string for parsing. If no, transcripts exist, a default message is returned.
    """
    with open(TRANSCRIPT_FILE, "r") as f:
        content = f.read()
    return content or "No transcripts returned."
