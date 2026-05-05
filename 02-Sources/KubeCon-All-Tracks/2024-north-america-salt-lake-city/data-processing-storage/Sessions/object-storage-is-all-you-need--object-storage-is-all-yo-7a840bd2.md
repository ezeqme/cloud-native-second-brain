---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Data Processing + Storage"
themes: ["Storage Data"]
speakers: ["Justin Cormack", "Docker"]
sched_url: https://kccncna2024.sched.com/event/1i7qV/object-storage-is-all-you-need-justin-cormack-docker
youtube_search_url: https://www.youtube.com/results?search_query=Object+Storage+Is+All+You+Need+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Object Storage Is All You Need - Justin Cormack, Docker

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]]
- País/cidade: United States / Salt Lake City
- Speakers: Justin Cormack, Docker
- Schedule: https://kccncna2024.sched.com/event/1i7qV/object-storage-is-all-you-need-justin-cormack-docker
- Busca YouTube: https://www.youtube.com/results?search_query=Object+Storage+Is+All+You+Need+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Object Storage Is All You Need.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7qV/object-storage-is-all-you-need-justin-cormack-docker
- YouTube search: https://www.youtube.com/results?search_query=Object+Storage+Is+All+You+Need+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ei0wwTy6_G4
- YouTube title: Object Storage Is All You Need - Justin Cormack, Docker
- Match score: 0.812
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/object-storage-is-all-you-need/ei0wwTy6_G4.txt
- Transcript chars: 28529
- Keywords: object, storage, actually, latency, applications, interesting, amazon, database, simple, primitive, write, source, basically, having, concurrency, thinking, another, exciting

### Resumo baseado na transcript

hi well nice to be here great to see so many people here I thought it was just going to be me and YouTube but um uh you're all the the hardcore people who are not going to leave until everything's done which is great hope you've been having a great Cube conon It's been a it's been a really really nice experience for me um bunch of people ask me why I'm giving a talk about object storage it's you know it's um like everyone else I've submitted talks

### Excerpt da transcript

hi well nice to be here great to see so many people here I thought it was just going to be me and YouTube but um uh you're all the the hardcore people who are not going to leave until everything's done which is great hope you've been having a great Cube conon It's been a it's been a really really nice experience for me um bunch of people ask me why I'm giving a talk about object storage it's you know it's um like everyone else I've submitted talks to cucon for a while and they've all been rejected and sometimes given that reach and sometimes I um haven't but anyway this time I thought well I'm just going to submit some you know a fun talk that I want to do because um that is unexpected um and is about the some of the things that have been really interesting me and that I think that you know maybe maybe other people can learn about too and understand about so um you know object storage I think is actually one of the most exciting kind of areas in Cloud native right now and I'll explain why anyway uh I'm Justin KAC I'm the CTO at Docker um I've been working at Docker for a long time we use a lot of object storage at Docker we have this thing called Docker Hub and it's a it's uses a very large amount of object storage so it's something that um you know we care about um but we also um I think there's a lot of other lessons from object storage um I think it can teach us a lot about what cloud native infrastructure looks like and why you know some you know it's one of those things that actually um is really kind of foundational and kind of interesting in the in the way the user experience and the way you can use it um Amazon S3 was my first experience of the cloud I think it was many people it was the first cloud service that Amazon launched back in 2006 um and I remember thinking this thing's kind of cool um and then bringing it in as Shadow it into a company I was working in and being told off for not using official Amazon servers and using my own private account but it's like well get get used to provisioning this stuff we're going to need more of this um and there's a whole lot of new stuff going on that I'm going to talk about like it's actually like this year has been actually like the most exciting year for object storage since 2006 I'd say so um there's actually an awful lot going on like most of my talks I'm going to start with a bit of History I I like understanding things through the view of how how we got here um and the brief for Amazon S3 was um ma
