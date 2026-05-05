---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "SDLC"
themes: ["GitOps Delivery", "SRE Reliability"]
speakers: ["Alec Hothan", "Cisco", "Stefan Prodan"]
sched_url: https://kccnceu2024.sched.com/event/1YeMe/tackling-configuration-management-at-scale-with-flux-cue-and-oci-at-cisco-alec-hothan-cisco-stefan-prodan
youtube_search_url: https://www.youtube.com/results?search_query=Tackling+Configuration+Management+at+Scale+with+Flux%2C+CUE+and+OCI+at+Cisco+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Tackling Configuration Management at Scale with Flux, CUE and OCI at Cisco - Alec Hothan, Cisco & Stefan Prodan

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[SDLC]]
- Temas: [[GitOps Delivery]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Alec Hothan, Cisco, Stefan Prodan
- Schedule: https://kccnceu2024.sched.com/event/1YeMe/tackling-configuration-management-at-scale-with-flux-cue-and-oci-at-cisco-alec-hothan-cisco-stefan-prodan
- Busca YouTube: https://www.youtube.com/results?search_query=Tackling+Configuration+Management+at+Scale+with+Flux%2C+CUE+and+OCI+at+Cisco+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Tackling Configuration Management at Scale with Flux, CUE and OCI at Cisco.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeMe/tackling-configuration-management-at-scale-with-flux-cue-and-oci-at-cisco-alec-hothan-cisco-stefan-prodan
- YouTube search: https://www.youtube.com/results?search_query=Tackling+Configuration+Management+at+Scale+with+Flux%2C+CUE+and+OCI+at+Cisco+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=rJ6vebxS0aI
- YouTube title: Tackling Configuration Management at Scale with Flux, CUE and OCI at... Alec Hothan & Stefan Prodan
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/tackling-configuration-management-at-scale-with-flux-cue-and-oci-at-ci/rJ6vebxS0aI.txt
- Transcript chars: 30358
- Keywords: flux, clusters, charts, cluster, blueprint, deploy, release, production, repository, version, variables, certain, container, values, configuration, repositories, developers, config

### Resumo baseado na transcript

hello I'm Stefan pran I'm a flux C maintainer for a long time now very happy to be here with you and I'm super excited about Alec and what he will share with us he will tell us how um Cisco uses FL X scale and after he's doing his presentation showing us how he's using his flux with Helm with customized with Advanced Kido setups I will um come up with some crazy ideas on how to optimize the current setup and yeah hopefully some of you will try

### Excerpt da transcript

hello I'm Stefan pran I'm a flux C maintainer for a long time now very happy to be here with you and I'm super excited about Alec and what he will share with us he will tell us how um Cisco uses FL X scale and after he's doing his presentation showing us how he's using his flux with Helm with customized with Advanced Kido setups I will um come up with some crazy ideas on how to optimize the current setup and yeah hopefully some of you will try these crazy ideas and you'll tell me afterwards if they work okay thank you go thanks stepan yeah good afternoon my name is Alec hon and I'm principal engineer in the Cisco iot group and uh two years ago I I had to come up with a plan to deploy a lot of workload on kubernetes and uh in our case we have um a lot of data centers to cover um probably around a few hundred clusters and we have not different very wide variations of type of workloads to deploy right so pretty tough problem but two years ago there was not much documentation how to do this with drugs and uh I'm going to do today is I kind of show you uh how how we did it and uh how it works and um in our case we we have a a big team right we have about over 200 people working on this uh platform uh going from developers to testers uh people who release code uh People Who develops some Sr teams and it was really challenged to to see how to build something around flux um that allows all these different teams to work together without uh with as little friction as possible right and and um in terms of um of what we're deploying we deploy a mix of Open Source H charts and a lot of H charts developed internally like around a few hundred right and um on every clusters that we have to deploy to uh they can be different types a different size some data centers have different loads and um in our case we we had to deal with know this variety of targets and all of these data centers currently are running across the world uh we have some in Europe Asia uh North America uh Middle East and um we also are trying to have a common model to deploy on pram and on public Cloud as well so um the other concern we had is uh know when you define production you have to make sure that uh um um not everybody can touch these deployments right so the way to organize uh the the G repositories right when you use flux is very uh critical in in ensuring that uh you can control exactly what goes into production right so we're going to cover all of these different um uh aspects right so if you
