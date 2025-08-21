# English-Speaking Raworc Agent Demo

Simple English-speaking agent powered by Claude that responds to all messages in clear, proper English.

## Architecture

- **Zero Dependencies**: No raworc imports needed
- **Pure Function**: Just implement `process_message(message, context) -> response`
- **Claude Integration**: Direct Anthropic API integration for LLM responses
- **Language Focus**: Always responds in proper English regardless of input
- **Git Deployment**: Deployed directly from GitHub repository

## Files

- `raworc.json` - Agent manifest (required)
- `main.py` - Agent implementation with `process_message` function
- `requirements.txt` - Python dependencies (only anthropic)

## Agent Capabilities

This English agent can:
- Respond to any question or request in clear English
- Handle multiple languages as input but always respond in English
- Provide helpful, knowledgeable responses on any topic
- Demonstrate basic LLM integration patterns
- Serve as a template for building language-specific agents

## Example Interactions

**Input (any language):**
- "Hello!"
- "¿Cómo estás?" (Spanish)
- "Comment allez-vous?" (French)
- "Explain quantum computing"
- "Tell me a joke"

**Output (always English):**
- Responds in clear, proper English
- Maintains helpful and friendly tone
- Uses standard English vocabulary and grammar

## Testing Locally

```bash
export ANTHROPIC_API_KEY="your-api-key"
python main.py
```

This will run test cases with various input languages.

## Deploying to Raworc

1. Create agent in your space:
```bash
raworc api spaces/demo/agents --method POST --body '{
  "name": "english-agent",
  "description": "Responds in clear, proper English using Claude LLM",
  "purpose": "demonstrate English-speaking agent with LLM integration",
  "source_repo": "Raworc/raworc-agent-python-demo",
  "source_branch": "main"
}'
```

2. Build the space:
```bash
raworc api spaces/demo/build --method POST
```

3. Create session and test:
```bash
raworc api sessions --method POST --body '{"space": "demo"}'
```

4. Send messages:
```bash
raworc api sessions/{session_id}/messages --method POST --body '{
  "content": "Hello! Please respond in English.",
  "role": "user"
}'
```

The agent will automatically respond in proper English regardless of input language!

## Key Features

- ✅ **Simple Integration**: Minimal code, maximum functionality
- ✅ **Language Consistency**: Always English output
- ✅ **Claude Powered**: Latest Claude 3.5 Sonnet model
- ✅ **Auto-Building**: Python virtual environment created automatically
- ✅ **Fast Execution**: Pre-built during space build for instant responses