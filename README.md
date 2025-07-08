# Local Strands MCP

A simple example of using the Model Context Protocol (MCP) with Strands for local AI agent development.

## Overview

This repository demonstrates how to create a simple MCP server and client using the Strands framework. The server provides a basic "add" function that can be used by the client to perform addition operations.

## Files

- `my_server.py`: A simple MCP server that provides an "add" tool
- `my_strands_client.py`: A client that connects to the server and uses the Strands Agent to perform operations

## Requirements

- Python 3.11+
- MCP library
- Strands library

## Installation

1. Clone this repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## Usage

1. Start the server:
   ```
   python my_server.py
   ```

2. In a separate terminal, run the client:
   ```
   python my_strands_client.py
   ```

## AWS Configuration

To use AWS services (if needed), configure your AWS profile:

```
export AWS_PROFILE=your-profile-name
export AWS_REGION=your-region
```

Or specify them when running the scripts:

```
AWS_PROFILE=your-profile-name AWS_REGION=your-region python my_server.py
```
