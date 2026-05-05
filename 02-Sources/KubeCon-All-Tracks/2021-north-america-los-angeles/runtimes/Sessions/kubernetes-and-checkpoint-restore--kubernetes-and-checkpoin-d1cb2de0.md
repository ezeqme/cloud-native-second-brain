---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Runtimes"
themes: ["Runtime Containers", "Kubernetes Core"]
speakers: ["Adrian Reber", "Red Hat"]
sched_url: https://kccncna2021.sched.com/event/lV2C/kubernetes-and-checkpoint-restore-adrian-reber-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+and+Checkpoint+Restore+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Kubernetes and Checkpoint Restore - Adrian Reber, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Runtimes]]
- Temas: [[Runtime Containers]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Adrian Reber, Red Hat
- Schedule: https://kccncna2021.sched.com/event/lV2C/kubernetes-and-checkpoint-restore-adrian-reber-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+and+Checkpoint+Restore+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Kubernetes and Checkpoint Restore.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV2C/kubernetes-and-checkpoint-restore-adrian-reber-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+and+Checkpoint+Restore+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=0RUDoTi-Lw4
- YouTube title: Kubernetes and Checkpoint Restore - Adrian Reber, Red Hat
- Match score: 0.839
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/kubernetes-and-checkpoint-restore/0RUDoTi-Lw4.txt
- Transcript chars: 20021
- Keywords: container, checkpoint, restore, process, running, another, containers, migration, information, processes, checkpointing, already, parasite, original, create, transfer, migrate, without

### Resumo baseado na transcript

welcome everyone to my session kubernetes and checkpoint restore my name is adrian rebo i work for red hat since 2015 and i'm involved in process migration which is the basis or which is the result of checkpoint resource restore for at least 10 11 years now um i'm involved in in creo in some way since 2012 crew is the basis as the tool we use to checkpoint and restore our processes and container here today and i'm focusing on on container migration around i would say 2015 and

### Excerpt da transcript

welcome everyone to my session kubernetes and checkpoint restore my name is adrian rebo i work for red hat since 2015 and i'm involved in process migration which is the basis or which is the result of checkpoint resource restore for at least 10 11 years now um i'm involved in in creo in some way since 2012 crew is the basis as the tool we use to checkpoint and restore our processes and container here today and i'm focusing on on container migration around i would say 2015 and the agenda for today is i first want to give an introduction about a few definitions i'm using then i want to show a few use cases why a checkpoint restore and container migration might be might be something something useful and then i want to give some details about um basically how crew enables us to checkpoint and restore processes and containers so first the definition of container life migration because the work to get checkpoint restore working with container is always also the possibility to migrate containers from one system to another one and and and basically the idea behind container live migration is transfer a running container from one system to another system you could also call it maybe stateful migration because the state of the application in the container is not lost um but continues to be there and a very on a from a very high level view um container migration is basically we serialize the container on the source system write it to disk and transfer the the image we written to disk to a destination system and on this destination system we restore from the image to process the container and so we have container migration um as mentioned this is all everything i'm talking about today is based on creo checkpoint in restoring user space the reason for the name is at the time creo was first developed there were different approaches to checkpointing and restoring in linux there were kernel-only approaches there were mixed kernel and user-based approaches there were approaches where you intercepted system calls and creo took another approach and completely did it from user space using existing interfaces to collect as many information about the running process as possible there are multiple integrations of preview in container engines container runtimes and want to present some of those here so the one i have to present first is the openvset integration because um they invented creo and they had some mechanism to migrate containers before crew um but i think they were not
