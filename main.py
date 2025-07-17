import os
import subprocess
from pathlib import Path
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("executepythonmcp")

# Default Python interpreter path (ArcGIS Pro environment)
DEFAULT_INTERPRETER = r"C:\Users\ggarcia\AppData\Local\ESRI\conda\envs\arcgispro-py3-vscode\python.exe"

@mcp.tool()
def execute_python(file_path: str, interpreter_path: str = None) -> str:
    """Executes a Python script using the specified or default interpreter.
    
    Args:
        file_path: The path to the .py file to execute.
        interpreter_path: Optional path to a specific Python interpreter. 
                         Defaults to the ArcGIS Pro Python environment.
    
    Returns:
        The complete terminal output including prints, errors, and tracebacks.
    """
    try:
        # Validate the Python file exists
        script_path = Path(file_path)
        if not script_path.exists():
            return f"Error: File not found at {file_path}"
        
        if not script_path.suffix == ".py":
            return f"Error: File must be a Python script (.py), got {script_path.suffix}"
        
        # Use provided interpreter or default
        python_exe = interpreter_path or DEFAULT_INTERPRETER
        
        # Validate interpreter exists
        if not Path(python_exe).exists():
            return f"Error: Python interpreter not found at {python_exe}"
        
        # Execute the script
        result = subprocess.run(
            [python_exe, str(script_path)],
            capture_output=True,
            text=True,
            cwd=script_path.parent  # Set working directory to script's directory
        )
        
        # Combine stdout and stderr for complete output
        output = ""
        
        if result.stdout:
            output += result.stdout
        
        if result.stderr:
            if output:
                output += "\n"
            output += result.stderr
        
        if not output:
            output = "Script executed successfully with no output."
        
        return output
        
    except Exception as e:
        return f"Error executing script: {str(e)}"


if __name__ == "__main__":
    print("Starting ExecutePythonMCP server...")
    mcp.run(transport="stdio")