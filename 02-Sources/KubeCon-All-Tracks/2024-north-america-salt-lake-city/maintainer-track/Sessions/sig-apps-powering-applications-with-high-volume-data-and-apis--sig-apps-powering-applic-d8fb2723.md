---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Storage Data", "Community Governance"]
speakers: ["Maciej Szulik", "Defense Unicorns", "Janet Kuo", "Google"]
sched_url: https://kccncna2024.sched.com/event/1howE/sig-apps-powering-applications-with-high-volume-data-and-apis-maciej-szulik-defense-unicorns-janet-kuo-google
youtube_search_url: https://www.youtube.com/results?search_query=SIG-Apps%3A+Powering+Applications+with+High-Volume+Data+and+APIs+CNCF+KubeCon+2024
slides: []
status: parsed
---

# SIG-Apps: Powering Applications with High-Volume Data and APIs - Maciej Szulik, Defense Unicorns & Janet Kuo, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Storage Data]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Maciej Szulik, Defense Unicorns, Janet Kuo, Google
- Schedule: https://kccncna2024.sched.com/event/1howE/sig-apps-powering-applications-with-high-volume-data-and-apis-maciej-szulik-defense-unicorns-janet-kuo-google
- Busca YouTube: https://www.youtube.com/results?search_query=SIG-Apps%3A+Powering+Applications+with+High-Volume+Data+and+APIs+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre SIG-Apps: Powering Applications with High-Volume Data and APIs.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1howE/sig-apps-powering-applications-with-high-volume-data-and-apis-maciej-szulik-defense-unicorns-janet-kuo-google
- YouTube search: https://www.youtube.com/results?search_query=SIG-Apps%3A+Powering+Applications+with+High-Volume+Data+and+APIs+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=NWZhAs69heA
- YouTube title: SIG-Apps: Powering Applications with High-Volume Data and APIs - Maciej Szulik & Janet Kuo
- Match score: 0.916
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/sig-apps-powering-applications-with-high-volume-data-and-apis/NWZhAs69heA.txt
- Transcript chars: 22430
- Keywords: working, controller, around, actually, controllers, running, initially, changes, particular, probably, eventually, various, update, stateful, basically, called, couple, feature

### Resumo baseado na transcript

so today we are going to present C gaps it's 10 year of kubernetes so we are going to do an overview of the history of what we've accomplished before and what we are going to do next so in seaps we have three chairs and the first is me Janet I remember my first contribution back in 2015 it was a simple duck update because it's just the beginning and then the journey starts there and then we have maek um his first contribution is was from 2014 and

### Excerpt da transcript

so today we are going to present C gaps it's 10 year of kubernetes so we are going to do an overview of the history of what we've accomplished before and what we are going to do next so in seaps we have three chairs and the first is me Janet I remember my first contribution back in 2015 it was a simple duck update because it's just the beginning and then the journey starts there and then we have maek um his first contribution is was from 2014 and he worked in the both in seaps and S CI he's also serving in the steering committee and his first contribution was back in 2014 and it was a um dependency update and the third chair is Ken so Ken cannot be here today um so I'll just introduce him virtually and then uh his contribution is in 2017 and it was a refactoring of the seful set API okay so the Sig apps that's a big word special interest group but the apps is such a broad topic but what the what the special interest group actually is overseeing so we have three areas which were slowly developing over the past decade the first one that we actually initially started with uh was the workloads application if you are working with Cube you're probably familiar with the apps API Group that's where we have deployment replica set we used to have replication controllers theoretically that still exist there stateful set then over time we were adding additional groups such as batch and batch is basically everything job related and Crown job and eventually in the meantime we also added a third Group which was uh which holds the PO disruption budget which helps us to ensure that at least the minimum um number of replicas are running of our application during eventual disruptions like node draining or upgrades of of nodes where we want to make sure the application are smoothly running so like Janet mentioned it's the first decade of cube I'm slowly reaching the time when I'll be able to say that I have 10 years of experience working on Cube It's like you saw on one of the first slides it's December 14th so I'm I'm eagerly waiting for that I'll I'll be broadly announcing that but let's let's quickly look look back what we've what we've accomplished over the past 10 years so Cube was initially announced in June of 2014 the actual first official release that you can find on GitHub was uh was 0.2 around September 24 2014 and if you look at what has happened over the years or especially in the first months there was a big turmo of changes we were quickly iterating over V1 bet
