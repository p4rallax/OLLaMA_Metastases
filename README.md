To run:

1. Download all files from the repo.
2. Navigate to the downloaded folder.
3. Copy the reports file to the folder with the rest of the files. Please ensure the reports file is named as PSMA_reports.xlsx. Also note that this docker image runs on the entire excel sheet.
4. IF required, modify the prompt template file, which contains the prompt being used with LLMs. Please ensure to keep a {report} tag so that the code replaces it with the actual report from the excel file later during execution.
5. Build the docker image using (ollama-pipeline-full can be replaced with a name of your choice) :
     ``` docker build -t ollama-pipeline-full . ```
6. Run the docker container using (replace model_name with desired ollama model (eg llama2), and also change path to output folder.):
   ``` docker run --gpus all --rm -v path/to/output/folder:/app   -v /path/to/models/folder:/models ollama-pipeline-full model_name ```
