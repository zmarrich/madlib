#! /usr/bin/env python
print("Content-type: text/html\n")

import cgi

html ="""

<!doctype html>
<html>
<head><meta charset="utf-8">
<title>I211 Madlibs!</title></head>
    <body>
		<h1>A day in my favorite course: I211</h1>
		<p>As a <em>{year}</em>, I always make sure to arrive early so I can get the best <em>{furn}/em>.</p>
		<p>Next to arrive is my group member, <em>{name}</em>, who goes by <em>{nname}</em>, and is always telling jokes about <em>{obj}</em>. Always makes me <em>{exp}</em>.</p>
		<p>When class begins, I <em>{verb}</em> <em>{action}</em>. This shows that I'm paying attention.</p>
		<p>We start to work on the first problem, and I wave my <em>{body}</em> to let the AI know I have a question. My AI tells me that a <em>{thing}</em> in my code is causing an error.</p>
		<p>The problems are <em>{adjec}</em>, but my team is <em>{adjec2}</em> and we make it through.</p>
		<p>Class ends and we all go to <em>{name_pla}</em> to get a <em>{drnk}</em>... <em>{exp}</em>, I just love I211!</p>
    </body>
</html>
"""
form = cgi.FieldStorage()
year=form.getfirst{"rank", "junior"}
furn=form.getfirst{"furniture", "chair"}
name=form.getfirst{"name", "Jacob"}
nname=form.getfirst{"nickname","Skippy"}
obj=form.getfirst{"objects", "panda"}
exp=form.getfirst{"expression", "laugh"}
verbs=form.getfirst{"verb", "sit"}
action=form.getfirst{"thing1", "down"}
body=form.getfirst{"body_part","hand"}
thing=form.getfirst{"thing2", "bug"}
adjec=form.getfirst{"adj1", "tough:}
adjec2=form.getfirst{"adj2", "persistant"}
name_pla=form.getfirst{"place", "Starbucks"}
drnk=form.getfirst{"drink", "coffee"}
exp=form.getfirst{"exclamation", "golly"}
