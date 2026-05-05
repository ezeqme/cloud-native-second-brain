---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Reliability + Operational Continuity"
themes: ["AI ML", "Runtime Containers", "SRE Reliability"]
speakers: ["Julian Portillo", "Relativity"]
sched_url: https://kccncna2022.sched.com/event/182Ea/lessons-from-scheduling-20-million-windows-containers-a-month-julian-portillo-relativity
youtube_search_url: https://www.youtube.com/results?search_query=Lessons+From+Scheduling+20+Million+Windows+Containers+a+Month+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Lessons From Scheduling 20 Million Windows Containers a Month - Julian Portillo, Relativity

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Reliability + Operational Continuity]]
- Temas: [[AI ML]], [[Runtime Containers]], [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Julian Portillo, Relativity
- Schedule: https://kccncna2022.sched.com/event/182Ea/lessons-from-scheduling-20-million-windows-containers-a-month-julian-portillo-relativity
- Busca YouTube: https://www.youtube.com/results?search_query=Lessons+From+Scheduling+20+Million+Windows+Containers+a+Month+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Lessons From Scheduling 20 Million Windows Containers a Month.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Ea/lessons-from-scheduling-20-million-windows-containers-a-month-julian-portillo-relativity
- YouTube search: https://www.youtube.com/results?search_query=Lessons+From+Scheduling+20+Million+Windows+Containers+a+Month+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=LxVcNXu04eg
- YouTube title: Lessons From Scheduling 20 Million Windows Containers a Month - Julian Portillo, Relativity
- Match score: 0.899
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/lessons-from-scheduling-20-million-windows-containers-a-month/LxVcNXu04eg.txt
- Transcript chars: 29794
- Keywords: windows, containers, failures, started, actually, production, running, container, issues, workloads, around, pretty, relativity, instead, working, problems, change, migration

### Resumo baseado na transcript

cool hi everybody my name is Julian Portillo I'm from relativity it's a small Enterprise company that is making a migration from VMS into kubernetes and we have run into a lot of foot guns and hopefully we can help you guys not hit as many feet and instead hit targets so we started to migrate to Windows containers in June of 2021. fall a little bit at scale uh turns out when you're scheduling like 30 million containers uh inside a single cluster um it's not fun to deal with those failures so we started to dig more deeply into what's actually causing these failures and like what what was happening on the nodes when we had these and because our host containers available we could poke around more easily than already peeing in and we could write things that would go capture logs send them a blob and then debug what non-production Canary things we also have metrics that we use and stuff but I like seeing things in slack because it's fun looks like we have some more 2019 failures since we started this talk but zero 2022 failures so that's pretty cool yay um but it'll roll out to the other regions over the next two or three weeks too so make sure you update make sure you grab that you'll be a lot happier Okay so tail shoe designs things been really sad really scary this is only

### Excerpt da transcript

cool hi everybody my name is Julian Portillo I'm from relativity it's a small Enterprise company that is making a migration from VMS into kubernetes and we have run into a lot of foot guns and hopefully we can help you guys not hit as many feet and instead hit targets so we started to migrate to Windows containers in June of 2021. for the first nine months of this year we've gone through 192 million Windows containers that are actually doing like production workloads 50 million that are doing Canary workloads and like testing see if nodes are working and we found 105 failed Windows nodes so obviously if you don't have an automated way to catch failures like that you're going to have a very bad time so help you figure out how you can catch failures such as those the number one lesson to take away as you migrate to kubernetes on a Linux world or a Windows world is these things are cattle not pets when you start your migration pods can be the cattle and then as you get higher and higher in your migration eventually nodes can be a cattle and shoot those things in the head and find new things and then eventually you can get to the world where clusters can be moved around and swapped at will and that's where you're in a very happy spot from a devops world so here's we're going to go through first who are we what is the team that I work on and what is relativity then a quick understanding of what our first kubernetes setup was why we started to use Windows containers and like the general motivation for it since it's not a super common way to move two years ago and then Windows container pain points we run into how you can avoid those and some recent very positive changes like literally this morning for Windows containers that you'll probably be pretty excited about so who are we I think in engineering especially platforming devops it's important to remember that it's a team sport you have to make sure that everybody in the team enjoys working together and that you have there's no one individual who knows everything about everything on what you're working on on our team we have about 30 really smart motivated happy platform Engineers that work on making sure that all of Relativity works well we've supported about 500 different application engineers and we uh have our own music video we've got team logos we've got movie trailers for demos and we do pretty fun game days where we like see how to break things in production and then how to come back from the dead when
