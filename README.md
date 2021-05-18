# api-demo-1

REST API to fetch the bank details using the query params

Data Source from this [repository](https://github.com/snarayanank2/indian_banks)

it can be hosted on Heroku, [steps to host](https://devcenter.heroku.com/articles/getting-started-with-python)

a test application is hosted on Heroku, it can be accessed by following urls

Autocomplete API to return possible matches based on the branch name ordered by IFSC code (ascending order) with limit and offset.
```
curl https://dry-lake-63632.herokuapp.com/api/branches/autocomplete?q=RTGS&limit=3&offset=0
```

Search API to return possible matches across all columns and all rows, ordered by IFSC code (ascending order) with limit and offset.
```
curl https://dry-lake-63632.herokuapp.com/api/branches?q=Bangalore&limit=4&offset=0
```
