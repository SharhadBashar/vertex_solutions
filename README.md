# Allied World

Before running, run `pip install -r requirments.txt`<br>

Go into `python` folder and run the next steps <br>
1. Run `setup.py` which will create the folders 
2. Download the necessary model from HuggingFace: https://huggingface.co/docs/hub/models-downloading
3. Save it into the `model` folder
4. Run `setup_model.py` which will set the config file for the model
5. Put the data you want to summarize into the `data` folder in a json in the following format `{"text": "<DATA HERE>"}` 
6. Run `python main.py`
7. Enter `1` for `single thread`, and `> 1` for `multi thread`
8. Response is saved in `response` folder. Each response has a unique id

<br>
For questions you can email me at sharhad.bashar@uwaterloo.ca

<br><br><br>
Normally I would put `data` in the `.gitignore`, and load that from AWS, but for simplicity, I includded it here