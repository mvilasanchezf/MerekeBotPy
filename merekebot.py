from twitchio.ext import commands
import pygame

encuestas = {}

class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token='oauth:zue8g1595crq3i9uoty8bce9xb3jxy', prefix='!', initial_channels=['merekebot'],channel='merekebot')

        pygame.mixer.init()

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        # Print the contents of our message to console...
        print(message.content)

        

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    

    @commands.command()
    async def hi(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g ?hello
        # We can also give our commands aliases (different names) to invoke with.

        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        await ctx.send(f'¡BUENAS  {ctx.author.name}!')
        pygame.mixer.music.load('heyhey.mp3')
        pygame.mixer.music.play()  

    @commands.command()
    async def lobo(self, ctx: commands.Context):
        pygame.mixer.music.load('lobo.mp3')
        pygame.mixer.music.play() 
    @commands.command()
    async def money(self, ctx: commands.Context):
        pygame.mixer.music.load('money.mp3')
        pygame.mixer.music.play()  
    @commands.command()
    async def gotcha(self, ctx: commands.Context):
        pygame.mixer.music.load('gotcha.mp3')
        pygame.mixer.music.play() 
    @commands.command()
    async def atomic(self, ctx: commands.Context):
        pygame.mixer.music.load('atomic.mp3')
        pygame.mixer.music.play() 
    @commands.command()
    async def kaguya(self, ctx: commands.Context):
        pygame.mixer.music.load('haaa.mp3')
        pygame.mixer.music.play()

    encuestas = {}
    @commands.command(name='encuesta')
    async def encuesta_command(ctx, pregunta: str, *opciones: str):
        # Aquí se define el comando 'encuesta'
        # El argumento 'pregunta' es obligatorio y los argumentos '*opciones' son opcionales
        # Este comando inicia una encuesta con la pregunta y las opciones especificadas
        
        if len(opciones) > 1:
            # Verifica si se proporcionaron al menos dos opciones para la encuesta
            opciones_str = '\n'.join(f'{i+1}. {opcion}' for i, opcion in enumerate(opciones))
            encuestas[ctx.channel.name] = {'pregunta': pregunta, 'opciones': opciones, 'votos': [0]*len(opciones)}
            await ctx.send(f'Nueva encuesta: {pregunta}\n{opciones_str}')
            # Envía el mensaje de la encuesta con la pregunta y las opciones
        else:
            await ctx.send('Debes proporcionar al menos dos opciones para la encuesta.')

    @commands.command(name='votar')
    async def votar_command(ctx, opcion: int):
        # Aquí se define el comando 'votar'
        # El argumento 'opcion' es obligatorio
        # Este comando permite a los usuarios votar por una opción en la encuesta actual

        if ctx.channel.name in encuestas:
            encuesta = encuestas[ctx.channel.name]
            if opcion > 0 and opcion <= len(encuesta['opciones']):
                encuesta['votos'][opcion-1] += 1
                opciones_str = '\n'.join(f'{i+1}. {opcion} ({votos} votos)' for i, (opcion, votos) in enumerate(zip(encuesta['opciones'], encuesta['votos'])))
                await ctx.send(f'Tu voto ha sido registrado.\n{encuesta["pregunta"]}\n{opciones_str}')
            else:
                await ctx.send('Debes elegir una opción válida.')
        else:
            await ctx.send('No hay ninguna encuesta activa en este canal.')


bot = Bot()
bot.run()
