---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Steven Wong", "Myles Gray", "VMware"]
sched_url: https://kccncna2021.sched.com/event/lV8U/kubernetes-vmware-user-group-using-gpus-with-k8s-on-vsphere-steven-wong-myles-gray-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+VMware+User+Group%3A+Using+GPUs+with+K8s+on+vSphere+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Kubernetes VMware User Group: Using GPUs with K8s on vSphere - Steven Wong & Myles Gray, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Steven Wong, Myles Gray, VMware
- Schedule: https://kccncna2021.sched.com/event/lV8U/kubernetes-vmware-user-group-using-gpus-with-k8s-on-vsphere-steven-wong-myles-gray-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+VMware+User+Group%3A+Using+GPUs+with+K8s+on+vSphere+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Kubernetes VMware User Group: Using GPUs with K8s on vSphere.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV8U/kubernetes-vmware-user-group-using-gpus-with-k8s-on-vsphere-steven-wong-myles-gray-vmware
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+VMware+User+Group%3A+Using+GPUs+with+K8s+on+vSphere+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_NYjvz92O58
- YouTube title: Kubernetes VMware User Group: Using GPUs with K8s on vSphere - Steven Wong & Myles Gray, VMware
- Match score: 0.877
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/kubernetes-vmware-user-group-using-gpus-with-k8s-on-vsphere/_NYjvz92O58.txt
- Transcript chars: 32969
- Keywords: gpu, bitfusion, container, fusion, client, running, integration, actually, server, cluster, servers, vmware, application, deploy, standard, essentially, python, processing

### Resumo baseado na transcript

hi welcome to kubecon 2021 in los angeles you're about to learn about some cool new tech that lets kubernetes workloads consume virtualized service from a pool of gpus a gpu does not have to be installed in the same physical worker node running the pod that is consuming the gpu i'm steve wong co-chair of the kubernetes vmware user group also presenting is going to be miles gray from the uk but because of travel difficulties he couldn't be here but he composed a great recording showing a deep here is we're going to add bitfusion or the bitfusion credentials more accurately to our kubernetes cluster to our tce cluster and this is brand new in bitfusion4 and to be honest i think this is a really really killer feature so if we go kubernetes clusters we click add it says cubeconfig and i've got my tceq config file here so click upload and we'll call it tce01 and you can see it's grabbed the ip address from the cubeconfig file automatically connected and pull back the namespaces so

### Excerpt da transcript

hi welcome to kubecon 2021 in los angeles you're about to learn about some cool new tech that lets kubernetes workloads consume virtualized service from a pool of gpus a gpu does not have to be installed in the same physical worker node running the pod that is consuming the gpu i'm steve wong co-chair of the kubernetes vmware user group also presenting is going to be miles gray from the uk but because of travel difficulties he couldn't be here but he composed a great recording showing a deep dive with a demo of this technology a word about the user group we're inclusive of all users running all uh forms of kubernetes on vmware infrastructure so what i'm talking about doesn't just apply to people running a vmware distribution uh this should be useful to you if you're running distributions like anthos eks anywhere openshift rancher or pure upstream uh kubernetes open source we'll start by talking about why you might want to use a gpu in your kubernetes workloads then miles is going to show you how to set this up with a step-by-step demo using kubernetes after you'll get details on how you can join the user group and a link to download this deck gpus got the name graphics processing units because they were originally designed to manipulate pixels for images and video people realize that the parallel processing capabilities could also be applied to many other general problems if they could be broken down to allow parallel processing and use of parallel algorithmic solutions machine learning is a common application but there are many more super computer pioneer seymour cray is said to have coined the marketing line which would you rather use a couple of strong oxen or a thousand chickens he said this back in the 90s well advancements in both hardware and software have changed the terrain and today you want the chickens now before some nitpicker in the audience looks at that picture carefully and points out that those are actually ducks and not chickens give me a little leeway and i want you to paint an even different picture visualize this in your head you can keep the ox but you know lose the ducks or chickens but i want you to bring in a shark and a school of piranha uh now imagine somebody is giving you the goal of creating a museum exhibit of an ox skeleton at the la uh county natural history museum and that museum by the way is just a short distance that way and i highly recommend it living in los angeles if you've got some spare time to kill but back to t
