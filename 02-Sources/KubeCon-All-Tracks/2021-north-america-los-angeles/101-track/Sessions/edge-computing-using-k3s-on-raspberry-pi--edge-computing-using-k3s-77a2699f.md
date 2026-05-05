---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "101 Track"
themes: ["101 Track"]
speakers: ["Jeff Spahr", "Lenovo"]
sched_url: https://kccncna2021.sched.com/event/lV53/edge-computing-using-k3s-on-raspberry-pi-jeff-spahr-lenovo
youtube_search_url: https://www.youtube.com/results?search_query=Edge+Computing+using+K3s+on+Raspberry+Pi+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Edge Computing using K3s on Raspberry Pi - Jeff Spahr, Lenovo

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[101 Track]]
- Temas: [[101 Track]]
- País/cidade: United States / Los Angeles
- Speakers: Jeff Spahr, Lenovo
- Schedule: https://kccncna2021.sched.com/event/lV53/edge-computing-using-k3s-on-raspberry-pi-jeff-spahr-lenovo
- Busca YouTube: https://www.youtube.com/results?search_query=Edge+Computing+using+K3s+on+Raspberry+Pi+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Edge Computing using K3s on Raspberry Pi.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV53/edge-computing-using-k3s-on-raspberry-pi-jeff-spahr-lenovo
- YouTube search: https://www.youtube.com/results?search_query=Edge+Computing+using+K3s+on+Raspberry+Pi+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=BgzQYlxYOmE
- YouTube title: Edge Computing using K3s on Raspberry Pi - Jeff Spahr, Lenovo
- Match score: 0.896
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/edge-computing-using-k3s-on-raspberry-pi/BgzQYlxYOmE.txt
- Transcript chars: 15715
- Keywords: version, pretty, upgrade, install, running, wanted, server, raspberry, controller, already, cluster, around, probably, actually, second, manifest, computing, option

### Resumo baseado na transcript

thanks everyone for joining this session on edge computing using keys on raspberry pi my name is jeff sparr i'm a senior engineering manager at lenovo so let's start with what is edge computing it's when you're bringing compute and storage closer to the source of the data this is typically sites that are not data centers so it could be factory floors vehicles retail stores or restaurants wind farms it could be constraints around space power or cost and what makes this project edge computing we've got a small with things out of the box that i needed like local storage provider and traffic ingress controller it has really good arm 64 support it's a very active project with a large user base and it's backed by a rancher so it's probably not going

### Excerpt da transcript

thanks everyone for joining this session on edge computing using keys on raspberry pi my name is jeff sparr i'm a senior engineering manager at lenovo so let's start with what is edge computing it's when you're bringing compute and storage closer to the source of the data this is typically sites that are not data centers so it could be factory floors vehicles retail stores or restaurants wind farms it could be constraints around space power or cost and what makes this project edge computing we've got a small form factor we've got the raspberry pi which is about the size of a wallet uh we have low power consumption with the arm 64 processor uh and uh keys has some abilities to bootstrap applications without an internet connection as well so why raspberry pi well the latest one comes in three sizes there's the two gig four gig and eight gig option uh that my inflection point for getting into this was when the eight gig option came out about mid-2020 for me that was uh yep that that's enough to go ahead and run a kubernetes node with the applications i'm interested in so this will be a fun home lab project they all have the same processor it's a quad-core arm 64.

they're small and quiet they're inexpensive and they have low power consumption uh this was important for me because i've always kind of had interest in having a home lab but i don't have a ton of space if i ever do the the the calculations of what the price would be to run a real server for an entire year in my home that's usually enough to to tell me uh that i'm not going to do that project to move on to something else so this was this was a good opportunity to get into this for me why keys that's k3s to pronounce keys by the way well it's packaged as a single binary so that makes it pretty easy to install it also gives it a smaller memory footprint it comes with things out of the box that i needed like local storage provider and traffic ingress controller it has really good arm 64 support it's a very active project with a large user base and it's backed by a rancher so it's probably not going anywhere for the parts list uh so i started with three raspberry pi's uh three sd cards uh i had a use case where i needed more capacity here so that here's a place where you can save some money if you don't need quite as big of an sd card uh three power supplies uh if you look around the internet on this most people recommend not to use a just a usbc phone charger that you have lying around because you're n
