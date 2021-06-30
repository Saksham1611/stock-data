## QUERY ON STOCK DATA

Refer to  `DOCUMENTATION.md` for Problem Statement

<BR>

### Install the project on your System 
```
mkdir -p assignment/project1
cd assignment/project1
```
#### Activate virtual environment

So, you can do a conda installation or simple python v-env . I have gone with python one ! As there I dont need that 

```bash
python3- m venv environmentname(venv)
windows: activate venv(windows)
linux  : source environmentname/bin/activate  
```
```bash
pip install -r requirements.txt
```

#### Why venv ? Package version of project remains unaffected when you update any library in local environment 

```git
git clone <url of the project>
```

#### Optional One more thing to take care of is to attach a requirements file. If you add any new library into it.  
```bash
pip freeze > requirements.txt
```

### Run the project 
I'm using sqlite for this , so I have to create folder before hand 

sqlite ->db-> consumer.db

```python 
python CreateDb.py
```

`Voila` Your Database is Created with all the entries

## Rechecking /Testing /Addition 

You can access all the functions inside the `final.ipynb` file , you can run the notebook for 
seeing how each function is working and also add your own logic .

### `test.py` and `app.py` 
Work is still under progress as desired output format couldn't be obtained 


