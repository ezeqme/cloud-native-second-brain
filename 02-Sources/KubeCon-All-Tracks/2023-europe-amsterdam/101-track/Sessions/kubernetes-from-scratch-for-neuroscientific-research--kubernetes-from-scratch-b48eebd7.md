---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "101 Track"
themes: ["Kubernetes Core"]
speakers: ["Carolina Lindqvist", "Daniel Fernández", "EPFL"]
sched_url: https://kccnceu2023.sched.com/event/1HyYl/kubernetes-from-scratch-for-neuroscientific-research-carolina-lindqvist-daniel-fernandez-epfl
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+from+Scratch+for+Neuroscientific+Research+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Kubernetes from Scratch for Neuroscientific Research - Carolina Lindqvist & Daniel Fernández, EPFL

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[101 Track]]
- Temas: [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Carolina Lindqvist, Daniel Fernández, EPFL
- Schedule: https://kccnceu2023.sched.com/event/1HyYl/kubernetes-from-scratch-for-neuroscientific-research-carolina-lindqvist-daniel-fernandez-epfl
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+from+Scratch+for+Neuroscientific+Research+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Kubernetes from Scratch for Neuroscientific Research.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyYl/kubernetes-from-scratch-for-neuroscientific-research-carolina-lindqvist-daniel-fernandez-epfl
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+from+Scratch+for+Neuroscientific+Research+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=QJUeZy-yslA
- YouTube title: Kubernetes from Scratch for Neuroscientific Research - Carolina Lindqvist & Daniel Fernández, EPFL
- Match score: 0.797
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/kubernetes-from-scratch-for-neuroscientific-research/QJUeZy-yslA.txt
- Transcript chars: 25310
- Keywords: cluster, puppet, organization, configuration, running, openshift, production, flux, finally, version, storage, application, applications, wanted, testing, worker, environment, started

### Resumo baseado na transcript

hello everyone and Welcome to our talk kubernetes from scratch for a neuroscientific research so a little bit about the agenda so we'll first tell you a bit about us and the target audience for this talk and then how did our interesting kubernetes start and then a bit about prototyping kubernetes and our organization's infrastructure overview and then how it is to run the kubernetes cluster and do maintenance and then the use cases that we have within the organization and the process of migrating to kubernetes and how is when we started this proof of concept based on vanilla kubernetes in this case we went for kubernetes 120 with containerdy and run C and since the beginning of the POC we had a few things clear uh we wanted to be virtualized running although at the beginning we started with seven and around one year ago we made an operating system upgrade the current version of kubernetes we are using in production is 125 so that means we did five upgrades in the last two years and we tried to run n minus one version of kubernetes in production being in the latest stable of kubernetes uh currently we have two different clusters brought for production and depth for development architecture wise they're both the same uh we have three control planes of nodes so we don't waste resources there since config wise they are both clusters hide identical we encourage our users to run...

### Excerpt da transcript

hello everyone and Welcome to our talk kubernetes from scratch for a neuroscientific research so a little bit about the agenda so we'll first tell you a bit about us and the target audience for this talk and then how did our interesting kubernetes start and then a bit about prototyping kubernetes and our organization's infrastructure overview and then how it is to run the kubernetes cluster and do maintenance and then the use cases that we have within the organization and the process of migrating to kubernetes and how it is from kubernetes users point of view so about us my name is Carolina Lindquist and I work as an SRE at epfl in the blue brain project and I'm in the team for neuroinformatics software engineering and my team is developing a storage application for neurosavientific data and hello everyone my name is Daniel Fernandez I'm also an SRE I've been in the blueprint project for the last three years as a necessary as well and I'm in the core service system and we can think of us as a small it department for the organization we take care of different I.T services for the users at the blueprint and we are a small team of six accessories so a little bit about our organization the blue Brain Project the ultimate goal is the digitally reconstruct and simulate the mouse brain and also Pioneer simulation neuroscience and we hope that it will better help the understanding of the human brain also with some potential applications in health and disease research and as you see from the organization chart we are coming from different parts of the organization so this was done as a as a collaboration and about their presentation so we want to give you some ideas for how to approach an on-premise cluster setup and these ideas can also be applied to a cloud environment and it's more intended as giving you some pointers to start and also some of our slides might take have a lot of text so we should also be able to use them as a reference after this talk and some useful prerequisites since this is the 101 track is like basic knowledge about kubernetes architecture and basic knowledge about some resource type and some knowledge of film and Helm chart is a plus but again if you haven't learned about this yet you can always come back to our presentation later as a recording so how did our interest in kubernetes start So within my team we were using openshift which was the organization's container platform and in the setup that we had there were some features that were
