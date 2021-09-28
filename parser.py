
from bs4 import Beautifulsoup
import request

url = "https://news.ycombinator.com/"

soup = Beautifulsoup(request,text, "html.parser")

