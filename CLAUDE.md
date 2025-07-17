# ExecutePythonMCP Context for Claude Code

## Project Overview
This is an MCP (Model Context Protocol) server that enables Claude Code to execute Python scripts on the local machine. It was created to give Claude Code the ability to test and debug Python scripts iteratively.

## Key Features
- Execute Python scripts with full terminal output capture
- Default interpreter: ArcGIS Pro Python environment
- Support for custom Python interpreters/venvs
- Secure execution (only .py files, no arbitrary code)

## Primary Use Case
When Claude Code is working on Python scripts, it can:
1. Edit the script
2. Execute it using `execute_python` tool
3. See any errors or output
4. Fix issues based on the output
5. Re-execute to verify fixes

## Tool Usage
```python
# Execute with default ArcGIS Pro Python
execute_python("path/to/script.py")

# Execute with custom interpreter
execute_python("path/to/script.py", "path/to/python.exe")
```

## Important Paths
- Default interpreter: `C:\Users\ggarcia\AppData\Local\ESRI\conda\envs\arcgispro-py3-vscode\python.exe`
- This allows running scripts that use ArcGIS/ArcPy libraries

## Development Notes
- Built with FastMCP for simplified MCP server creation
- Uses subprocess.run() for secure script execution
- Captures both stdout and stderr for complete debugging info
- Sets working directory to script location for proper relative imports