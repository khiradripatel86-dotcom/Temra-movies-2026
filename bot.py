import os
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Aapke Bot ka Token (jo aapko BotFather se mila tha)
TOKEN = '8779345278:AAGUeRRmEx0C2MP2q4xDmNQUVlcyh_GRRR4'  # Yeh token aapko BotFather se milega

# Start command: Jab user /start likhe
def start(update, context):
    update.message.reply_text("Hello! Type /movie <movie_name> to search a movie!")

# Movie search command: /movie <movie_name>
def movie(update, context):
    movie_name = ' '.join(context.args)  # User jo movie ka naam dega, wo capture hoga
    if movie_name:
        # Movie ka naam milne par, hum movie ka link ya file return karenge
        movie_info = get_movie_info(movie_name)
        if movie_info:
            link, file_id = movie_info
            if file_id:
                update.message.reply_document(file_id)  # Agar movie ka file hai
            elif link:
                update.message.reply_text(f"Here is your movie link: {link}")  # Agar movie ka link hai
        else:
            update.message.reply_text(f"Sorry, we couldn't find information for '{movie_name}'.")
    else:
        update.message.reply_text("Please provide a movie name. Example: /movie Inception")

# Movie information ko fetch karna (abhi mock data hai)
def get_movie_info(movie_name):
    movie_data = {
        "Inception": ("https://example.com/inception", None),  # Movie link
        "The Dark Knight": (None, "file_id_for_the_movie"),  # Movie file
    }
    return movie_data.get(movie_name)

# Setup the Updater and Dispatcher
def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Handlers for start and movie commands
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('movie', movie))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
