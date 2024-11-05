from telethon import TelegramClient, events
import asyncio

# Replace these with your own credentials
api_id = '00000000000'      # replace with the api_id
api_hash = '0101010101010101'          #replace with the api_hash
phone_number = '010101010101010'       #replace with the phone number
target_chat_id = '01010101010101010'  # Replace with the target chat ID

# Create a client instance
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone_number)
    
    @client.on(events.NewMessage)
    async def handler(event):
        # Forward the message to the target chat
        if event.message:
            await event.message.forward_to(target_chat_id)

    # Keep the script running
    print("Listening for new messages...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
