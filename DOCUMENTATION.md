#### Evaluation Criteria 

- Solution to a problem
- Appropriate Variable names
- Appropriate Error Handling
- Logs
- Appropriate comments
- Optimized Solution. Maximum use of inbuilt functions.
- Reusability of code.

Consume -  https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&apikey=NQCFKOVGZASY3EZ9&symbol=MSFT
 
Where symbol = MSFT is company name and is configurable.
Below are few example of company names - 
1) MSFT<br>
2) ABB<br>
3) AAL            AMERICAN AIRLINES GROUP INC<br>
4) AAPL            APPLE INC<br>
5) DELL            DELL TECHNOLOGIES INC<br>
 
 
This API will return Time Series data per date of given company. 
 
- Function which will crawl this API which returns json output and insert into database per company, per date data of all 8 factors.
 
#### Perform below operations on already consumed data -

- function which return all opening, closing, high, low for given company and date, also write this output to csv and json file.

- function which will return per date difference between closing and opening value of a given company.

- function which will calculate per date average of all companies' difference between closing and opening value.

- function which will return maximum number of continuous days where closing value was greater than opening value(where trend is positive) for a given company. 
