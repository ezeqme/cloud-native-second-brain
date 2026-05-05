---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Operations + Performance"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability"]
speakers: ["James Wilson", "nOps", "Haoran Qiu", "Microsoft", "Katie Gamanji", "Apple", "Jasmine James", "Square", "Josh Cypher", "Sonos"]
sched_url: https://kccncna2024.sched.com/event/1i7s0/the-state-of-kubernetes-optimization-and-the-role-of-ai-james-wilson-nops-haoran-qiu-microsoft-katie-gamanji-apple-jasmine-james-square-josh-cypher-sonos
youtube_search_url: https://www.youtube.com/results?search_query=The+State+of+Kubernetes+Optimization+and+the+Role+of+AI+CNCF+KubeCon+2024
slides: []
status: parsed
---

# The State of Kubernetes Optimization and the Role of AI - James Wilson, nOps; Haoran Qiu, Microsoft; Katie Gamanji, Apple; Jasmine James, Square; Josh Cypher, Sonos

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: James Wilson, nOps, Haoran Qiu, Microsoft, Katie Gamanji, Apple, Jasmine James, Square, Josh Cypher, Sonos
- Schedule: https://kccncna2024.sched.com/event/1i7s0/the-state-of-kubernetes-optimization-and-the-role-of-ai-james-wilson-nops-haoran-qiu-microsoft-katie-gamanji-apple-jasmine-james-square-josh-cypher-sonos
- Busca YouTube: https://www.youtube.com/results?search_query=The+State+of+Kubernetes+Optimization+and+the+Role+of+AI+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre The State of Kubernetes Optimization and the Role of AI.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7s0/the-state-of-kubernetes-optimization-and-the-role-of-ai-james-wilson-nops-haoran-qiu-microsoft-katie-gamanji-apple-jasmine-james-square-josh-cypher-sonos
- YouTube search: https://www.youtube.com/results?search_query=The+State+of+Kubernetes+Optimization+and+the+Role+of+AI+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=O4otXH3CNRU
- YouTube title: The State of Kubernetes Optimization and the Role of AI - Panel
- Match score: 1.028
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/the-state-of-kubernetes-optimization-and-the-role-of-ai/O4otXH3CNRU.txt
- Transcript chars: 34949
- Keywords: carpenter, sustainability, little, within, decisions, actually, workloads, looking, question, definitely, models, scaling, organization, excited, infrastructure, simple, aspect, autoscaling

### Resumo baseado na transcript

all right well thanks for joining us today uh this is the state of kubernetes optimization and the role of AI my name is James Wilson and I lead engineering at a company called enops where we're thinking about this stuff every day uh and I'm excited to be joined today by my dream panel some of you I I know pretty well at this point uh we've gotten to know each others others were just a dream for me to reach out to and say hey let's get together

### Excerpt da transcript

all right well thanks for joining us today uh this is the state of kubernetes optimization and the role of AI my name is James Wilson and I lead engineering at a company called enops where we're thinking about this stuff every day uh and I'm excited to be joined today by my dream panel some of you I I know pretty well at this point uh we've gotten to know each others others were just a dream for me to reach out to and say hey let's get together and and talk about what's going on in this space so before we get going two things how's everybody's cubec con yeah yeah let's hear for the cncf I mean this was a a really really great event and uh what a sense of community this week like just I I think best conference ever so um thank you all for joining us now let's get some introductions just go down the line uh yeah I'm Josh Cipher I'm a senior devops engineer at Sonos um and I'm going be talking a little bit about Carpenter today hi I'm Jasmine James I lead developer infrastructure um at Square specifically for Hardware excited to kind of talk to you about the internal aspects of optimization of kubernetes hello everyone I'm H ran from uh Microsoft azer I'm a research engineer working on building systems for efficient AI applications lar models thank you for being here as well my name is Ki and currently I'm a senior field engineer at Apple I'm focusing a lot on adoption but at the same time contributions to schol in addition to that I'm part of the of the technical oversight and part of the T well which is the technical Advisory board so I'm more than happy to provide the sustainability aspect of this final but if you have any questions in regards to any of the CCF projects or if would like to be a member of all right well um I'm so excited to to get into this conversation so we all know that Docker container orchestration and really kubernetes have changed the the shape and and the way that we manage our our workloads at scale and in the public cloud and you know uh kubernetes just turned 10 uh I think for about the last eight years I've watched the the way that the auto scaling at both the the container and the infrastructure level has evolved uh but before we get started uh Haren uh you know I I first became aware of you when one of my engineers said you've got to read this paper on multi-dimensional autoscaling and I got so excited that I just reached out to you and said I need to talk uh so I can't think of anyone better to to give us a little bit of a pr
