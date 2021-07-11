# TCG Cards Classifier

TCG-Classifier is a Python library for classifying Card images of the Trading Card Games YuGiOh, Magic The Gathering and Pokemon TCG.

## Installation

**1** - Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt (You could also use conda)

```bash
pip install -r requirements.txt
```

**2** - (__OPTIONAL__) you can use the pre-trained model (complete_trained_model) 

## Usage

To classify images run:

```bash
python3 scripts/classifier.py
```
if you want to load a model test data, edit `scripts/classifier.py` like:

```python
start = "load"
dir = 'path/to/card/images'
model_path = 'models/YOUR-MODEL-NAME'

if start == "load":
    ...
```

## To Run Project from Pycharm
Just type in the Python Console of Pycharm:
```bash
execfile('scripts/classifier.py')
```
or simply run the classifier file. 

## Contributing
Maybe you'll be able to contribute soon.

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)