import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonX import app, Telegram
@app.on_message(
    command(["زد إي سورس","سورس","السورس","سورس زد إي", "زد إي"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/dd6c46b812395a1b607e9.jpg",
        caption=f"""
╭──── • ◈ • ────╮ 
么  [𝒔𝒐𝒖𝒓𝒄𝒆 𝒛𝒆♡](t.me/UI_XB)
么 [𝒎𝒐𝒅𝒚]♡(t.me/UP_UO)
╰──── • ◈ • ────╯ 
  
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝒎𝒐𝒅𝒚♡", url=f"https://t.me/UP_UO"), 
                ],[
                    InlineKeyboardButton(
                        "𝒔𝒐𝒖𝒓𝒄𝒆 𝒛𝒆 ♡", url=f"t.me/UI_XB"),
                ],

            ]

        ),

    )
@app.on_message(
   command(["احمد","المبرمج احمد","المطور احمد","حمودي"])
)

@app.on_edited_message(command(["احمد","المبرمج احمد","احمد""حمودي"])
)
async def zohary(client: Client, message: Message):
  usr = await app.get_users(5650717789)
  user = await client.get_chat(5650717789)
  Bio = user.bio
  name = usr.first_name
  async for photo in app.get_chat_photos(5650717789,limit=1):
    await message.reply_photo(photo.file_id,       caption=f"""ᦔꫀꪜ | - {usr.mention} 🕷
                       
ꪊ𝘴ꫀ𝘳 ᦔꫀꪜ | - @{usr.username} 🕷
                       
ႦᎥ᥆ | - {Bio} 🕷       
                         
Ꭵժ | - 5650717789 🕷 """,
reply_markup=InlineKeyboardMarkup(
          [              
            [          
              InlineKeyboardButton (name, url=f"https://t.me/{usr.username}")
            ],             
          ]                 
       )                     
    )
    zoharyus = usr.mention
    sender_id = message.from_user.id
    message_link = await Telegram.get_linok(message)
    sender_name = message.from_user.first_name
    invitelink = await app.export_chat_invite_link(message.chat.id)
    await app.send_message(5650717789, f"مبرمجي العزيز {zoharyus}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name} \n\n لينك الماسدج : {message_link} \n\n لينك البار : {invitelink}")
@app.on_message(
    command(["موضي","المبرمج مودي","مودي"])
)
@app.on_edited_message(command(["موضي","المبرمج مودي","مودي"])
)
async def zohary(client: Client, message: Message):
  usr = await app.get_users(5650717789)
  user = await client.get_chat(5650717789)
  Bio = user.bio
  name = usr.first_name
  async for photo in app.get_chat_photos(5650717789,limit=1):
    await message.reply_photo(photo.file_id,       caption=f"""ᦔꫀꪜ | - {usr.mention} 🕷
                       
ꪊ𝘴ꫀ𝘳 ᦔꫀꪜ | - @{usr.username} 🕷
                       
ႦᎥ᥆ | - {Bio} 🕷       
                         
Ꭵժ | - 5650717789 🕷 """,
reply_markup=InlineKeyboardMarkup(
          [              
            [          
              InlineKeyboardButton (name, url=f"https://t.me/{usr.username}")
            ],             
          ]                 
       )                     
    )
    zoharyus = usr.mention
    sender_id = message.from_user.id
    message_link = await Telegram.get_linok(message)
    sender_name = message.from_user.first_name
    invitelink = await app.export_chat_invite_link(message.chat.id)
    await app.send_message(5650717789, f"مبرمجي العزيز {zoharyus}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name} \n\n لينك الماسدج : {message_link} \n\n لينك البار : {invitelink}")
@app.on_message(
    command(["مولتو","المبرمج مولتو","المطور مولتو"])
)
@app.on_edited_message(command(["مودي","المبرمج مودي","المطور مودي"])
)
async def zohary(client: Client, message: Message):
  usr = await app.get_users(5650717789)
  user = await client.get_chat(5650717789)
  Bio = user.bio
  name = usr.first_name
  async for photo in app.get_chat_photos(5650717789,limit=1):
    await message.reply_photo(photo.file_id,       caption=f"""ᦔꫀꪜ | - {usr.mention} 🕷
                       
ꪊ𝘴ꫀ𝘳 ᦔꫀꪜ | - @{usr.username} 🕷
                       
ႦᎥ᥆ | - {Bio} 🕷       
                         
Ꭵժ | - 5650717789 🕷 """,
reply_markup=InlineKeyboardMarkup(
          [              
            [          
              InlineKeyboardButton (name, url=f"https://t.me/{usr.username}")
            ],             
          ]                 
       )                     
    )
    zoharyus = usr.mention
    sender_id = message.from_user.id
    message_link = await Telegram.get_linok(message)
    sender_name = message.from_user.first_name
    invitelink = await app.export_chat_invite_link(message.chat.id)
    await app.send_message(5650717789, f"مبرمجي العزيز {zoharyus}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name} \n\n لينك الماسدج : {message_link} \n\n لينك البار : {invitelink}")
                        
