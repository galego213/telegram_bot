import telebot
import os

# Token protegido via variável de ambiente
TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

# Evento de novos membros com pedido de entrada
@bot.chat_member_handler()
def handle_join_request(message):
    chat_id = message.chat.id
    user = message.new_chat_member.user

    # Aprova automaticamente o pedido de entrada
    bot.approve_chat_join_request(chat_id, user.id)

    # Mensagem de boas-vindas
    bot.send_message(chat_id, f"👋 Bem-vindo(a), @{user.username or user.first_name}!")

    # Log para Railway
    print(f"✅ Usuário aprovado: {user.username or user.first_name}")

# Inicia o bot com polling infinito, ideal para produção
bot.infinity_polling(timeout=10, long_polling_timeout=5)
