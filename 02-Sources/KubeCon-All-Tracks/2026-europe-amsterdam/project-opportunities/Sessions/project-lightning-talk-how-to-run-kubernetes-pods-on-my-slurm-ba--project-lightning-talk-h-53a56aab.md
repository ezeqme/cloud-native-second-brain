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
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Diego Ciangottini", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFwd/project-lightning-talk-how-to-run-kubernetes-pods-on-my-slurm-based-hpc-center-diego-ciangottini-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+How+To+Run+Kubernetes+Pods+On+My+Slurm-Based+HPC+Center+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: How To Run Kubernetes Pods On My Slurm-Based HPC Center - Diego Ciangottini, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Diego Ciangottini, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFwd/project-lightning-talk-how-to-run-kubernetes-pods-on-my-slurm-based-hpc-center-diego-ciangottini-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+How+To+Run+Kubernetes+Pods+On+My+Slurm-Based+HPC+Center+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: How To Run Kubernetes Pods On My Slurm-Based HPC Center.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFwd/project-lightning-talk-how-to-run-kubernetes-pods-on-my-slurm-based-hpc-center-diego-ciangottini-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+How+To+Run+Kubernetes+Pods+On+My+Slurm-Based+HPC+Center+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=K-Z4l7SOa3o
- YouTube title: Project Lightning Talk: How To Run Kubernetes Pods On My Slurm-Based HPC Center - Diego Ciangottini
- Match score: 0.977
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-how-to-run-kubernetes-pods-on-my-slurm-based-hp/K-Z4l7SOa3o.txt
- Transcript chars: 3827
- Keywords: interlink, network, center, supercomputer, talking, running, whatever, notebook, either, supercomput, seamless, though, access, laptop, remote, distant, requirements, components

### Resumo baseado na transcript

Yeah, I'm a researcher at the uh National Institute of Nuclear Physics in Italy. But today I'm going to introduce Interlink uh as one of the maintainers. Okay, we are really talking about something that is remotely access slurm based resources from your own kubernetes that can run on your laptop on your cloud or whatever. Hope you like this picture because it cost me to to make it works on the plane with the Wi-Fi. Um the requirements first of all yeah um decently recent Kubernetes uh version and if you want the full-fledged capabilities of the system you might want also to have an ingress with wild cards or whatever is the equivalent approach on Zoom side on the The first one is a cublet virtual cublet provider for interlinker installed on the kubernetes cluster and the other one is an interlink server on the remote HPC side can be a login node or a dedicated machine on the edge of your supercomputer and

### Excerpt da transcript

Yeah, I'm a researcher at the uh National Institute of Nuclear Physics in Italy. But today I'm going to introduce Interlink uh as one of the maintainers. So what's this tool for? First of all, uh well, you can imagine that you create a pod on Kubernetes and with it manifest either you or your framework and you want to translate this into something that can run on a supercomput and the supercomputer might be managed in a different way like with a Zur uh batch system and you want something a translator in the middle. Um this is the role of interlink uh and the ambition of interlink to make this as seamless as possible. What I mean by seamless well no CRDs plain pods definition and no root administrative network privileges to do all the the magic around. So there are two disclaimer though the first one is that we are not talking about running slurm under kubernetes. So man managing u demons through kubernetes and we are not either talking about a situation where you have a bunch of nodes and you want to manage slurm and kubernetes side by side.

Okay, we are really talking about something that is remotely access slurm based resources from your own kubernetes that can run on your laptop on your cloud or whatever. So it can be closely remote meaning in the same center but with some network segregation or distant like right very distant from a plane running K3S. Hope you like this picture because it cost me to to make it works on the plane with the Wi-Fi. So yeah, wasn't a good idea. Um the requirements first of all yeah um decently recent Kubernetes uh version and if you want the full-fledged capabilities of the system you might want also to have an ingress with wild cards or whatever is the equivalent approach on Zoom side on the nodes you have to run a container runtime and share the file system across nodes and at the edge node where you have to install one of the components the network capability are caveat that uh should use unshare command on the nodes. So interlink it's composed by three main core components. The first one is a cublet virtual cublet provider for interlinker installed on the kubernetes cluster and the other one is an interlink server on the remote HPC side can be a login node or a dedicated machine on the edge of your supercomputer and then you need a network plug plugin if you want your pods offloaded to the HPC to be able to talk with the internal pod network of your kubernetes cluster and that's all then you need just to target the vir
