import web

urls = (
  '/', 'index'
)

content = """
<HTML>
<Head>
<Titlte>test</Title>
</Head>
<Body>
<h1>test</h1>
<br>
<p>test</p>
</Body>
</HTML>
"""


class index:
    def GET(self):
	import randomize
	print "run"
        return content

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
