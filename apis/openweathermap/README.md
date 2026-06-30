# OpenWeatherMap Client Exercise

API docs: https://openweathermap.org/api

OpenWeatherMap is useful for practicing authenticated API clients, query construction, units, and weather-specific response parsing.

## Credentials

Create a local credentials file that is ignored by git:

```bash
cp apis/openweathermap/.env.example apis/openweathermap/.env
```

Then set:

```bash
OPENWEATHERMAP_API_KEY=replace-me
```

Do not commit the real `.env` file.

## Client acceptance criteria

Build a Python client that can:

- read an API key from the environment
- request current weather for a city, ZIP code, or latitude/longitude
- support optional units such as standard, metric, and imperial
- handle authentication failures clearly
- handle rate-limit and non-2xx responses clearly
- expose async methods for IO-bound operations
- include tests that mock authenticated requests and error responses

## API features to exercise

- API key authentication
- query-string construction
- optional parameters and units
- error handling for auth/rate-limit failures
- response normalization into Python dictionaries or typed models
