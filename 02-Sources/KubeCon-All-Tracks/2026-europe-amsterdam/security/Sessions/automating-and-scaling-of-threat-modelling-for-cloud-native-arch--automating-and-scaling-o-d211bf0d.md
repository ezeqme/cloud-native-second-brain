---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Security"
themes: ["Security", "SRE Reliability"]
speakers: ["Hanna Papirna", "Emma Yuan Fang", "EPAM Systems"]
sched_url: https://kccnceu2026.sched.com/event/2CW1W/automating-and-scaling-of-threat-modelling-for-cloud-native-architecture-hanna-papirna-emma-yuan-fang-epam-systems
youtube_search_url: https://www.youtube.com/results?search_query=Automating+and+Scaling+of+Threat+Modelling+for+Cloud+Native+Architecture+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Automating and Scaling of Threat Modelling for Cloud Native Architecture - Hanna Papirna & Emma Yuan Fang, EPAM Systems

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Hanna Papirna, Emma Yuan Fang, EPAM Systems
- Schedule: https://kccnceu2026.sched.com/event/2CW1W/automating-and-scaling-of-threat-modelling-for-cloud-native-architecture-hanna-papirna-emma-yuan-fang-epam-systems
- Busca YouTube: https://www.youtube.com/results?search_query=Automating+and+Scaling+of+Threat+Modelling+for+Cloud+Native+Architecture+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Automating and Scaling of Threat Modelling for Cloud Native Architecture.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW1W/automating-and-scaling-of-threat-modelling-for-cloud-native-architecture-hanna-papirna-emma-yuan-fang-epam-systems
- YouTube search: https://www.youtube.com/results?search_query=Automating+and+Scaling+of+Threat+Modelling+for+Cloud+Native+Architecture+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=GGdc0vihJOI
- YouTube title: Automating and Scaling of Threat Modelling for Cloud Native Archit... Hanna Papirna & Emma Yuan Fang
- Match score: 0.894
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/automating-and-scaling-of-threat-modelling-for-cloud-native-architectu/GGdc0vihJOI.txt
- Transcript chars: 25879
- Keywords: threat, modeling, tenant, identity, security, environment, threats, process, approach, architecture, boundaries, basically, thread, attack, automate, compromise, actors, stride

### Resumo baseado na transcript

there are hundreds there could be hundreds of attack surfaces and the average fraoding process wouldn't be able to solve that. So I Emma and I have my colleague here Hannah from EPAM systems together we will be sharing some solutions that might be able to solve your problem today. So that means that sometimes um as a customer we are really uh struggle to understand what is the uh what is the security controls that within our limits and we have a lot of APIs and it's a distributed uh system and a lot So the problem that we are trying to solve here is how can we automate and scale this environment I mean the threat modeling of this environment. We defined everything to do with the technical component of the uh architecture. So that would allow us to easy um threat model this um this very big complex architecture and then we can identify and attack uh actors and map them to the uh attack uh vectors um like surfaces with that we can identify the list of threats.

### Excerpt da transcript

there are hundreds there could be hundreds of attack surfaces and the average fraoding process wouldn't be able to solve that. So I Emma and I have my colleague here Hannah from EPAM systems together we will be sharing some solutions that might be able to solve your problem today. All right let's get started Hannah. Yeah. Hello everyone. I'm Hana. Uh I'm a lead security engineer in EPOM systems. So my primary uh knowledge sphere is in cloud security engineering also threat modeling. Uh yeah and >> yeah so my name is Emma Emma Fang. Um I'm also from EPAM. I'm a consultant and senior security architect. Um so uh I've been involved in a field diversity and inclusions initiative including the women in cyber security. Um I'm affiliate leader at the UK affiliate. Um so I'm specialized in cloud native security right okay so that is the state of the uh of the cloud native probably familiar. So we have a lot of um as you can see that we have a lot of managed services and microservices and um cross tenant it could be uh depending on the hosting um style of your of your environment and we have a lot of um containers serless functions.

So what are the challenges of uh threat modeling this kind of uh environment? So there are some of the challenges that we like to discuss here share responsibility models. So that means that sometimes um as a customer we are really uh struggle to understand what is the uh what is the security controls that within our limits and we have a lot of APIs and it's a distributed uh system and a lot of times that we are not able to um encounter all the um the attack surfaces within this environment and um we have a lot of shortlived workloads within this environment as well containers and serless functions. So the problem that we are trying to solve here is how can we automate and scale this environment I mean the threat modeling of this environment. So that is what we are going to propose is to use the AI assisted approach and also be using um a method that can be integrated within your CI/CD pipeline. So this is a typical uh threat modeling process. I just going to briefly go through this. Um so at the very start we will define the architectural diagram.

We defined the trust boundaries. We defined everything to do with the technical component of the uh architecture. Um we defined the data classification and so on. And then we can break down the system into smaller manageable uh components or subsystems. So that would allow us to easy um thr
