import discord
from discord.ext import commands
import random

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados com {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá, eu sou um bot!')

@bot.command()
async def moeda(ctx):
    resultado = random.choice(['Cara', 'Coroa'])
    await ctx.reply(resultado)

@bot.command()
async def calc(ctx, numero1: float, operacao: str, numero2: float):
    ops = {'+': numero1 + numero2, '-': numero1 - numero2, '*': numero1 * numero2}

    if operacao == '/':
        if numero2 == 0:
            return await ctx.reply('❌ Não é possível dividir por zero!')
        ops['/'] = numero1 / numero2

    if operacao not in ops:
        return await ctx.reply('❌ Operação inválida! Use: `+` `-` `*` `/`')

    resultado = ops[operacao]
    if resultado == int(resultado):
        resultado = int(resultado)

    await ctx.reply(f'🧮 `{numero1} {operacao} {numero2} = {resultado}`')

bot.run("SEU_TOKEN_AQUI")
