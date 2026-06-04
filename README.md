markdown
# JASPAR MCP Server

An MCP server that provides access to transcription factor motif data from the JASPAR database. Allows LLMs like Claude to search for TF binding profiles by factor name and species.

## Features

- Search for transcription factor motifs by name (e.g., TEAD1, CEBPA, TP53)
- Filter by species (human, mouse, rat, drosophila)
- Returns complete matrix data including sequence logos and API links
- Compatible with Claude Code and other MCP clients

## Requirements

- Python 3.12 or higher
- An MCP client (Claude Code recommended)

## Installation

Clone the repository:

```bash
git clone https://github.com/daniil-11-ger/mcp-jaspar.git
cd mcp-jaspar
Create and activate a virtual environment:

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
pip install -r requirements.txt
Configuration for Claude Code
Create a file named .mcp.json in your project folder with the following content:

json
{
  "mcpServers": {
    "jaspar": {
      "command": "python",
      "args": ["server.py"]
    }
  }
}
Run Claude Code from the same directory:

bash
claude
Usage
Once connected, ask Claude to search for motifs:

"Use search_jaspar to find motifs for TEAD1 in human"

The tool supports the following parameters:

Parameter	Type	Description	Default
tf_name	string	Transcription factor name (e.g., TEAD1, CEBPA)	required
species	string	human, mouse, rat, drosophila	human
Example Response
When searching for TEAD1 in human, the server returns:

json
{
  "count": 4,
  "next": null,
  "previous": null,
  "results": [
    {
      "matrix_id": "MA0090.1",
      "name": "TEAD1",
      "collection": "CORE",
      "species": "9606",
      "sequence_logo": "https://jaspar.elixir.no/static/logos/svg/MA0090.1.svg"
    }
  ]
}
Testing Without MCP
Run the direct test script to verify the API connection:

bash
python test_direct.py
Project Structure
text
mcp-jaspar/
├── server.py          # MCP server implementation
├── test_direct.py     # Standalone API test script
├── requirements.txt   # Python dependencies
└── README.md          # This file
License
MIT

Author
Daniil Gerassimov

## Demo

Claude Code successfully searching for TEAD1 motifs in JASPAR database:

![TEAD1 search result](screenshots/Снимок%20экрана%202026-06-05%20015655.png)

MCP inspector confirming the server has one registered tool:

![MCP inspect Tools: 1](screenshots/Снимок%20экрана%202026-06-05%20015842.png)
