# Python Rain Alert

This is repo contains code that I generate while working on the [100 Days of Code](https://www.udemy.com/course/100-days-of-code/) udemy course for learning Python.

This repo covers the project for day 35 of the course. This project is a "rain alert" that checks the current weather data and sends a SMS message if it is expected to rain that day. The whole project technically called for the Twilio API to be used to send an SMS message. I didn't really want to do that, so it just pipes out to the console. I already understand how to call data from an API, so I didn't really feel it was necessary to subscribe to a paid API just to finish the project in this way.

![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/darkstar-holdings-edu/python_rain_alert)
![GitHub](https://img.shields.io/github/license/darkstar-holdings-edu/python_rain_alert)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

```sh
# Install dependencies
pipenv install --dev

# Setup pre-commit hooks
pipenv run pre-commit install -t pre-commit
```

## Usage

- `config.json`: Create this file and add your openweather API key.
- `main.py`: Executable to launch the application.

## License

Distributed under the MIT License. See [LICENSE](https://github.com/darkstar-holdings-edu/python_rain_alert/blob/master/LICENSE) for more information.
