#!/bin/bash
MODEL=${1:-mistral}
export OLLAMA_HOST=127.0.0.1
echo "Starting Ollama using model: $MODEL"

# Start Ollama in the background

ollama serve &
OLLAMA_PID=$!
sleep 10
ollama pull $MODEL

# Wait until the API endpoint is ready 
sleep 10

echo "Ollama API is ready. Running the report processor."

python process_reports.py "$MODEL"

kill $OLLAMA_PID