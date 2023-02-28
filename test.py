import pyflp
import eel

flp = pyflp.parse("C:\\Users\\alexkarabetsos\\Downloads\\tee.flp")

tempo = flp.tempo
time_spent = flp.time_spent
created_on = flp.created_on
channels = [channel.name for channel in flp.channels]
playlist = flp.arrangements[0]

print(playlist)

eel.init('web')
eel.start('/templates/main.html', size=(700, 600),
          mode='electron')
