---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Rajith Attapattu", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFz3/project-lightning-talk-opencost-cost-and-resource-management-rajith-attapattu-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+OpenCost%3A+Cost+And+Resource+Management+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: OpenCost: Cost And Resource Management - Rajith Attapattu, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Rajith Attapattu, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFz3/project-lightning-talk-opencost-cost-and-resource-management-rajith-attapattu-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+OpenCost%3A+Cost+And+Resource+Management+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: OpenCost: Cost And Resource Management.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFz3/project-lightning-talk-opencost-cost-and-resource-management-rajith-attapattu-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+OpenCost%3A+Cost+And+Resource+Management+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=w-_PJXitKI8
- YouTube title: Project Lightning Talk: OpenCost: Cost And Resource Management - Rajith Attapattu, Maintainer
- Match score: 0.891
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-opencost-cost-and-resource-management/w-_PJXitKI8.txt
- Transcript chars: 6254
- Keywords: cost, clusters, cluster, resource, vendor, visibility, architecture, workloads, running, opencast, carpenter, allocation, network, question, awesome, neutral, pretty, plug-in

### Resumo baseado na transcript

I can't remember the times off the top of my head, but we'd love for you to come by and and visit and ask any questions. All right, I'm going to take you through three slides and I have a quick hands-on demo and um if I have enough time I can show you around the the UI a little bit. Uh tomorrow I have a a deep dive into opencast a regular session where we're going to go deeper into the architecture and talk about um you know promis versus uh you know uh Prometheus mode and some other innovative things that we're going to do in the project. uh when day two operations come, people want to know how to keep their cost in check and more importantly, how do we get visibility into the efficiency of the cluster so we can rightsize the clusters and the workloads? Um, with with open cost, you get visibility into the cost makeup of your cluster. your overhead cost which is where the control plane costs any extra cost that you you know might think of running it and then you have the allocation costs.

### Excerpt da transcript

All right, pleasure to be here. Um, all right. So, I'm going to talk to you about the open cost project. How many of you have heard about it? Hooray. That's that's awesome. Uh, this time we have, uh, 3 days at the project pavilion. Just drop by. I can't remember the times off the top of my head, but we'd love for you to come by and and visit and ask any questions. All right, I'm going to take you through three slides and I have a quick hands-on demo and um if I have enough time I can show you around the the UI a little bit. All right. Okay. So, uh what's open cost? It's a vendor neutral CNCF incubating project. It provides a unified u model for your allocations and assets. Um it gives you a way to um you know get visibility into your Kubernetes clusters, right? has uh multi cloud support. If you're running on prem, you can give a custom pricing sheet. Um has a pretty extensible architecture. Uh there's a plug-in uh architecture there where you can um build things like, you know, for example, someone built a data dog plugin.

Um there's a snowflake plug-in that's kind of making its way through the PRs. So you can build um cost models for other non- Kubernetes stuff and then kind of bring that data into into Opencast itself. uh has a pretty flexible deployment model. Uh it uh currently uses Prometheus but obviously there are some performance challenges especially when you have a lots of workloads in very large clusters. So uh the community is working on a promless um mode. Um still in alpha mode but we encourage you to come and you know try it out. Uh tomorrow I have a a deep dive into opencast a regular session where we're going to go deeper into the architecture and talk about um you know promis versus uh you know uh Prometheus mode and some other innovative things that we're going to do in the project. All right. So uh why does it matter? Um you know we all uh adopted Kubernetes which is why we all here. uh when day two operations come, people want to know how to keep their cost in check and more importantly, how do we get visibility into the efficiency of the cluster so we can rightsize the clusters and the workloads?

Yeah, we do have carpenter and things like that, but you'd be surprised to see how many clusters are grossly overprovisioned, mostly because the workloads are not sort of right sized. Um, with with open cost, you get visibility into the cost makeup of your cluster. And very quickly, I'll kind of talk about the sort of like the fundamental
