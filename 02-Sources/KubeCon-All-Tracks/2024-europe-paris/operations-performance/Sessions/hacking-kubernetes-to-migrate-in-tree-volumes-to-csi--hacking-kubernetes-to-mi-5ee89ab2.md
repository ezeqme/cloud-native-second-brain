---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Operations + Performance"
themes: ["AI ML", "Storage Data", "Kubernetes Core", "SRE Reliability"]
speakers: ["Baptiste Girard-Carrabin", "Antoine Gaillard", "Datadog"]
sched_url: https://kccnceu2024.sched.com/event/1YeQl/hacking-kubernetes-to-migrate-in-tree-volumes-to-csi-baptiste-girard-carrabin-antoine-gaillard-datadog
youtube_search_url: https://www.youtube.com/results?search_query=Hacking+Kubernetes+to+Migrate+in-Tree+Volumes+to+CSI+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Hacking Kubernetes to Migrate in-Tree Volumes to CSI - Baptiste Girard-Carrabin & Antoine Gaillard, Datadog

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Baptiste Girard-Carrabin, Antoine Gaillard, Datadog
- Schedule: https://kccnceu2024.sched.com/event/1YeQl/hacking-kubernetes-to-migrate-in-tree-volumes-to-csi-baptiste-girard-carrabin-antoine-gaillard-datadog
- Busca YouTube: https://www.youtube.com/results?search_query=Hacking+Kubernetes+to+Migrate+in-Tree+Volumes+to+CSI+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Hacking Kubernetes to Migrate in-Tree Volumes to CSI.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeQl/hacking-kubernetes-to-migrate-in-tree-volumes-to-csi-baptiste-girard-carrabin-antoine-gaillard-datadog
- YouTube search: https://www.youtube.com/results?search_query=Hacking+Kubernetes+to+Migrate+in-Tree+Volumes+to+CSI+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=sVQtO55910I
- YouTube title: Hacking Kubernetes to Migrate in-Tree Volumes to CSI - Baptiste Girard-Carrabin & Antoine Gaillard
- Match score: 0.792
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/hacking-kubernetes-to-migrate-in-tree-volumes-to-csi/sVQtO55910I.txt
- Transcript chars: 21624
- Keywords: volume, volumes, migration, inside, create, manager, components, server, storage, cluster, driver, provider, trying, controller, access, handle, communities, called

### Resumo baseado na transcript

okay uh hello everyone uh Welcome to our talk uh we'll tell you our story uh of our journey migrating in three volumes to proper CSI ons so uh we'll start by a quick reminder about how storage work in communities uh then what's the CSI migration and how we made it work for us um so uh I'm antoan I'm a senior software engineer datadog I joined the company six years ago and uh it's been two years now that I work on our kuber stack and today I'm

### Excerpt da transcript

okay uh hello everyone uh Welcome to our talk uh we'll tell you our story uh of our journey migrating in three volumes to proper CSI ons so uh we'll start by a quick reminder about how storage work in communities uh then what's the CSI migration and how we made it work for us um so uh I'm antoan I'm a senior software engineer datadog I joined the company six years ago and uh it's been two years now that I work on our kuber stack and today I'm with hi I'm batist software engineer at data dog where I do everything related to storage inside kues and first let me give you a brief int introduction of how storage Works inside kues um well in if you want to have access to some kind of persistent data inside communities the most basic way is to use um what's called like the nod per local dis through for instance an MTD or um an host pass but if you want access to more advanced storage uh a p can create what's called a PVC persistent volume claim which is the way for the P to ask access to some kind of volume with a certain size and the storage class which is the the way of the for the P to Define what kind of uh volume it wants for instance here the P can ask for gp3 volumes in AWS EBS and the cruster will try to satisfy this claim using a persistent volume which is the wave of for KU to represent the backing disk used by a pod which can be a multiple which can use multiple kind of volume providers like AWS EBS or gcp persistant discs and once we have a PV and a PVC they can be bound together and the PO can have access to the underlying data initially in kubernetes the the way to get persistent volumes was through in three volumes in three because the code responsible for creating those volumes inside kubernetes was part of the inry kubernetes source code so it was a historical way of getting volumes inside communities but it had several drawbacks because the of the fact that it's inside of the kuun source code mainly um storage drivers would have to open source their code inside communities and follow the release cycle of kubernetes which is a bit cumbersome when you just want to make some small changes to your driver and how in three volumes worked where well you have a a pod that can ask for a PVC and the controller manager in particular the volume controller will watch for those PVCs and what it no is one it will invoke like it will call the volume provider to create a disk inside the volume provider once the dis is created the volume controller can create an
