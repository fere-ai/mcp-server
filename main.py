#!/usr/bin/env python3
"""
0xMONK MCP Server Entry Point

This script starts the MCP server for the 0xMONK API.
"""
import logging
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import after environment variables are loaded
from src.main import mcp

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("monk-mcp")

def main():
    """Run the 0xMONK MCP server."""
    logger.info("Starting 0xMONK MCP server...")
    
    # Set API key from environment
    api_key = os.getenv("API_KEY")
    if not api_key:
        logger.warning("API_KEY not set in environment variables")
    
    # Run the server
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main() 