# Telegram Channel Message Scraper

This script connects to Telegram using the Telethon API and retrieves messages from specified channels, saving them to CSV files for further analysis.

## Features
- Connects to Telegram channels using API credentials
- Retrieves messages with their metadata (date, text, sender ID, message ID)
- Exports data to CSV files with automatic naming based on channel and timestamp
- Handles authentication and error cases

## Prerequisites
- Python 3.8+
- Telegram API credentials (API ID and API Hash)
- Your phone number registered with Telegram

## Setup Instructions

1. **Create and activate a virtual environment** (Important for dependency management)
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   > **Important Note**: If you encounter dependency issues with Telethon, make sure to:
   > 1. Create a fresh virtual environment
   > 2. Activate it
   > 3. Reinstall requirements.txt
   > This helps avoid conflicts with existing package versions.

3. **Configure environment variables**
   - Create a `.env` file in the project root
   - Add your Telegram API credentials:
     ```
     API_ID='your_api_id'
     API_HASH='your_api_hash'
     PHONE_NUMBER='your_phone_number'
     ```

## Usage
1. Update the `channel_id` in the script with your target channel's ID
2. Run the script:
   ```bash
   python telegram_api_connection.py
   ```
3. The script will:
   - Connect to Telegram
   - Authenticate your account
   - Retrieve messages from the specified channel
   - Save them to a CSV file in the current directory

## Output
The script generates CSV files with the naming format:
`telegram_messages_ChannelName_YYYYMMDD_HHMMSS.csv`

Each CSV contains:
- Message date
- Message text
- Sender ID
- Message ID

## Troubleshooting
1. **Dependency Issues**
   - Always use a fresh virtual environment
   - Install requirements in the correct order
   - If issues persist, try removing and recreating the virtual environment

2. **Authentication Issues**
   - Ensure your API credentials are correct
   - Verify you're a member of the target channel
   - Check that your phone number is correctly formatted

3. **Channel Access Issues**
   - Verify the channel ID format (should include -100 prefix for channels)
   - Ensure you're a member of the channel
   - Check if the channel is private/restricted
