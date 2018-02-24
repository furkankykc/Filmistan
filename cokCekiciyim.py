import urllib.request as ur
import re
from django.template.defaultfilters import slugify
from filmistan.models import Film, Genre, Actor,Director,Year,Trailer
from django.contrib.auth import get_user_model
from django.utils.text import slugify
import sys

User = get_user_model()

def getyourself(a):
    try:
        d = Trailer.objects.get(code=a)
    except:
        d = Trailer.objects.create(code=a)
    d.save()
    return d


def getyearornot(a):
    try:
        d = Year.objects.get(yy=a)
    except:
        d = Year.objects.create(yy=a)
    d.save()
    return d

def getgenre(a):
    try:
        d = Genre.objects.get(title=a)
    except:
        d = Genre.objects.create(title=a)
    d.save()
    return d


def ff():
    try:
        for i in range(1100, 2600):
            site = "http://www.sinemalar.com/film/"+str(i)
            htmlkodu = ur.urlopen(site).read()

            genreregex = '<span itemprop="genre">(.*?)</span></a>'
            genrecomp = re.compile(genreregex)
            genres = re.findall(genrecomp, htmlkodu.decode('utf-8'))

            titleregex = '<h1 class=\"fl\"><span itemprop=\"name\" content=\"(.*?)\">'
            titlecomp = re.compile(titleregex)
            titles = re.findall(titlecomp, htmlkodu.decode('utf-8'))

            actorregex = '<span itemprop="name">(.*?)</span></a>'
            actorcomp = re.compile(actorregex)
            actors = re.findall(actorcomp, htmlkodu.decode('utf-8'))

            direcregex = 'itemprop="url"><span itemprop="name">(.*?)</span></a></span>'
            direccomp = re.compile(direcregex)
            directors = re.findall(direccomp, htmlkodu.decode('utf-8'))

            picregex = '<img src="(.*?)" title="'
            piccomp = re.compile(picregex)
            pictures = re.findall(piccomp, htmlkodu.decode('utf-8'))

            tarihregex ='<label>Vizyon Tarihi<span class="fr" >: </span></label>\r\n                    <span class="sinemalar-color">\r\n                        <strong>(.*?)</strong>'
            tarihcomp = re.compile(tarihregex)
            tarihler = re.findall(tarihcomp, htmlkodu.decode('utf-8'))

            descregex = '<div class="dsc-more" id="dscMore"> <p itemprop="description">(.*?)</p></div>'
            desccomp = re.compile(descregex)
            descrption = re.findall(desccomp, htmlkodu.decode('utf-8'))

            trailerregex = 'data-videoId="(.*?)"'
            trailercomp = re.compile(trailerregex)
            trailer = re.findall(trailercomp, htmlkodu.decode('utf-8'))

            ratingregex = '<span id="rating" itemprop="ratingValue" class="puan">(.*?)</span>'
            ratingcomp = re.compile(ratingregex)
            rating = re.findall(ratingcomp,htmlkodu.decode('utf-8'))

            aut = User.objects.get(pk=1)
            for title in titles:
                yy = str(tarihler).split(" ")
                try:
                    yy2 = getyearornot(yy[2].replace("']", ""))
                except:
                    yy2 = getyearornot("0")
                try:
                    film = Film.objects.get(title=title, author=aut, year= yy2)
                except:
                    film = Film.objects.create(title=title, author=aut, year=yy2)
                img_path = 'photos\\filmler\\'+slugify(title) + ".jpg"
                image_path = 'static\\' + img_path
                ur.urlretrieve(pictures[0], image_path)
                film.title = title
                film.release()
                film.description = descrption
                film.rating = rating[0]
                film.save()
                print(i, " ",title, " ", genres, " ", actors, " ", pictures, " ", rating, " ", tarihler, "\n")

            for gen in genres:

                film.genre.add(getgenre(gen))

            for act in actors:
                try:
                    a = Actor.objects.get(name=act)
                except:
                    a = Actor.objects.create(name=act)
                film.cast.add(a)

            for dir in directors:
                try:
                    d = Director.objects.get(name=dir)
                except:
                    d = Director.objects.create(name=dir)
                film.director.add(d)
            for cc in trailer:
                film.youtube_trailer.add(getyourself(cc))
            film.profile_image = img_path
            film.save()
    except OSError as err:
        print("OS error: {0}".format(err))
        i += 1
    except ValueError:
        print("Could not convert data to an integer.")
        i += 1
    except:
        print("Unexpected error:", sys.exc_info()[0])
        i+=1
