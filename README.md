Walltz
======
##Poetry from a Facebook Wall

###What?
Creates a beautiful poetic work of staggering genius based on a person's Facebook wall posts.


Hi there. I'm totally a work in progress. But, here's an overview of what I'm supposed to do:

####`get_wall_data(username)`
Returns an array of dictionaries for the first bit of a persons Facebook wall by making 10 requests to Facebook's Graph API.

####`get_posts(wall_data)`
Returns a string of concatenated post text from the entire wall data JSON made by `get_wall_data`.

####`make_poetry(corpus)`
Returns sentences (poetry!) generated from a corpus (with the help of NLTK, of course).
Currently TOTALLY broken :-) !!!
