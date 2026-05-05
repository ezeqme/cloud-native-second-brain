---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Project Opportunities"
themes: ["AI ML", "Storage Data", "Kubernetes Core", "Community Governance"]
speakers: ["Gabriele Bartolini", "Maintainer"]
sched_url: https://kccncna2025.sched.com/event/27d5y/project-lightning-talk-cloudnativepg-running-postgres-the-kubernetes-way-gabriele-bartolini-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+CloudNativePG%3A+Running+Postgres+The+Kubernetes+Way+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: CloudNativePG: Running Postgres The Kubernetes Way - Gabriele Bartolini, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Gabriele Bartolini, Maintainer
- Schedule: https://kccncna2025.sched.com/event/27d5y/project-lightning-talk-cloudnativepg-running-postgres-the-kubernetes-way-gabriele-bartolini-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+CloudNativePG%3A+Running+Postgres+The+Kubernetes+Way+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: CloudNativePG: Running Postgres The Kubernetes Way.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27d5y/project-lightning-talk-cloudnativepg-running-postgres-the-kubernetes-way-gabriele-bartolini-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+CloudNativePG%3A+Running+Postgres+The+Kubernetes+Way+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=pYwYwehQX3U
- YouTube title: Project Lightning Talk: CloudNativePG: Running Postgres The Kubernetes Way - Gabriele Bartolini
- Match score: 0.963
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-cloudnativepg-running-postgres-the-kubernetes-w/pYwYwehQX3U.txt
- Transcript chars: 4503
- Keywords: posgus, stateful, everyone, elephant, database, contributor, please, production, adopters, posgress, failover, synchronous, manage, controller, performance, native, declarative, important

### Resumo baseado na transcript

I'm Gabriel and I'm a maintainer of Cloud NetPG and the data on Kubernetes ambassador. Okay, so now for everyone of you who just raised your hand, especially production users, my most important question for you is, are you on the adopters list? I need at least one synchronous replica and please give me a separate volume for any uh world files for performance. Cloud netpg lets you keep uh uh your database logically in the same name space as your micros service but use kubernetes affinity taints and tolerations to place those elephant pods physically even on high performance bare metal nodes with local mvmemes for example. So this allows you to build the share nothing architecture that database people love right inside Kubernetes. You get declarative micros service native organization and the bare metal performance that posgus deserves.

### Excerpt da transcript

Ciao Cubon. I'm Gabriel and I'm a maintainer of Cloud NetPG and the data on Kubernetes ambassador. I'm a posgus contributor and I've used posgus for 25 years. We only have five minutes so let's get interactive immediately. Please raise your hands. Who has heard here about cloud netpg? Okay, so keep them up. Keep them up. Who's using it today in any environment? And let's get to the most important question. Who's using it in production? Okay, thanks. That's fantastic. Okay, so now for everyone of you who just raised your hand, especially production users, my most important question for you is, are you on the adopters list? So the QR code points to the official list of on GitHub. The adopters file is for us critical because uh we just joined the CNCF sandbox at the start of this year and our next major goal is to become an incubating project. So to do that we need to prove that uh the project is mature and that it's got wide adoption. So your story here is the single best way for us to do that. So please if you're using it add the PR.

Okay. So but everyone else for everyone else why is everyone using uh clonerpg so what is the problem that we solve? So we all love kubernetes because it's declarive but it's built it's built for cattle. Historically a database like posgress is stateful and it's a pet. So it needs all these complex day-to-day operations like failover backups upgrades security observability. So how do we solve all of these? The default Kubernetes answer is a stateful set. But a stateful set is a generic resource and doesn't understand posgress streaming and synchronous replication. So it doesn't understand also write ahead logs. So how can you truly manage a stateful pet like posgus when you are forced to use a generic controller that that treats all the apps the same? So you're still fighting the system. So this is why we wrote claronet PG an operator that doesn't use stateful sets but comes with its own custom controller that manages pods and PVC directly. This gives us the fine grained control to truly manage posgress the right way.

This is what we call the Kubernetes way. So you write your uh YAML file and say for example I want three uh instances. I need at least one synchronous replica and please give me a separate volume for any uh world files for performance. So our posgus native controller does all the hard work to uh to make that YAML file a reality and maintain it over time. So this declarative model enables what I call the elephant
