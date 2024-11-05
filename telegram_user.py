from telethon import TelegramClient, events

# Remember to use your own values from my.telegram.org!
api_id = 000000000000000000000                    #replace with the api_id
api_hash = '010101010101010101001010'        #replace with the api_hash

client = TelegramClient('anon', api_id, api_hash)



@client.on(events.NewMessage)
async def handler(event):
    chat = await event.get_chat()
    chat_id = event.chat_id
    print("{}{}".format(chat_id,chat))


    if chat_id == -1002350843605:
        await client.send_message(-1002262485055, event.raw_text)
    
client.start()
client.run_until_disconnected()
