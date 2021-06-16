import cherrypy

class QuestionR(object):
    def index(self):
        # Formulaire demandant son nom à l'utilisateur :
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
            res = '<p>You that is possible. You could use:</p>\n\n<ul>\n<li><a href="https://rstudio.github.io/DT/shiny.html" rel="nofollow noreferrer">DT for interactive tables, see section 2.</a></li>\n<li><a href="https://plot.ly/r/shiny-coupled-events/" rel="nofollow noreferrer">plotly_selected or plotly_click for interactive charts</a></li>\n</ul>\n\n<p>You could then use <a href="https://shiny.rstudio.com/reference/shiny/latest/observeEvent.html" rel="nofollow noreferrer">observeEvents</a> to listen to these actions, and make your application act accordingly.</p>\n\n<p>Hope this helps you in the right direction.</p>\ni'
            #on récupère les réponses
            return res
        else:    # Aucun nom n'a été fourni :
            return 'Veuillez poser une question <a href="/">ici</a>.'
    query.exposed = True

cherrypy.quickstart(QuestionR(), config ="server.conf")

