import pandas as pd
import os
import cherrypy
import whoosh.index as index

from whoosh.qparser import QueryParser

cherrypy.config.update({'server.socket_port': 8099})
cherrypy.engine.restart()

header = '''
<head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>
'''

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return open('public/html/index.html')

    @cherrypy.expose
    def search(self, search_text=""):
        project_IDs = self.get_projects(search_text)

        results = []
        for project_ID in project_IDs:
            df = pd.read_csv(f'../../SingleCell-Files/percentiles/{project_ID}.percentiles.csv')
            df = df[df['gen_name'] == search_text]
            df = df.drop(['gen_name'], axis=1)
            df['project_ID'] = [project_ID]
            results.append(df)

        df = pd.concat(results, axis=0)
        df = df[['project_ID'] + [column for column in df.columns if column != 'project_ID']]

        return header + df.to_html(index=False)

    def get_projects(self, search_text):
        ix = index.open_dir("../../SingleCell-Files/index")
        qp = QueryParser("content", ix.schema)
        q = qp.parse(search_text)

        project_IDs = []

        with ix.searcher() as s:
            results = s.search(q, limit=None)
            for result in results:
                project_IDs.append(result['title'])

        return project_IDs


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(StringGenerator(), '/', conf)