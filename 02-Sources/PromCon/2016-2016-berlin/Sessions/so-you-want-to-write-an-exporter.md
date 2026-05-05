---
type: promcon-talk
conference: PromCon
edition: "PromCon 2016"
edition_id: 2016-berlin
year: 2016
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core"]
speakers: []
source_url: https://promcon.io/2016-berlin/talks/so-you-want-to-write-an-exporter/
youtube_url: https://www.youtube.com/watch?v=KXq5ibSj2qA
youtube_search_url: https://www.youtube.com/results?search_query=So+You+Want+to+Write+an+Exporter+PromCon+2016
video_match_score: 0.841
status: video-found
---

# So You Want to Write an Exporter

## Identificação

- Edição: PromCon 2016
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]]
- Speakers: N/A
- Página oficial: https://promcon.io/2016-berlin/talks/so-you-want-to-write-an-exporter/
- YouTube: https://www.youtube.com/watch?v=KXq5ibSj2qA

## Resumo

Speaker: Brian Brazil In the glorious future, cancer will be cured, world hunger will solved and all because everything was directly instrumented for Prometheus. Until then however, we need to write exporters. This talk will look at how to go about this and all the tradeoffs involved in writing a good exporter.

## Abstract oficial

Speaker: Brian Brazil

In the glorious future, cancer will be cured, world hunger will solved and all
because everything was directly instrumented for Prometheus. Until then
however, we need to write exporters. This talk will look at how to go about
this and all the tradeoffs involved in writing a good exporter.

## Links

- Página oficial: https://promcon.io/2016-berlin/talks/so-you-want-to-write-an-exporter/
- YouTube: https://www.youtube.com/watch?v=KXq5ibSj2qA
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KXq5ibSj2qA
- YouTube title: PromCon 2016: So You Want to Write an Exporter - Brian Brazil
- Match score: 0.841
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2016/so-you-want-to-write-an-exporter/KXq5ibSj2qA.txt
- Transcript chars: 29999
- Keywords: exporter, actually, metric, prometheus, metrics, seconds, everything, exporters, across, request, latency, underscore, client, scrape, standard, called, instrumentation, directly

### Resumo baseado na transcript

all right so the man who needs no introduction the master of metrics with two phd in time series instrumentation and a nobel prize in proving that languages are touring complete um i give you brian brazil telling you how to write an exporter so so it has come to this yes and you now must write an exporter so we know all this already don't be a test so if you're raising prometheus what you're meant to do is directly instrument your code using the client library directly without is obviously having problems responding yeah it's just better to return instantly into those situations rather than timeout because you're using a slight amount more resources but yeah i mean you're turning 500 to via export like not all client libraries will do that actually but i'm not a physicist i just have two eight phds in uh monitoring and a nobel prize in demonstrating monitoring and string completion some of the client libraries also export the unit of the of the metric um how is prometheus currently i think

### Excerpt da transcript

all right so the man who needs no introduction the master of metrics with two phd in time series instrumentation and a nobel prize in proving that languages are touring complete um i give you brian brazil telling you how to write an exporter so so it has come to this yes and you now must write an exporter so we know all this already don't be a test so if you're raising prometheus what you're meant to do is directly instrument your code using the client library directly without wrapping it uh and because then you can get kind of an intrusive view throughout your stack and see everything but in reality you know tyrion practice interior the same in practice they aren't uh because we have the exporters now there are a small number i think there's about ten things out there that directly expose from edius metrics like etcd kubernetes robust irc but today most things don't and that's just the fact of life we have to deal with uh but a lot of applications expose metrics in a myriad of formats and the consistencies between them don't exist like maybe they're using json like we actually have a regular question can permeate except json it's like yes can you accept this piece of text i've written in the latin alphabet it's like well i know the latin alphabet but i had no idea what language you're using so in reality what we need is a custom bit of code in all cases to convert this into something that makes sense differentius and makes sense to us as human operators using the system i'm using promptql because what exporters are is that in principle prometheus will be going direct to the code and an exporter kind of just sits in the middle as a middleman and just takes in the scrape sends it on processes it and sends it back again that's what it's doing it's just a simple idea because the not directly instrumented binary doesn't have a slash metrics or if it does it's probably in json and the thing is that because of that we want an exporter to look as much as possible like a directly instrumented app so this means that prometheus is what takes care of service discovery and scheduling that means that exporters shouldn't have any logic to figure out where teams are prometheus figures it out from console or ec2 or whatever you're using similarly prometheus decides when the scrapes happen because if you're using horizontal monitoring or different people want to do different things that needs to all come from prometheus so a radius exporter should just act statelessly it t
