import discord
from discord.ext import commands
# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'estamos logados com {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'ola, eu sou um bot {bot.UserWarning}')

@bot.command()
async def moeda(ctx)
    resultado = flip()
    await ctx.reply(resultado)

bot.run("")
