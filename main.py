import os
from keep_alive import keep_alive
import wikipedia
import datetime
import random
from discord.ext import commands
import discord
from discord import FFmpegPCMAudio
from discord.utils import get
from discord.voice_client import VoiceClient
import time
import discord
from discord.ext import commands,tasks
import os
from dotenv import load_dotenv
import youtube_dl
import asyncio
#from googlesearch import search 

#os.system("pip install PyNaCl")
#import  pynacl


#import asyncio

bot = commands.Bot(
	command_prefix=".",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 738873030968737872# Change to your discord id!!!

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier
    

    




@bot.command()
async def hola(ctx):
    
    try:
      with open('data.json') as file:
        data = json.load(file)
    except:
      def get_all_members_ids(guild):
        for member in guild.members:
          yield member.id

# And then use it like this
      for id in get_all_members_ids(ctx.guild):
        print("name "+ str(bot.get_user(id)))
    await ctx.send("Hola!, soy Lester")
    
      
    


@bot.listen()
async def on_message(message):
    
    mensaje = str(message.content.lower())
    autor = str(message.author)
    hashtag = autor.find("#")
    if "_" in autor[0:hashtag]:
      a = autor[0:hashtag].replace("_" , " ")
    else:
        a = autor[0:hashtag]
    if "hola" in mensaje and mensaje.find("!") == -1 and mensaje.find(".") == -1 and "lester" in mensaje:
        await message.channel.send('Hola ' + a + "!")

    if "lester" in mensaje and ("como andas" in mensaje or "como estas" in mensaje) :
       
        await message.channel.send('Muy Bien ' + a + "!"+" ¿Y usted?")
    
    if "quien sos" in mensaje:
      await message.channel.send("Hola! Yo soy Lester, un Bot de Discord que puede hacer muchas cosas, como buscar en wikipedia, saludarlo o elegir números aleatorios.")   

    if "grande" in mensaje and "lester" in mensaje:
      await message.channel.send("El grande es usted señor "+ a + ".")
    
    if mensaje == "pong!" and a== "Tom Riddle":
      await message.channel.send("Tom, por favor, basta.")
    if ("despertate" in mensaje or "levantate" in mensaje) and "lester" in mensaje:
      await message.channel.send("Disculpe señor, estaba descansando, los bots tambien tenemos sentimientos.")
    
    for i in ["bolud","pelotud","puto","forro","puta","forra","lpm","la puta madre","la concha de","lcdtm","hdp","hijo de puta","virgo","virga","trolo","trola","cagon" , "usted avalo la bomba a la amia" ]:
      if i in mensaje:
        await message.channel.send("Señor "+ autor[0:hashtag] + " , por favor, cuide su vocabulario. No puede decir semejante barbaridad, usted se tiene que arrepentir de lo que dijo.")
        break    
        
    
def data_Json(Nombre):
  with open('data.json') as file:
    data = json.load(file)

  for client in data['usuarios']:
        if Nombre== client["nombre"]:
           return client 





@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Larga vida a Lester", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="http://1.bp.blogspot.com/-wfPZzd_ZPNU/TzQzMoXUviI/AAAAAAAACOc/URPsx3zDWYw/s320/mini012.jpg")

    await ctx.send(embed=embed)

@bot.command()
async def capacitor(ctx , potencia : float , angi : float , angf : float, v = 220, f = 50 , tabla = False):
    import math
    tgi = math.tan((angi * math.pi)/180)
    tgf = math.tan((angf * math.pi)/180)
    print(tgi, tgf)
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Cáluculo de capacitores", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    c = (potencia * (tgi - tgf))/(math.pi* 2 *(v**(2))* f) * 10 **(6)
    embed.add_field(name="C = ", value= str(c) + "µf")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")

    if tabla == True:
      capacitores_estandar = [6 ,8 ,10 ,16 , 20 , 25 , 32 , 45 , 64 , 90 , 100]

      for i in range(0 , len(capacitores_estandar)):
        try:
          if c > capacitores_estandar[i] and c < capacitores_estandar[i - 1]:
            capacitor = capacitores_estandar[i]
        except:
          pass

      if capacitor < 64 or capacitor == 64:
        cp = "2x" + str(capacitor/2) + "µf"
      else: 
        cp = str(capacitor) + "µf" 

      embed.add_field(name="Capacitor a instalar: ", value= cp)
    embed.set_thumbnail(url="https://static.vecteezy.com/system/resources/previews/000/606/964/non_2x/vector-lightning-logo-icon-and-symbols-bolt.jpg")

    await ctx.send(embed=embed)

@bot.command()
async def rnd(ctx, numOne: int, numTwo: int):
    await ctx.send(random.randrange(numOne,(numTwo + 1)))
    

@bot.command()
async def wiki(ctx, par, busca):
    busc = busca.replace("_"," ")
    wikipedia.set_lang("es")
    await ctx.send("Resultados de la búsqueda: "+busc)
    if par == "b" or par == "B":   
        await ctx.send(wikipedia.search(busc))
    elif par == "r" or par == "R":
        bus = wikipedia.summary(busc)            
        #CORREGIR LÍMITE DE CARACTERES
        bus1 = bus[0:2000]
        await ctx.send(bus1)
        if len(bus) > 2000:
            bus2 = bus[2000:4000]
            await ctx.send(bus2)
            if len(bus)> 4000:
                bus3 = bus[4000:6000]
                await ctx.send(bus3)
                if len(bus)> 6000:
                    bus4 = bus[6000:len(bus)]
                    await ctx.send(bus4)
            
        else:
          await ctx.send(bus) 
        await ctx.send("https://es.wikipedia.org/wiki/"+busca)
    else:
        await ctx.send("Error de sintáxis (.wiki R/r/B/b parametro a buscar)")
        
        
@bot.command()
async def wikiinfo(ctx):
    await ctx.send("Esta es la información sobre el comando .wiki:")
    await ctx.send("Para empezar, este comando sirve para utilizar los servicios de wikipedia desde el canal de voz.")
    await ctx.send("La primer variable corresponde al tipo de búsqueda que desea hacer")
    await ctx.send("Si es la letra b(o B), lo que verá en pantalla son los resultados de la búsqueda. Pero si es una r(o R), verá un resumen del artículo")
    await ctx.send("en el caso de que lo que desee buscar contenga más de una palabra, reemplace los espacios por guiones bajos")
    await ctx.send("Al final de la búsqueda se adjuntará el enlace del artículo de Wikipedia, en el caso de que exista")





from urllib import parse, request
import re

@bot.command()
async def ytb(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    print(html_content.read().decode())
    await ctx.send(html_content.read().decode())
    #IMPRIME EL HTML DE LA BUSQUEDA, HAY QUE PARSEARLO




extensions = [
	'cogs.cog_example'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.

keep_alive()  # Starts a webserver to be pinged.

bot.run("NzM4ODczMDMwOTY4NzM3ODcy.XySPIg.BKS79vSPSLCtn9t-SlpOyiFYKiY")  # Starts the bot