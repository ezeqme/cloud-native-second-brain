---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Uma Mukkara", "Karthik S", "Prithvi Raj", "Harness"]
sched_url: https://kccncna2022.sched.com/event/18ofR/chaos-engineering-for-hybrid-targets-with-litmuschaos-uma-mukkara-karthik-s-prithvi-raj-harness
youtube_search_url: https://www.youtube.com/results?search_query=Chaos+Engineering+For+Hybrid+Targets+With+LitmusChaos+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Chaos Engineering For Hybrid Targets With LitmusChaos - Uma Mukkara, Karthik S & Prithvi Raj, Harness

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Uma Mukkara, Karthik S, Prithvi Raj, Harness
- Schedule: https://kccncna2022.sched.com/event/18ofR/chaos-engineering-for-hybrid-targets-with-litmuschaos-uma-mukkara-karthik-s-prithvi-raj-harness
- Busca YouTube: https://www.youtube.com/results?search_query=Chaos+Engineering+For+Hybrid+Targets+With+LitmusChaos+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Chaos Engineering For Hybrid Targets With LitmusChaos.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/18ofR/chaos-engineering-for-hybrid-targets-with-litmuschaos-uma-mukkara-karthik-s-prithvi-raj-harness
- YouTube search: https://www.youtube.com/results?search_query=Chaos+Engineering+For+Hybrid+Targets+With+LitmusChaos+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=BZL-ngvbpbU
- YouTube title: Chaos Engineering For Hybrid Targets With LitmusChaos - Uma Mukkara, Karthik S & Prithvi Raj
- Match score: 0.837
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/chaos-engineering-for-hybrid-targets-with-litmuschaos/BZL-ngvbpbU.txt
- Transcript chars: 30696
- Keywords: litmus, experiment, scenario, actually, experiments, control, application, running, scenarios, probes, engineering, center, resilience, support, probably, little, cluster, called

### Resumo baseado na transcript

so thank you for uh making it on a on the last day of pipcon Friday afternoon post lunch session so really appreciate you all coming in um this is the maintenance track session for litmus chaos kiosk engineering project it's an incubation project in cncf so we'll probably get started with uh the introductions so I'm Karthik I'm one of the maintainers of the rhythmus chaos project I want to talk to them I am gothic one of the maintainers of the fitness chaos project I worked as a

### Excerpt da transcript

so thank you for uh making it on a on the last day of pipcon Friday afternoon post lunch session so really appreciate you all coming in um this is the maintenance track session for litmus chaos kiosk engineering project it's an incubation project in cncf so we'll probably get started with uh the introductions so I'm Karthik I'm one of the maintainers of the rhythmus chaos project I want to talk to them I am gothic one of the maintainers of the fitness chaos project I worked as a principal software engineer at harness here hi everyone um I'm um I am the head of chaos engineering at hardness but Karthik and I started litmus we co-created it back in 2018 we've been maintaining um this project ever since so it is an incubating project at cncf for the last one year nice to be here nice to meet you all okay so this is what we have on the agenda we'll do a quick introduction to litmus chaos project I'm sure a lot of you have heard about chaos engineering already so we'll not spend too much time talking about what it is we'll directly get into the project specifics and we'll talk about one specific feature um we'll probably stress upon it for a few minutes that's about how you can use a single Chaos Control plane for doing Chaos against varied infrastructure targets you know across your different Cloud environments and we'll talk about what we got done since the last kubecon so I think the the project Cycles nowadays are measured uh in kubecons so we'll talk about what we did from the Europe cubecon time and then Uma will speak about the 3.0 beta for the response project and also talk about the community a little bit right so this is just a quick refresher just to set the context before we start off so chaos engineering is essentially injecting controlled failures into your environment and the idea is to introduce these parts to find out weaknesses if there is something that's unknown something that's you've saw probably not accounted for you will find those things out using chaos engineering so there's a lot of material on the internet around what it is it's especially used for distributed systems right as far as litmus chaos goes it's a project that started around 2018 19 time we are an incubation project the litmus tool or framework is kubernetes native it's just a kubernetes application you can install it via command Helm command you can do a Helm install and you can just go do whatever configuration you need in the values so you can do the installation of req
