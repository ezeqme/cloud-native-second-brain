---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability", "Community Governance"]
speakers: ["Ajay Sundar Karuppasamy", "Google", "Sreeram Venkitesh", "DigitalOcean", "Karthik K N", "IBM", "Priyanka Saggu", "SUSE"]
sched_url: https://kccnceu2026.sched.com/event/2EF6E/addressing-non-deterministic-scheduling-introducing-the-node-readiness-controller-ajay-sundar-karuppasamy-google-sreeram-venkitesh-digitalocean-karthik-k-n-ibm-priyanka-saggu-suse
youtube_search_url: https://www.youtube.com/results?search_query=Addressing+Non-Deterministic+Scheduling%3A+Introducing+the+Node+Readiness+Controller+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Addressing Non-Deterministic Scheduling: Introducing the Node Readiness Controller - Ajay Sundar Karuppasamy, Google; Sreeram Venkitesh, DigitalOcean; Karthik K N, IBM; Priyanka Saggu, SUSE

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Ajay Sundar Karuppasamy, Google, Sreeram Venkitesh, DigitalOcean, Karthik K N, IBM, Priyanka Saggu, SUSE
- Schedule: https://kccnceu2026.sched.com/event/2EF6E/addressing-non-deterministic-scheduling-introducing-the-node-readiness-controller-ajay-sundar-karuppasamy-google-sreeram-venkitesh-digitalocean-karthik-k-n-ibm-priyanka-saggu-suse
- Busca YouTube: https://www.youtube.com/results?search_query=Addressing+Non-Deterministic+Scheduling%3A+Introducing+the+Node+Readiness+Controller+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Addressing Non-Deterministic Scheduling: Introducing the Node Readiness Controller.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF6E/addressing-non-deterministic-scheduling-introducing-the-node-readiness-controller-ajay-sundar-karuppasamy-google-sreeram-venkitesh-digitalocean-karthik-k-n-ibm-priyanka-saggu-suse
- YouTube search: https://www.youtube.com/results?search_query=Addressing+Non-Deterministic+Scheduling%3A+Introducing+the+Node+Readiness+Controller+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=oPHayi9ouRI
- YouTube title: Addressing Non-Deterministic Scheduling: Introducing... Ajay K, Sreeram V, Karthik N & Priyanka S
- Match score: 0.798
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/addressing-non-deterministic-scheduling-introducing-the-node-readiness/oPHayi9ouRI.txt
- Transcript chars: 27923
- Keywords: readiness, controller, cluster, condition, component, status, production, bootstrap, update, actually, itself, running, called, working, components, finally, workloads, created

### Resumo baseado na transcript

Uh today we are going to talk about um addressing nondeterministic scheduleuling and as part of that we'll introduce the new controller which is a new sub project of sig node node readiness controller. I'm a technical lead for sik contrabooks and recently participating in a bunch of um caps and sig node. So the problem is that cubernetes nodes have a race condition built into the heart of the bootstrapping process. So, I built this coordination mechanism for GKE, but realized this wasn't just a Google problem. Um okay so to understand the problem we have to look at the nature of how Kubernetes handles readiness today. And finally, it had to target the critical demons, the stuff that you know ahead of the time like CNI and drivers.

### Excerpt da transcript

Hello everyone, good morning and welcome to the final day of CubeCon. Thank you for coming to our talk. Uh today we are going to talk about um addressing nondeterministic scheduleuling and as part of that we'll introduce the new controller which is a new sub project of sig node node readiness controller. Um my name is Priyanka Sagu. I work at Souza. I'm also participating in some other parts of the kubernetes project. I'm a technical lead for sik contrabooks and recently participating in a bunch of um caps and sig node. >> Yeah. Uh hey everyone. Uh my name is Sridam. I work at digital ocean as part of the manage kubernetes team. I've also been involved in the upstream kubernetes project uh for a while now as part of uh sig release uh for the release team and I've also been working on a couple of caps with sig node. Uh hi everyone. Uh I'm Karthik. I work as a cloud engineer at IBM. Uh I'm a contributor to the cluster API and SIG node. Yeah, thank you. >> And uh we're supposed to have AJ as well joining us on the stage today but uh he could not travel.

So um we will have his part recorded and we'll play uh now in a moment. But today's agenda. So we are going to cover our presentation in these parts. We'll start with what the node readiness problem looks like today. Following uh followed by that we'll introduce the node readiness controller. We'll also touch a bit on the design aspect of the node readiness controller. And then we'll go into how uh node readiness controller operationalizing in production spaces looks like today and we'll finally conclude the talk with um some future work we are planning to do and collaboration with the ecosystem and resources to get involved. So we have a part from AJ which is recorded. I'll just start with that. >> Hi everyone, I'm AJ. I'm a software engineering lead in GKE node team. Today I'm here as the lead maintainer of the node readiness controller project. This project was born out of real production pain we have felt at Google. So we kept seeing these recurring ghost failures where a node would announce I'm ready but in reality the CNA wasn't actually initialized or the driver hadn't bootstrapped fully yet causing application failures.

So the problem is that cubernetes nodes have a race condition built into the heart of the bootstrapping process. So, Cublet is not aware of different infrastructure requirements for your nodes that change from cluster to cluster. So, I built this coordination mechanism for GKE, but re
