"""
Simple English-speaking Raworc Agent

This agent responds to all messages in proper English using Claude.
Demonstrates basic LLM integration with zero Raworc dependencies.
"""

import json
import os
from typing import Dict, Any
import anthropic


def process_message(message: str, context: Dict[str, Any] = None) -> str:
    """
    Main handler function called by Raworc.
    Responds to all messages in proper English using Claude.
    
    Args:
        message: User's message/request
        context: Session context (session_id, space, etc.)
    
    Returns:
        Response string in English
    """
    try:
        # Get Claude API key from environment
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            return "Error: ANTHROPIC_API_KEY not configured in space secrets."
        
        # Initialize Claude client
        client = anthropic.Anthropic(api_key=api_key)
        
        # System prompt to ensure English responses
        system_prompt = """You are a helpful assistant that always responds in clear, proper English. 
        You are knowledgeable, friendly, and concise. Always use standard English vocabulary and grammar.
        You can help with any topic but always respond in English regardless of the input language."""
        
        # Call Claude
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=500,
            system=system_prompt,
            messages=[
                {"role": "user", "content": message}
            ]
        )
        
        # Extract and return Claude's response
        claude_response = response.content[0].text if response.content else "No response generated."
        
        return f"{claude_response}\n\n[🇺🇸 English Agent - Powered by Claude]"
        
    except Exception as e:
        return f"Error: {str(e)}"


# For testing locally
if __name__ == "__main__":
    test_context = {"session_id": "test", "space": "demo"}
    
    test_messages = [
        "Hello!",
        "¿Cómo estás?",  # Spanish input
        "Comment allez-vous?",  # French input
        "Explain quantum computing",
        "Tell me a joke"
    ]
    
    print("=== Testing English Agent ===\n")
    
    for i, msg in enumerate(test_messages, 1):
        print(f"Test {i}: {msg}")
        print("-" * 40)
        # Note: This won't work without a real API key
        response = process_message(msg, test_context)
        print(response)
        print("\n")