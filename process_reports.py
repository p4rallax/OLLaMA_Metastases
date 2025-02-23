import sys
import pandas as pd
import requests
import re
import time

# Accept model name from command-line argument, default to 'mistral'
model_name = sys.argv[1] if len(sys.argv) > 1 else 'mistral'

# CONFIG
input_excel = 'PSMA_reports.xlsx'
prompt_template_file = 'prompt_template.txt'
output_excel = 'skeletal_mets_results.xlsx'
ollama_api_url = 'http://localhost:11434/api/generate'

# Load the input Excel file
df = pd.read_excel(input_excel,header=1)

# Load the prompt template
with open(prompt_template_file, 'r') as f:
    prompt_template = f.read()

results = []

# Wait a few seconds to ensure Ollama is ready (if needed)
time.sleep(5)
df =df.head(10)
for idx, row in df.iterrows():
    study_id = row['StudyID']
    report = row['Text']
    
    # Substitute the report text into the template
    prompt = prompt_template.replace('{report}', report)
    
    payload = {
        "model": model_name,
        "prompt": prompt,
        "stream" : False
    }
    
    try:
        response = requests.post(ollama_api_url, json=payload)
        response.raise_for_status()
        data = response.json()
        # Assuming the response text is in the key 'response'
        result_text = data.get('response', '')
        
        # Parse number from the response text
        match = re.search(r'\b(\d+)\b', result_text)
        skeletal_mets = int(match.group(1)) if match else None
    except Exception as e:
        print(f"Error processing StudyID {study_id}: {e}")
        skeletal_mets = None

    results.append({
        "StudyID": study_id,
        "Skeletal mets": skeletal_mets
    })

# Write results to an Excel file
results_df = pd.DataFrame(results)
results_df.to_excel(output_excel, index=False)

print(f"Results saved to {output_excel}")
