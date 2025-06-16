# Movie Era Classification

There's a lot of talk about "eras" of filmmaking and how each has a different aesthetic and style. The era
changes everything about the film from mise en scene to camera work, right down to the poster. Recently, Marvel
popularized the "Avengers Poster," a plain background overlaid with a collection of headshots to flaunt their
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
Any division of film eras is arbitrary, but I am going to try to take a hybrid approach, weaving in historical content based on pivotal films, emerging technologies, industry shifts, and cultural changes. Another thing I will try to do is conform a little bit more to my data. Aside from the most recent era, I am going to try to keep a roughly even split between numbers of movies for each era, so the model does not skew towards high density eras to reduce cost.

Because of the nature of filmmaking, movies will exhibit characteristics of a preceding era or pioneer features of new eras, but I believe these subdivisions adequately capture shifts. While no transition is a hard cutoff, certain movies and events offer clear signals of change. So here's how cinema unfolds across the decades:

<ol>

<li>
<b>Classical Hollywood and the Golden Era (1939 - 1954)</b>
<br/><br/>
The studios defined Hollywood's first real golden age, and they had complete control over all aspects of the process including distribution and stars. Beginning in 1939 with <i>The Wizard of Oz</i> and <i>Gone With the Wind</i>, the era progressed to include patriotic films and escapism along with melodrama in the post-war years. Popular directors included Billy Wilder and John Ford, and the era gave rise to legends like Humphrey Bogart, Ingrid Bergman, Jimmy Stewart, and Grace Kelly. Shamelessly, it also had a few of my all-time favorite movies Casablanca, Double Indemnity, and It's a Wonderful Life. 

The Paramount Decree in 1948 marks a shift and the beginning of the end of this era when the US Government dismantled the studio monopolies and gave rise to more personal, psychological cinema like *On The Waterfront (1954)* and *Rear Window (1954)*.
</li>

<li>
<b>Pre New Hollywood Transition (1955 - 1966)</b>
<br/><br/>
Without the studio system and TV beginning to cut in to box office dominance, Hollywood decided to bet on what made cinema unique: color, huge screens, and spectacle. Epics like <i>Ben Hur (1959)</i> define this idea. However, a more drastic shift was laying root under the surface of this circus with European cinema gaining prevalence and even American directors like Hitchcock experimenting further with form and content. Hitchcock's <i>Psycho (1960)</i> and Kubrick's <i>Dr.Strangelove (1964)</i> are nothing like the classical era that came before.

Acting styles also shifted, and actors like Marlon Brando and James Dean popularized a more realistic form of acting made possible by the advances in microphone technology. Though it was a transition period, the foundation began to crack, and this era plants the seeds for arguably the most artistically fertile era of cinema in history.
</li>

<li>
<b> New Hollywood and the American Renaissance (1967 - 1982)</b>
<br/><br/>
Cinema increasingly shifts towards auteur-driven filmmaking set off by movies such as <i>Bonnie and Clyde (1967)</i>, <i>The Graduate (1967)</i>, and <i>2001: A Space Odyssey</i>. Cynicism ran rampant in the period with era-defining events like Watergate and The Vietnam War which permeated into filmmaking in marked ways in <i>Taxi Driver (1976)</i>, <i>Blow Out (1981)</i>, <i>Apocalypse Now (1979)</i>, and <i>Chinatown (1974)</i>. Even the big blockbusters were director driven: think George Lucas in <i>Star Wars (1977)</i> or Spielberg in <i>Jaws (1975)</i>. These early blockbusters set the stage for the next era of effects and action. 
</li>
</br/>

<li>
<b>The Blockbuster Era (1983 - 1994)</b>
<br/><br/>
Movies once again focused on spectacle. The popularization of digital effects allowed filmmakers to create whole new worlds and studios capitalized on the groundwork laid by the aforementioned blockbusters. Effects-driven, family friendly films like the <i>Indiana Jones</i> series, <i>Back to the Future (1985)</i>, and <i>Ghostbusters (1984)</i>. Action dominated (<i>Die Hard, Terminator</i>), but under the surface, cinema was cycling back to the more personal films of the previous era. Steven Soderbergh and Richard Linklater would emerge at the end of this era, and propel a new age of digital indie cinema.
</li>
<br/>

<li>
<b>Digital Revolution (1995 - 2006)</b>
<br/><br/>
The popularization of the digital camera made filmmaking much more accessible, allowing companies and directors with less do more than they ever had before. The Sundance boom brought independent directors like Quentin Tarantino, the Coen Brothers, and PTA to the forefront. These director's drove new ways to tell stories and defined the cool, character-driven cinema. However, digital also allowed a lot more different types of films to become profitable, so filmmakers could also produce the spectacle of earlier ages, which became even more riveting with the progress of CGI. <i>The Matrix (1999)</i> and the <i>The Lord of the Rings</i> series combined practical and digital effects with great success.

The Lord of the Rings especially stands out because of its ability to make wide audiences take the fantasy genre more seriously. In previous decades it would've been incredibly difficult to get this type of move financed, let alone make it profitable. But experimentation became more prevalent and audiences hungered for totally new ideas.  
</li>

<li>
<b>The Franchise Era and Streaming (2007 - 2019)</b>
<br/><br/>
The MCU was born, and cinema changed forever. <i>Iron Man (2008)</i> kicked off a sprawling interconnected universe that redefined franchise filmmaking. Studios began to prioritize cinematic universes, IP, and reboots over one-offs.

Meanwhile, Netflix and Amazon disrupted the distribution model, premiering films online and even winning Oscars. Directors like Nolan (Inception), Villeneuve (Arrival), and Gerwig (Lady Bird) proved that bold, original voices could still find mass appeal, but these became the exception rather than the norm, and independent voices increasingly began premiering on streaming rather than the big screen.
</li>

<li>
<b>Post-Covid/Current Era (2020-Current)</b>
<br/><br/>
The pandemic forced a rapid evolution. Theaters shuttered, release calendars collapsed, and studios experimented with hybrid models (<i>Dune, Black Widow, The Batman</i>).Streaming became dominant, and movies had to adapt to shorter attention spans and more personalized content ecosystems. <i>Everything Everywhere All at Once (2022)</i> signaled a new maximalist originality exemplifying this idea. Maybe this forecasts changes still to come. Movies like <i>Top Gun: Maverick (2022)</i> and <i>Barbie (2023)</i> showed that audiences still have an appetite for the theater, but studios seem more unsure about how to get them there. 

At the same time, AI and virtual production technologies (like Unreal Engine) began influencing how films are written, shot, and marketed. Like with any new technology throughout the history of film, the art will change. It will be interesting to see how. 
</li>

</ol>

I love film and care about it deeply, but I want to emphasize that I am by no means an expert in film history. These are simply the subdivisions based on research by some guy who happened to minor in film in college. I'm always happy to discuss movies and even these subdivisions, so feel free to <a href='#contact'>reach out</a> and we can always discuss.

## Tools
* [![Python][python-shield]][python-url]
* [![PyTorch][pytorch-shield]][pytorch-url]
* [![Jupyter Notebook][juypternb-shield]][jupyternb-url]
* [![Matplotlib][matplotlib-shield]][matplotlib-url]

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
[matplotlib-shield]: https://img.shields.io/badge/-Matplotlib-000000?style=flat&logo=python
[matplotlib-url]: https://matplotlib.org/stable/index.html