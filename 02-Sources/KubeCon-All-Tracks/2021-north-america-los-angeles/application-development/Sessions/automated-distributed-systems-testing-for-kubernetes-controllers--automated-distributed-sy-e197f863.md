---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Application + Development"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Lalith Suresh", "VMware", "Xudong Sun", "University of Illinois at Urbana-Champaign"]
sched_url: https://kccncna2021.sched.com/event/lV0S/automated-distributed-systems-testing-for-kubernetes-controllers-lalith-suresh-vmware-xudong-sun-university-of-illinois-at-urbana-champaign
youtube_search_url: https://www.youtube.com/results?search_query=Automated%2C+Distributed+Systems+Testing+for+Kubernetes+Controllers+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Automated, Distributed Systems Testing for Kubernetes Controllers - Lalith Suresh, VMware & Xudong Sun, University of Illinois at Urbana-Champaign

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Application + Development]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Lalith Suresh, VMware, Xudong Sun, University of Illinois at Urbana-Champaign
- Schedule: https://kccncna2021.sched.com/event/lV0S/automated-distributed-systems-testing-for-kubernetes-controllers-lalith-suresh-vmware-xudong-sun-university-of-illinois-at-urbana-champaign
- Busca YouTube: https://www.youtube.com/results?search_query=Automated%2C+Distributed+Systems+Testing+for+Kubernetes+Controllers+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Automated, Distributed Systems Testing for Kubernetes Controllers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV0S/automated-distributed-systems-testing-for-kubernetes-controllers-lalith-suresh-vmware-xudong-sun-university-of-illinois-at-urbana-champaign
- YouTube search: https://www.youtube.com/results?search_query=Automated%2C+Distributed+Systems+Testing+for+Kubernetes+Controllers+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6JnhjgOaZVk
- YouTube title: Automated, Distributed Systems Testing for Kubernetes Controllers - Lalith Suresh & Xudong Sun
- Match score: 0.917
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/automated-distributed-systems-testing-for-kubernetes-controllers/6JnhjgOaZVk.txt
- Transcript chars: 25391
- Keywords: controller, testing, cluster, sequence, learning, basically, controllers, reconciler, workload, particular, faults, server, second, distributed, resource, running, timestamp, desired

### Resumo baseado na transcript

hi everyone i'm alex suresh from vmware research and today with my colleague dongsan we're going to tell you about our work on making kubernetes controllers easier to test in the presence of various kinds of distributed systems faults so the focus of this talk is going to be on kubernetes controllers which as many of you are familiar is very central to extending kubernetes with new capabilities for example if you want to run a certain kind of database in a cloud native way on kubernetes we would write

### Excerpt da transcript

hi everyone i'm alex suresh from vmware research and today with my colleague dongsan we're going to tell you about our work on making kubernetes controllers easier to test in the presence of various kinds of distributed systems faults so the focus of this talk is going to be on kubernetes controllers which as many of you are familiar is very central to extending kubernetes with new capabilities for example if you want to run a certain kind of database in a cloud native way on kubernetes we would write a controller to manage that database in a cluster or we might add controllers to manage things to add new kinds of container networking capabilities or new kinds of storage capabilities right so for the purpose of illustration in this talk i'm just going to say hey let's have a controller manage something new that i'm writing called my app whatever it is so the standard way to go about this is to register a new kind of resource in the kubernetes api that describes an instance of my app and this resource will have a spec field which says what the desired state of my app should be now the controller monitors the current state of my app and it issues different kinds of side effects in order to reconcile the desired state and current state of this myapp instance right and in order to do so it might issue more commands back to the kubernetes api or it might use some kind of out-of-band mechanisms to reconfigure my app right so now the cache here is that this controller is simply just one component in a fairly complex distributed system so the cool and why is that because the kubernetes api itself is actually a bunch of api servers uh in a highly available setup backed by a bunch of lcd instances which is really the persistent store for the actual cluster state now the controller in order to do its job might lean on some built-in controllers and kubernetes for example it might be managing my app as a stateful set and that will require an interaction with the staple set controller in kubernetes or it might even rely on third-party controllers right and my app itself might be this there might be a bunch of processors running in different parts representing something like let's say a distributed database or something right so the controller is just one entity in this fairly complex distributed system and that means the controller is not immune from any of the distributed systems he challenges that any system has to deal with right like a controller has to deal with al
