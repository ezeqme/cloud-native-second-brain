---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Networking"
themes: ["Networking", "Kubernetes Core"]
speakers: ["Dan Finneran", "Equinix"]
sched_url: https://kccncna2021.sched.com/event/lUzp/roll-out-the-red-carpet-for-production-kubernetes-clusters-with-a-kube-vip-dan-finneran-equinix
youtube_search_url: https://www.youtube.com/results?search_query=Roll+Out+the+Red+Carpet+for+Production+Kubernetes+Clusters+with+a+Kube-vip+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Roll Out the Red Carpet for Production Kubernetes Clusters with a Kube-vip - Dan Finneran, Equinix

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Networking]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Dan Finneran, Equinix
- Schedule: https://kccncna2021.sched.com/event/lUzp/roll-out-the-red-carpet-for-production-kubernetes-clusters-with-a-kube-vip-dan-finneran-equinix
- Busca YouTube: https://www.youtube.com/results?search_query=Roll+Out+the+Red+Carpet+for+Production+Kubernetes+Clusters+with+a+Kube-vip+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Roll Out the Red Carpet for Production Kubernetes Clusters with a Kube-vip.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lUzp/roll-out-the-red-carpet-for-production-kubernetes-clusters-with-a-kube-vip-dan-finneran-equinix
- YouTube search: https://www.youtube.com/results?search_query=Roll+Out+the+Red+Carpet+for+Production+Kubernetes+Clusters+with+a+Kube-vip+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=JvDjQLrAGSY
- YouTube title: Roll Out the Red Carpet for Production Kubernetes Clusters with a Kube-vip - Dan Finneran, Equinix
- Match score: 0.956
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/roll-out-the-red-carpet-for-production-kubernetes-clusters-with-a-kube/JvDjQLrAGSY.txt
- Transcript chars: 27486
- Keywords: address, traffic, network, leader, control, effectively, cluster, actually, typically, provide, additional, cubevip, election, router, clusters, available, inside, running

### Resumo baseado na transcript

hello and thank you very much uh for coming to this talk today um if you are watching this is a recording then unfortunately i'm unable to be with you today however uh again uh thank you for coming to my talk today today we're going to be talking about rolling out the red carpet for production kubernetes clusters with a cube vip um my name is daniel finneran also known as the bsd box on github and and twitter and other places and i'm currently leading the engineering efforts

### Excerpt da transcript

hello and thank you very much uh for coming to this talk today um if you are watching this is a recording then unfortunately i'm unable to be with you today however uh again uh thank you for coming to my talk today today we're going to be talking about rolling out the red carpet for production kubernetes clusters with a cube vip um my name is daniel finneran also known as the bsd box on github and and twitter and other places and i'm currently leading the engineering efforts in developer relations at equinix metal so to kick things off a bit of background i guess into the the cube vip project many many roles ago i was predominantly focused on helping customers and end users roll out bare metal kubernetes servers and clusters and from that i i kind of spawned a bare metal provisioning project in order to kind of alleviate a lot of the issues that i was finding getting these these uh clusters rolled out so it's quite a simple project to automate the deployment of bare metal servers it would typically stand up the operating system and then once i kind of got that automated it later kind of developed into a provisioning engine um to not only stand up the operating system but then to stand up the kubernetes clusters that sat on top of it i then started to kind of take it i guess to the next level by looking at building a cappy so a cluster api provider to automate um the entire end-to-end platform and this is typically where i i started to hit a number of problems mainly around kind of the the life cycle and and turning these clusters into something that was a bit more kind of production ready so um the you know the kind of typical architecture of kubernetes clusters are that we have a control plane which should be made up of more than one control plane node and then typically as many workers as required in order to run applications and workloads and things like that the high available in the production kind of side of things typically mean that we need to really kind of protect the control plane because without the control plane we no longer have access to do anything with that kubernetes cluster your workloads more than likely will continue to carry on running however we can no longer change things we can no longer get the state of everything that's actually running within that kubernetes cluster so we need to look at making the control plane highly available so typically in order for a highly available kubernetes cluster we obviously need more than one contr
