---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Emerging + Advanced"
themes: ["Kubernetes Core"]
speakers: ["Nikhita Raghunath", "Natalie Fisher", "Broadcom", "Nigel Jones", "IBM", "Ricardo Rocha", "CERN", "Tomas Gustavsson", "Keyfactor"]
sched_url: https://kccnceu2025.sched.com/event/1tx7l/quantum-ready-kubernetes-how-do-we-get-there-nikhita-raghunath-natalie-fisher-broadcom-nigel-jones-ibm-ricardo-rocha-cern-tomas-gustavsson-keyfactor
youtube_search_url: https://www.youtube.com/results?search_query=Quantum-Ready+Kubernetes%3A+How+Do+We+Get+There%3F+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Quantum-Ready Kubernetes: How Do We Get There? - Nikhita Raghunath & Natalie Fisher, Broadcom; Nigel Jones, IBM; Ricardo Rocha, CERN; Tomas Gustavsson, Keyfactor

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Nikhita Raghunath, Natalie Fisher, Broadcom, Nigel Jones, IBM, Ricardo Rocha, CERN, Tomas Gustavsson, Keyfactor
- Schedule: https://kccnceu2025.sched.com/event/1tx7l/quantum-ready-kubernetes-how-do-we-get-there-nikhita-raghunath-natalie-fisher-broadcom-nigel-jones-ibm-ricardo-rocha-cern-tomas-gustavsson-keyfactor
- Busca YouTube: https://www.youtube.com/results?search_query=Quantum-Ready+Kubernetes%3A+How+Do+We+Get+There%3F+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Quantum-Ready Kubernetes: How Do We Get There?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx7l/quantum-ready-kubernetes-how-do-we-get-there-nikhita-raghunath-natalie-fisher-broadcom-nigel-jones-ibm-ricardo-rocha-cern-tomas-gustavsson-keyfactor
- YouTube search: https://www.youtube.com/results?search_query=Quantum-Ready+Kubernetes%3A+How+Do+We+Get+There%3F+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=SsTUGO9YbnQ
- YouTube title: Quantum-Ready Kubernetes: How Do We Get There?
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/quantum-ready-kubernetes-how-do-we-get-there/SsTUGO9YbnQ.txt
- Transcript chars: 31414
- Keywords: quantum, computing, workloads, algorithms, actually, computers, cryptography, around, learning, working, interested, projects, talked, looking, access, hybrid, already, interesting

### Resumo baseado na transcript

Now we make it even more complicated by throwing quantum computing into the mix. Um and so most of us have heard the term quantum computing mostly as a theoretical pursuit. Um responsible for the teams uh doing cloudnative deployments as well as machine learning deployments and uh now also starting to look at uh quantum computing management. So I I think we're all learning about quantum computers and we're still looking for real world use cases but these systems are developing rapidly and we know that at some point if we take cryptography for example you know that some of the mathematical for quantum services in the cloud and so it is about then making those available to people so that they can start experimenting and start learning um with them. of the algorithms and identifying the use cases where where things can match but also ensuring that uh we can manage these workloads and deploy them uh uh efficiently and cost efficive as as well.

### Excerpt da transcript

Hello everyone. Welcome to the panel about quantum computing and Kubernetes. We've talked a lot about how Kubernetes is complicated. Now we make it even more complicated by throwing quantum computing into the mix. Um and so most of us have heard the term quantum computing mostly as a theoretical pursuit. We've not really seen what the real world applications around it are and what does it really mean to run quantum workloads on Kubernetes and how we can make the Kubernetes and cloudnative ecosystem quantum safe. We've talked a lot about AI. Then why are we even talking about quantum now? Because AI is already so complicated because if we don't start talking about quantum now, we're going to run into trouble later on. So, we need to make progress while we still have time. So, since we're short on time, we've got just got 30 minutes and I'll try to leave some time for questions. Let's dive right into it. So, we've got a wonderful set of panelists here. Uh why don't you all go and introduce yourselves?

So, my name is Natalie Fischer. I work for VMware by Broadcom with Nikita on the Kubernetes um area stack. So, uh I work as a product manager there. Hi there everyone. I'm Nigel Jones. I work for IBM research. Um so I'm involved in postquantum cryptography and uh quantum and our services there and now doing some work with AI. So it's an interesting intersection to talk about today. Yeah. And I'm Thomas Koson. I'm chief PKI officer at key factor and I've been working with cyber security and public key infrastructure PI and opensource for the past 30 years. Hi, I'm Ricardo. Uh I lead the platforms infrastructure uh team at CERN. Um responsible for the teams uh doing cloudnative deployments as well as machine learning deployments and uh now also starting to look at uh quantum computing management. Awesome. Thank you. And as Natalie already said um I also work at Broadcom. Uh my name is Nikita. I'm a principal engineer there. I've been involved in the Kubernetes space for a long time. Now, quantum space interests me and I thought why not we talk more about this at CubeCon.

So, let's get started. Um, we've talked a lot about the AI hype, so I just want to circle back and talk about the quantum hype. When when's that going to happen? So I I think we're all learning about quantum computers and we're still looking for real world use cases but these systems are developing rapidly and we know that at some point if we take cryptography for example you know that some of
