---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Service Mesh"
themes: ["Networking"]
speakers: ["Christian Hüning", "Lutz Behnke", "finleap connect"]
sched_url: https://kccnceu2021.sched.com/event/iE2Z/compliance-the-easy-way-zero-conf-mtls-for-dev-and-smooth-day-2-for-ops-christian-huning-lutz-behnke-finleap-connect
youtube_search_url: https://www.youtube.com/results?search_query=Compliance+the+Easy+Way%3A+Zero-conf+mTLS+for+Dev+and+smooth+Day-2+for+Ops+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Compliance the Easy Way: Zero-conf mTLS for Dev and smooth Day-2 for Ops - Christian Hüning & Lutz Behnke, finleap connect

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Service Mesh]]
- Temas: [[Networking]]
- País/cidade: Virtual / Virtual
- Speakers: Christian Hüning, Lutz Behnke, finleap connect
- Schedule: https://kccnceu2021.sched.com/event/iE2Z/compliance-the-easy-way-zero-conf-mtls-for-dev-and-smooth-day-2-for-ops-christian-huning-lutz-behnke-finleap-connect
- Busca YouTube: https://www.youtube.com/results?search_query=Compliance+the+Easy+Way%3A+Zero-conf+mTLS+for+Dev+and+smooth+Day-2+for+Ops+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Compliance the Easy Way: Zero-conf mTLS for Dev and smooth Day-2 for Ops.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE2Z/compliance-the-easy-way-zero-conf-mtls-for-dev-and-smooth-day-2-for-ops-christian-huning-lutz-behnke-finleap-connect
- YouTube search: https://www.youtube.com/results?search_query=Compliance+the+Easy+Way%3A+Zero-conf+mTLS+for+Dev+and+smooth+Day-2+for+Ops+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KoweR6u0t8c
- YouTube title: Compliance the Easy Way: Zero-conf mTLS for Dev and smooth Day-2 f... Christian Hüning & Lutz Behnke
- Match score: 0.892
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/compliance-the-easy-way-zero-conf-mtls-for-dev-and-smooth-day-2-for-op/KoweR6u0t8c.txt
- Transcript chars: 16151
- Keywords: certificates, cluster, tenant, prometheus, quickly, control, linker, metrics, challenge, basically, already, automatically, version, create, around, particular, probably, platform

### Resumo baseado na transcript

welcome my name is christian and together with my colleague lutz i will talk about how we solved compliance by adopting a link id2 and what we had to do for day two operations at finlibconnect this talk is organized around the idea of the challenges we faced and how we solved them so here's the first challenge the challenge involved how to encrypt all traffic between applications in our cluster in no time and with zero developer overhead to understand why we had this particular challenge of doing it thank you christian um as the christian told you the linker d has automatic tls out of the box but that involves setting up quite a number of certificates that have to provide certain characteristics and we had some problems in achieving those what is great about the setup is that you get it all automatically when you install link rd either by the cli command link or the install or by deploying the appropriate helm chart the certificates and their private keys are stored as kubernetes secrets and the

### Excerpt da transcript

welcome my name is christian and together with my colleague lutz i will talk about how we solved compliance by adopting a link id2 and what we had to do for day two operations at finlibconnect this talk is organized around the idea of the challenges we faced and how we solved them so here's the first challenge the challenge involved how to encrypt all traffic between applications in our cluster in no time and with zero developer overhead to understand why we had this particular challenge of doing it with no time and zero developer overhead it's probably important to understand where it all started it all started in 2018 when lutz and me together with some other friends of ours joined the company finley connect to rebuild the present internal cloud platform the platform that was there before was rather traditional openstack based and ran at capacity so it had to be rebuilt had to be modernized these kind of things the new platform was meant to be based completely on kubernetes all containerized it was supposed to be a private cloud that ran on bare metal in our own data centers so on the right side you see roughly the setup it's one large logical production cluster spanning three data centers in frankfurt the specifics of this and why it had to be is probably subject of a different talk but in short affinity connect holds a payment institution license so we are from the financial services industry and hence have to fulfill requirements that are pretty strict regarding security and compliance and as you may have guessed especially towards the encryption of traffic between services that run in our cluster to make it worse this whole project faced several challenges including a very tight timeline of only five to six months to implement the solution we had some time to plan it beforehand we had a cloud team of around about five people some were only able to join a bit later so it was we started with two people and in the end we ended up with being six people um and a new platform before going live had to pass compliance checks from customers and regulators alike and last but not least the development teams in the company had to do a lot of things and wrap the hats around a lot of new concepts as we were together with implementing the new platform also making the transition to a fully cloud native setup that involved like some services had to be rewritten changes of databases introduction of helm charts these kind of things so that were the challenges that we f
