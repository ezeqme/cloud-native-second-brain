---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Tomasz Pietrek", "Synadia Communications"]
sched_url: https://kccnceu2022.sched.com/event/ytm8/state-of-nats-core-persistence-materialized-views-tomasz-pietrek-synadia-communications
youtube_search_url: https://www.youtube.com/results?search_query=State+of+NATS%3A+Core%2C+Persistence%2C+%26+Materialized+Views+CNCF+KubeCon+2022
slides: []
status: parsed
---

# State of NATS: Core, Persistence, & Materialized Views - Tomasz Pietrek, Synadia Communications

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: Tomasz Pietrek, Synadia Communications
- Schedule: https://kccnceu2022.sched.com/event/ytm8/state-of-nats-core-persistence-materialized-views-tomasz-pietrek-synadia-communications
- Busca YouTube: https://www.youtube.com/results?search_query=State+of+NATS%3A+Core%2C+Persistence%2C+%26+Materialized+Views+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre State of NATS: Core, Persistence, & Materialized Views.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytm8/state-of-nats-core-persistence-materialized-views-tomasz-pietrek-synadia-communications
- YouTube search: https://www.youtube.com/results?search_query=State+of+NATS%3A+Core%2C+Persistence%2C+%26+Materialized+Views+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=MPda_7EPrNU
- YouTube title: State of NATS: Core, Persistence, & Materialized Views - Tomasz Pietrek, Synadia Communications
- Match score: 0.801
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/state-of-nats-core-persistence-materialized-views/MPda_7EPrNU.txt
- Transcript chars: 24971
- Keywords: object, stream, actually, storage, basically, values, delete, cluster, history, pretty, features, clusters, allows, whatever, simple, important, little, jetstream

### Resumo baseado na transcript

hello everybody uh welcome to the nuts presentation i'm really happy that you are so many of you it was not easy to find the place uh this talk is about state of nuts about the core persistence materialized views i will walk through some basics of nuts with you and also update you on on the new things my name is thomas and i am engineer at scenadia as an area is company behind nuts i'm a maintainer of the last client mainly and also contributing to the other

### Excerpt da transcript

hello everybody uh welcome to the nuts presentation i'm really happy that you are so many of you it was not easy to find the place uh this talk is about state of nuts about the core persistence materialized views i will walk through some basics of nuts with you and also update you on on the new things my name is thomas and i am engineer at scenadia as an area is company behind nuts i'm a maintainer of the last client mainly and also contributing to the other repositories and scenarios companies as i said behind nuts and is having another service and most of the contributors actually uh at at the company okay so what would be the agenda first of all as i said i want to do some introduction to nuts for those of you who are maybe heard of it or not yet and want to not be out of the context when i will get on the features then we'll get through the new features and we'll do some hopefully successful demo of chosen features which are key value storage and object store so before i start how many of you heard about nuts that's it that's impressive how many of you use nuts in production those are really impressive numbers and actually this is something i wanted to talk about for a moment which was not part of my agenda but i think it's really interesting and impressive for me that when we arrived here uh the amount of people that reached us that we the companies that we met that are using nuts on the pavilions like half of them were at some stage of doing pocs or knowing about it or having it in production that that part of nuts that it just was downward from the community actually the adoption that came is something that's just i was shocked and as positively as i can be and that's what makes us really happy and really impressed those hands reason tells a lot but okay so i feel now it's a little pointless to talk about what did not if most of you use it in production so let's go through it anyway um so basically it's performance simplicity security and availability it's the same very simple thing that is at the same time very performant and very easy to secure to the point you could call it like uh zero trust and properly secured uh in addition for last one year especially more than one year when jetstream arrived i think that it improved a lot in terms of the feature coverage because it it's not only pops up it it was it had not streaming but it was not as simple as without it and with jetstream built in the snap server which is this 15 megabytes binary we get b
