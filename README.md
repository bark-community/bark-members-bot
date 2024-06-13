# BARK Membership Payments Bot

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Running the Bot](#running-the-bot)
7. [Usage](#usage)
8. [Folder Structure](#folder-structure)
9. [Code Overview](#code-overview)
    - [Configuration](#configuration)
    - [Handlers](#handlers)
    - [Utils](#utils)
    - [Main](#main)
10. [License](#license)

## Introduction

The BARK Membership Payments Bot is a Telegram bot that facilitates the creation of paid Telegram groups where users can charge for access using SOL (Solana), BARK, and CNFT (Solana Non-Fungible Token) payments. This bot provides a streamlined solution for creators to monetize content and services on the Telegram platform.

## Features

- **Easy Payment Verification:** Supports payment verification using SOL, BARK, and CNFT tokens.
- **Automated Group Management:** Automatically adds users to Telegram groups upon successful payments or token ownership.
- **Customizable Settings:** Allows configuration of payment amounts, wallet addresses, and CNFT token IDs for tiered access.

## Requirements

- Python 3.7+
- Telegram Bot API token
- Solana wallet address
- BARK token address
- CNFT token addresses
- Telegram group chat IDs

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/bark-community/bark_membership_payments_bot.git
    cd bark_membership_payments_bot
    ```

2. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

## Configuration

Edit the `config/settings.py` file with your bot token, wallet addresses, payment amounts, CNFT token IDs, and Telegram group chat IDs.

Example `settings.py`:

```python
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
SOL_WALLET_ADDRESS = 'YOUR_SOL_WALLET_ADDRESS'
BARK_WALLET_ADDRESS = 'BARK1X2VgwF1auwH6NzwLgXcAuMzrGnfsssAxaMczJLV'
SOL_PAYMENT_AMOUNT = 1  # Amount in SOL required to join
BARK_PAYMENT_AMOUNT = 100000  # Amount in BARK required to join
CNFT_PROSPECT_TIER_TOKEN = 'PROSPECT_TOKEN_ID'
CNFT_FULL_MEMBER_TIER_TOKEN = 'FULL_MEMBER_TOKEN_ID'
CNFT_VETERAN_MEMBER_TIER_TOKEN = 'VETERAN_TOKEN_ID'
CNFT_SOLDIER_TIER_TOKEN = 'SOLDIER_TOKEN_ID'
THE_PEAKY_BARKERS_CLUB_CHAT_ID = 'YOUR_CLUB_GROUP_CHAT_ID'
THE_PEAKY_BARKERS_CHAT_ID = 'YOUR_BARKERS_CHAT_ID'
BARKERS_PROSPECT_GROUP_CHAT_ID = 'YOUR_PROSPECT_GROUP_CHAT_ID'
BARKERS_FULL_MEMBER_GROUP_CHAT_ID = 'YOUR_FULL_MEMBER_GROUP_CHAT_ID'
BARKERS_VETERAN_GROUP_CHAT_ID = 'YOUR_VETERAN_GROUP_CHAT_ID'
BARKERS_SOLDIER_GROUP_CHAT_ID = 'YOUR_SOLDIER_GROUP_CHAT_ID'
```

## Running the Bot

To start the bot, simply run:

```sh
python main.py
```

## Usage

Users can join the paid group by sending the `/join <wallet_address>` command to the bot.

Example:

```
/join 5Q2sjk4F4q6a8H6Ryw24mjeHD2Uo1tRAz5Fd3VL9y2Qz
```

## Folder Structure

```
bark_payments_bot/
├── config/
│   ├── __init__.py
│   ├── settings.py
├── handlers/
│   ├── __init__.py
│   ├── join_group.py
│   ├── payment_verification.py
├── utils/
│   ├── __init__.py
│   ├── solana_utils.py
│   ├── bark_utils.py
│   ├── cnft_utils.py
├── main.py
├── requirements.txt
├── README.md
```

## Code Overview

### Configuration

**config/settings.py**

This file contains configuration variables like the bot token, wallet addresses, payment amounts, CNFT token IDs, and Telegram group chat IDs.

### Handlers

**handlers/join_group.py**

This file contains the handler function for the `/join` command. It checks for SOL, BARK, and CNFT payments or token ownership and adds the user to the respective groups.

### Utils

**utils/solana_utils.py**

This file contains functions to interact with the Solana blockchain, such as checking SOL payments.

**utils/bark_utils.py**

This file contains functions to interact with the BARK token, such as checking BARK payments.

**utils/cnft_utils.py**

This file contains functions to interact with CNFT tokens, such as checking CNFT token ownership.

### Main

**main.py**

This is the main entry point of the bot. It initializes the bot, registers handlers, and starts polling.

## License

This project is licensed under the MIT License.