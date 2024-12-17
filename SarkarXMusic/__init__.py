from SarkarXMusic.core.bot import Sarkari
from SarkarXMusic.core.dir import dirr
from SarkarXMusic.core.git import git
from SarkarXMusic.core.userbot import Userbot
from SarkarXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Sarkari()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
