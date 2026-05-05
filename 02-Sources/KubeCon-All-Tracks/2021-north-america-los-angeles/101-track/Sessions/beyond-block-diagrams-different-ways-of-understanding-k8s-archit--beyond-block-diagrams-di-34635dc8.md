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
speakers: ["Kim Schlesinger", "DigitalOcean"]
sched_url: https://kccncna2021.sched.com/event/lV37/beyond-block-diagrams-different-ways-of-understanding-k8s-architecture-kim-schlesinger-digitalocean
youtube_search_url: https://www.youtube.com/results?search_query=Beyond+Block+Diagrams%3A+Different+Ways+of+Understanding+K8s+Architecture+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Beyond Block Diagrams: Different Ways of Understanding K8s Architecture - Kim Schlesinger, DigitalOcean

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[101 Track]]
- Temas: [[101 Track]]
- País/cidade: United States / Los Angeles
- Speakers: Kim Schlesinger, DigitalOcean
- Schedule: https://kccncna2021.sched.com/event/lV37/beyond-block-diagrams-different-ways-of-understanding-k8s-architecture-kim-schlesinger-digitalocean
- Busca YouTube: https://www.youtube.com/results?search_query=Beyond+Block+Diagrams%3A+Different+Ways+of+Understanding+K8s+Architecture+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Beyond Block Diagrams: Different Ways of Understanding K8s Architecture.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV37/beyond-block-diagrams-different-ways-of-understanding-k8s-architecture-kim-schlesinger-digitalocean
- YouTube search: https://www.youtube.com/results?search_query=Beyond+Block+Diagrams%3A+Different+Ways+of+Understanding+K8s+Architecture+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=X40LJM0KuQ8
- YouTube title: Beyond Block Diagrams: Different Ways of Understanding K8s Architecture - Kim Schlesinger
- Match score: 0.977
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/beyond-block-diagrams-different-ways-of-understanding-k8s-architecture/X40LJM0KuQ8.txt
- Transcript chars: 19992
- Keywords: request, diagram, server, distributed, tracing, sequence, cluster, diagrams, mental, create, actually, traces, understand, control, models, second, jaeger, career

### Resumo baseado na transcript

items different ways of understanding kubernetes architecture my name is kim schlesinger and i want to tell you a little bit about my career and how i got to the tech industry currently i am a developer advocate at digitalocean where i focus on cloud native technologies before this job i was a site reliability engineer for a few years prior to that i was a javascript developer and my first few jobs out of college i was an elementary school teacher teaching here in the united states i bring and open telemetry project that creates standards for how tools that do this are built i really like distributed tracing tools because of the visuals that you get and i've done a lot of learning by seeing distributed traces in production so the example that

### Excerpt da transcript

items different ways of understanding kubernetes architecture my name is kim schlesinger and i want to tell you a little bit about my career and how i got to the tech industry currently i am a developer advocate at digitalocean where i focus on cloud native technologies before this job i was a site reliability engineer for a few years prior to that i was a javascript developer and my first few jobs out of college i was an elementary school teacher teaching here in the united states i bring up my career timeline to tell you how i got into tech so when i left the classroom and i was looking for a new career i eventually landed on wanting to write code wanting to be in the tech industry so i attended a coding bootcamp where i learned front end and back-end javascript and then became a web developer for a few years although i enjoyed web development during that time i realized i was really interested in ops and devops and system administration and how do applications get on the internet and how do they become accessible to users and so i eventually found my way into a job as a site reliability engineer i started that job in 2018 and i was working at a company called fairwinds which is a kubernetes consulting agency and so my first set of experiences as a system administrator and as an ops person was as someone who was a kubernetes administrator which was really really tough so there are a lot of people like me who start in the tech industry and they are already working immediately in the cloud and i'm going to refer to these people as the cloud native generation cloud native generation is anyone who starts their career by writing software and deploying it into the cloud and it can be really difficult as someone in the cloud native generation to really fully understand the systems that we're working with because it's very hard to build mental models of things that you can't see and touch so we all use mental models to think about and interact with systems like kubernetes and a good definition of mental models is any framework that you hold as a mental representation of an external reality when i started at fairwinds and i had more senior engineers mentoring me and trying to help me understand kubernetes the system itself often static block diagrams would come up we've all seen things like this and they are really helpful diagrams and representations of kubernetes but they're most helpful if you understand the technologies and the practices that kubernetes is re
