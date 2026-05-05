---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Unclassified"
themes: ["Cloud Native"]
speakers: ["Madelyn Olson", "AWS"]
sched_url: https://kccncna2023.sched.com/event/1R2ol/real-time-caching-for-cloud-native-applications-with-redis-madelyn-olson-aws
youtube_search_url: https://www.youtube.com/results?search_query=Real-Time+Caching+for+Cloud+Native+Applications+with+Redis+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Real-Time Caching for Cloud Native Applications with Redis - Madelyn Olson, AWS

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[Cloud Native]]
- País/cidade: United States / Chicago
- Speakers: Madelyn Olson, AWS
- Schedule: https://kccncna2023.sched.com/event/1R2ol/real-time-caching-for-cloud-native-applications-with-redis-madelyn-olson-aws
- Busca YouTube: https://www.youtube.com/results?search_query=Real-Time+Caching+for+Cloud+Native+Applications+with+Redis+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Real-Time Caching for Cloud Native Applications with Redis.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2ol/real-time-caching-for-cloud-native-applications-with-redis-madelyn-olson-aws
- YouTube search: https://www.youtube.com/results?search_query=Real-Time+Caching+for+Cloud+Native+Applications+with+Redis+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=zjsNZRvD2Aw
- YouTube title: Real-Time Caching for Cloud Native Applications with Redis - Madelyn Olson, AWS
- Match score: 0.946
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/real-time-caching-for-cloud-native-applications-with-redis/zjsNZRvD2Aw.txt
- Transcript chars: 33652
- Keywords: database, caching, basically, little, everything, source, latency, information, cluster, client, actually, called, stream, update, updates, working, common, reddis

### Resumo baseado na transcript

all right hello everyone hope you guys are enjoying your first full day at uh cucon North America 2023 uh my name is Mal olssen um we're all here today to talk about um how to build realtime highly performing applications and how you can do that with reddis um sort of I'm hoping you guys all at least know what reddis is does anyone here not know what reddis is good uh I will not be explaining it at all so none of the basics we're only here for

### Excerpt da transcript

all right hello everyone hope you guys are enjoying your first full day at uh cucon North America 2023 uh my name is Mal olssen um we're all here today to talk about um how to build realtime highly performing applications and how you can do that with reddis um sort of I'm hoping you guys all at least know what reddis is does anyone here not know what reddis is good uh I will not be explaining it at all so none of the basics we're only here for advanced stuff um yeah so I'm here to talk kind of about um sort of the talk about some basic concepts in caching and how you can extend those with res and then some of the more advanced patterns we see uh that I've seen people used um so I said my name is mine I am a principal engineer at AWS uh and I'm also one of the open source reddits maintainers so I want to start off this talk by sort of just you know a little bit of a warning which is that a lot of people these days kind of view uh like latency as like the new outage like a lot of people hear this quote where if someone sees your application being slow that's like the number one reason for people to not come back um but that doesn't necessarily mean you should put a cach there which is what we see a lot of people do and that doesn't always work great so before you know anyone tries to like suggest putting a cash in application you should really make sure like the data is cachable and that you know you can identify that piece of information with the key and then you're doing a lot of frequent lookups on that key you're not you know constantly you know updating that data and you need to reest it um so that's the first thing the second thing is make sure that you're actually like experiencing the problem on the read path we see a lot of people trying to figure out how to put caches in the right path and they generally don't work out super well you can do something you can like buffer data but that's not quite caching we see people start losing data like don't don't do that either um um the other good reason to start adding caches when you start hitting scaling limits you usually want to start rethinking how your architecture work if that's the problem you're having it's probably not caching um and also tolerate eventual consistency so many people just think like oh we can just put a cache in front of our like user apis and then it works and it doesn't so those are sort of like you know I'm going to talk more about you know making sure you're following these in a
