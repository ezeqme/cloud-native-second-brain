---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Operations + Performance"
themes: ["SRE Reliability"]
speakers: ["Cyril Becker", "Vincent Bernaud", "XBTO"]
sched_url: https://kccnceu2024.sched.com/event/1YeR8/high-performance-multi-regions-messaging-with-nats-cyril-becker-vincent-bernaud-xbto
youtube_search_url: https://www.youtube.com/results?search_query=High+Performance+Multi+Regions+Messaging+with+Nats+CNCF+KubeCon+2024
slides: []
status: parsed
---

# High Performance Multi Regions Messaging with Nats - Cyril Becker & Vincent Bernaud, XBTO

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Operations + Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Cyril Becker, Vincent Bernaud, XBTO
- Schedule: https://kccnceu2024.sched.com/event/1YeR8/high-performance-multi-regions-messaging-with-nats-cyril-becker-vincent-bernaud-xbto
- Busca YouTube: https://www.youtube.com/results?search_query=High+Performance+Multi+Regions+Messaging+with+Nats+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre High Performance Multi Regions Messaging with Nats.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeR8/high-performance-multi-regions-messaging-with-nats-cyril-becker-vincent-bernaud-xbto
- YouTube search: https://www.youtube.com/results?search_query=High+Performance+Multi+Regions+Messaging+with+Nats+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=pSEEKZdOzMc
- YouTube title: High Performance Multi Regions Messaging with Nats - Cyril Becker & Vincent Bernaud, XBTO
- Match score: 0.826
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/high-performance-multi-regions-messaging-with-nats/pSEEKZdOzMc.txt
- Transcript chars: 31163
- Keywords: cluster, region, infrastructure, everything, basically, clusters, trading, processes, feature, around, connect, performance, available, another, latency, platform, architecture, connected

### Resumo baseado na transcript

hi everyone thanks for joining this session so today we'll talk together about high performance multi- region messaging with NS so before to do that let's talk about who we are so I'm serial Beaker I'm Ed infrastructure at xbto uh where I lead and managed infrastructure team since 2022 I started as a Linux HPC C and me I have more than 15 year experience in open source infrastructure and services uh I just discover kubernetes andat in 2017 and I designed previously many highly scalable platform in the just choose a gold old VPN on the internet that is doing the tricks um on each region so all our processes are running into multiple kubernetes clusters so we use eks on AWS but also on Prem air ke on distribution I think soon

### Excerpt da transcript

hi everyone thanks for joining this session so today we'll talk together about high performance multi- region messaging with NS so before to do that let's talk about who we are so I'm serial Beaker I'm Ed infrastructure at xbto uh where I lead and managed infrastructure team since 2022 I started as a Linux HPC C and me I have more than 15 year experience in open source infrastructure and services uh I just discover kubernetes andat in 2017 and I designed previously many highly scalable platform in the public Cloud for Di Tech and the mobile game industry and I'm V berno I'm de at xbto for more than three years now uh I'm mainly focusing on dev and trading teams and I have five years experience in CIS admin and Cloud native applications so web who we are and what are we doing so we are cryp crypto trading uh FM uh we were built in 2015 um as a proprietary crypto trading investment firm but today we are full service company offering different service around crypto and investment in 2023 we acquire a custodian trading platform that is called stable house and then uh now stabil housee um secure some oh sorry for that secure some big deal with the fifth largest FM that is called Apex um I think there's a word thing with the TV sorry for that should be good sorry um so may maybe some of you already know us because we signed uh lonel Messi at the food Miami football club yers and we are also the main corporate in Jersey sponsor of Miami a football club co-owned by David Beckham and George Mass we are licensed by The Bermuda monetary Authority and have a present in five location so Bermuda Miami New York London Paris and Abu Dhabi next so what about the agenda first we'll present our needs uh and why we uh choose NS then we'll present quickly NS for those of you who don't know the the technology then we'll Deep dive into the platform and the architecture and the change we faced and at the end we'll present a quick tool that we developed uh ourselves and we'll answer all of your questions at the end so let's talk about our needs and our use case so what what we want to do at xbto is to share collected data between processes located in different region around the world so what we want is to have a full mesh technology that can connect several local message boost together to our messages we want also something that have clustering technology to have rency and availability something stateless that do not require to rating to disk and that store all the data in memory
