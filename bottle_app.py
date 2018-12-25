from bottle import route, run, default_app, debug
from bottle import static_file, route, request
from hashlib import sha256

# Taken from https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py
def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()


password = '2e4d172380133b1a43f9faec17ab2be5bf8f3e189b96eb6354e1e4b6e4cdab89'

def index():
    return htmlify("My lovely website",
                   "This is going to be an awesome website, when it is finished.")

@route('static/<filename>')
def static_file_callback(filename):
    return static_file(filename, root='./static')

comment_form = '''<form action = "/static/soundtracks.html" method = "post">
	<fieldset>
	<legend>Comment Section:</legend>
	<legend>Comment:</legend>
	<textarea name="comment" rows="10" cols="60">Please be nice on your comments</textarea>
	<legend>Password:</legend>
	<input type = "password" name = "password" ><br>
	<input type = "submit">
	</fieldset>
	</form>
	'''

previous_comments = []

@route('/static/soundtracks.html')
def comment_section():
	page = '''<!DOCTYPE html>
	<html lang="en">
	<head>
		<link rel="icon" href="/static/icon.png">
		<title>Westworld Soundtracks</title>
		<meta charset="utf-8"/>
		<style>
			*{font-family:American Typewriter, serif;}
			body {background-color:#00020d}
			ul {
				border: 5px solid white;
				list-style-type: none;
				margin:18px;
				margin-bottom:0;
				padding:0;
				overflow:hidden;
				background-color:#00020d;
			}
			#navbar li {
				float:left;
			}
			#navbar li a {
				display:block;
				color:#ececec;
				text-align:center;
				padding:16px;
				text-decoration:none;
			}
			#navbar li a:hover {
				color:black;
				background-color:#ececec;
			}
			ol {
				list-style-type:upper-roman;
			}
			h1 {color:#ffffe6;text-align:center;}
			details {
				position:fixed;
				right:0px;
				bottom:0px;
				color:#ececec;
			}
			#cover {
				margin:0;
				padding:55px;
				font-size:55px;
				background-image:url('/static/pwithlogo.png');
				background-repeat:no-repeat;
				background-position:center;
			}
			fieldset{
			float: left;
			width: 100%;
			display: table;
			}
			legend {
			color:white;
			}
			p{
				color:white;
			}
		</style>
	</head>
	<body>
		<ul id="navbar">
		<li><a href="/static/index.html">Home</a></li>
		<li><a href="/static/characters.html">Characters</a></li>
		<li><a href="/soundtracks.html">Soundtracks and Comments</a></li>
		</ul>
		<h1 id="cover"><code>Westworld Fan Page</code></h1>
		<ol>
		<li style="color:white;">Season 1
		<ul class = "songs">
			<li><cite>Ain't No Grave - Johnny Cash</cite></li>
			<li><cite>Paint It, Black - Ramin Djawadi</cite></li>
			<li><cite>Black Hole Sun - Ramin Djawadi</cite></li>
			<li><cite>No Surprises - Ramin Djawadi </cite></li>
			<li><cite>Peacherine Rag - Maple Leaf Ragtime Band</cite></li>
			<li><cite>Pineapple Rag - Scott Joplin</cite></li>
			<li><cite>A Forest - Ramin Djawadi</cite></li>
		</ul>
		</li>
		<li style="color:white;">Season 2
			<ul class = "songs">
				<li><cite>Heart-Shaped Box - Ramin Djawadi</cite></li>
				<li><cite>Runaway - Ramin Djawadi</cite></li>
				<li><cite>Sweetvater - Ramin Djawadi</cite></li>
				<li><cite>The Entertainer - Ramin Djawadi</cite></li>
				<li><cite>Seven Nation Army - The White Stripes</cite></li>
				<li><cite>C.R.E.A.M - Ramin Djawadi</cite></li>
			</ul>
		</li>
		</ol>
		<class = "comments">
			''' + comment_form
	page_end = '''<details>
			</class>
			<summary>Lists are taken from</summary>
			<p>http://www.lyricsoundtrack.com/tv-shows/westworld-season1-songs-music/</p>
			<p style="text-align:center;">and</p>
			<p>http://www.lyricsoundtrack.com/tv-shows/westworld-season2-songs-music/</p>
			</details>
			</body>
			</html>'''
	i = 1
	page += "<p>Guest Comments<br><p>"
	for comment in previous_comments:
			page += "<p>%d. %s<br><p>" % (i, comment)
			i+=1
	page += page_end
	return page

@route('/static/soundtracks.html', method='POST')
def post_comment():
	page = '''<!DOCTYPE html>
	<html lang="en">
	<head>
		<link rel="icon" href="/static/icon.png">
		<title>Westworld Soundtracks</title>
		<meta charset="utf-8"/>
		<style>
			*{font-family:American Typewriter, serif;}
			body {background-color:#00020d}
			ul {
				border: 5px solid white;
				list-style-type: none;
				margin:18px;
				margin-bottom:0;
				padding:0;
				overflow:hidden;
				background-color:#00020d;
			}
			#navbar li {
				float:left;
			}
			#navbar li a {
				display:block;
				color:#ececec;
				text-align:center;
				padding:16px;
				text-decoration:none;
			}
			#navbar li a:hover {
				color:black;
				background-color:#ececec;
			}
			ol {
				list-style-type:upper-roman;
			}
			h1 {color:#ffffe6;text-align:center;}
			details {
				position:fixed;
				right:0px;
				bottom:0px;
				color:#ececec;
			}
			#cover {
				margin:0;
				padding:55px;
				font-size:55px;
				background-image:url('/static/pwithlogo.png');
				background-repeat:no-repeat;
				background-position:center;
			}
			fieldset{
			float: left;
			width: 100%;
			display: table;
			}
			legend {
			color:white;
			}
			p{
				color:white;
			}
		</style>
	</head>
	<body>
		<ul id="navbar">
		<li><a href="/static/index.html">Home</a></li>
		<li><a href="/static/characters.html">Characters</a></li>
		<li><a href="/soundtracks.html">Soundtracks and Comments</a></li>
		</ul>
		<h1 id="cover"><code>Westworld Fan Page</code></h1>
		<ol>
		<li style="color:white;">Season 1
		<ul class = "songs">
			<li><cite>Ain't No Grave - Johnny Cash</cite></li>
			<li><cite>Paint It, Black - Ramin Djawadi</cite></li>
			<li><cite>Black Hole Sun - Ramin Djawadi</cite></li>
			<li><cite>No Surprises - Ramin Djawadi </cite></li>
			<li><cite>Peacherine Rag - Maple Leaf Ragtime Band</cite></li>
			<li><cite>Pineapple Rag - Scott Joplin</cite></li>
			<li><cite>A Forest - Ramin Djawadi</cite></li>
		</ul>
		</li>
		<li style="color:white;">Season 2
			<ul class = "songs">
				<li><cite>Heart-Shaped Box - Ramin Djawadi</cite></li>
				<li><cite>Runaway - Ramin Djawadi</cite></li>
				<li><cite>Sweetvater - Ramin Djawadi</cite></li>
				<li><cite>The Entertainer - Ramin Djawadi</cite></li>
				<li><cite>Seven Nation Army - The White Stripes</cite></li>
				<li><cite>C.R.E.A.M - Ramin Djawadi</cite></li>
			</ul>
		</li>
		</ol>
		<class = "comments">
			''' + comment_form
	if request.POST and (create_hash(request.POST['password'])) == password:
		print(5)
		previous_comments.append(request.POST['comment'])
	page_end = '''<details>
			</class>
			<summary>Lists are taken from</summary>
			<p>http://www.lyricsoundtrack.com/tv-shows/westworld-season1-songs-music/</p>
			<p style="text-align:center;">and</p>
			<p>http://www.lyricsoundtrack.com/tv-shows/westworld-season2-songs-music/</p>
			</details>
			</body>
			</html>'''
	i = 1
	page += "<p>Guest Comments<br><p>"
	for comment in previous_comments:
			page += "<p>%d. %s<br><p>" % (i, comment)
			i+=1
	page += page_end
	return page



#####################################################################
# Don't alter the below code.
# It allows this website to be hosted on Heroku
# OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
    run()
