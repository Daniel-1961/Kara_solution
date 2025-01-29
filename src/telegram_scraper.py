from telethon import TelegramClient
import asyncio
import csv
import os
import logging
api_id= 27766028
api_hash= a0a5c47fd7d5405d8e74dce6619d5adb
phone_number= +251935448251
target_channels=[
    "DoctorsET",
    "lobelia4cosmetics",
    "yetenaweg",
    "EAHCI"
]
#output directory to store data and csv file
output_dir='telegram_data'
os.mkedirs(output_dir, exist_ok=True)
#CSV file to store scrapped data
csv_file=os.path.join(output_dir,'scraped_data.csv')
#logging configuration
logging.basicConfig(
    filename=os.path.join(output_dir,'scraping.log'),
    level=logging.INFO,
    format='%(asctime)s-%(levelname)s-%(message)s'
    )
#intialize Telegram Client
client=TelegramClient('session_name', api_id, api_hash)
async def scrape_channel(channel_username):
    """
    Scrape messages and images from a Telegram channel.
    """
    try:
        logging.info(f"Scraping data from {channel_username}...")
        messages = []
        async for message in client.iter_messages(channel_username, limit=100):  # Adjust limit as needed
            # Extract message details
            message_data = {
                'channel': channel_username,
                'date': message.date.isoformat(),
                'text': message.text,
                'media': False,
                'image_path': None
            }

            # Check if the message contains media (e.g., images)
            if message.media:
                # Download the image
                image_path = os.path.join(output_dir, f"{channel_username}_{message.id}.jpg")
                await client.download_media(message.media, file=image_path)
                message_data['media'] = True
                message_data['image_path'] = image_path

            # Add the message data to the list
            messages.append(message_data)

        logging.info(f"Scraped {len(messages)} messages from {channel_username}.")
        return messages

    except Exception as e:
        logging.error(f"Error scraping {channel_username}: {e}")
        return []

async def main():
    """
    Main function to scrape data from all target channels.
    """
    # Start the Telegram client
    await client.start(phone=phone_number)

    # Scrape data from all target channels
    all_data = []
    for channel in target_channels:
        channel_data = await scrape_channel(channel)
        all_data.extend(channel_data)
        await asyncio.sleep(5)  # Add delay to avoid rate limits

    # Save scraped data to a CSV file
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['channel', 'date', 'text', 'media', 'image_path'])
        writer.writeheader()
        writer.writerows(all_data)

    logging.info(f"Scraped data saved to {csv_file}.")

# Run the script
if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
  
