# Movie Era Classification

There's a lot of talk about "eras" of filmmaking and how each has a different aesthetic and style. The era
changes everything about the film from mise en scene to camera work, right down to the poster. Recently, Marvel
popularized the "Avengers Poster," a plain background overlayed with a collection of headshots to flaunt their
star-studded casts. Many designers yearn for the days of "creativity," which got me thinking, what did those posters
look like? And more importantly, can we find a marked difference in the posters between different eras of filmmaking?

Special thank to The Movie Database&copy; for letting me scrape their website for all this movie data totally for free. 

## Table of Contents
* [Tools](#Tools)
* [Installation](#Installation)
* [Contact](#Contact)

## Tools
* [![Python][python-shield]][python-url]
* [![PyTorch][pytorch-shield]][pytorch-url]
* [![Jupyter Notebook][juypternb-shield]][jupyternb-url]

## Installation

## Optimization
Here, we use threading to efficiently process and scrape all the data instead of asynchronous programming. That is intentional.
This is a discussion my team had while I was a temp Data Engineer at State Farm, so let me sidetrack for a little.
<br/><br/>
<u>Async vs Threading</u>
* By definition, async does not block the current thread, which means we can kick off a process and then do something
else while we  wait for it to complete. On the other hand, threading still waits for the process to complete without switching, the
advantage is that we have multiple threads waiting for different things. 
* Async is fantastic when something has a delay. A great example is I/O and literal time delays; in async programming we can
switch to something else until the request does something interesting.
* Threading is best for items that have high compute. If we have to do something that takes forever but the process is
monolithic, we can kick off each run of this big process with a different thread to let it run in parallel
* Finally, in terms of implementation, it's usually easier to add a thread to an existing blocking implementation
than turning the whole code asynchronous
<br /><br />
For the reasons outlined above, THREADING is actually best for this use case. We have an existing blocking
implementation, and more importantly, our bottleneck is not the API calls. Our API responses are almost instant, but our big
time sink is the process of downloading each page of images which is a constant process which takes a lot of compute. After analyzing
the use case, it turns out implementing threading is both simpler and will likely give us better performance benefits.
<br /><br />
For reference, I have attached small demos of the **threaded vs non-threaded implementations** in the example directory with time output
so you can see the difference. It's more than a 75% improvement!


## Contact

[python-shield]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://docs.python.org/3/
[pytorch-shield]: https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white
[pytorch-url]: https://docs.pytorch.org/docs/stable/index.html
[juypternb-shield]: https://img.shields.io/badge/Jupyter%20Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white
[jupyternb-url]: https://docs.jupyter.org/en/latest/