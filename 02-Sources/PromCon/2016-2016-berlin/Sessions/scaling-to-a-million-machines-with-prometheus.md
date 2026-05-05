---
type: promcon-talk
conference: PromCon
edition: "PromCon 2016"
edition_id: 2016-berlin
year: 2016
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Kubernetes", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2016-berlin/talks/scaling-to-a-million-machines-with-prometheus/
youtube_url: https://www.youtube.com/watch?v=likpVWB5Lvo
youtube_search_url: https://www.youtube.com/results?search_query=Scaling+to+a+Million+Machines+with+Prometheus+PromCon+2016
video_match_score: 0.88
status: video-found
---

# Scaling to a Million Machines with Prometheus

## Identificação

- Edição: PromCon 2016
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Kubernetes]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2016-berlin/talks/scaling-to-a-million-machines-with-prometheus/
- YouTube: https://www.youtube.com/watch?v=likpVWB5Lvo

## Resumo

Speaker: Matthew Campbell Digital Ocean hosts a public facing monitoring platform that runs on top of Prometheus. We will discuss how we scale Prometheus up to millions of virtual machines. How we manage and maintain the largest Prometheus cluster in the world.

## Abstract oficial

Speaker: Matthew Campbell

Digital Ocean hosts a public facing monitoring platform that runs on top of
Prometheus. We will discuss how we scale Prometheus up to millions of virtual
machines. How we manage and maintain the largest Prometheus cluster in the
world. Also how we do multi-tenancy in Prometheus.

## Links

- Página oficial: https://promcon.io/2016-berlin/talks/scaling-to-a-million-machines-with-prometheus/
- YouTube: https://www.youtube.com/watch?v=likpVWB5Lvo
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=likpVWB5Lvo
- YouTube title: PromCon 2016: Scaling to a Million Machines with Prometheus - Matthew Campbell
- Match score: 0.88
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2016/scaling-to-a-million-machines-with-prometheus/likpVWB5Lvo.txt
- Transcript chars: 26266
- Keywords: prometheus, actually, servers, server, metrics, machines, basically, cassandra, wanted, vulcan, interface, started, cluster, machine, sharding, special, storage, scrape

### Resumo baseado na transcript

this is Matthew from digitalocean last year at velocity Julius I velocity New York there many velocities we visited the digitalocean office and that was the first time we realized somebody is out there that runs a bigger Prometheus setup and SoundCloud that's pretty nice because we always consider ourselves the biggest user of Prometheus but then now there are many bigger uses I guess some are doing weird things but at digitalocean scales to millions of machines and that what Matthew will tell us about awesome thanks yeah so

### Excerpt da transcript

this is Matthew from digitalocean last year at velocity Julius I velocity New York there many velocities we visited the digitalocean office and that was the first time we realized somebody is out there that runs a bigger Prometheus setup and SoundCloud that's pretty nice because we always consider ourselves the biggest user of Prometheus but then now there are many bigger uses I guess some are doing weird things but at digitalocean scales to millions of machines and that what Matthew will tell us about awesome thanks yeah so the original top title was about scaling for me theists to a million machines but I thought I would change it to how he broke Prometheus in every way possible I think it's a bit more fun to talk about how he broke things and how we got past all the breaking just as a show a hand here who here has like a million things that they're monitoring with Prometheus oh there's one oh there's two other people oh well I mean I'm talking millions of scrape targets okay how about tens of thousands thousands okay we got like four yes all right and then hundreds I would expect at least the whole audience should have hundreds okay cool so hopefully next year we'll have a lot more people that will have much larger installations and we'll be breaking new ground here so just really quick about me I work on the time series team at digitalocean I live in Bangkok so I may have traveled the farthest anybody here travel farther than Bangkok to get here oh Indonesia all right awesome so I I didn't win this one yeah so I kind of want to structure this talk as kind of the dark days of dizzier ocean before we found Prometheus to where we are now where we have a million Prometheus servers so when I originally started at digitalocean every single team had a different monitoring and metric solution there was teams that were running by their teams they were running in flux DB and for some godforsaken reason we had a 50 node open TS DB cluster which somehow I am inherited when I started there so one of the first things we did was just turn that off so we started using this Prometheus thing so my managers of time Ian he's gonna give a talk later is he's like this Prometheus thing looks pretty cool so we started to use it and it was really small at the beginning we were just kind of monitoring a few micro services here and there and basically each team had their own Prometheus server and each team would manually set up their Prometheus server with manual targets they wo
