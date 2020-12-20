from telegram.ext import Updater
import os
from dotenv import load_dotenv
load_dotenv()

BOT_API = os.getenv("BOT_API")
updater = Updater(token=BOT_API, use_context=True)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="""Hey there, Dear BookCrush member!
I can help you request any book in the group easily.
Also you can make yourself familiar with the rules of @bookcrushgroup.
Currently I only work in inline mode. so why don't you type "@bkcrushbot" in the text box below and see how you can request any ebook/audiobook/Kindle Unlimited book.
You can also try <code>@bkcrushbot grouprules</code> to know the rules of the @bookcrushgroup. <code>@bkcrushbot press</code> to know the rules of @bookcrushpress.
""", parse_mode='HTMl')

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

#def echo(update, context):
#    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

#from telegram.ext import MessageHandler, Filters
#echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
#dispatcher.add_handler(echo_handler)

# def caps(update, context):
#     # if context.args == null:
#     #     context.bot.send_message(chat_id=update.effective_chat.id, text="send some text, you fool!")
#     print("arguments are" + context.args)
#     text_caps = ' '.join(context.args).upper()
#     context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

# caps_handler = CommandHandler('caps', caps)
# dispatcher.add_handler(caps_handler)

from uuid import uuid4
from telegram import InlineQueryResultArticle, InputTextMessageContent
def inline_caps(update, context):
    query = update.inline_query.query
    results = list()
    if query.lower() == '' or query.lower().strip() == 'help':
        results.append(
                    InlineQueryResultArticle(
                    id=uuid4(),
                    title='How to use me to make a request:',
                    input_message_content=InputTextMessageContent("""Type r,BookName(s),AuthorName,AmazonLink(for audible/KU),Language Tags(if any)""", parse_mode='HTML'),
                    description='Type r, BookName(s), AuthorName, AmazonLink(for audible/KU), Language Tags(if any)',
                )
        )
    #Individual rules
    if query.lower().strip() == '1':
            results = list()
            results.append(
            InlineQueryResultArticle(
                id=uuid4(),
                title='1. Before You Request -> 1.1. Verify the name and author of the ebook/audiobook...',
                input_message_content=InputTextMessageContent("""<b>1. Before You Request</b>

        1.1. Verify the name and author of the ebook/audiobook and that the book has been released in the particular format in which you want(ebook/audiobook).""", parse_mode ='HTML')))
            results.append(
            InlineQueryResultArticle(
                id=uuid4(),
                title='1.2. If you want a book series or multiple books...',
                input_message_content=InputTextMessageContent("""
        1.2. If you want a <i>book series or multiple books</i> then individually request each one with correct names of the titles.""", parse_mode='HTML')))
            results.append(
            InlineQueryResultArticle(
                id=uuid4(),
                title='1.3. Only request for ebooks which are preferably on...',
                input_message_content=InputTextMessageContent("""
        1.3. Only request for ebooks which are preferably on <i>Amazon</i> and audiobooks that are on <i>Audible</i>.""", parse_mode='HTML')))
            results.append(
            InlineQueryResultArticle(
                id=uuid4(),
                title='1.4. DON\'T request for books that are...',
                input_message_content=InputTextMessageContent("""
        1.4. <b>DON'T</b> request for books that are;

            1.4.1. Available only in <i>paperback/hardcover</i>.

            1.4.2. <a href="https://t.me/BookCrushGroup/165744">Academic textbooks</a>.

            1.4.3. In <a href="https://t.me/BookCrushGroup/141180">DMCA list</a>""", parse_mode='HTML', disable_web_page_preview=True)))
            results.append(
            InlineQueryResultArticle(
                id=uuid4(),
                title='1.5. DON\'T be choosy about...',
                input_message_content=InputTextMessageContent("""
        1.5. <b>DON'T</b> be choosy about ebook formats or narrators for audiobooks.""", parse_mode='HTML')))
            results.append(
            InlineQueryResultArticle(
                id=uuid4(),
                title='1.6. DON\'T just send links or covers...',
                input_message_content=InputTextMessageContent("""
        1.6. <b>DON'T</b> just send links or covers of books that you want. Instead be a good lad and follow the request format.""", parse_mode='HTML')))
            results.append(
            InlineQueryResultArticle(
                id=uuid4(),
                title='1.7. Search before requesting...',
                input_message_content=InputTextMessageContent("""
        1.7. Click on the 🔍 icon in the top right and search if that ebook/audiobook has been shared already in the group. Follow this tutorial on how to search in the group.""", parse_mode='HTML')))
        
    if query.lower().strip() == '2':
            results = list()
            results.append(
            InlineQueryResultArticle(
                id=uuid4(),
                title='2. Request Format -> 2.1. If that book has not been shared before, request using...',
                input_message_content=InputTextMessageContent("""<b>2. Request Format</b>

        2.1. If that book has not been shared before, request using the following format:
    <code>#request
    Book's name
    Author's name 
    #ebook or #audiobook</code>
    [Amazon link to audiobook/KU book, if applicable]""", parse_mode ='HTML')))
            results.append(
            InlineQueryResultArticle(
                id=uuid4(),
                title='2.2.1. ebook example',
                input_message_content=InputTextMessageContent("""
            2.2.1. ebooks:
    <code>#request
    Sapiens: A Brief History of Humankind
    Yuval Noah Harari
    #ebook</code>""", parse_mode='HTML')))
            results.append(
            InlineQueryResultArticle(
                id=uuid4(),
                title='2.2.2. Audible Audiobook example',
                input_message_content=InputTextMessageContent("""
        2.2.2. Audible Audiobooks:
    <code>#request
    Dark Matter
    Blake Crouch
    #audiobook
    https://www.audible.in/pd/Dark-Matter-Audiobook/B07B7BFH4M</code>""", parse_mode='HTML', disable_web_page_preview=True)))
            results.append(
            InlineQueryResultArticle(
                id=uuid4(),
                title='2.2.3. Kindle Unlimited book example',
                input_message_content=InputTextMessageContent("""
        2.2.3. Kindle Unlimited(KU) books:
    <code>#request
    Harry Potter and the Chamber of Secrets
    J.K. Rowling
    #KU
    https://www.amazon.in/Harry-Potter-Chamber-Secrets-Rowling-ebook/dp/B019PIOJY0</code>""", parse_mode='HTML', disable_web_page_preview=True)))

    if query.lower().strip() == '3':
        results.append(
        InlineQueryResultArticle(
                id=uuid4(),
                title='3. Hashtags',
                input_message_content=InputTextMessageContent("""<b>3. Hashtags</b>

    Include appropriate hashtags in your requests which will help us track them better:

        3.1. For languages other than English, Use <code>#Hindi</code>, <code>#Marathi</code>, <code>#Spanish</code> and so on.

        3.2. For Kindle Unlimited - <code>#KU</code> ; Audible Audiobooks - <code>#audiobook</code> or #audible (provide their links as well).""", parse_mode='HTML'),
                description='Hashtags to include in your request'
            )
        )
    if query.lower().strip() == '4':
        results.append(
        InlineQueryResultArticle(
                id=uuid4(),
                title='4. Request Limits',
                input_message_content=InputTextMessageContent("""<b>4. Request Limits</b>

        4.1. <b>DON'T</b> request for more than 3 books(ebooks+audiobooks) in a day. Exceeding it will trigger @ShiiinaBot to delete your request and you will have to wait for 24 hours to request again. Deleting and re-requesting if you made any mistake in your original request will not reset the count, instead learn how to Edit your message.

        4.2. <b>Hoarding</b> books(even within request limit) is strictly not tolerated. Request only what you want to read/listen in the near future.""", parse_mode='HTML'),
            description='How many can you request per day?')
        )
    if query.lower().strip() == '5':
            results = list()
            results.append(
            InlineQueryResultArticle(
                id=uuid4(),
                title='5. After you request -> 5.1. Sit back and wait, DON\'T tag or PM admins...',
                input_message_content=InputTextMessageContent("""<b>5. After You Request</b> 

        5.1. Sit back and wait, DON'T tag or PM admins. """, parse_mode ='HTML')))
            results.append(
            InlineQueryResultArticle(
                id=uuid4(),
                title='5.2. Asking Updates',
                input_message_content=InputTextMessageContent("""
        5.2. <b>DON'T</b> ask for updates on the book before 48 hours. You will receive an @ notification from a contributor or BookCrush Buddy when it is fulfilled.""", parse_mode='HTML')))
            results.append(
            InlineQueryResultArticle(
                id=uuid4(),
                title='5.3. Wait 48 Hours',
                input_message_content=InputTextMessageContent("""
        5.3. If your request is not fulfilled, repost after <b>48 hours</b>. Subsequent reminders should also be spaced out 48 hours between each one.""", parse_mode='HTML')))
            results.append(
            InlineQueryResultArticle(
                id=uuid4(),
                title='5.4. DON\'T ask for specific format',
                input_message_content=InputTextMessageContent("""
        5.4. After you get the book, <b>DON'T</b> be lazy and ask us for a specific format like pdf, epub etc. Convert it yourself online(@SmartConverter_bot or @cloud_convert_bot). """, parse_mode='HTML')))

    if query.lower().strip() == '6':
            results = list()
            results.append(
            InlineQueryResultArticle(
                id=uuid4(),
                title='6. Communication -> 6.1. Use English at all times....',
                input_message_content=InputTextMessageContent("""<b>6. Communication</b>

        6.1. Use English at all times. """, parse_mode ='HTML')))
            results.append(
            InlineQueryResultArticle(
                id=uuid4(),
                title='6.2. Asking Updates',
                input_message_content=InputTextMessageContent("""
        6.2. Refrain from any off-topic chatter.""", parse_mode='HTML')))
            results.append(
            InlineQueryResultArticle(
                id=uuid4(),
                title='6.3. Wait 48 Hours',
                input_message_content=InputTextMessageContent("""
        6.3. <b>DON'T</b> PM any group member without permission.""", parse_mode='HTML')))
            results.append(
            InlineQueryResultArticle(
                id=uuid4(),
                title='6.4. DON\'T ask for specific format',
                input_message_content=InputTextMessageContent("""
        6.4. <b>DON'T</b> spam with gifs/stickers, promotional messages or channel/group invites(t.me links) either in group or in PM. """, parse_mode='HTML')))
    
    if query.lower().strip() == '7':
        results.append(
        InlineQueryResultArticle(
                id=uuid4(),
                title='7. Disallowed Names/Usernames',
                input_message_content=InputTextMessageContent("""<b>7. Disallowed Names/Usernames</b>

        7.1. Names/Usernames containing single letter/double letters, NSFW words, Just emojis, special characters, punctuation marks or Annoying Unicode/RTL characters which mess up the Telegram UI. 

        <i>Anyone violating this rule will be muted until the username no longer violates any of the above conditions. Message any admin to be un-muted once you comply with the name rule.</i>""", parse_mode='HTML'),
            )
        )
    if query.lower().strip() == '8':
            results = list()
            results.append(
            InlineQueryResultArticle(
                id=uuid4(),
                title='8. What will get you muted/kicked/(f)banned? -> 8.1. Violating any of the....',
                input_message_content=InputTextMessageContent("""<b>8. What will get you muted/kicked/(f)banned?</b>

        8.1. <b>Violating</b> any of the above rules(1-7) will be first met with a friendly notice, repeated violations will each lead to a warning and 5 such warnings to getting muted forever.""", parse_mode ='HTML')))
            results.append(
            InlineQueryResultArticle(
                id=uuid4(),
                title='8.2. Abuse',
                input_message_content=InputTextMessageContent("""
        8.2. <b>Abusing</b> members/admins in PM will directly lead to getting fedbanned in all BookCrush groups.""", parse_mode='HTML')))
            results.append(
            InlineQueryResultArticle(
                id=uuid4(),
                title='8.3. Hoarding',
                input_message_content=InputTextMessageContent("""
        8.3. <b>Hoarding</b> books without considering the time and effort of admins/contributors that goes into ripping ebooks/audiobooks. Such violators will be tracked and muted/banned accordingly.""", parse_mode='HTML')))
            results.append(
            InlineQueryResultArticle(
                id=uuid4(),
                title='8.4. Alt IDs',
                input_message_content=InputTextMessageContent("""
        8.4. <b>Having</b> one or more Alternate IDs so as to bypass the request limit. """, parse_mode='HTML')))

    #END of individual rules
    #Full group rules
    if query.lower().startswith('grouprules'):
        results.append(
        InlineQueryResultArticle(
                id=uuid4(),
                title='BookCrush:Requests',
                input_message_content=InputTextMessageContent("https://telegra.ph/BookCrushRequests-Group-Rules-12-03", disable_web_page_preview=False),
                description='Complete Rules of the Group',
                thumb_url='https://telegra.ph/file/c20df171f38eda7ad316f.png',
                thumb_width=30,
                thumb_height=30
            )
        )
        #context.bot.answer_inline_query(update.inline_query.id, results)
        #results = list()

        results.append(
            InlineQueryResultArticle(
                id=uuid4(),
                title='1. Before You Request',
                input_message_content=InputTextMessageContent("""<b>1. Before You Request</b>

        1.1. Verify the name and author of the ebook/audiobook and that the book has been released in the particular format in which you want(ebook/audiobook).

        1.2. If you want a <i>book series or multiple books</i> then individually request each one with correct names of the titles.

        1.3. Only request for ebooks which are preferably on <i>Amazon</i> and audiobooks that are on <i>Audible</i>.

        1.4. <b>DON'T</b> request for books that are;

            1.4.1. Available only in <i>paperback/hardcover</i>.

            1.4.2. <a href="https://t.me/BookCrushGroup/165744">Academic textbooks</a>.

            1.4.3. In <a href="https://t.me/BookCrushGroup/141180">DMCA list</a>.

        1.5. <b>DON'T</b> be choosy about ebook formats or narrators for audiobooks.

        1.6. <b>DON'T</b> just send links or covers of books that you want. Instead be a good lad and follow the request format.

        1.7. Click on the 🔍 icon in the top right and search if that ebook/audiobook has been shared already in the group. Follow this tutorial on how to search in the group.""", parse_mode='HTML'),
            description='What you need to remember before requesting?')
        )
        
        
        results.append(
            InlineQueryResultArticle(
                id=uuid4(),
                title='2. Request Format',
                input_message_content=InputTextMessageContent("""<b>2. Request Format</b>

        2.1. If that book has not been shared before, request using the following format:
    <code>#request
    Book's name
    Author's name 
    #ebook or #audiobook</code>
    [Amazon link to audiobook/KU book, if applicable]

        2.2. Examples

            2.2.1. ebooks:
    <code>#request
    Sapiens: A Brief History of Humankind
    Yuval Noah Harari
    #ebook</code>

            2.2.2. Audible Audiobooks:
    <code>#request
    Dark Matter
    Blake Crouch
    #audiobook
    https://www.audible.in/pd/Dark-Matter-Audiobook/B07B7BFH4M</code>

            2.2.3. Kindle Unlimited(KU) books:
    <code>#request
    Harry Potter and the Chamber of Secrets
    J.K. Rowling
    #KU
    https://www.amazon.in/Harry-Potter-Chamber-Secrets-Rowling-ebook/dp/B019PIOJY0</code>""", parse_mode='HTML')
            )
        )

        results.append(
        InlineQueryResultArticle(
                id=uuid4(),
                title='3. Hashtags',
                input_message_content=InputTextMessageContent("""<b>3. Hashtags</b>

    Include appropriate hashtags in your requests which will help us track them better:

        3.1. For languages other than English, Use <code>#Hindi</code>, <code>#Marathi</code>, <code>#Spanish</code> and so on.

        3.2. For Kindle Unlimited - <code>#KU</code> ; Audible Audiobooks - <code>#audiobook</code> or #audible (provide their links as well).""", parse_mode='HTML'),
                description='Hashtags to include in your request'
            )
        )

        results.append(
        InlineQueryResultArticle(
                id=uuid4(),
                title='4. Request Limits',
                input_message_content=InputTextMessageContent("""<b>4. Request Limits</b>

        4.1. <b>DON'T</b> request for more than 3 books(ebooks+audiobooks) in a day. Exceeding it will trigger @ShiiinaBot to delete your request and you will have to wait for 24 hours to request again. Deleting and re-requesting if you made any mistake in your original request will not reset the count, instead learn how to Edit your message.

        4.2. <b>Hoarding</b> books(even within request limit) is strictly not tolerated. Request only what you want to read/listen in the near future.""", parse_mode='HTML'),
            description='How many can you request per day?')
        )

        results.append(
        InlineQueryResultArticle(
                id=uuid4(),
                title='5. After You Request',
                input_message_content=InputTextMessageContent("""<b>5. After You Request</b> 

        5.1. Sit back and wait, DON'T tag or PM admins. 

        5.2. <b>DON'T</b> ask for updates on the book before 48 hours. You will receive an @ notification from a contributor or BookCrush Buddy when it is fulfilled.

        5.3. If your request is not fulfilled, repost after <b>48 hours</b>. Subsequent reminders should also be spaced out 48 hours between each one.

        5.4. After you get the book, <b>DON'T</b> be lazy and ask us for a specific format like pdf, epub etc. Convert it yourself online(@SmartConverter_bot or @cloud_convert_bot). """, parse_mode='HTML'),
            description='What you need to do after you request?')
        )

        results.append(
        InlineQueryResultArticle(
                id=uuid4(),
                title='6. Communication',
                input_message_content=InputTextMessageContent("""<b>6. Communication</b>

        6.1. Use English at all times.

        6.2. Refrain from any off-topic chatter.

        6.3. <b>DON'T</b> PM any group member without permission.

        6.4. <b>DON'T</b> spam with gifs/stickers, promotional messages or channel/group invites(t.me links) either in group or in PM.""", parse_mode='HTML'),
            description='Etiquette for communicating in the group')
        )

        results.append(
        InlineQueryResultArticle(
                id=uuid4(),
                title='7. Disallowed Names/Usernames',
                input_message_content=InputTextMessageContent("""<b>7. Disallowed Names/Usernames</b>

        7.1. Names/Usernames containing single letter/double letters, NSFW words, Just emojis, special characters, punctuation marks or Annoying Unicode/RTL characters which mess up the Telegram UI. 

        <i>Anyone violating this rule will be muted until the username no longer violates any of the above conditions. Message any admin to be un-muted once you comply with the name rule.</i>""", parse_mode='HTML'),
            )
        )

        results.append(
        InlineQueryResultArticle(
                id=uuid4(),
                title='8. What will get you muted/kicked/(f)banned?',
                input_message_content=InputTextMessageContent("""<b>8. What will get you muted/kicked/(f)banned?</b>

        8.1. <b>Violating</b> any of the above rules(1-7) will be first met with a friendly notice, repeated violations will each lead to a warning and 5 such warnings to getting muted forever.

        8.2. <b>Abusing</b> members/admins in PM will directly lead to getting fedbanned in all BookCrush groups.

        8.3. <b>Hoarding</b> books without considering the time and effort of admins/contributors that goes into ripping ebooks/audiobooks. Such violators will be tracked and muted/banned accordingly.

        8.4. <b>Having</b> one or more Alternate IDs so as to bypass the request limit.""", parse_mode='HTML'),
            description='Things you shouldn\'t do to be a good member')
        )
    
    from telegram import InlineKeyboardButton, InlineKeyboardMarkup
    #requesting using the bot
    if query.lower().strip().startswith('r'):
        origquery = query
        request = query.split(',',4)
        fullrequest = ''
        for req in request:
            if(req == 'r'):
                continue;
            #if(req.isspace()):
            #    continue;
            fullrequest = fullrequest + req.strip() + """\n""" #if req.startswith('http') else fullrequest + req.strip().title() + """\n"""
        results = list()
        keyboard = [
        [
            InlineKeyboardButton("Repost/Edit", switch_inline_query_current_chat=origquery),
            
        #],
        #[
            InlineKeyboardButton("New Request", switch_inline_query_current_chat=''),
        ]
        ]
        markup = InlineKeyboardMarkup(keyboard)
        try:
            results.append(
            InlineQueryResultArticle(
            id=uuid4(),
            title='Request ebook: '+request[1].strip().title()+' ; '+request[2].strip().title(),
            input_message_content=InputTextMessageContent("""#request\n"""+
    fullrequest.strip()+
    """\n#ebook"""
    , parse_mode='HTML', disable_web_page_preview=True),
                reply_markup= markup,
                description='Request an ebook',
                thumb_url='https://telegra.ph/file/f9bc07b2d216238b2a910.png',
                thumb_width=30,
                thumb_height=30
            )
        )
        except:
            #results = list()
            results.append(
                InlineQueryResultArticle(
                id=uuid4(),
                title='Author Name Missing!',
                input_message_content=InputTextMessageContent("""<i>Author Name Missing!\nTry again...\nType r, BookName(s), AuthorName, Language Tags(if any)</i>""", parse_mode='HTML'),
                description='Type r, BookName(s), AuthorName, Language Tags(if any)',
                thumb_url='https://telegra.ph/file/f9bc07b2d216238b2a910.png',
                thumb_width=30,
                thumb_height=30
                )
            ) 
    #print(fullrequest)
        try:
            results.append(
            InlineQueryResultArticle(
            id=uuid4(),
            title='Request audiobook: '+request[1].strip().title()+' ; '+request[2].strip().title()+' ; '+request[3].strip(),
            input_message_content=InputTextMessageContent("""#request\n"""+ 
        fullrequest.strip()+
        """\n#audiobook"""
        , parse_mode='HTML', disable_web_page_preview=True),
                    reply_markup= markup,
                    description='Request an Audible Audiobook',
                    thumb_url='https://telegra.ph/file/f91a6a03e5592573a6ff4.jpg',
                    thumb_width=30,
                    thumb_height=30
                    )
                )
        except:
            #results = list()
            results.append(
            InlineQueryResultArticle(
            id=uuid4(),
            title='Audible Link Missing!',
            input_message_content=InputTextMessageContent("""<i>Audible Link Missing!\nTry again...\nType r, BookName(s), AuthorName, AudibleLink, Language Tags(if any)</i>""", parse_mode='HTML'),
            description='Type r, BookName(s), AuthorName, AudibleLink, Language Tags(if any)',
            thumb_url='https://telegra.ph/file/f91a6a03e5592573a6ff4.jpg',
            thumb_width=30,
            thumb_height=30
            )
            )
        try:
            print("link is"+request[3])                      
            results.append(
            InlineQueryResultArticle(
            id=uuid4(),
            title='Request KU book: '+request[1].strip().title()+' ; '+request[2].strip().title()+' ; '+request[3].strip(),
            input_message_content=InputTextMessageContent("""#request\n"""+
        fullrequest.strip()+
        """\n#KU"""
        , parse_mode='HTML', disable_web_page_preview=True),
                    reply_markup= markup,
                    description='Request a Kindle Unlimited ebook',
                    thumb_url='https://telegra.ph/file/31bdcc94a29e964acc5d9.png',
                    thumb_width=30,
                    thumb_height=30
                    )
                )
        except:
            #results = list()
            results.append(
            InlineQueryResultArticle(
            id=uuid4(),
            title='KU Link Missing!',
            input_message_content=InputTextMessageContent("""<i>KU Link Missing!\nTry again...\nType r, BookName(s), AuthorName, Amazon KU Link, Language Tags(if any)</i>""", parse_mode='HTML'),
            description='Type r, BookName(s), AuthorName, Amazon KU Link, Language Tags(if any)',
            thumb_url='https://telegra.ph/file/31bdcc94a29e964acc5d9.png',
            thumb_width=30,
            thumb_height=30
            )
            )                       
    #request format
    if query.lower() == 'format':
            results = list()
            results.append(
            InlineQueryResultArticle(
            id=uuid4(),
            title='Request Format',
            input_message_content=InputTextMessageContent("""<code>#request
Book's name
Author's name 
#ebook or #audiobook
[Amazon link to audiobook/KU book, if applicable]</code>""", parse_mode='HTML'),
        )
    )
    #bookcrushpress rules
    if query.lower() == 'press':
            results = list()
            results.append(
            InlineQueryResultArticle(
            id=uuid4(),
            title='BookCrushPress Rules',
            input_message_content=InputTextMessageContent("""https://telegra.ph/BookCrush-Press-Group-Rules-12-05""", parse_mode='HTML'),
            thumb_url='https://telegra.ph/file/9cc715bb08a9ce45c0ef6.png',
            thumb_width=30,
            thumb_height=30
        )
    )

    context.bot.answer_inline_query(update.inline_query.id, results)


from telegram.ext import InlineQueryHandler
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)


updater.start_polling()