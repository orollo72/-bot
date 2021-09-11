from discord.ext import commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
 await ctx.send('pong')


@bot.command()
async def hallo(ctx):
    await ctx.send('なんやおめぇ誰だ！')


@bot.command()
async def nice(ctx):
 await ctx.send('ナイス！')

　
@bot.command()
async def kami(ctx):
 await ctx.send('呼んだか?')

@bot.command()
async def rank(ctx):
 await ctx.send('ゴミにそんなことできるとでも？')


@bot.command()
async def neko(ctx):
 await ctx.send('にゃぁ')


@bot.command()
async def pei(ctx):
 await ctx.send('ぺい？ん？大丈夫？')


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
