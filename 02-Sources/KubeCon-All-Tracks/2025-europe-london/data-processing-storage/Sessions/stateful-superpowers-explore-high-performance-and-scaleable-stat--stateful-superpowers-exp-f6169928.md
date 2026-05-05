---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Data Processing + Storage"
themes: ["AI ML", "Storage Data", "SRE Reliability"]
speakers: ["Alex Chircop", "Chris Milsted", "Alex Reid", "Akamai", "Lori Lorusso", "Percona"]
sched_url: https://kccnceu2025.sched.com/event/1txEs/stateful-superpowers-explore-high-performance-and-scaleable-stateful-workloads-on-k8s-alex-chircop-chris-milsted-alex-reid-akamai-lori-lorusso-percona
youtube_search_url: https://www.youtube.com/results?search_query=Stateful+Superpowers%3A+Explore+High+Performance+and+Scaleable+Stateful+Workloads+on+K8s+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Stateful Superpowers: Explore High Performance and Scaleable Stateful Workloads on K8s - Alex Chircop, Chris Milsted & Alex Reid, Akamai; Lori Lorusso, Percona

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[AI ML]], [[Storage Data]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Alex Chircop, Chris Milsted, Alex Reid, Akamai, Lori Lorusso, Percona
- Schedule: https://kccnceu2025.sched.com/event/1txEs/stateful-superpowers-explore-high-performance-and-scaleable-stateful-workloads-on-k8s-alex-chircop-chris-milsted-alex-reid-akamai-lori-lorusso-percona
- Busca YouTube: https://www.youtube.com/results?search_query=Stateful+Superpowers%3A+Explore+High+Performance+and+Scaleable+Stateful+Workloads+on+K8s+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Stateful Superpowers: Explore High Performance and Scaleable Stateful Workloads on K8s.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txEs/stateful-superpowers-explore-high-performance-and-scaleable-stateful-workloads-on-k8s-alex-chircop-chris-milsted-alex-reid-akamai-lori-lorusso-percona
- YouTube search: https://www.youtube.com/results?search_query=Stateful+Superpowers%3A+Explore+High+Performance+and+Scaleable+Stateful+Workloads+on+K8s+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=JtMYdR50-KU
- YouTube title: Stateful Superpowers: Explore High Performa... Alex Chircop, Chris Milsted & Alex Reid, Lori Lorusso
- Match score: 0.735
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/stateful-superpowers-explore-high-performance-and-scaleable-stateful-w/JtMYdR50-KU.txt
- Transcript chars: 29196
- Keywords: storage, database, native, cluster, operator, operators, running, course, postgress, source, performance, actually, number, stateful, workloads, systems, application, projects

### Resumo baseado na transcript

Um, and I'm also, uh, a member of the technical oversight committee for the CNCF. So, why should we be thinking about um cloud native storage because it's often something that's that's uh ignored in our in our environments. It also allows you to easily scale and and apply um scaling as your capacity or your uh RPS requirements grow over time. And when it comes to performance with all the um flexibility that we have with nodes in a in a cloud native workload like Kubernetes where you have um uh local NVMe for example or distributed storage solutions that you can utilize you're also talking about now getting native performance like there isn't an overhead of of deploying in a cloudnative environment and more importantly the ability to get deterministic performance right so so the ability that the ability for a particular query to always take the same amount of And when we talk about cloud native storage, it's obviously more than just storage.

### Excerpt da transcript

Hello, welcome. Who knew so many people wanted to learn about stful storage? Um, so my name is Alex Kirkup. Uh, I'm a chief architect at Akamise Cloud. Um, and I'm also, uh, a member of the technical oversight committee for the CNCF. Um, this is my colleague. Hey y'all. My name is Lori. I'm the head of community at Perona and I am also a CNCF ambassador. Hey, I'm Alex Reed. I'm a principal engineer at Akami. And last but not least, my name is Chris Milstead. I'm a product architect at Akami as well. Welcome everyone. And back to you, Alex. Okay, then. So, why should we be thinking about um cloud native storage because it's often something that's that's uh ignored in our in our environments. I mean, seriously, hasn't everything been stateless forever? Now, this is something which I always put up in in all my talks to kind of say there is no such thing as a stateless architecture. It's just someone else's problem and it's probably all of your problems or some some of your problems. Um because all applications end up storing state somewhere.

And why would we want therefore our storage to be cloudnative? Because of course we've learned so much over the years from our Kubernetes environments where we've made workloads declarative and self-healing and autoscaling. So of course all of the stateful workloads can also benefit from the automation that you get from a cloud native environment, the ability to easily scale and deploy complex topologies, the self-healing and the automatic failover and of course the performance. And what do we mean by all of those things? So when we talk about automation, we're talking about the declarative nature of cloud native storage. You can have a set of YAML that defines not only that you want to run uh or or define a a stable workload, but it also allows you to define very complex topologies using operators. And we're going to give some demos to show that. It also allows you to easily scale and and apply um scaling as your capacity or your uh RPS requirements grow over time. And it provides an automatic self-healing.

So when you want to upgrade nodes, when you when a node fails and you need to fail over a workload somewhere else, you get that automatic self-healing failover. And when it comes to performance with all the um flexibility that we have with nodes in a in a cloud native workload like Kubernetes where you have um uh local NVMe for example or distributed storage solutions that you can utilize you're also talking about n
