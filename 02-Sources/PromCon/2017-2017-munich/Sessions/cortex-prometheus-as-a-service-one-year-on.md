---
type: promcon-talk
conference: PromCon
edition: "PromCon 2017"
edition_id: 2017-munich
year: 2017
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Remote Write Storage", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2017-munich/talks/cortex-prometheus-as-a-service-one-year-on/
youtube_url: https://www.youtube.com/watch?v=_8DmPW4iQBQ
youtube_search_url: https://www.youtube.com/results?search_query=Cortex%3A+Prometheus+as+a+Service%2C+One+Year+On+PromCon+2017
video_match_score: 0.908
status: video-found
---

# Cortex: Prometheus as a Service, One Year On

## Identificação

- Edição: PromCon 2017
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Remote Write Storage]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2017-munich/talks/cortex-prometheus-as-a-service-one-year-on/
- YouTube: https://www.youtube.com/watch?v=_8DmPW4iQBQ

## Resumo

Speaker: Tom Wilkie At PromCon 2016, I presented "Project Frankenstein: A multitenant, horizontally scalable Prometheus as a service". It's now one year later, and lots has changed - not least the name! This talk will discuss what we've learnt running a Prometheus service for the past year, the architectural changes we made from the original design, and the improvements we've made to the Cortex user experience.

## Abstract oficial

Speaker: Tom Wilkie

At PromCon 2016, I presented "Project Frankenstein: A multitenant, horizontally scalable Prometheus as a service". It's now one year later, and lots has changed - not least the name! This talk will discuss what we've learnt running a Prometheus service for the past year, the architectural changes we made from the original design, and the improvements we've made to the Cortex user experience.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2017-munich/talks/cortex-prometheus-as-a-service-one-year-on/
- YouTube: https://www.youtube.com/watch?v=_8DmPW4iQBQ
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_8DmPW4iQBQ
- YouTube title: PromCon 2017: Cortex: Prometheus as a Service, One Year On - Tom Wilkie
- Match score: 0.908
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2017/cortex-prometheus-as-a-service-one-year-on/_8DmPW4iQBQ.txt
- Transcript chars: 31368
- Keywords: prometheus, dynamodb, cortex, actually, write, queries, storage, bigtable, distributor, throughput, schema, wanted, cost, performance, number, distributed, latency, getting

### Resumo baseado na transcript

[Music] hello everybody welcome to day two how are you feeling after the beer last night so a priority had a few fights I was a - and so a few small notices there are still some slots for electing talks so just write your name down on the board outside above Ritchie's name because he's going to last you also if all speakers if you could send on our slides please so we can link to them from the schedule so now you're going to have Tom who is

### Excerpt da transcript

[Music] hello everybody welcome to day two how are you feeling after the beer last night so a priority had a few fights I was a - and so a few small notices there are still some slots for electing talks so just write your name down on the board outside above Ritchie's name because he's going to last you also if all speakers if you could send on our slides please so we can link to them from the schedule so now you're going to have Tom who is going to talk about cortex which is long-term storage - distributed radius yes yes okay good hello everyone thanks instruction brian i said i'm talk about context but first I'd like everyone to put their hand up everyone no excuses right and now if you weren't here last year you can put them down again if you weren't yeah okay not as many as I was hoping so this is going to be a bit of her what we taught them because it's going to be very referential to last year's talk and I'm kind of try and build on that last year I presented cortex which is a horizontally scalable distributed prometheus version of Prometheus basically Prometheus compatible monitoring system I guess you should all go and read that or watch that video so I'll give you about five minutes here okay so yeah about a year ago I had a different haircut I'll give you a brief overview of what we discussed last year and then I'm just going to build on it and give you my experience of running this system and improving the system for the last year so what is prometheus Prometheus is a natively multi-tenant where we Prometheus service where we isolate different customers in the same services we did this because a year ago I worked for a company called weave works which is sponsoring this event and we wanted to offer Prometheus as a service as part of our product which is called weave so we needed multi-tenancy we want him to do it in that in a single service not give like a container to each customer because we wanted it to be nice and easy to operate we wanted it to be more scalable and so on we had a bit of experience running a container per customer and it wasn't good one of the main motivations for cortex was making it cost-effective to run you know we've worked the business to make money and so therefore we had to you know sell this thing for more than it cost us to run it and you'll see that later in in my experience we also wanted to offer a different set of trade-offs around scalability in hey CheY and Prometheus is a very high-performance system you know
