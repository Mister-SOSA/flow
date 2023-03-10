import pyflp
import eel

flp = pyflp.parse("C:\\Users\\alexkarabetsos\\Downloads\\tee.flp")

tempo = flp.tempo
time_spent = flp.time_spent
created_on = flp.created_on
channels = [channel.name for channel in flp.channels]
playlist = flp.arrangements[0]


@eel.expose
def get_project_info(path):
    flp = pyflp.parse(path)
    tempo = flp.tempo
    time_spent = flp.time_spent
    created_on = flp.created_on
    channels = [channel.name for channel in flp.channels]
    playlist = flp.arrangements[0]
    return tempo, time_spent, created_on, channels, playlist


eel.init('web')

eel.browsers.set_path('electron', './node_modules/electron/dist/electron')

eel.start('./main.html', mode='electron', port=8000,
          size=(400, 600), jinja_templates='templates')
