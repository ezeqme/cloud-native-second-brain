---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Networking"
themes: ["Networking", "Kubernetes Core"]
speakers: ["Antonio Ojea", "RedHat"]
sched_url: https://kccnceu2021.sched.com/event/iE3g/kubernetes-advanced-networking-testing-with-kind-antonio-ojea-redhat
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Advanced+Networking+Testing+with+KIND+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Kubernetes Advanced Networking Testing with KIND - Antonio Ojea, RedHat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Networking]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Antonio Ojea, RedHat
- Schedule: https://kccnceu2021.sched.com/event/iE3g/kubernetes-advanced-networking-testing-with-kind-antonio-ojea-redhat
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Advanced+Networking+Testing+with+KIND+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Kubernetes Advanced Networking Testing with KIND.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE3g/kubernetes-advanced-networking-testing-with-kind-antonio-ojea-redhat
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Advanced+Networking+Testing+with+KIND+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-18U84TS75o
- YouTube title: Kubernetes Advanced Networking Testing with KIND - Antonio Ojea, RedHat
- Match score: 0.908
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/kubernetes-advanced-networking-testing-with-kind/-18U84TS75o.txt
- Transcript chars: 15388
- Keywords: cluster, create, container, network, docker, scenarios, server, clusters, latency, emulate, created, networks, testing, containers, images, feature, topology, traffic

### Resumo baseado na transcript

hello everybody welcome to this presentation about kubernetes advanced networking testing with kine my name is antonio here and i'm a contributor in kubernetes and kind projects for those of you that are not familiar with kind kind is a tool that is able to deploy kubernetes in docker containers it was created by benjamin elder some time ago to improve the testing of the kubernetes project one of the most important features of kind is that it allows you to create multi-node scenarios very useful to test conformance and

### Excerpt da transcript

hello everybody welcome to this presentation about kubernetes advanced networking testing with kine my name is antonio here and i'm a contributor in kubernetes and kind projects for those of you that are not familiar with kind kind is a tool that is able to deploy kubernetes in docker containers it was created by benjamin elder some time ago to improve the testing of the kubernetes project one of the most important features of kind is that it allows you to create multi-node scenarios very useful to test conformance and it's very optimized for performance and stability it's able to boost to with the crust and in less than 30 seconds the way that kind works is using a special node images these node images are container images that come preloaded with systemd cumulating container d binaries and the rest of the kubernetes components container images the way that kind works is using these images to create a cluster and once the images are created and running it runs cubadmin on top to configure the cluster so in the slide you can see what is the most common deployment of kind for testing with one control plane node and two worker nodes for this presentation we are going to focus in the networking so what we are interested in is how kind implements the networking kind in by default uses docker and the docker networking creates a linux bridge then then all the container images are attached to this linux bridge using bs interfaces on top of that we have a lot of iptable rules in different layers so for example docker uses ip tables to implement forwarding from the horse to the containers and kind or the kubernetes cluster uses iptables by q proxy to create the services abstraction for networking and kinetic ec to create to warp the pod to pod communication another important feature from kind is that it has an api and we can use this api to create plugins so we don't need to wait for the project to implement the feature that we want we just can use this api and this is what we are going to demonstrate in this presentation how to use kine api to create complex network scenarios one of the most common requests in kind that we didn't implement it officially is to be able to simulate nodes with multiple interfaces and multiple networks this usually this is common in bare metal scenarios when you want to provide different networks for different functionalities in this case in the example we have an installer a storage network and an external network so let's explain how
