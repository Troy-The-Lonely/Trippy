#!/usr/bin/env python3
#-*- coding: UTF-8 -*-
#
# Autor: Troy Oliveira
#

# Módulos:
# --------

import discord
import privado


# Variáveis importantes:
# ----------------------

token = privado.token()
client = discord.Client()

# 1° Evento - Analisando se o bot está online:
# --------------------------------------------

@client.event
async def on_ready():
    print('-------------- Online --------------')
    print('Nome: {}'.format(client.user.name))
    print('  ID: {}'.format(client.user.id))
    print('------------------------------------')

    await client.change_presence(game=discord.Game(name="💕", type=1))


# 2° Evento - Entrada no Servidor:
# --------------------------------

@client.event
async def on_member_join(member):

	# Canal de Entrada
	entrada1 = client.get_channel("464177757459578890")
	entrada2 = client.get_channel("452201188545396737")

	# Mensagens boas-vindas
	mensagem = discord.Embed(
		title=':heart_eyes: Entrada!',
		color=0x00ff33,
		description='Olá {}, Seja bem-vindo ao `Trippy` 💕.'.format(member.mention)
	)

	mensagem.set_image(url="https://i.imgur.com/ccBQKAI.gif")

	# Imprimindo as mensagens
	await client.send_message(entrada1, embed=mensagem)
	await client.send_message(entrada2, 'Shhh, silêncio! {} entrou no servidor. :joy:'.format(member.mention))

# 3° Evento - Saída do Servidor:
# ------------------------------

@client.event
async def on_member_remove(member):

	# Sala de saída
	saida1 = client.get_channel("464177780196769792")
	saida2 = client.get_channel("452201188545396737")

	# Mensagem de saída
	mensagem = discord.Embed(
		title=':sob: Saída!',
		color=0xff0000,
		description='Até nunca mais {}...'.format(member.mention)
	)

	mensagem.set_image(url="https://i.imgur.com/8va5GBO.gif")

	# Imprimindo a mensagem de saída
	await client.send_message(saida1, embed=mensagem)
	await client.send_message(saida2, "{} Saiu do servidor!".format(member.mention))

# 4° Evento - Comandos para mensagens do bot:
# -------------------------------------------

@client.event
async def on_message(message):

	# ^avatar → Vê imagem de perfil dos membros / Vê sua própria imagem:
	# ------------------------------------------------------------------

	if message.content.lower().startswith('^avatar'):
		try:
			membro = message.mentions[0]

			avatar1 = discord.Embed(
				title="Avatar",
				color=0xff00d5,
				description=':mountain: [Download]('+membro.avatar_url+') {}!'.format(membro.name)
			)

			avatar1.set_image(url=membro.avatar_url)
			await client.send_message(message.channel, embed=avatar1)

		except:
			membro = message.author

			avatar2 = discord.Embed(
				title='Seu avatar:'.format(membro.name),
				color=0x4d0083,
				description=':mountain: [Download]('+membro.avatar_url+') {}!'.format(membro.name)
			)

			avatar2.set_image(url=membro.avatar_url)
			await client.send_message(message.channel, embed=avatar2)


client.run(token)
