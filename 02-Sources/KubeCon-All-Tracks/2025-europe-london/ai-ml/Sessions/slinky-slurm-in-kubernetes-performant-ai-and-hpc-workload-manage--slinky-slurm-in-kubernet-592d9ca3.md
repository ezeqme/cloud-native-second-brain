---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "AI + ML"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Tim Wickberg", "SchedMD"]
sched_url: https://kccnceu2025.sched.com/event/1tx8y/slinky-slurm-in-kubernetes-performant-ai-and-hpc-workload-management-in-kubernetes-tim-wickberg-schedmd
youtube_search_url: https://www.youtube.com/results?search_query=Slinky%3A+Slurm+in+Kubernetes%2C+Performant+AI+and+HPC+Workload+Management+in+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Slinky: Slurm in Kubernetes, Performant AI and HPC Workload Management in Kubernetes - Tim Wickberg, SchedMD

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Tim Wickberg, SchedMD
- Schedule: https://kccnceu2025.sched.com/event/1tx8y/slinky-slurm-in-kubernetes-performant-ai-and-hpc-workload-management-in-kubernetes-tim-wickberg-schedmd
- Busca YouTube: https://www.youtube.com/results?search_query=Slinky%3A+Slurm+in+Kubernetes%2C+Performant+AI+and+HPC+Workload+Management+in+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Slinky: Slurm in Kubernetes, Performant AI and HPC Workload Management in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx8y/slinky-slurm-in-kubernetes-performant-ai-and-hpc-workload-management-in-kubernetes-tim-wickberg-schedmd
- YouTube search: https://www.youtube.com/results?search_query=Slinky%3A+Slurm+in+Kubernetes%2C+Performant+AI+and+HPC+Workload+Management+in+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=gvp2uTilwrY
- YouTube title: Slinky: Slurm in Kubernetes, Performant AI and HPC Workload Management in Kubernetes - Tim Wickberg
- Match score: 1.007
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/slinky-slurm-in-kubernetes-performant-ai-and-hpc-workload-management-i/gvp2uTilwrY.txt
- Transcript chars: 34227
- Keywords: workloads, running, scheduling, bridge, resource, workload, compute, cluster, resources, control, within, management, little, everything, native, manage, around, machine

### Resumo baseado na transcript

I'm the chief technical officer for Sketmd and I'm here to talk about Slinky Slurm in Kubernetes performant AI and HPC workload management. Um, I also have our title slide uh broken out into our own uh format as well here backing it up with our logo. Um it's a toolkit of different projects to integrate Slurm into Kubernetes. Slurm operator is designed to manage slurm clusters running underneath Kubernetes. Uh give you easier ways to deploy reference slurm installations underneath Kubernetes potentially a managed Kubernetes offering from one of the cloud providers. The idea here is to enable slurm scheduling wherewithal not just for slurm based workloads but for kubernetes pods and kubernetes workflows.

### Excerpt da transcript

All right, good afternoon guys. I'm Tim Wickberg. I'm the chief technical officer for Sketmd and I'm here to talk about Slinky Slurm in Kubernetes performant AI and HPC workload management. Um, I also have our title slide uh broken out into our own uh format as well here backing it up with our logo. Um, and I do also need to uh give a lot of appreciation to the developers behind a lot of this effort. Skyler, Owlet, and Marlo, uh, who aren't here with me this week, but are behind all of the underpinnings I'm about to talk about today. Uh, wow, some of the slides are out of order. That's going to be fun. Okay, introduction. First of all, what is SLURM? Slurm is a leading HPC workload manager. Uh, workload manager roughly means a job scheduler combined with a resource manager. um roughly equivalent to an orchestrator uh such as Kubernetes and and what it does and manages on the compute nodes. Uh those two components there are scheduler prioritizes and decides which compute jobs to run on what parts of the system sort of when where and why.

And then the resource management layer of that is tracking node state, node resources, and dealing with actual job launch, job dispatch, potentially pulling in different container run times and ecosystems. Slur manages the majority of the top 500 supercomputers in the world. Um, roughly 60 to 70% last we checked. um also manages most AIM ML training workloads. Even for a lot of companies that run cloud native for the rest of their stack, slurm is usually involved in managing those training workloads for them. Today, uh slurm scales well beyond 15,000 nodes in a single cluster. Um we are able to on some machines launch 10,000 plus node simulation work in sub 10 seconds. uh which is something that we don't believe uh other orchestrators are able to accomplish today. Slurm is open source uh GPLv2 plus with an openSSL exception technically um and has been available to the broad community for a couple decades. It's going to be real fun how I got to figure out why the slides are out of order here. Uh so who is SKTMD?

Uh SKTMD are the developers of Slurm and also now Slinky. We originally spun off from from Lawrence Livermore National Lab back in 2012 to support SLURM's rapid adoption in the HPC industry. Um, our founders are Mo and Danny. They're the M andD in SKEMD. We are not medical doctors. Please do not solicit medical advice from many of our support staff. They are not qualified to answer that. SKETMD provides commercial
