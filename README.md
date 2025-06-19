# Sorty-API-test
Sporty - API coding challenge
This project is created as a solution for the Sporty test for API testing.
It uses APIs from: https://weatherstack.com/documentation
Specifically, it tests test current weather endpoint /current

BASE_URL = 'https://api.weatherstack.com'
ENDPOINT = 'current'
LOCATIONS=['New Delhi']
access_key is provided as a parameter - initially it is stored to the repository secrets and in the Github action it will be passed through the cmd params

## Test cases:

### Happy path
1. GET {BASE_URL}/{ENDPOINT}?query={city}&access_key={access_key}
2. Assert response status code = 200
3. Assert location.city = New Delhi  (if more cities provided in LOCATIONS, it will be automatically tested as well)
4. Validate json schema

### Test missing access key
1. GET {BASE_URL}/{ENDPOINT}?query={city}
2. Assert response status code = 200
3. Assert success in data
4. Assert success = false
5. Assert data['error']['type'] = 'missing_access_key'

### Test missing query
1. GET {BASE_URL}/{ENDPOINT}?access_key={access_key}
2. Assert response status code = 200
3. Assert 'success' in data
4. Assert data['success'] = False
5. Assert data['error']['type'] = 'missing_query'


### Test scientific units
1. GET {BASE_URL}/{ENDPOINT}?query={city}&access_key={access_key}&units=s
2. Assert response status code = 200
3. Assert 'location' in data
4. Assert data['location']['name'] = New Delhi
5. Assert data['current']['temperature'] > 200

## Run tests locally
If you have python3 installed:
`python3 -m venv venv`
Then activate venv (this works on mac and linux):
`source venv/bin/activate`
Then install requirements:
`pip install -r requirements.txt`
And start tests with:
`python3 -m pytest --access_key <your_access_key> -o log_cli=true -o log_cli_level=INFO -v tests/ --html=report.html --self-contained-html`
Start report with: 
`open report.html`

## Run tests through the github action
Click on Actions and just start tests
Once tests are executed, there will be report.html provided to review test results



