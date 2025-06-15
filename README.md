# Movie Era Classification

There's a lot of talk about "eras" of filmmaking and how each has a different aesthetic and style. The era
changes everything about the film from mise en scene to camera work, right down to the poster. Recently, Marvel
popularized the "Avengers Poster," a plain background overlayed with a collection of headshots to flaunt their
star-studded casts. Many designers yearn for the days of "creativity," which got me thinking, what did those posters
look like? And more importantly, can we find a marked difference in the posters between different eras of filmmaking?

Special thank to The Movie Database&copy; for letting me scrape their website for all this movie data totally for free. 

## Table of Contents
* [Film Eras](#eras)
* [Tools](#tools)
* [Installation](#Installation)
* [Optimization](#optimization)
* [Contact](#Contact)

## Eras
Any division of film eras is arbitrary, but I am going to try to take a hybrid approach, weaving in historical content based on pivotal films, emerging technologies, industry shifts, and cultural changes. Another thing I will try to do is conform a little bit more to my data. Aside from the most recent era, I am going to try to keep a roughly even split between numberes of movies for each era, so the model does not skew towards high density eras to reduce cost.

Because of the nature of filmmaking, movies will exhibit characteristics of a preceeding era or pioneer features of new eras, but I believe these subdivisions adequately capture shifts. While no transition is a hard cutoff, certain movies and events offer clear signals of change. So here's how cinema unfolds across the decades:

<ol>

<li>
<b>Classical Hollywood and the Golden Era (1939 - 1954)</b>
<br/><br/>
The studios defined Hollywood's first real golden age, and they had complete control over all aspects of the process incluing distribution and stars. Beginning in 1939 with <i>The Wizard of Oz</i> and <i>Gone With the Wind</i>, the era progressed to include patrotic films and escapism along with melodrama in the post-war years. Popular directors included Billy Wilder and John Ford, and the era gave rise to legends like Humphrey Bogart, Ingrid Bergman, Jimmy Stewart, and Grace Kelly. Shamelessly, it also had a few of my all-time favorite movies Casablanca, Double Indemnity, and It's a Wonderful Life. 

The Paramount Decree in 1948 marks a shift and the beginning of the end of this era when the US Government dismantled the studio monopolies and gave rise to more personal, psychological cinema like *On The Waterfront (1954)* and *Rear Window (1954)*.
</li>

<li>
<b>Pre New Hollywood Transition (1955 - 1966)</b>
<br/><br/>
Without the studio system and TV beginning to cut in to box office dominance, Hollywood decided to bet on what made cinema unique: color, huge screens, and spectacle. Epics like <i>Ben Hur (1959)</i> define this idea. However, a more drastic shift was laying root under the surface of this circus with European cinema gaining prevalence and even American directors like Hitchcock experimenting further with form and content. Hitchcock's <i>Pyscho (1960)</i> and Kubrick's <i>Dr.Strangelove</i> are nothing like the classical era that came before.

Acting styles also shifted, and actors like Marlon Brando and James Dean popularized a more realistic form of acting made possible by the advances in microphone technology. Though it was a transition period, the foundation began to crack, and this era plants the seeds for arguably the most artistically fertile era of cinema in histrory.
</li>

</ol>

I love film and care about it deeply, but I want to emphasize that I am by no means an expert in film history. These are simply the subdivisions based on research by some guy who happened to minor in film in college. I'm always happy to discuss movies and even these subdivisions, so feel free to reach out and we can always discuss.

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