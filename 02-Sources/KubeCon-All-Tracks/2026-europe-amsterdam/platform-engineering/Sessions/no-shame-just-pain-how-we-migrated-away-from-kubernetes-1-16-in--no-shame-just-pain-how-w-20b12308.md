---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Platform Engineering"
themes: ["AI ML", "Platform Engineering", "Kubernetes Core"]
speakers: ["Jannis Relakis", "Michael Seiwald-McCarty", "Celonis"]
sched_url: https://kccnceu2026.sched.com/event/2CVyQ/no-shame-just-pain-how-we-migrated-away-from-kubernetes-116-in-2025-jannis-relakis-michael-seiwald-mccarty-celonis
youtube_search_url: https://www.youtube.com/results?search_query=No+Shame%2C+Just+Pain%3A+How+We+Migrated+Away+From+Kubernetes+1.16+in+2025+CNCF+KubeCon+2026
slides: []
status: parsed
---

# No Shame, Just Pain: How We Migrated Away From Kubernetes 1.16 in 2025 - Jannis Relakis & Michael Seiwald-McCarty, Celonis

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jannis Relakis, Michael Seiwald-McCarty, Celonis
- Schedule: https://kccnceu2026.sched.com/event/2CVyQ/no-shame-just-pain-how-we-migrated-away-from-kubernetes-116-in-2025-jannis-relakis-michael-seiwald-mccarty-celonis
- Busca YouTube: https://www.youtube.com/results?search_query=No+Shame%2C+Just+Pain%3A+How+We+Migrated+Away+From+Kubernetes+1.16+in+2025+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre No Shame, Just Pain: How We Migrated Away From Kubernetes 1.16 in 2025.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVyQ/no-shame-just-pain-how-we-migrated-away-from-kubernetes-116-in-2025-jannis-relakis-michael-seiwald-mccarty-celonis
- YouTube search: https://www.youtube.com/results?search_query=No+Shame%2C+Just+Pain%3A+How+We+Migrated+Away+From+Kubernetes+1.16+in+2025+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=MNAcbHUBERU
- YouTube title: No Shame, Just Pain: How We Migrated Away From Kubernete... Jannis Relakis & Michael Seiwald-McCarty
- Match score: 0.825
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/no-shame-just-pain-how-we-migrated-away-from-kubernetes-1-16-in-2025/MNAcbHUBERU.txt
- Transcript chars: 28851
- Keywords: migration, cluster, clusters, wormhole, needed, basically, environments, migrate, everything, application, migrated, platform, started, migrations, traffic, already, flavors, certain

### Resumo baseado na transcript

Uh no shame just pain how we migrated away from Kubernetes 116 in brackets in 2025. I'm a senior platform engineer at Salonus and today with me on stage is Michael. I'm going to share the lessons learned and also the mistakes that we made along the way so that you can avoid them. So before we get into the details of the migration, we want to take a step back and um give you a little introduction of our Kubernetes setup and also the history and how we accumulated so many flavors which then triggered the migration project in the first place. Uh we had the additional requirement to run in Azure and also back then Gardner was really like an innovative concept which running Kubernetes inside Kubernetes and then have lightweight clusters. Also, this was the first time we had professional support for our Kubernetes clusters.

### Excerpt da transcript

Hello everyone and thank you for joining us in the session. Uh no shame just pain how we migrated away from Kubernetes 116 in brackets in 2025. So yeah um today it's going to be me Janisle. I'm a senior platform engineer at Salonus and today with me on stage is Michael. He's a staff platform engineer but also there are a few other people in the crowd that were part of this project. So yeah, raise your hands, get the credit that you deserve. All right. Um, okay. So, we are Salonus. Uh, we are the company that helps other companies improve their business processes. Uh, we introduced the term process mining in 2011. And, uh, our product evolved into the process intelligence platform in 2023. And as you can see on the left part of the screen, we have a bunch of renowned customers and also renowned partners. So why are we standing here? Why are we having this talk? Why am I talking to you? Um the reason is that recently I heard u an interesting stat. 70% of all large scale migrations fail. And in the words of XKCD, I couldn't describe it better so I let the professional do it here.

um he's talking about the proliferation of standards. There are 14 standards. That's ridiculous. We need to consolidate. We need to bring it down to one. What tends to happen is you end up with 15 standards. So, um we were in a similar situation. We had six Kubernetes flavors and we wanted to consolidate them down to three, one for each cloud provider. And the fear was that we going to end up with nine. And um spoiler alert, that didn't happen. And that ties back to the why. I'm standing here to share how we avoided that from happening. I'm going to share the lessons learned and also the mistakes that we made along the way so that you can avoid them. So before we get into the details of the migration, we want to take a step back and um give you a little introduction of our Kubernetes setup and also the history and how we accumulated so many flavors which then triggered the migration project in the first place. So in Solonus we have what we call environments which are basically full installations of the Salonus platform and one environment consists of multiple clusters and these environments are created based on certain criteria.

One is tenency. So we have shared environments where we have uh multiple clusters and customers sometimes hundreds of customers but we also have uh dedicated private uh environments for just a single customer. Furthermore, we run on multiple cloud providers
