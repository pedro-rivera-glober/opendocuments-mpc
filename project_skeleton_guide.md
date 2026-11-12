# Project Architecture & Skeleton Guide

Welcome to the OpenDocument MCP Server project! This guide explains the directory structure we use and the responsibilities of each file. 

As a software engineer, one of the most important habits you can build is maintaining a clean **Separation of Concerns**. In this project, that means keeping our Model Context Protocol (MCP) communication logic completely separate from our OpenDocument generation logic.

## Directory Tree

```text
odf_mcp_server/
├── .gitignore
├── pyproject.toml
├── README.md
├── src/
│   └── odf_mcp/
│       ├── __init__.py
│       ├── __main__.py
│       ├── server.py
│       └── core/
│           ├── __init__.py
│           ├── parser.py
│           ├── writer.py
│           ├── calc.py
│           └── impress.py
└── tests/
    ├── __init__.py
    ├── conftest.py
    ├── test_server.py
    └── core/
        ├── test_parser.py
        └── test_writer.py
```

## Root Level Files

These files configure the project as a whole, managing dependencies, environments, and Git tracking.

*   **`.gitignore`**: Tells Git which files to ignore (e.g., `.venv/`, `__pycache__/`, `.pytest_cache/`, and generated `.odt` test files).
*   **`pyproject.toml`**: The modern standard for Python packaging. We use this with `uv` to define our dependencies (like `fastmcp`, `odfpy`, `markdown-it-py`), project metadata, and crucially, our CLI entry point so the LLM client can run our server via `uvx`.
*   **`README.md`**: The front page of our project (setup instructions, goals, and milestones).

## Source Code (`src/odf_mcp/`)

We use the `src/` layout. This is a Python best practice that prevents accidental import errors during testing by forcing Python to use the installed package rather than the local directory.

*   **`__init__.py`**: Exposes the main version and package details.
*   **`__main__.py`**: Allows the package to be run as a module (e.g., `python -m odf_mcp`). This usually just imports and calls the `main()` function from `server.py`.
*   **`server.py`**: **The Transport Layer.** This file initializes the `FastMCP` application. It defines the `@mcp.tool()` endpoints (`create_odt`, `update_odt`). 
    *   *Important:* This file should **not** contain raw XML manipulation. It simply receives strings from the LLM, passes them to the `core/` modules, and returns success/error strings back to the LLM.

### The Core Domain (`src/odf_mcp/core/`)

This is where the actual business logic lives. These files are pure Python and have zero knowledge of MCP or LLMs. This makes them incredibly easy to test.

*   **`parser.py`**: Shared logic for converting Markdown text into an Abstract Syntax Tree (AST) using libraries like `markdown-it-py`.
*   **`writer.py`**: Contains functions like `generate_odt(markdown_ast, output_path)`. Uses `odfpy` to build the XML tree for text documents.
*   **`calc.py`**: (Milestone 3) Logic for building `.ods` spreadsheets from Markdown tables.
*   **`impress.py`**: (Milestone 3) Logic for building `.odp` presentations.

## Testing (`tests/`)

Writing tests is how we prove our code works without manually clicking through it every time. We use `pytest`.

*   **`conftest.py`**: A place to define shared "fixtures." For example, we might create a fixture that generates a temporary directory for our tests to write `.odt` files into, so we don't clutter up our workspace.
*   **`test_server.py`**: Tests the FastMCP endpoints (ensuring they return the right error messages if a file path is invalid, for example).
*   **`core/test_writer.py`**: Tests the pure Python logic. We can pass a simple Markdown string here, generate an `.odt` file in a temporary folder, and assert that the file was created successfully.

## A Note on Mentoring & Growth

When tackling a new feature:
1. Start in `tests/core/` and write a test for what you want to achieve.
2. Build the logic in `src/odf_mcp/core/`.
3. Once that works perfectly, wire it up to the LLM in `server.py`. 