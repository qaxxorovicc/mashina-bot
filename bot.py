from telethon import TelegramClient, events

API_ID = '34102886'
API_HASH = '03b4cbf8d1a5429d380282944fe6d868'

client = TelegramClient('forwarder_session', API_ID, API_HASH)

SOURCE_CHANNEL = '@moshina_bozorim'
TARGET_CHANNEL = '@ozbe_bozor'

REPLACE_RULES = {
    "Savdoga Admin javobgar emas!!!": "mashina uchun oldindan tolov qilmang. Savdoga admin javobgar emas❗️❗️❗️",
    "https://telegram.me/+65nM4eMsBdIxNDc6": "https://t.me/+aUi-3h501IsyYzAy",
    "baraka bo'pti tabriklaymiz 👏👏👏": "sotildi barakasini bersin✅",
    "‼️Diqat. Mashinani ko'rmasdan turib pul tashlamang!": "Eslatma📌"
}

def replace_text(text):
    if not text:
        return text
    for old, new in REPLACE_RULES.items():
        text = text.replace(old, new)
    return text

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    message = event.message
    original_text = message.text or message.caption or ""
    new_text = replace_text(original_text)
    
    try:
        if message.media:
            await client.send_file(
                TARGET_CHANNEL,
                message.media,
                caption=new_text,
                formatting_entities=message.entities
            )
        elif new_text:
            await client.send_message(
                TARGET_CHANNEL,
                new_text,
                formatting_entities=message.entities,
                link_preview=False
            )
        print("Xabar ko'chirildi!")
    except Exception as e:
        print(f"Xatolik: {e}")

def main():
    print("Bot ishga tushdi...")
    client.start()
    client.run_until_disconnected()

if name == 'main':
    main()
