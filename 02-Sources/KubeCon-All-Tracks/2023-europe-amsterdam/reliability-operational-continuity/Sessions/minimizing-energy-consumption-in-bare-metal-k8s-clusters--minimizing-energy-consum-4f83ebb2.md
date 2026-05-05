---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Reliability + Operational Continuity"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability", "Sustainability"]
speakers: ["Marco Schröder", "David Meder-Marouelli", "1&1 Mail", "Media"]
sched_url: https://kccnceu2023.sched.com/event/1HybW/minimizing-energy-consumption-in-bare-metal-k8s-clusters-marco-schroder-david-meder-marouelli-11-mail-media
youtube_search_url: https://www.youtube.com/results?search_query=Minimizing+Energy+Consumption+in+Bare+Metal+K8s+Clusters+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Minimizing Energy Consumption in Bare Metal K8s Clusters - Marco Schröder & David Meder-Marouelli, 1&1 Mail & Media

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Reliability + Operational Continuity]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]], [[Sustainability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Marco Schröder, David Meder-Marouelli, 1&1 Mail, Media
- Schedule: https://kccnceu2023.sched.com/event/1HybW/minimizing-energy-consumption-in-bare-metal-k8s-clusters-marco-schroder-david-meder-marouelli-11-mail-media
- Busca YouTube: https://www.youtube.com/results?search_query=Minimizing+Energy+Consumption+in+Bare+Metal+K8s+Clusters+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Minimizing Energy Consumption in Bare Metal K8s Clusters.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HybW/minimizing-energy-consumption-in-bare-metal-k8s-clusters-marco-schroder-david-meder-marouelli-11-mail-media
- YouTube search: https://www.youtube.com/results?search_query=Minimizing+Energy+Consumption+in+Bare+Metal+K8s+Clusters+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jsBSNCuSI74
- YouTube title: Minimizing Energy Consumption in Bare Metal K8s Clusters - Marco Schröder & David Meder-Marouelli
- Match score: 0.832
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/minimizing-energy-consumption-in-bare-metal-k8s-clusters/jsBSNCuSI74.txt
- Transcript chars: 28299
- Keywords: consumption, servers, energy, question, center, actually, basically, course, numbers, server, applications, hardware, clusters, running, measure, couple, answer, available

### Resumo baseado na transcript

very nice to see so many people joining a presentation on a relatively narrowly focused topic namely minimizing energy consumption in bare metal kubernetes clusters I'm David Miller I'm working for one and one Mainland media which is not immediately obvious what we are doing we are Germany's largest email provider with about 40 million active customers I'm the lead architect for our infrastructure platform covering the entire life cycle of artifacts from the first line of code until running it in production in kubernetes clusters along that way I

### Excerpt da transcript

very nice to see so many people joining a presentation on a relatively narrowly focused topic namely minimizing energy consumption in bare metal kubernetes clusters I'm David Miller I'm working for one and one Mainland media which is not immediately obvious what we are doing we are Germany's largest email provider with about 40 million active customers I'm the lead architect for our infrastructure platform covering the entire life cycle of artifacts from the first line of code until running it in production in kubernetes clusters along that way I became sort of an expert for continuous integration and continuous delivery and as you can see I spent quite a lot of time in IIT by now so that's my history in a nutshell yeah hi everyone I'm Marco and yes I'm getting old and doing it operations since a while currently I have the honor to lead a group of people basically Cloud Engineers within the company to provide the platform based on kubernetes that David is has mentioned so but of course yeah this is not about me or us today I would like to start with a question actually so who of you in the audience is doing bare metal kubernetes wow okay that surprises me a bit honestly um but then of course you're in the right talk and maybe we have a chat afterwards and we can have a conversation about our challenges um but today the topic is basically Energy savings in bare metal so to give a bit more of context David mentioned we are the largest email provider in Germany over 42 million active users so that's quite a lot um in the yesterday's keynote I saw someone um telling why they do Cloud native because it accelerates their development it helps growing the business and this reminded me we had the same kind of Journey five six seven years ago so the company decided okay we break we break it down into microservices and then it gets very very easily in the direction of having a container runtime and so today we are doing a multi-tenant kubernetes platform for our internal um users on bare metal since uh 2017 by the way we do this on premise why do we do it on premise the short answer is yeah because we can um the bit longer answer is we have some data protection constraints we take we take security very serious and also Jonas the company who operates the data centers for us is also a member of the the larger corporation that one-on-one male in media where we work is part of to give some numbers there on the slides we have like uh about 70 000 CPU cores in our clusters
