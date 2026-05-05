---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Mark Fussell", "Chris Gillium", "Diagrid"]
sched_url: https://kccncna2023.sched.com/event/1R2ta/dapr-workflows-and-the-road-ahead-mark-fussell-chris-gillium-diagrid
youtube_search_url: https://www.youtube.com/results?search_query=Dapr%2C+Workflows%2C+and+the+Road+Ahead+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Dapr, Workflows, and the Road Ahead - Mark Fussell & Chris Gillium, Diagrid

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Mark Fussell, Chris Gillium, Diagrid
- Schedule: https://kccncna2023.sched.com/event/1R2ta/dapr-workflows-and-the-road-ahead-mark-fussell-chris-gillium-diagrid
- Busca YouTube: https://www.youtube.com/results?search_query=Dapr%2C+Workflows%2C+and+the+Road+Ahead+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Dapr, Workflows, and the Road Ahead.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2ta/dapr-workflows-and-the-road-ahead-mark-fussell-chris-gillium-diagrid
- YouTube search: https://www.youtube.com/results?search_query=Dapr%2C+Workflows%2C+and+the+Road+Ahead+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=yNo3P_n7AU4
- YouTube title: Dapr, Workflows, and the Road Ahead - Mark Fussell & Chris Gillium, Diagrid
- Match score: 0.733
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/dapr-workflows-and-the-road-ahead/yNo3P_n7AU4.txt
- Transcript chars: 36918
- Keywords: workflow, dapper, inside, running, another, workflows, applications, broker, little, component, pattern, patterns, message, together, application, activity, actually, approval

### Resumo baseado na transcript

hey good morning welcome to ccon and Cloud native comom and to the Dapper maintainance talk um we'll introduce ourselves my name is Mark fussel I'm a Dappa maintainer and I'm also the CEO of diagrid and I'm Chris Gillum uh software uh architect at Microsoft so focusing on serous uh Cloud platforms and so today we kind of want to dive into a little bit about what Dapper is just give a little bit of the background um we're going to spend quite a lot of time and Chris's

### Excerpt da transcript

hey good morning welcome to ccon and Cloud native comom and to the Dapper maintainance talk um we'll introduce ourselves my name is Mark fussel I'm a Dappa maintainer and I'm also the CEO of diagrid and I'm Chris Gillum uh software uh architect at Microsoft so focusing on serous uh Cloud platforms and so today we kind of want to dive into a little bit about what Dapper is just give a little bit of the background um we're going to spend quite a lot of time and Chris's particularly on workflows which is probably one of the most exciting things that we've been building into Dapper in the last few releases um and then I'll kind of follow up with a little bit about talking about some of the things in the latest release particularly around the outbox pattern and then we're going to finish up with sort of the road ahead and where the actual project is going and sort of dive into sort of looking beyond the future you know what is Dapper um Dapper is effectively a set of apis that allow developers to build distributed applications build Cloud native applications you know it brings product activity for you to build across distributed platforms like kubernetes in essence Dapper is a set of apis that codify best practice patterns that save you time building things like request reply or Pub sub event messaging or long running stateful or workflow applications and by combining these together and coming it it from any language or any run runtime of your favorite you can build applications that run on a set of VMS cross kubernetes is not bound to community platform but you know about productivity for developers so when you're building applications de daa apis allow you to you know distinctly build them more productively fast and then half the time you'd expect in fact we did a great um state of Dappa survey a few months back and it showed that you know Dapper itself saves developers 30% of the time getting their applications into um production now um you know another way to think about this is that you know Dapper is a set of patterns um that you can use from each one of of your runtimes so you can take a one of your favorite languages you can take your favorite framework inside the all and you can think of them as patterns that you see typically codified like Saga workflows or request reply or long running event driven applications and you know da alone you know is very powerful but you can be used alongside other you a um apis and Frameworks that you use it doesn't have
