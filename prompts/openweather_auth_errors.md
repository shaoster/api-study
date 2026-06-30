# Drill: OpenWeatherMap Auth and Errors

Timebox: 45 minutes

Docs: https://openweathermap.org/current

## Task

Implement a small async function that fetches current weather for a city.

Start from something like:

```python
async def get_current_weather(city: str, units: str = "metric") -> dict:
    ...
```

## Requirements

- Read the API key from `OPENWEATHERMAP_API_KEY`.
- Send the key using the API's expected query parameter.
- Include city and units in the request.
- Raise a clear exception if the API key is missing.
- Raise a clear exception for 401/403 auth failures.
- Raise a clear exception for 429 rate limits.
- Return the decoded JSON on success.

## Sample response shape

```json
{
  "weather": [
    {"main": "Clouds", "description": "broken clouds"}
  ],
  "main": {
    "temp": 21.5,
    "humidity": 65
  },
  "name": "San Francisco"
}
```

## Follow-up prompts an interviewer might add

- Normalize the result into `{city, temp, humidity, description}`.
- Support latitude/longitude instead of city name.
- Validate `units`.
- Add a tiny in-memory cache.
- Avoid logging or printing secrets.

## Tests to consider

- Missing API key raises before making a request.
- Successful request includes `q`, `units`, and API key params.
- 401/403 responses raise an auth-specific exception.
- 429 response raises a rate-limit-specific exception.
- Successful response is returned unchanged or normalized, depending on your chosen interface.
