import requests
BASE_URL="http://127.0.0.1:5000/"

"""
company_name : eg ABB, DELL etc should be mentioned inside 'ABB' , otherwise you'll get an error 
exmample responses for each function are mentioned below 
 """

response=requests.get(BASE_URL + "difference/'ABB'")
print(response.json())
