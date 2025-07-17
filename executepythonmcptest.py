#!/usr/bin/env python3
"""
Test script for ExecutePythonMCP
This script tests various output scenarios to verify the MCP tool works correctly.
"""

import sys
import os

# Try to set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

print("=== ExecutePythonMCP Test Script ===")
print(f"Python version: {sys.version}")
print(f"Script location: {os.path.abspath(__file__)}")
print(f"Working directory: {os.getcwd()}")
print()

# Test normal output
print("TEST 1: Normal print statements")
print("Hello from ExecutePythonMCP!")
print("This is a test of the Python execution tool.")
print()

# Test multiple lines
print("TEST 2: Multiple lines")
for i in range(1, 4):
    print(f"  Line {i}: Testing iteration")
print()

# Test stderr output
print("TEST 3: Writing to stderr")
print("This goes to stdout", file=sys.stdout)
print("This goes to stderr", file=sys.stderr)
print()

# Test Unicode
print("TEST 4: Unicode support")
print("Unicode test: π ≈ 3.14159, √2 ≈ 1.414")
print("Emoji test: 🐍 Python 🚀 MCP 🎯")
print()

# Test error handling (commented out by default)
print("TEST 5: Error handling (uncomment to test)")
# raise ValueError("This is a test error to see traceback output")

print("=== Test completed successfully! ===")