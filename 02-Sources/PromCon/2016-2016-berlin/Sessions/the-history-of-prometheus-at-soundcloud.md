---
type: promcon-talk
conference: PromCon
edition: "PromCon 2016"
edition_id: 2016-berlin
year: 2016
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Alerting", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2016-berlin/talks/the-history-of-prometheus-at-soundcloud/
youtube_url: https://www.youtube.com/watch?v=cdKc8ePbj4A
youtube_search_url: https://www.youtube.com/results?search_query=The+History+of+Prometheus+at+SoundCloud+PromCon+2016
video_match_score: 0.866
status: video-found
---

# The History of Prometheus at SoundCloud

## Identificação

- Edição: PromCon 2016
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Alerting]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2016-berlin/talks/the-history-of-prometheus-at-soundcloud/
- YouTube: https://www.youtube.com/watch?v=cdKc8ePbj4A

## Resumo

Speaker: Tobias Schmidt The way SoundCloud monitors its services and infrastructure has dramatically changed over the last couple of years. Monitoring, alerting, and being on-call is now deeply ingrained in every engineering team and we have learned a lot on the way. This talk will describe our transition from an ops team to a "you build it, you own it" approach, why we needed something like Prometheus, as well as how Prometheus helped us to achieve that and highlight a few success and failure stories.

## Abstract oficial

Speaker: Tobias Schmidt

The way SoundCloud monitors its services and infrastructure has dramatically
changed over the last couple of years. Monitoring, alerting, and being on-call
is now deeply ingrained in every engineering team and we have learned a lot on
the way.

This talk will describe our transition from an ops team to a "you build it,
you own it" approach, why we needed something like Prometheus, as well as how
Prometheus helped us to achieve that and highlight a few success and failure
stories.

## Links

- Página oficial: https://promcon.io/2016-berlin/talks/the-history-of-prometheus-at-soundcloud/
- YouTube: https://www.youtube.com/watch?v=cdKc8ePbj4A
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=cdKc8ePbj4A
- YouTube title: PromCon 2016: The History of Prometheus at SoundCloud - Tobias Schmidt
- Match score: 0.866
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2016/the-history-of-prometheus-at-soundcloud/cdKc8ePbj4A.txt
- Transcript chars: 48679
- Keywords: actually, started, pretty, server, julius, soundcloud, metrics, always, client, monitoring, already, prometheus, beginning, bazooka, application, worked, working, everyone

### Resumo baseado na transcript

Thanks fine uh uh yeah my name is wise or yes better known as well be everywhere pretty much and the internet besides Twitter unfortunately yeah a couple of months ago actually I Julius talk to me and announced there will be a permissive conference and afterwards he kind of talked me into flying over from New York to Berlin and to give it to work and I thought about okay what could I talk about and I came up with see history of promises because I thought like valve RabbitMQ client and she put like one canary instance and then yeah he came to her might even have been me I came to like developers of the mothership and side like okay how can i get like metrics for this instance and weather like config uh one lesson learned here I want yeah talk to me afterwards we find it interesting don't do that don't put like team or a product or like any meteor information into your welding these things change and you don't want to update your impact I mean he kicked off parameters he kicked off our understanding of like we need metrics and metrics important we can't scale without that he kicked off service discovery he actually worked a lot also on the on-call schedules and lex introduction of on-call get metrics at that point for our for female jobs mostly MapReduce jobs running on Hadoop or then also the shaft client itself so all the stuff which disappears after like a couple of...

### Excerpt da transcript

Thanks fine uh uh yeah my name is wise or yes better known as well be everywhere pretty much and the internet besides Twitter unfortunately yeah a couple of months ago actually I Julius talk to me and announced there will be a permissive conference and afterwards he kind of talked me into flying over from New York to Berlin and to give it to work and I thought about okay what could I talk about and I came up with see history of promises because I thought like valve want would be a good point to give like that kind of torque it probably like the first conference afterwards it's known to everyone and you might ask BK why am I the guy to like talk about the history of committees so they are like obviously the founders Julius and Matt of committees and then they're like to be very active core contributors like beer and wine and fabian and i guess i would describe myself as kind of like the companion of parameters i happen to be the third one on his third one who committed to prometheus the third one was on the mailing list and the third one who joined the ISE channel I so I was like I kind of always like new primitives I you might have seen I both will be client export it will be client library and a couple of exporters but mostly just glued from easiest together at SoundCloud and let the other people like do the actual hot work but yeah that gave me like a pretty good inside and like actually healthy honored to like work together was like all the core contributors except wine as you said because he was never actually at some cloud I so without further ado let's talk about the history of committees so November 24 2012 comedians were started at soundcloud that's actually completely 1i soundcloud did not start promises actually a verse in the beginnings Matt proud tour started to work on permissive to think about time series data bases to think about like the problem of monitoring he told me like even in 2011 in for real and with real experiments he started plan in February 2012 so like way before he actually joined soundcloud he saw a huge need for like great open source type series monitoring and actually he his vision or his go did not limit it to just infrastructure monitoring as we now camisas like mostly these days the like application monitoring network monitoring and like all this OP stuff he actually envisioned something way bigger and i guess we have like some use cases for that as well he has like friends and like talk to other people in biology in ch
