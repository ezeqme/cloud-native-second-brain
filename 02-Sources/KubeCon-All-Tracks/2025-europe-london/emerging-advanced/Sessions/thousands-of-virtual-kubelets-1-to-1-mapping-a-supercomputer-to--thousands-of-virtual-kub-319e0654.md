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
speakers: ["Dennis Marttinen", "Aalto University"]
sched_url: https://kccnceu2025.sched.com/event/1tx7r/thousands-of-virtual-kubelets-1-to-1-mapping-a-supercomputer-to-kubernetes-with-supernetes-dennis-marttinen-aalto-university
youtube_search_url: https://www.youtube.com/results?search_query=Thousands+of+Virtual+Kubelets%3A+1-to-1+Mapping+a+Supercomputer+To+Kubernetes+With+Supernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Thousands of Virtual Kubelets: 1-to-1 Mapping a Supercomputer To Kubernetes With Supernetes - Dennis Marttinen, Aalto University

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Dennis Marttinen, Aalto University
- Schedule: https://kccnceu2025.sched.com/event/1tx7r/thousands-of-virtual-kubelets-1-to-1-mapping-a-supercomputer-to-kubernetes-with-supernetes-dennis-marttinen-aalto-university
- Busca YouTube: https://www.youtube.com/results?search_query=Thousands+of+Virtual+Kubelets%3A+1-to-1+Mapping+a+Supercomputer+To+Kubernetes+With+Supernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Thousands of Virtual Kubelets: 1-to-1 Mapping a Supercomputer To Kubernetes With Supernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx7r/thousands-of-virtual-kubelets-1-to-1-mapping-a-supercomputer-to-kubernetes-with-supernetes-dennis-marttinen-aalto-university
- YouTube search: https://www.youtube.com/results?search_query=Thousands+of+Virtual+Kubelets%3A+1-to-1+Mapping+a+Supercomputer+To+Kubernetes+With+Supernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=QbR908kgk1Y
- YouTube title: Thousands of Virtual Kubelets: 1-to-1 Mapping a Supercomputer To Kubernetes With... Dennis Marttinen
- Match score: 0.983
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/thousands-of-virtual-kubelets-1-to-1-mapping-a-supercomputer-to-kubern/QbR908kgk1Y.txt
- Transcript chars: 25420
- Keywords: running, essentially, environment, workloads, bridge, however, cluster, computing, hardware, virtual, solutions, performance, systems, moment, tenants, thanks, actually, finally

### Resumo baseado na transcript

This is thousands of virtual cublets onetoone mapping a supercomputer to Kubernetes with superetes. I'm a security and cloud computing master student at Ald University in Finland as well as Nineu in Norway. On the highest level, the difference between cloud computing and high performance computing is this. The cloud assumes infinite resources and finite demand while high performance computing assumes finite resources and infinite demand. On the high performance computing side, on the other hand, single workloads may span across the entire system limited only by the number of nodes in total. Initially, this paints a picture that there are fundamentally different assumptions at play when building for the cloud versus high performance computing platforms.

### Excerpt da transcript

Thanks everyone for coming to my talk. This is thousands of virtual cublets onetoone mapping a supercomputer to Kubernetes with superetes. Let's get started. So hi everyone, I'm Deness. I'm a security and cloud computing master student at Ald University in Finland as well as Nineu in Norway. My cloudnative career started at Weave Works where I co-authored weave ignite. Currently I'm working on my master's thesis at the astroinformatics research group at Aldo University with a focus on supercomputer and cloud integration. So let's start with a quick poll to see which backgrounds you're coming from. First raise your hand if you're familiar with high performance computing or supercomputing on any level. Okay, it's a bit hard to see but I see a lot of hands. Nice. And then raise your hand if you're familiar with cloud computing or Kubernetes. again on any level. Yeah. Okay. A lot more as to be expected for CubeCon. Nice. So, let's hop straight into some comparisons then to get everyone on the same page. On the highest level, the difference between cloud computing and high performance computing is this.

The cloud assumes infinite resources and finite demand while high performance computing assumes finite resources and infinite demand. So, sort of the opposite. In practice, this means that cloud workloads are typically bound to a small set of nodes while there is node capacity for running a lot of workloads in parallel. On the high performance computing side, on the other hand, single workloads may span across the entire system limited only by the number of nodes in total. Initially, this paints a picture that there are fundamentally different assumptions at play when building for the cloud versus high performance computing platforms. However, with the advent of artificial intelligence workloads in today's market, the tables have turned for the cloud. Nowadays, cloud and HPC requirements look increasingly similar. The demand for resources by workloads is increasing while platform limits are starting to show. Last September, the European Commission published a report by the former European Central Bank President Mario Draghi.

Mario was tasked to prepare a report of his personal vision on the future of European competitiveness. In the report, Mario encouraged opening up HBC capacity to startups, small tomediumsiz enterprises, and the broader AI community as a whole. He also highlighted the importance of expanding Euro HPC to additional cloud and storage capabili
