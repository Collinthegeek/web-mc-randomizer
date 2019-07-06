#Collin Norwood 2019
#(I wrote only this file, Sethbling wrote randomize.py and Mojang wrote loot_tables/*)

import web

urls = (
  '/', 'index',
  '/download', 'Download'
)

content = """
<HTML>
 <Head>
  <Title>Random loot</Title>
 </Head>
 <Body>
  <h1>Random loot datapack</h1>
  <br>
  <p>
  Install this datapack
  <br><br>
  <a href="download">Download - random_loot.zip</a>
  </p>
 </Body>
</HTML>
"""


class index:
    def GET(self):
	import randomize #run the script
        return content   #display the html

class Download: #returns the result when you visit /download
	def GET(self):
		path = 'random_loot.zip'
		web.header('Content-Disposition', 'attachment; filename="random_loot.zip"')
           	web.header('Content-type','application/zip')
           	web.header('Content-transfer-encoding','binary') 
		return open(path, 'rb').read()


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
