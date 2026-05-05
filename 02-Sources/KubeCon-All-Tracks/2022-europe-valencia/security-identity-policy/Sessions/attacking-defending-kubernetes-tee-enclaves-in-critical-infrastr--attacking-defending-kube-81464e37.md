---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Security + Identity + Policy"
themes: ["Security", "Kubernetes Core"]
speakers: ["Robert Ficcaglia", "SunStone Secure", "LLC"]
sched_url: https://kccnceu2022.sched.com/event/ytrJ/attacking-defending-kubernetes-tee-enclaves-in-critical-infrastructure-robert-ficcaglia-sunstone-secure-llc
youtube_search_url: https://www.youtube.com/results?search_query=Attacking+%26+Defending+Kubernetes+TEE+Enclaves+in+Critical+Infrastructure+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Attacking & Defending Kubernetes TEE Enclaves in Critical Infrastructure - Robert Ficcaglia, SunStone Secure, LLC

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Robert Ficcaglia, SunStone Secure, LLC
- Schedule: https://kccnceu2022.sched.com/event/ytrJ/attacking-defending-kubernetes-tee-enclaves-in-critical-infrastructure-robert-ficcaglia-sunstone-secure-llc
- Busca YouTube: https://www.youtube.com/results?search_query=Attacking+%26+Defending+Kubernetes+TEE+Enclaves+in+Critical+Infrastructure+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Attacking & Defending Kubernetes TEE Enclaves in Critical Infrastructure.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytrJ/attacking-defending-kubernetes-tee-enclaves-in-critical-infrastructure-robert-ficcaglia-sunstone-secure-llc
- YouTube search: https://www.youtube.com/results?search_query=Attacking+%26+Defending+Kubernetes+TEE+Enclaves+in+Critical+Infrastructure+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=s0ITAQxZffE
- YouTube title: Attacking & Defending Kubernetes TEE Enclaves in Critical Infrastructure - Robert Ficcaglia
- Match score: 0.972
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/attacking-defending-kubernetes-tee-enclaves-in-critical-infrastructure/s0ITAQxZffE.txt
- Transcript chars: 30760
- Keywords: enclave, memory, attack, hardware, trusted, enclaves, application, probably, computing, encryption, operating, little, source, critical, usually, trying, infrastructure, security

### Resumo baseado na transcript

okay good morning everyone welcome to the session attacking and defending kubernetes te enclaves and critical infrastructure my name is robert ficalia i'm the co-chair of the kubernetes policy work group and a member of the cncf security tag have led some security assessments in that group and i'm also assisting with kubernetes third party audit in my day job i work with high security critical systems things in payments banking health care and government and of course i've i'm enjoying the spanish hospitality as i hope you all have

### Excerpt da transcript

okay good morning everyone welcome to the session attacking and defending kubernetes te enclaves and critical infrastructure my name is robert ficalia i'm the co-chair of the kubernetes policy work group and a member of the cncf security tag have led some security assessments in that group and i'm also assisting with kubernetes third party audit in my day job i work with high security critical systems things in payments banking health care and government and of course i've i'm enjoying the spanish hospitality as i hope you all have as well so what is a te when they assigned me the auditorium i assumed that lots of people were coming for a free t-shirt but we're not talking about teas in that sense talking about trusted execution environments these are hardware-enabled enclaves that allow you to protect your code and data while in use so many of you are probably familiar with the concept of protecting data at rest on disk storage in data stores and transit tls your tcpip sockets protected by encryption integrity here we're talking about actually making sure the code that is executing in the cpu is protected isolated and the data is encrypted just to show a hand how many of you are familiar with what tees or enclaves are so few a few any of you using those in production today so more the experimental stage i think that's the norm oh and i have lost money so those of you who may have done attack modeling threat modeling or even trust modeling will at some point start making assumptions documenting those assumptions and if you're operating in userland usually you're making assumptions like i can trust my hardware provider i can trust my chip manufacturer i can trust my cloud provider i can trust my sis admin my root users who are employed and background checked but what if you can't who would who would need this level of trust and integrity well we're talking about critical energy infrastructure well really any critical physical infrastructure systems defense military systems if there's a large financial opportunity then you may be storing value in the billions of dollars and so it becomes a high value target so that's the audience we're really addressing today those are the attackers that we're interested in and those of us who are defending those are the environments that we're defending i mentioned some of the use cases but i think where tes and enclaves really got their their start was enabling a more scalable version of what had already been used for a de
