---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "AI + ML"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Susan Wu", "Google", "Lucy Sweet", "Uber", "Mitch McKenzie", "Weave", "Aditya Shanker", "Crusoe", "Rebecca Weekly", "Geico"]
sched_url: https://kccncna2024.sched.com/event/1i7mO/making-kubernetes-simpler-for-accelerated-workloads-susan-wu-google-lucy-sweet-uber-mitch-mckenzie-weave-aditya-shanker-crusoe-rebecca-weekly-geico
youtube_search_url: https://www.youtube.com/results?search_query=Making+Kubernetes+Simpler+for+Accelerated+Workloads+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Making Kubernetes Simpler for Accelerated Workloads - Susan Wu, Google; Lucy Sweet, Uber; Mitch McKenzie, Weave; Aditya Shanker, Crusoe; Rebecca Weekly, Geico

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Susan Wu, Google, Lucy Sweet, Uber, Mitch McKenzie, Weave, Aditya Shanker, Crusoe, Rebecca Weekly, Geico
- Schedule: https://kccncna2024.sched.com/event/1i7mO/making-kubernetes-simpler-for-accelerated-workloads-susan-wu-google-lucy-sweet-uber-mitch-mckenzie-weave-aditya-shanker-crusoe-rebecca-weekly-geico
- Busca YouTube: https://www.youtube.com/results?search_query=Making+Kubernetes+Simpler+for+Accelerated+Workloads+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Making Kubernetes Simpler for Accelerated Workloads.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7mO/making-kubernetes-simpler-for-accelerated-workloads-susan-wu-google-lucy-sweet-uber-mitch-mckenzie-weave-aditya-shanker-crusoe-rebecca-weekly-geico
- YouTube search: https://www.youtube.com/results?search_query=Making+Kubernetes+Simpler+for+Accelerated+Workloads+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=HlDj-obxxwQ
- YouTube title: Making Kubernetes Simpler for Accelerated Workloads - Panel
- Match score: 1.024
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/making-kubernetes-simpler-for-accelerated-workloads/HlDj-obxxwQ.txt
- Transcript chars: 39074
- Keywords: platform, actually, hardware, models, gpu, across, business, workloads, infrastructure, training, interesting, customers, especially, running, cluster, trying, specific, question

### Resumo baseado na transcript

hi my name is Susan woo I'm in Cloud networking I'm a product manager and so here we're talking about making kubernetes simpler for Accelerated workloads I have this steam panel I'm going to let them introduce themselves go ahead first testing hey Cool Works um so I'm ad I work as a product manager at cruser cruser Cloud I guess um what we do is wear any iCloud but we collocate our data centers next day stranded wasted or sustainable energy sources so we do some interesting things with

### Excerpt da transcript

hi my name is Susan woo I'm in Cloud networking I'm a product manager and so here we're talking about making kubernetes simpler for Accelerated workloads I have this steam panel I'm going to let them introduce themselves go ahead first testing hey Cool Works um so I'm ad I work as a product manager at cruser cruser Cloud I guess um what we do is wear any iCloud but we collocate our data centers next day stranded wasted or sustainable energy sources so we do some interesting things with energy in the way we power our Cloud um yeah I manage sort of our platform services and orchestration there and before this I spent a bunch of time with ews building out to the selfless computer Lambda and then couple other companies before that hi I'm Lucy I'm a senior software engineer at Uber who I think most of you familiar with if you took an Uber here thanks for keeping me in a job uh I run uh and work on a stateless compute platform called up which we have a 3 million CPU Calles behind and that runs everywhere from uh the most the uh trip serving apps for web applications all the way all the way through to uh a Ai workloads and accelerated workloads everything that is effectively stateless uh and yeah hi I'm Rebecca Weekley I run infrastructure engineering at Geico and you might wonder what that means at Geico we have six data centers we have eight different clouds uh so it is actually the hybrid Cloud footprint across all of our infrastructure needs to support our business hey I'm Mitch McKenzie I'm a site reliability engineer at weave Communications and uh we uh we're a software company we sell a small uh software to small to mediumsized businesses to uh help them run their offices so primarily focused on you know dental offices optometrist uh you know vet type offices and um yeah we're we're sort of like in the early stages of building out our ml platform and and uh running workloads on accelerators and and Kates so we uh Mitch had to travel in but his company is headquartered where Lehi 45 minutes south so okay let's get Dive Right In so you know this session is all about platform engineers and so for the platform Engineers that we have in this very panel do you generally offer kubernetes for conventional software development and then add AI or do you have dedicated teams for AI and uh I'm going to start with Lucy on that one y sure um so uh I work on our stateless computer platform and we offer kubernetes and effectively service service deployment to all teams ac
