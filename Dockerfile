# Use an NVIDIA PyTorch base image for GPU support
FROM nvcr.io/nvidia/pytorch:23.12-py3

# Set noninteractive installation
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt update && apt install -y curl git python3-pip

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Install Python dependencies
RUN pip install pandas openpyxl requests

# Create app directory
WORKDIR /app

# Copy processing script, input files, prompt template, and entrypoint script into container
COPY process_reports.py .
COPY PSMA_reports.xlsx .
COPY prompt_template.txt .
COPY entrypoint.sh .

# Expose Ollama API port (if needed)
EXPOSE 11434

# Make the entrypoint executable and set it as the entrypoint
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]