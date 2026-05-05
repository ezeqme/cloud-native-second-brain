---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "AI + ML"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Alan Mutschelknaus", "Tim Wickberg", "SchedMD"]
sched_url: https://kccncna2025.sched.com/event/27FW5/slurm-bridge-slurm-scheduling-superpowers-in-kubernetes-alan-mutschelknaus-tim-wickberg-schedmd
youtube_search_url: https://www.youtube.com/results?search_query=Slurm+Bridge%3A+Slurm+Scheduling+Superpowers+in+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Slurm Bridge: Slurm Scheduling Superpowers in Kubernetes - Alan Mutschelknaus & Tim Wickberg, SchedMD

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Alan Mutschelknaus, Tim Wickberg, SchedMD
- Schedule: https://kccncna2025.sched.com/event/27FW5/slurm-bridge-slurm-scheduling-superpowers-in-kubernetes-alan-mutschelknaus-tim-wickberg-schedmd
- Busca YouTube: https://www.youtube.com/results?search_query=Slurm+Bridge%3A+Slurm+Scheduling+Superpowers+in+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Slurm Bridge: Slurm Scheduling Superpowers in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FW5/slurm-bridge-slurm-scheduling-superpowers-in-kubernetes-alan-mutschelknaus-tim-wickberg-schedmd
- YouTube search: https://www.youtube.com/results?search_query=Slurm+Bridge%3A+Slurm+Scheduling+Superpowers+in+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Vi8chqAFuN0
- YouTube title: Slurm Bridge: Slurm Scheduling Superpowers in Kubernetes - Alan Mutschelknaus & Tim Wickberg
- Match score: 0.855
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/slurm-bridge-slurm-scheduling-superpowers-in-kubernetes/Vi8chqAFuN0.txt
- Transcript chars: 29416
- Keywords: placeholder, scheduling, resource, running, filter, bridge, little, resources, kublet, controller, actually, trying, slinky, multi-node, support, associated, ecosystem, generated

### Resumo baseado na transcript

Um, we're here to talk about the Slurm Bridge, part of the Slinky project. Um, the term workload manager uh roughly means it is both a job scheduler as well as a resource manager allocating resources out on individual compute nodes providing orchestration and and management of individual compute processes out on those. So, Slinky itself, we we try to describe it as a toolkit of related components to integrate Slurm into Kubernetes. Um, those different components are designed to be able to mix and match with one another, but they can also be used standalone. Um, slurm bridge is sort of the newer bigger piece bringing slurm directly into the kubernetes scheduling layer. um especially being able to optimize like network layout and network placement for interconnects like Nvidia's DGX systems making sure that the planning for those simulations matches the underlying interconnect and are efficiently placed for best performance.

### Excerpt da transcript

Good afternoon. Um, we're here to talk about the Slurm Bridge, part of the Slinky project. Um, bringing Slurm scheduling superpowers into the Kubernetes stack. Uh, I'm Tim Wber. I'm the CTO for SKMD, the main Slurm developers. And >> Alan mic check. >> I'm Alan Moouse, one of the developers on the Slinky team. >> So, to start with, what is Slurm? Um, slurm is a leading HPC workload manager. Um, the term workload manager uh roughly means it is both a job scheduler as well as a resource manager allocating resources out on individual compute nodes providing orchestration and and management of individual compute processes out on those. Um, this all roughly equates in the cloudnative ecosystem into an orchestrator such as Kubernetes. Um the scheduling part again is kind of this higher level process that is prioritizing deciding what compute jobs what simulation jobs to run on what section of the system. Resource management layer is is really dedicated to the lower level plumbing of getting processes bootstrapped and executing on actual compute nodes.

Slurm itself was originally just a resource manager that was the R and the M out of Slurm. uh but then evolved all of these scheduling capabilities and some of what we're sort of experimenting with with the slurm bridge is getting slurm to behave just as a pureuler and actually being able to switch in kubernetes or slurm's own resource management layers to do the actual process management and process launch. Um slur manages the majority of the top 500 supercomputers in the world. Um this is a list that the HPC space has been maintaining for years. um we kind of look at that as our our benchmark of our our ability to to get slurm out into that audience. Um there is not really an equivalent uh list to point at for a IML workloads although our market research implies that we we do run the vast majority of AI training workloads today because of slurm's unique multi-node job scheduling capabilities that don't really exist directly in the cube ecosystem yet. Slarm also very frequently scales beyond 15,000 nodes in a cluster.

We we again run on these largest systems on the world. Um Slarm is open source under the GPL v2 or later license with an OpenSSL license exception. Um a little distinct from from stuff that's more native to the cloud ecosystem. Sketmd just to step back yet again um we are the developers of Slurm and now Slinky. Um, we actually spun off from Lawrence Livermore National Lab back in 2012 to to support
