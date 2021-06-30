# QUERY ON STOCK DATA

### BEFORE INSTALLING THE PROJECT , EXPLORE `final.ipynb` TO GET AN OVERVIEW !!

### Refer to  `DOCUMENTATION.md` for Problem Statement

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



### `test.py` and `app.py`
```
Run flask app : python app.py 

Open other terminal to run the `test.py` file  

Run : python test.py

#change the url location or company as per your
#requirements in the `test.py` file 
```  
#### POINTS TO REMEMBER
```
1) DATABASE PATH 
2) CONNECTION IS BEING ESTABLISHED OR NOT
3) QUERYING WITH THE CORRECT FORMAT OF COMPANY NAME
4) CHECK THAT YOU ARE WRITING THE CORRECT URL PATH 

```

If anything is not clear from installation to running a query in browser
You can revert me back, I'll be happy to sole your query  :) 


