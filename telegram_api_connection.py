from telethon import TelegramClient
from telethon.tl.types import PeerChannel
import asyncio
from dotenv import load_dotenv
import os
import pandas as pd

# (Create a new enviornment and reinstall requirements.txt to avoid
# Dependency problems) - Do not forget -> INCORPORATE IN README

# Loading environment variables from .env file
load_dotenv()

# Access Necessary Keys from .env
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone_number = os.getenv('PHONE_NUMBER')

# Creating the telegram client
client = TelegramClient('Retrieving-Messages-From-Channel', api_id, api_hash)


# async functions -> used when tasks involve waiting times, so the program doesn't freeze while waiting
async def main():
    
    print('Starting Client...')
    # await pauses the main function until client.start() finishes doing the job
    # basically waiting for telegram to answer, so the script doesnt proceed until it has 'finalized' the starter action in this case (log-in)
    await client.start(phone=phone_number)

    print('Listing all accessible dialogs')
    # Listing all chats, groups, channels to get their names
    # entities known as dialogs
    #async for dialog in client.iter_dialogs():
    #    print(dialog.name, '| ID: ', dialog.id, '| Type: ', dialog.entity.__class__.__name__ ) # Commenting out 

    try:

        # Once identified the target group name and ID
        channel_id = -1001894858568  
        
        print(f'\nAttempting to access channel with ID: {channel_id}')
        
        # Try to get the channel entity
        channel = await client.get_entity(channel_id)
        
        print(f'\nSuccessfully accessed channel: {getattr(channel, "title", "Unknown")}')
        
        # Creating  a list to store message data
        messages_data = []


        # Fetching messages
        print('\nFetching messages...')
        async for message in client.iter_messages(channel, limit=80):

            # Storing message data in a dictionary
            message_dict = {
                'date': message.date,
                'text': message.text,
                'sender_id': message.sender_id,
                'message_id': message.id,
            }
            messages_data.append(message_dict)

            print(f"\nMessage:")
            print(f"Date: {message.date}")
            print(f"Text: {message.text}")
            print("-----------")

        # Dataframe Generation
        df = pd.DataFrame(messages_data)
        
        # Creating a filename with channel title and timestamp
        channel_title = getattr(channel, "title", "Unknown").replace(" ", "_")
        filename = f"telegram_messages_{channel_title}_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        # Saving to CSV
        df.to_csv(filename, index=False, encoding='utf-8')
        print(f"\nMessages saved to {filename}")
        
            
    except Exception as e:
        print("\nError accessing the channel. Let's troubleshoot:")
        print("1. Verifying your session is properly authenticated...")
        print(f"   - Logged in: {await client.is_user_authorized()}")
        print("\n2. Please check:")
        print("   - You've joined the channel/group from your Telegram app")
        print("   - The channel/group is not private or restricted")
        print("   - You're using the correct channel ID")
        print(f"\nTechnical error details: {str(e)}")

with client:
    client.loop.run_until_complete(main())

print(phone_number)
print('Success')
# python telegram_api_connection.py