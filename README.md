### https://github.com/ElliottLandsborough/dog-ceo-api#endpoints

###Cd to project root directory and create a virtualenv to isolate project requirements

`
conda create -y -n venv python=3.8
activate venv
pip install -r requirements.txt
`
### Running tests

`
python -m pytest tests/test_breeds_endpoint/test_all_breeds_endpoint.py
python -m pytest tests/test_breeds_endpoint/test_breeds_endpoint.py
python -m pytest tests/test_breeds_endpoint/test_breed_endpoint.py
`
