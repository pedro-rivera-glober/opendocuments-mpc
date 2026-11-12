# OpenDocument MCP Server

A Model Context Protocol (MCP) server that empowers Large Language Models (LLMs) to autonomously create, read, and update OpenDocument files (`.odt`, `.ods`, `.odp`) using Markdown.

This project is built in Python using the `FastMCP` framework and managed via `uv`.

## 🎯 Project Goals

The primary goal of this project is to provide a zero-configuration, cross-platform MCP tool for document generation. 

**Architectural Principles:**
1. **Separation of Concerns:** Core document rendering logic (converting Markdown to ODF XML) must be strictly decoupled from the MCP transport layer. This ensures the document logic is easily unit-testable.
2. **Zero System Dependencies:** We rely on pure-Python libraries (e.g., `odfpy`, `markdown-it-py`) rather than shelling out to system binaries like `pandoc`. This ensures the tool runs seamlessly via `uvx` on any machine.
3. **MCP Hygiene:** All logging and debugging output must be routed to `stderr`. Writing to `stdout` will corrupt the JSON-RPC communication between the LLM and the server.

## 🛠️ Prerequisites

* **Python:** 3.10 or higher
* **Package Manager:** [uv](https://docs.astral.sh/uv/) installed on your Linux system.
* **Viewer:** LibreOffice (optional, but recommended for visually QA'ing the generated files).

## 🚀 Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd odf-mcp-server
   ```

2. **Sync dependencies and create the virtual environment:**
   ```bash
   uv sync
   ```

3. **Activate the virtual environment (optional, for running tests):**
   ```bash
   source .venv/bin/activate
   ```

## 💻 Development Workflow

### Project Structure

```text
odf_mcp_server/
├── pyproject.toml        # Project metadata and uv dependencies
├── src/
│   └── odf_mcp/
│       ├── __init__.py
│       ├── server.py     # FastMCP server definition and tool routing
│       └── core/         # Pure-Python document logic (US-1)
│           ├── __init__.py
│           ├── writer.py # Markdown to .odt conversion
│           ├── calc.py   # Markdown to .ods conversion
│           └── impress.py# Markdown to .odp conversion
└── tests/                # Pytest unit tests
```

### Running Tests

We use `pytest` for all unit testing. Focus tests on the `src/odf_mcp/core/` modules first before testing the MCP server logic.

```bash
uv run pytest
```

### Running the MCP Inspector (Dev Mode)

To test the MCP server interactively without connecting it to a full LLM client, use the FastMCP dev server:

```bash
uv run fastmcp dev src/odf_mcp/server.py
```
This will launch a local web inspector where you can manually invoke the `create_odt` and `update_odt` tools and view their outputs.

## 📦 Using with an LLM Client

Once the package is built and tested, it can be run directly by an MCP client (like Claude Desktop) using `uvx`. 

Add the following to your MCP client's configuration file (e.g., `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "odf-generator": {
      "command": "uvx",
      "args": [
        "--from",
        "/absolute/path/to/this/repository",
        "odf-mcp"
      ]
    }
  }
}
```
*(Note: Replace `/absolute/path/to/this/repository` with the actual path on your Linux machine).*

## 🗺️ Roadmap & Milestones

* **Milestone 1: Writer / `.odt` Basics**
  * Convert Markdown to `.odt` via core Python logic.
  * Wrap with FastMCP.
  * Package for `uvx` execution.
* **Milestone 2: Iterative Updates**
  * Update existing `.odt` files (append mode and section replacement).
* **Milestone 3: Spreadsheets & Presentations**
  * Generate `.ods` from Markdown tables.
  * Generate `.odp` from Markdown outlines.