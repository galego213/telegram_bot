import asyncio
import nest_asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes

TOKEN = "7814430830:AAFjRJA_41Z0nhkJYbPNAD8CKUB5lr6uDnw"

WELCOME_MESSAGE = "👋 Olá, {name}! Seja muito bem-vindo ao nosso grupo!"

# Função que será chamada quando houver uma solicitação de entrada no grupo
async def aprovar_solicitacao(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user
    chat_id = update.chat_join_request.chat.id

    # Aprova automaticamente o usuário
    await context.bot.approve_chat_join_request(chat_id=chat_id, user_id=user.id)

    # Envia mensagem de boas-vindas
    await context.bot.send_message(
        chat_id=chat_id,
        text=WELCOME_MESSAGE.format(name=user.full_name)
    )

# Função principal que configura e roda o bot
async def main():
    print("🤖 Bot iniciado e aguardando solicitações...")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(aprovar_solicitacao))
    await app.run_polling()

# Rodar o bot corretamente mesmo em ambientes com loop ativo
if __name__ == "__main__":
    nest_asyncio.apply()  # Evita erro de loop já rodando
    asyncio.run(main())
