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
themes: ["Networking", "Storage Data"]
speakers: ["Aloys Augustin", "Cisco", "Chris Tomkins", "Tigera"]
sched_url: https://kccncna2021.sched.com/event/lV4o/calicovpp-using-calicos-pluggable-dataplanes-for-fun-and-fast-networking-aloys-augustin-cisco-chris-tomkins-tigera
youtube_search_url: https://www.youtube.com/results?search_query=Calico%2FVPP%3A+Using+Calico%E2%80%99s+Pluggable+Dataplanes+for+Fun+and+Fast+Networking+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Calico/VPP: Using Calico’s Pluggable Dataplanes for Fun and Fast Networking - Aloys Augustin, Cisco & Chris Tomkins, Tigera

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Networking]]
- Temas: [[Networking]], [[Storage Data]]
- País/cidade: United States / Los Angeles
- Speakers: Aloys Augustin, Cisco, Chris Tomkins, Tigera
- Schedule: https://kccncna2021.sched.com/event/lV4o/calicovpp-using-calicos-pluggable-dataplanes-for-fun-and-fast-networking-aloys-augustin-cisco-chris-tomkins-tigera
- Busca YouTube: https://www.youtube.com/results?search_query=Calico%2FVPP%3A+Using+Calico%E2%80%99s+Pluggable+Dataplanes+for+Fun+and+Fast+Networking+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Calico/VPP: Using Calico’s Pluggable Dataplanes for Fun and Fast Networking.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV4o/calicovpp-using-calicos-pluggable-dataplanes-for-fun-and-fast-networking-aloys-augustin-cisco-chris-tomkins-tigera
- YouTube search: https://www.youtube.com/results?search_query=Calico%2FVPP%3A+Using+Calico%E2%80%99s+Pluggable+Dataplanes+for+Fun+and+Fast+Networking+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9zBu4Zcf__c
- YouTube title: Calico/VPP: Using Calico’s Pluggable Dataplanes for Fun and Fast N... Aloys Augustin & Chris Tomkins
- Match score: 0.911
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/calico-vpp-using-calicos-pluggable-dataplanes-for-fun-and-fast-network/9zBu4Zcf__c.txt
- Transcript chars: 26635
- Keywords: calico, applications, network, interface, networking, performance, packet, packets, control, software, traffic, features, second, application, planes, available, kernel, cluster

### Resumo baseado na transcript

hi and welcome to this talk entitled calico vpp using calico's plugable data planes for fun and fast networking my name is chris tompkins i'm a developer advocate at tigera i champion user needs and support the community and users i've been working in networking since about 2000 and after a few years i realized that a per device cli is not a great solution for a large environment so i took an early interest in infrastructure as code and automation and and i still pursue those today when i'm

### Excerpt da transcript

hi and welcome to this talk entitled calico vpp using calico's plugable data planes for fun and fast networking my name is chris tompkins i'm a developer advocate at tigera i champion user needs and support the community and users i've been working in networking since about 2000 and after a few years i realized that a per device cli is not a great solution for a large environment so i took an early interest in infrastructure as code and automation and and i still pursue those today when i'm not working in it i love reading films music i also fly radio controlled gliders which is a strange coincidence as our other speaker today alois augustine who's a software engineer at cisco um also does like flying radio control planes um he is one of the calico vpp data plane author uh team um so without further ado let's get started so i'm going to start and just talk a little bit about calico first of all just very briefly so what is calico well it's an open source networking and network security solution for containers virtual machines and native host based workloads it supports a broad range of platforms including kubernetes openshift marantes kubernetes engine openstack and bare metal services and whether you opt to use the ebpf data plane or linux's standard networking data plane or vpp um or the windows host networking service data plane um calico delivers blazing fast performance and cloud native scalability it provides developers and cluster operators with a consistent experience and a set of capabilities whether you're running in cloud or on-prem so we have more than 6 000 slack channel members more than 150 contributors and more than a million compute nodes are powered by calico every day so when calico was designed it was designed with a four-tier architecture from day one so software modularity and software loose coupling were included by design in the in the software architecture and that has paid great dividends so you might be aware that network hardware is often designed with a paradigm of having a control plane and a data plane we'll go into what those are in a moment but calico also follows that model software modularity is the concept of the dividing software code intentionally into blocks that work together to create a larger hole and software loose coupling is the concept of making these blocks opaque to each other so that they can only talk via strictly defined interfaces together these concepts make the software easier to fix troubleshoot and re
