# ExecutePythonMCP

A Model Context Protocol (MCP) server that enables AI assistants to execute Python scripts using local interpreters. Initially developed to give Windows native Claude Code a way to execute, test, and debug Python scripts iteratively.

## Overview

This MCP server provides a secure bridge for AI language models to execute Python scripts on your local machine. It captures complete terminal output including prints, errors, and tracebacks, enabling AI assistants to debug and iterate on Python code effectively.

## Features

- **Flexible Interpreter Support**: Use default ArcGIS Pro Python environment or specify custom interpreters
- **Complete Output Capture**: Returns all stdout and stderr output including tracebacks
- **Security**: Only executes specified .py files, no arbitrary code execution
- **Working Directory Management**: Automatically sets working directory to script location
- **Error Handling**: Comprehensive validation and error reporting

## Available Tools

### `execute_python`
Executes a Python script using the specified or default interpreter.

**Parameters:**
- `file_path` (string, required): The path to the .py file to execute
- `interpreter_path` (string, optional): Path to a specific Python interpreter
  - Default: `C:\Users\ggarcia\AppData\Local\ESRI\conda\envs\arcgispro-py3-vscode\python.exe`

**Returns:**
Complete terminal output including all print statements, errors, and tracebacks.

**Example Usage:**
```python
# Execute with default interpreter
execute_python("C:\\scripts\\my_script.py")

# Execute with custom venv interpreter
execute_python(
    "C:\\projects\\myproject\\script.py",
    "C:\\projects\\myproject\\venv\\Scripts\\python.exe"
)
```

## Setup

### Prerequisites
- Python 3.11 or higher
- UV package manager (for virtual environment)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/GarrickGarcia/ExecutePythonMCP.git
   cd ExecutePythonMCP
   ```

2. Create and activate a virtual environment with UV:
   ```bash
   uv venv
   .venv\Scripts\activate  # On Windows
   ```

3. Install the package:
   ```bash
   uv pip install -e .
   ```

### Running the Server

```bash
python main.py
```

The server will start and listen for MCP connections via stdio transport.

## Configuration

To use a different default Python interpreter, modify the `DEFAULT_INTERPRETER` constant in `main.py`:

```python
DEFAULT_INTERPRETER = r"C:\path\to\your\python.exe"
```

## Use Cases

- **Script Development**: Test Python scripts immediately after editing
- **Debugging**: See complete error messages and tracebacks
- **Iterative Development**: Quickly iterate on solutions based on error output
- **Environment Testing**: Test scripts across different Python environments
- **Automation**: Let AI assistants run and debug Python automation scripts

## Security Considerations

- Only executes files with `.py` extension
- Validates file existence before execution
- No arbitrary code execution - must specify exact file path
- Working directory is constrained to script location

## Integration with Claude Code

This MCP server is designed to work seamlessly with Claude Code, allowing it to:
1. Edit a Python script
2. Execute it using this MCP tool
3. Read the output including any errors
4. Make corrections based on the errors
5. Re-execute to verify fixes

This creates a powerful development loop for Python scripting tasks.
