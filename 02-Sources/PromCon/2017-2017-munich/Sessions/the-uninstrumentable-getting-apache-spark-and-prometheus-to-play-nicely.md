---
type: promcon-talk
conference: PromCon
edition: "PromCon 2017"
edition_id: 2017-munich
year: 2017
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2017-munich/talks/the-uninstrumentable-getting-apache-spark-and-prometheus-to-play-nicely/
youtube_url: https://www.youtube.com/watch?v=KMk1aJaAkhw
youtube_search_url: https://www.youtube.com/results?search_query=The+Uninstrumentable%3B+Getting+Apache+Spark+and+Prometheus+to+Play+Nicely+PromCon+2017
video_match_score: 1.046
status: video-found
---

# The Uninstrumentable; Getting Apache Spark and Prometheus to Play Nicely

## Identificação

- Edição: PromCon 2017
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2017-munich/talks/the-uninstrumentable-getting-apache-spark-and-prometheus-to-play-nicely/
- YouTube: https://www.youtube.com/watch?v=KMk1aJaAkhw

## Resumo

Speaker 1: Dan Rathbone Speaker 2: Joe Stringer Instrumenting your code with Prometheus is simple and easy. Or so we thought until we tried to instrument our Python application running under Apache Spark… The distributed nature of Spark presents some interesting challenges when it comes to instrumenting your code effectively, for example a lack of global state, transient processes and no control over the execution profile. We’ll talk about our myriad failed attempts at instrumenting under Spark and our journey to finally getting something working effectively, without DOSing Prometheus with millions of time series!

## Abstract oficial

Speaker 1: Dan Rathbone

Speaker 2: Joe Stringer

Instrumenting your code with Prometheus is simple and easy. Or so we thought until we tried to instrument our Python application running under Apache Spark… The distributed nature of Spark presents some interesting challenges when it comes to instrumenting your code effectively, for example a lack of global state, transient processes and no control over the execution profile.

We’ll talk about our myriad failed attempts at instrumenting under Spark and our journey to finally getting something working effectively, without DOSing Prometheus with millions of time series! :)



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2017-munich/talks/the-uninstrumentable-getting-apache-spark-and-prometheus-to-play-nicely/
- YouTube: https://www.youtube.com/watch?v=KMk1aJaAkhw
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KMk1aJaAkhw
- YouTube title: PromCon 2017: The Uninstrumentable; Getting Apache Spark and Prometheus to Play Nicely
- Match score: 1.046
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2017/the-uninstrumentable-getting-apache-spark-and-prometheus-to-play-nicel/KMk1aJaAkhw.txt
- Transcript chars: 21757
- Keywords: python, prometheus, metrics, context, workers, actually, working, cluster, running, processes, scrape, pretty, little, counters, process, gateway, around, trying

### Resumo baseado na transcript

[Music] all right so our next talk is gonna have a little bit of a personality disorder well because there's two speakers I'd like to welcome Joe Rathbone and Joe stringer from infinite works a little bit of story so many many years ago I was working for a web company and they ran a very popular web portal that had stuff like news articles and sports articles the platforming ran on was was at capacity and it would regularly suffer service outages and this was particularly bad when there

### Excerpt da transcript

[Music] all right so our next talk is gonna have a little bit of a personality disorder well because there's two speakers I'd like to welcome Joe Rathbone and Joe stringer from infinite works a little bit of story so many many years ago I was working for a web company and they ran a very popular web portal that had stuff like news articles and sports articles the platforming ran on was was at capacity and it would regularly suffer service outages and this was particularly bad when there was a really interesting football match on because people would log in and try to look at all the live scores as they were happening so one evening muggins here is on call trying to support this platform so I'm sat at home in my apartment trying to eat my dinner which is the expertly photoshopped meatballs so I've kind of sit there eating dinner and all I've got to really gauge whether or not this system is on fire or not is a captai graph that updates once every five minutes which shows me the CPU usage aggregated across the the web cluster so I'm sat there munching away occasionally glance up with this graph to see but how perilously close to a hundred percent are we right now and I think I think I like we just just about scraped by with 90 something percent so it's quite quite hairy evening so yeah not a great day for me yeah so that's a cool story down but why is it relevant to us here today that's a good question joke so it's it's relevant it's relevant because I think the point here is I had no visibility of what was going on I knew whether the system was on fire or if it wasn't on fire that was kind of it there was no fine-grained real-time monitoring it so it's about really the importance of that may not have that so I can see what's going on akka proactively even fix a problem before it happens yes so that's no the crooks of what we're talking about today is kind of fine-grain real-time monitoring yep absolutely so we're gonna talk to you a bit about our data processing system we're on at the minute it runs apache spark the pie spark - so we're gonna talk a bit about their failed attempts we had on getting it instrumented some of the crazy ideas we tried to get the instrumentation working and then in the solution we have at the minute that's actually working and gives us all our nice graph ana graphs so join us a bit about the project down I do yes okay so this is kind of it in a nutshell so it's we're a consultancy company so we work on behalf of clients this is t
