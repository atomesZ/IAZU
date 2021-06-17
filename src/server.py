import cherrypy
import pandas as pd

from top5 import get_top5

data_path = './data/'

try :
    pd_tags = pd.read_csv(data_path + 'Tags.csv')
    pd_answ = pd.read_csv(data_path + 'Answers.csv')
    pd_qst = pd.read_csv(data_path + 'Questions.csv')
    
except OSError:
    print("Could not open Tags.csv, Questions.csv or Answers.csv check if thoses files are in the good directory.")

class QuestionR(object):



    def index(self):
        # Formulaire demandant sa query à l'utilisateur :
        return '''
      <form action="query" method="GET">
      Bonjour, quelle est votre question ?
      <input type="text" name="reponses" />
      <input type="submit" value="OK" />
      </form>
      '''
    index.exposed = True

    def query(self, reponses = None):
        if reponses:
            #on balance aux autres
            print(reponses)

            # get the 2 lists
            matched_answ, matched_qst = get_top5(reponses, pd_tags, pd_answ, pd_qst)

            separator = "<br><br>#############################################<br><br>"
            
            res = ""

            for answ, qst in zip(matched_answ, matched_qst):
                res += "<h1>Question:</h1><br>" + qst + "<br><br><h1>Answer:</h1>" + answ + separator

            if res == "":
                res = '<iframe width="1600" height="900" src="https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'

            #on récupère les réponses
            return res
        else:    # Aucun nom n'a été fourni :
            return 'Veuillez poser une question <a href="/">ici</a>.'
    query.exposed = True

cherrypy.quickstart(QuestionR(), config ="server.conf")

