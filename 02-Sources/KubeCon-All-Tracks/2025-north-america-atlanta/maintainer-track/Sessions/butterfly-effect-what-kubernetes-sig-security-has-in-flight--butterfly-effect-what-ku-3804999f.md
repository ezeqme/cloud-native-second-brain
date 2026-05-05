---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Kubernetes Core", "Community Governance"]
speakers: ["Ian Coldwater", "Independent", "Savitha Raghunathan", "Red Hat", "Carol Valencia", "KrolCloud"]
sched_url: https://kccncna2025.sched.com/event/27Nni/butterfly-effect-what-kubernetes-sig-security-has-in-flight-ian-coldwater-independent-savitha-raghunathan-red-hat-carol-valencia-krolcloud
youtube_search_url: https://www.youtube.com/results?search_query=Butterfly+Effect%3A+What+Kubernetes+SIG+Security+Has+in+Flight+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Butterfly Effect: What Kubernetes SIG Security Has in Flight - Ian Coldwater, Independent; Savitha Raghunathan, Red Hat; Carol Valencia, KrolCloud

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Ian Coldwater, Independent, Savitha Raghunathan, Red Hat, Carol Valencia, KrolCloud
- Schedule: https://kccncna2025.sched.com/event/27Nni/butterfly-effect-what-kubernetes-sig-security-has-in-flight-ian-coldwater-independent-savitha-raghunathan-red-hat-carol-valencia-krolcloud
- Busca YouTube: https://www.youtube.com/results?search_query=Butterfly+Effect%3A+What+Kubernetes+SIG+Security+Has+in+Flight+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Butterfly Effect: What Kubernetes SIG Security Has in Flight.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Nni/butterfly-effect-what-kubernetes-sig-security-has-in-flight-ian-coldwater-independent-savitha-raghunathan-red-hat-carol-valencia-krolcloud
- YouTube search: https://www.youtube.com/results?search_query=Butterfly+Effect%3A+What+Kubernetes+SIG+Security+Has+in+Flight+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=q4ryxYhAenM
- YouTube title: Butterfly Effect: What Kubernetes SIG Security Has in F... I. Coldwater, S. Raghunathan, C. Valencia
- Match score: 0.853
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/butterfly-effect-what-kubernetes-sig-security-has-in-flight/q4ryxYhAenM.txt
- Transcript chars: 25566
- Keywords: security, started, documentation, little, tooling, involved, working, meeting, projects, everybody, important, create, section, assessment, couple, contribute, knowledge, infrastructure

### Resumo baseado na transcript

This is butterfly effect and if you are here for a different talk you are in the wrong room and that's cool. My name is Kor Valencia >> and we are here for Kubernetes SIG security. You will be hearing more about these later and working group audit got together for a while and eventually decided that maybe they wanted to make a SIG out of it and have it be SIG security. And when six security got ratified, me and the first co-chair, Tabitha Sable, who is presenting with us, but is not here with us today, um we're like, we're going to call a meeting and we're going to put out a big column. And we got our first sub projects out of that which again you're going to hear more about in a second which were SIG security documentation. SIG security tooling and working group audit was already working group audit but became one of our sub projects.

### Excerpt da transcript

Welcome to the SIG security maintainer track talk. This is butterfly effect and if you are here for a different talk you are in the wrong room and that's cool. We will hang out with you anyway. My name is Ian Kov water. >> My name is Savvitraatan. My name is Kor Valencia >> and we are here for Kubernetes SIG security. So Kubernetes 6 security we've been a SIG in Kubernetes since 2020. The way that Kubernetes as a project works is that its governance is governed by um a network of special interest groups SIGs for short which each have its own kind of part of the project that they are responsible for. So for example, SIG architecture is responsible for architecture and SIG O is responsible for O and SIG security does security. At first um when I first got involved in Kubernetes which was about 2016 back when the wheels were not quite on the bus yet um there was no SIG security and the idea was that security was everybody's responsibility which is true and also what that meant in practice was that a lot of people who were interested in doing security stuff related to Kubernetes would go to SIG O as a sort of de facto SIG security and then Sigoth would be like great do you want to work on this authorization component and the people coming in would be like well we were hoping that we could do more general things related to security.

So it wasn't quite a natural fit. So time passed we had working group audit um which was responsible for the first Kubernetes thirdparty audit. You will be hearing more about these later and working group audit got together for a while and eventually decided that maybe they wanted to make a SIG out of it and have it be SIG security. So, six security got ratified in 2020. And when six security got ratified, me and the first co-chair, Tabitha Sable, who is presenting with us, but is not here with us today, um we're like, we're going to call a meeting and we're going to put out a big column. We're going to hope somebody shows up, maybe, hopefully. And as it turns out, people did show up. And we got our first sub projects out of that which again you're going to hear more about in a second which were SIG security documentation. SIG security tooling and working group audit was already working group audit but became one of our sub projects. The other ones came later. So um that is the start of it. We've been a SIG together since 2020.

And what we have been doing since then is creating a space that is on purpose really warm, really welcom
