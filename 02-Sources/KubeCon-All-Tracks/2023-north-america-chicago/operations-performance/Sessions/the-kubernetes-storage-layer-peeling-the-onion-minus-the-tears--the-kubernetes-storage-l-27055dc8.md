---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Operations + Performance"
themes: ["Storage Data", "Kubernetes Core", "SRE Reliability"]
speakers: ["Madhav Jivrajani", "VMware"]
sched_url: https://kccncna2023.sched.com/event/1R2wD/the-kubernetes-storage-layer-peeling-the-onion-minus-the-tears-madhav-jivrajani-vmware
youtube_search_url: https://www.youtube.com/results?search_query=The+Kubernetes+Storage+Layer%3A+Peeling+the+Onion+Minus+the+Tears+CNCF+KubeCon+2023
slides: []
status: parsed
---

# The Kubernetes Storage Layer: Peeling the Onion Minus the Tears - Madhav Jivrajani, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Storage Data]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Madhav Jivrajani, VMware
- Schedule: https://kccncna2023.sched.com/event/1R2wD/the-kubernetes-storage-layer-peeling-the-onion-minus-the-tears-madhav-jivrajani-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=The+Kubernetes+Storage+Layer%3A+Peeling+the+Onion+Minus+the+Tears+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre The Kubernetes Storage Layer: Peeling the Onion Minus the Tears.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2wD/the-kubernetes-storage-layer-peeling-the-onion-minus-the-tears-madhav-jivrajani-vmware
- YouTube search: https://www.youtube.com/results?search_query=The+Kubernetes+Storage+Layer%3A+Peeling+the+Onion+Minus+the+Tears+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=TNNJFtfy7iU
- YouTube title: The Kubernetes Storage Layer: Peeling the Onion Minus the Tears - Madhav Jivrajani, VMware
- Match score: 0.918
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/the-kubernetes-storage-layer-peeling-the-onion-minus-the-tears/TNNJFtfy7iU.txt
- Transcript chars: 34170
- Keywords: resource, version, request, server, requests, called, object, specify, happens, events, cluster, controller, current, deployment, replica, versions, storage, controllers

### Resumo baseado na transcript

so uh I think let's get started first of all thank you so much for making it it's the last talk of a very very long week so thank you everyone for making it and I've had I I hope you've had a nice fun productive successful cubec con if not anything else I hope you made a new friend so uh my name is madav I I work at VMware um I I'm I'm a technical lead of s contributor experience I'm a GitHub adman for the kubernetes project

### Excerpt da transcript

so uh I think let's get started first of all thank you so much for making it it's the last talk of a very very long week so thank you everyone for making it and I've had I I hope you've had a nice fun productive successful cubec con if not anything else I hope you made a new friend so uh my name is madav I I work at VMware um I I'm I'm a technical lead of s contributor experience I'm a GitHub adman for the kubernetes project and I've worked on the kubernetes storage layer on some really really fun parts of it uh so because of that I've had to shed many a teer trying to understand what was going on so hopefully I can peel that onion of abstraction for you without the tears so let's get started before we start uh just a public call to help we need help migrating proud jobs to community clusters so if you're a person interested in infrastructure and want to get involved in the kubernetes community check that link out uh so before we get into like the core of it let's get a few prerequisites out of the way so we'll take a 50,000 super super high level view of what the kubernetes machine looks like and how it works we have something called the API server which clients such as cube cutle interact with and kubernetes being something called a declarative system we declare what we want our intended state to be so in this case we want a deployment which has three pods and we specify that as something called replicas so if I do Cube cutle apply with this deployment what happens behind the scenes uh API server takes this deployment persists it into hcd and also now we have a bunch of controllers that run on the Clusters these controllers are binaries or the tldr of this is that they are binaries that look for changes that happen in the cluster State they need to know where we are currently they need to know where we need to be and then based on these two things the sort of calculate a set of actions to take in order to get to where we need to be so we have uh I've there are a lot of controllers in the kubernetes cluster by default but I've specified three of them here we have the scheduler we have the deployment controller and we have the replica set controller so the deployment controller sees that okay also we have a bunch of nodes in the cluster each node has a cube letter which also is a controller and each of them talk to API server no one talks to HD directly everything goes through the API server so deployment controller sees that there's a deployment it's like
