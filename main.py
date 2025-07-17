import os
import subprocess
import datetime
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
        The path to the output file containing the execution results.
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
        
        # Create output file path
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = script_path.parent / f"{script_path.stem}_output_{timestamp}.txt"
        
        # Execute the script with output redirected to file
        with open(output_file, 'w') as outfile:
            # Write header
            outfile.write(f"=== Executing: {script_path.name} ===\n")
            outfile.write(f"Time: {datetime.datetime.now()}\n")
            outfile.write(f"Interpreter: {python_exe}\n")
            outfile.write("="*50 + "\n\n")
            outfile.flush()
            
            # Execute script
            try:
                result = subprocess.run(
                    [python_exe, str(script_path)],
                    stdout=outfile,
                    stderr=subprocess.STDOUT,  # Combine stderr with stdout
                    cwd=script_path.parent,
                    timeout=30
                )
                
                # Write footer
                outfile.write(f"\n\n" + "="*50 + "\n")
                outfile.write(f"Exit code: {result.returncode}\n")
                outfile.write(f"Completed at: {datetime.datetime.now()}\n")
                
            except subprocess.TimeoutExpired:
                outfile.write(f"\n\n" + "="*50 + "\n")
                outfile.write("ERROR: Script execution timed out after 30 seconds\n")
                return f"Error: Script timed out. Partial output saved to: {output_file}"
        
        # Return the path to the output file
        return f"Script executed successfully. Output saved to: {output_file}"
        
    except Exception as e:
        return f"Error executing script: {str(e)}"


if __name__ == "__main__":
    print("Starting ExecutePythonMCP server...")
    mcp.run(transport="stdio")