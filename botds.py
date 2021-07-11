import discord
from discord.ext import commands

TOKEN = 'ODYzNDkzNzE2NzMxODg3NjQ3.YOntMQ.v8u5tbPeg0SRNHOd6-K3Sisln_Y'
bot = commands.Bot(command_prefix='!')


@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def test(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send(arg)  # отправляем обратно аргумент


bot.run(TOKEN)
