# MIT License

# Copyright (c) 2022 Muhammed

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Telegram Link : https://telegram.dog/Mo_Tech_Group
# Repo Link : https://github.com/PR0FESS0R-99/LuciferMoringstar-Robot
# License Link : https://github.com/PR0FESS0R-99/LuciferMoringstar-Robot/blob/LuciferMoringstar-Robot/LICENSE

START_MESSAGE = """
𝖧𝖾𝗒 {mention}, 𝖭𝗂𝖼𝖾 𝖳𝗈 𝖬𝖾𝖾𝗍 𝗒𝗈𝗎 🌝
𝖬𝗒 𝖭𝖺𝗆𝖾 𝖨𝗌 [{name}](t.me/{username}). 𝖨'𝗆 𝖩𝗎𝗌𝗍 𝖠 𝖲𝗂𝗆𝗉𝗅𝖾 𝖯𝗋𝖾-𝖥𝗎𝗇𝖼𝗍𝗂𝗈𝗇𝖾𝖽 𝖠𝗎𝗍𝗈𝖿𝗂𝗅𝗍𝖾𝗋 𝖡𝗈𝗍.

𝖨𝗍'𝗌 𝖤𝖺𝗌𝗒 𝗍𝗈 𝗎𝗌𝖾 𝗆𝖾; 𝖩𝗎𝗌𝗍 𝖠𝖽𝖽 𝗆𝖾 𝗍𝗈 𝗒𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 𝖺𝗌 𝖠𝖽𝗆𝗂𝗇."""


HELP_MESSAGE = """
𝖧𝖾𝗒 {mention},
𝖨 𝖢𝖺𝗇 𝖦𝗎𝗂𝖽𝖾 𝖸𝗈𝗎 𝖳𝗁𝗋𝗈𝗎𝗀𝗁 𝖠𝗅𝗅 𝖮𝖿𝖿 [{name}](https://t.me/{username})', 𝖢𝗈𝗈𝗅 𝖥𝖾𝖺𝗍𝗎𝗋𝖾𝗌 𝖠𝗇𝖽 𝖧𝗈𝗐 𝖳𝗈 𝖯𝗋𝗈𝗉𝖾𝗋𝗅𝗒 𝖴𝗌𝖾 𝗍𝗁𝖾𝗆. 𝖳𝗁𝖾 𝖡𝗎𝗍𝗍𝗈𝗇𝗌 𝖡𝖾𝗅𝗈𝗐 𝖳𝗈 𝖭𝖺𝗏𝗂𝗀𝖺𝗍𝖾 𝖳𝗁𝖾𝗈𝗎𝗀𝗁 𝖠𝗅𝗅 𝖮𝖿 𝖳𝗁𝖾 𝖬𝗈𝖽𝗎𝗅𝖾𝗌
"""

ABOUT_MESSAGE = """
➲ 𝖬𝗒 𝖭𝖺𝗆𝖾 : [{name}](t.me/{username})
➲ 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 : [𝖠𝗍𝗁𝗎𝗅](https://t.me/athulx80)
➲ 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : 𝖯𝗒𝗍𝗁𝗈𝗇𝟥
➲ 𝖫𝗂𝖻𝗋𝖺𝗋𝗒 : 𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆 {pyro_version}
➲ 𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾 : [𝖬𝗈𝗇𝗀𝗈𝖣𝖡](https://www.mongodb.com/)
➲ 𝖦𝗂𝗍𝖧𝗎𝖻 : [𝖥𝗈𝗅𝗅𝗈𝗐](https://github.com/athulx80)
➲ 𝖦𝗋𝗈𝗎𝗉 : [𝖢𝗅𝗂𝖼𝗄 𝖧𝖾𝗋𝖾](https://t.me/+hC5tRAvQHHplMWQ1)
➲ 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 : [𝖢𝗅𝗂𝖼𝗄 𝖧𝖾𝗋𝖾](https://t.me/+L8SWfrF_7m04ODZl)
➲ 𝖵𝖾𝗋𝗌𝗂𝗈𝗇 : {version}
➲ 𝖲𝖾𝗋𝗏𝖾𝗋 : [𝖧𝖾𝗋𝗈𝗄𝗎](https://dashboard.heroku.com/)
"""

SETTINGS_MESSAGE = """
**𝖢𝗁𝖺𝗇𝗀𝖾 𝖸𝗈𝗎𝗋 𝖲𝖾𝗍𝗍𝗂𝗇𝗀𝗌 𝖥𝗈𝗋Change {title} 𝖠𝗌 𝖸𝗈𝗎𝗋 𝖶𝗂𝗌𝗁.⚙"""

CHAT_LOGS_MESSAGE = """
• **{title}**\n• `{id}`\n• **{join}**"""

SPELLMODE_MESSAGE = """
**__Heyy {mention}!**__
**__Couldn't Find {query} ?  Please Click Your Request Name**__"""

REQUEST_MESSAGE = """
**Requested By:** {mention}\n**Requested Name:** {query}\n™ {group_name}"""

WELCOME_MESSAGE = """
𝖧𝖾𝗒𝗒 {mention}! 𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝖳𝗈 {group_name}!!"""

FILECAPTION_MESSAGE = """
• `{file_name}` \n ᴊᴏɪɴ : @MEmpire_Official_Group"""

ADMIN_CMD_MESSAGE = """
𝙰𝙳𝙼𝙸𝙽𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 :-
\n • /broadcast : 𝚁𝙴𝙿𝙻𝚈 𝙰𝙽𝚃 𝙼𝙴𝙳𝙸𝙰/𝙼𝚂𝙶\n • /total : 𝙶𝙴𝚃 𝙵𝙸𝙻𝙴𝚂 𝙲𝙾𝚄𝙽𝚃\n • /delete : 𝙳𝙴𝙻𝙴𝚃𝙴 𝚂𝙸𝙽𝙶𝙻𝙴 𝙵𝙸𝙻𝙴𝚂\n • /delall : 𝙳𝙴𝙻𝙴𝚃𝙴 𝙰𝙻𝙻 𝙵𝙸𝙻𝙴𝚂\n • /logs : 𝙶𝙴𝚃 𝙱𝙾𝚃 𝙻𝙾𝙶𝚂"""

STATUS_MESSAGE = """
× {bot_name} ꜱᴛᴀᴛᴜꜱ :-
× ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ : {users}\n× ᴛᴏᴛᴀʟ ꜰɪʟᴇꜱ : {files}\n× ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ : {chats}"""

GETFILE_TEXT = """
𝖧𝖾𝗒𝗒 {mention} 𝖸𝗈𝗎𝗋 𝖥𝗂𝗅𝖾𝗌 𝖨𝗌 𝖱𝖾𝖺𝖽𝗒!
\nꜰɪʟᴇɴᴀᴍᴇ : `{file_name}`\n\nꜰɪʟᴇꜱɪᴢᴇ : {file_size}"""

NOT_SUB = """
𝖨 𝖫𝗂𝗄𝖾 𝖸𝗈𝗎𝗋 𝖲𝗆𝖺𝗋𝗍𝗇𝖾𝗌𝗌, 𝖡𝗎𝗍 𝖣𝗈𝗇'𝗍 𝖡𝖾 𝖮𝗏𝖾𝗋𝗌𝗆𝖺𝗋𝗍 😏.\n 𝖥𝗂𝗋𝗌𝗍 𝖲𝗎𝖻𝗌𝖼𝗋𝗂𝖻𝖾 𝖬𝗒 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 😒"""              










