---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2022"
edition_id: 2022-munich
year: 2022
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2022-munich/talks/why-is-it-so-big-analysing-the-m/
youtube_url: https://www.youtube.com/watch?v=vc5LgoiP_CA
youtube_search_url: https://www.youtube.com/results?search_query=Why+Is+It+so+Big%3F+Analysing+the+Memory+Consumption+of+Prometheus+PromCon+2022
video_match_score: 1.017
status: video-found
---

# Why Is It so Big? Analysing the Memory Consumption of Prometheus

## Identificação

- Edição: PromCon EU 2022
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2022-munich/talks/why-is-it-so-big-analysing-the-m/
- YouTube: https://www.youtube.com/watch?v=vc5LgoiP_CA

## Resumo

Speaker(s): Bryan Boreham A large Prometheus instance may take 100GB of RAM, or even more. In this talk I will walk through the main internal data structures that contribute to that size. This talk should be of interest to anyone who would like their Prometheus to be a bit smaller.

## Abstract oficial

Speaker(s): Bryan Boreham

A large Prometheus instance may take 100GB of RAM, or even more.
In this talk I will walk through the main internal data structures that contribute to that size.

This talk should be of interest to anyone who would like their Prometheus to be a bit smaller.
Attendees will take away potential changes in configuration or workload that make the size go down.

## Links

- Página oficial: https://promcon.io/2022-munich/talks/why-is-it-so-big-analysing-the-m/
- YouTube: https://www.youtube.com/watch?v=vc5LgoiP_CA
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vc5LgoiP_CA
- YouTube title: PromCon EU 2022: Why Is It so Big? Analysing the Memory Consumption of Prometheus
- Match score: 1.017
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2022/why-is-it-so-big-analysing-the-memory-consumption-of-prometheus/vc5LgoiP_CA.txt
- Transcript chars: 26386
- Keywords: prometheus, memory, garbage, little, picture, labels, series, another, chunks, number, structure, bigger, actually, called, gigabytes, everything, reason, samples

### Resumo baseado na transcript

[Music] hi hello everyone let me uh figure out how to get uh my thing on screen oh that's pretty good let's just uh figure out how the mouse works okay so we're going to do this one view full screen okay so now we can get going hello hello um my name is Brian boram as uh Julius was just saying and um so my talk uh I I sort of changed the title I I called it dude where's my memory um and then I thought that's that's little bit dangerous so I'm I'm recommending the the relative measure so if if you if you beat up your Prometheus if you really make it go fast like do a lot of queries a lot of work um then then it will get bigger

### Excerpt da transcript

[Music] hi hello everyone let me uh figure out how to get uh my thing on screen oh that's pretty good let's just uh figure out how the mouse works okay so we're going to do this one view full screen okay so now we can get going hello hello um my name is Brian boram as uh Julius was just saying and um so my talk uh I I sort of changed the title I I called it dude where's my memory um and then I thought that's that's not inclusive so uh Prometheus where did where did my memory go um this uh chart on the right here is uh uh sort of approximately the point where um where I decided to fix one bug in particular or or to sort of say where you know because it it hit 400 gigabytes I don't know if you can read the text but uh this is one of our production Prometheus um in one of our largest clusters and it it it hit 400 GB and crashed and uh uh anyway we'll tell you a little bit about about how we got there um so uh yeah I should say a little bit I I work at graffin Labs on what we call the databases we store things in our cloud service and and use with um several open source projects uh so we store metrics in mimir we store logs in Loki we store traces in temp Po and um we run a lot of this we do all of our monitoring on our own system MIM which which holds all of the uh metrics for everyone so it might be a little weird like why do I care about Prometheus well we run we run Prometheus as a backup uh because we're we're sort of afraid that our own uh tool might fall over and um so we we run both and the uh uh point of mimir is to be horizontally scalable you you can you can spread the work out over many many computers but Prometheus is is vertically scalable everything has to fit in one process um so let's see what I guess some of you must experience this so who's who runs Prometheus nearly everyone okay okay keep keep your hand up if you have a Prometheus bigger than um 100 GB oh lots of people like a third of the audience 100 gbes nothing uh what about the one I had 400 GB few okay who who's got bigger who's got one keep your hand up if you're bigger than 400 gigabytes there's one okay so this talk is for you um oh yeah one thing I I met someone outside who wanted to know why his exporter was taking so much memory and sadly I'm going to have to do that talk another day uh this talk is about Prometheus the server where the that's what I'm talking about today not the exporters um okay uh so another bit of History um recent history so this was uh Ganesh uh very plea
