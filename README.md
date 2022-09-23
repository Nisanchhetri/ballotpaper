# Ballot Paper
An image classification project (CV) of AI training phase III.

## Project structure
```
.
├── api
├── app
│   └── app.py
├── docs
├── env
├── logs
├── ml
│   ├── configs
│   │   └── configs.py
│   │   
│   ├── dataset
│   │   └── fetch_data.py
│   │        
│   ├── main.py
│   ├── model
│   │   ├── prepare_model.py
│   │   └── store_model.py
│   │   
│   ├── src
│   │   ├── predict.py
│   │   └── train.py
│   │   
│   └── utils
│       └── preprocess_data.py
├── notebook
│   └── Balot paper.ipynb
├── out
│   ├── count.png
│   ├── DenseNet_accuracy.png
│   ├── DenseNet_loss.png
│   ├── InceptionNet_accuracy.png
│   ├── InceptionNet_loss.png
│   ├── LeNet_accuracy.png
│   ├── LeNet_loss.png
│   ├── Letnet_architecture.png
│   └── test_count.png
├── README.md
└── requirements.txt
```
## Get started
1. First, clone this project with the clone button at the top
2. Create virtual environment in `env` folder using `virtualenv venv python==3.7` command.

## Requirements 
To run this project, first you have to install some dependencies in your virtual environment by following.
1. Activate the installed virtual environment as
```
source venv/bin/activate
```
2. Now, install the project dependencies as
```
pip install -r requirements.txt
```
Now, you are ready to lunch.

## Run
To run this project, you can run `main.py` file which is inside the `ml` folder.
```
python main.py
```
## Complete overview
The complete compiled project can be found inside the `notebook` folder as `Balot paper.ipynb`. You can just simply look over it to see.
