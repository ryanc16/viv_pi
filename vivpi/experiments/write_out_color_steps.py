

def write_out_color_steps(steps):
	mapped = map(lambda rgb: ",".join(map(lambda c: str(round(c)), rgb.as_rgb())), steps)
	# val = "\n".join(mapped)
	# f = open("colorsteps.csv", "w")
	# f.write(val)
	# f.close()
	html = open("colorsteps.html", "w")
	html.write("<html><head>")
	html.write("<style> * {margin: 0;padding: 0;line-height: 1;}\nbody {display: flex;}\nspan {display: inline-block;height: 100px;width: 1px;filter:brightness(5);}</style>")
	html.write("</head><body>")
	html.write("\n".join(map(lambda c: '<span style="background-color:rgb(' + c + ')"></span>', mapped)))
	html.write("</body></html>")
	html.close()

	write_out_color_steps()