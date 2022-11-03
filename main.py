import datetime
import pronotepy
import time
from discord_webhook import DiscordWebhook, DiscordEmbed

client = pronotepy.Client('https://XXXXXX.index-education.net/pronote/eleve.html?login=true',
                              username='XXXXXXXX',
                              password='XXXXXXXX')

if client.logged_in:
    nom_utilisateur = client.info.name
    print(f'Connecté via {nom_utilisateur}')
    running = True
else:
    print("Connexion impossible")
    running = False

today = datetime.date.today()

notes = []

periods = client.periods

for period in periods:
    for grade in period.grades:
            notes.append(f'{grade.grade}/{grade.out_of}')

def display_note(note, bareme, coefficient, noteMax, noteMin):
    print("Affichage :")
    print("Note", note)
    print("Bareme", bareme)
    print("Coefficient", coefficient)
    print("Note Max", noteMax)
    print("Note Min", noteMin)

    message = str(note + "/" + bareme + " | C: " + coefficient + " | Max:" + noteMax + " | Min:" + noteMin)

    webhook = DiscordWebhook(url='XXXXXXX', content=message)
    embed = DiscordEmbed(title='Nouvelle note!', description="", color='03b2f8')

    embed.add_embed_field(name='Note', value=note)
    embed.add_embed_field(name='Bareme', value=bareme)
    embed.add_embed_field(name='Coefficient', value=coefficient)
    embed.add_embed_field(name='Note Maximal', value=noteMax)
    embed.add_embed_field(name='Note Minimal', value=noteMin)

    webhook.add_embed(embed)
    response = webhook.execute()
while running:
    temp = f'{grade.grade}'

    if temp != notes[-1]:
        print('Nouvelle note : ', f'{grade.grade}/{grade.out_of}')
        display_note(f'{grade.grade}',f'{grade.out_of}', f'{grade.coefficient}', f'{grade.max}', f'{grade.min}')

        notes.append(temp)
    else:
        time.sleep(5.0)
