# CryptoParsTGBOT

CryptoParsTGBOT is a Telegram bot that allows users to request current cryptocurrency prices and calculate their value in US dollars based on a specified amount (e.g., BTC = $62342, 2 BTC = $124784).

# Getting Started
These instructions will help you set up a copy of the bot locally on your computer or server for development and testing. Follow these steps to configure your copy.

### Prerequisites
Before you begin, ensure you have:

* Python 3.6 or higher
* pip (Python package manager)

### Installation
First, clone the repository to your local computer:

`git clone https://github.com/ssq0-0/CryptoParsTGBOT.git`

Navigate to the project directory:

`cd CryptoParsTGBOT`

Install the necessary dependencies:

`pip install -r requirements.txt`

### Configuration

To ensure the bot works correctly, you need to add your Telegram and CryptoRank API tokens to the `tg_token.py` file:

```python
token='your_token'

api_key = 'your_token'
```

### Running

After configuring, you can start the bot with the command:

`python main.py`

### Deployment on a Server

To deploy the bot on a server, it is recommended to use git to clone the project directly on the server and then repeat the installation and configuration steps.

### Tools Used

* [Python](https://docs.python.org/3/) - Programming language
* [Telegram Bot API](https://core.telegram.org/bots/api) - API for creating bots on Telegram
* [CryptoRank API](https://api.cryptorank.io/docs) - API for obtaining cryptocurrency data

### Author

Project developer - [ssq0-0](https://github.com/ssq0-0)
