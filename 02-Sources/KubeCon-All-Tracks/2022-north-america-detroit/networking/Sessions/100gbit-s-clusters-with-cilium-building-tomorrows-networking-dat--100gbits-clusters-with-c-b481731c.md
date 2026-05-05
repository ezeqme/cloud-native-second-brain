---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Networking"
themes: ["Networking", "Storage Data", "Kubernetes Core"]
speakers: ["Daniel Borkmann", "Nikolay Aleksandrov", "Isovalent"]
sched_url: https://kccncna2022.sched.com/event/182DB/100gbits-clusters-with-cilium-building-tomorrows-networking-data-plane-daniel-borkmann-nikolay-aleksandrov-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=100Gbit%2FS+Clusters+With+Cilium%3A+Building+Tomorrow%E2%80%99s+Networking+Data+Plane+CNCF+KubeCon+2022
slides: []
status: parsed
---

# 100Gbit/S Clusters With Cilium: Building Tomorrow’s Networking Data Plane - Daniel Borkmann & Nikolay Aleksandrov, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Networking]]
- Temas: [[Networking]], [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Daniel Borkmann, Nikolay Aleksandrov, Isovalent
- Schedule: https://kccncna2022.sched.com/event/182DB/100gbits-clusters-with-cilium-building-tomorrows-networking-data-plane-daniel-borkmann-nikolay-aleksandrov-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=100Gbit%2FS+Clusters+With+Cilium%3A+Building+Tomorrow%E2%80%99s+Networking+Data+Plane+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre 100Gbit/S Clusters With Cilium: Building Tomorrow’s Networking Data Plane.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182DB/100gbits-clusters-with-cilium-building-tomorrows-networking-data-plane-daniel-borkmann-nikolay-aleksandrov-isovalent
- YouTube search: https://www.youtube.com/results?search_query=100Gbit%2FS+Clusters+With+Cilium%3A+Building+Tomorrow%E2%80%99s+Networking+Data+Plane+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Kvdh78TURck
- YouTube title: 100Gbit/S Clusters With Cilium: Building Tomorrows Networking- Daniel Borkmann & Nikolay Aleksandrov
- Match score: 0.894
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/100gbit-s-clusters-with-cilium-building-tomorrows-networking-data-plan/Kvdh78TURck.txt
- Transcript chars: 24163
- Keywords: address, kernel, cluster, essentially, gateway, sodium, ebpf, basically, support, packets, device, latency, packet, clusters, gigabit, second, actually, course

### Resumo baseado na transcript

hello and welcome to my talk uh I'm Daniel Brockman I work on sodium itself and also on the Linux kernel so I co-maintain ebpf in the Linux kernel and today's talk is about 100 gigabit per second clusters with psyllium building tomorrow's networking data plane so when looking at data center networks what are the the large challenges and essentially I think you can put them into three big pillars scale performance and operations probably all of them would deserve like a talk on its own so scale scaling with tomorrow's data plane in mind so how can we get to a higher scale opinionated data plane and if I look at psyllium as a standalone Gateway so we we achieve this through ebpf on the xtp layer to a layer for load balancing which has a programmable API it supports Mark left DSR graceful back-end termination and then the new things with the net for six and six four Gateway so that you can build V6 only clusters and then the other side so psyllium inside kubernetes as

### Excerpt da transcript

hello and welcome to my talk uh I'm Daniel Brockman I work on sodium itself and also on the Linux kernel so I co-maintain ebpf in the Linux kernel and today's talk is about 100 gigabit per second clusters with psyllium building tomorrow's networking data plane so when looking at data center networks what are the the large challenges and essentially I think you can put them into three big pillars scale performance and operations probably all of them would deserve like a talk on its own so scale scaling out into many nodes many parts performance making the best use of the resources and operations making changes to your clusters frequently without disruptions for example so my question is what if IPv6 could address both scale and performance requirements from those three pillars so that's what I'm going to elaborate in this talk uh before going and looking into more into the future I actually want to take a step back and look into 2016 because then we actually first announced the psyllium experiment you know we started out with IPv6 only container networking uh together with EE BPF and xtp for those of you who don't know what ebpf is it's kernel technology that makes makes the kernel programmable customizable in a safe way so yeah so this is how we started out IPv6 only networking scalable flexible Global addressing it only net um so we try to abstract away from traditional networking models only focusing on on layer 3 and and above and we built all of sodium on top of ebpf for the for maximum efficiency so until you know we were really excited about IPv6 because the way how we can implement the data plane with that until of course reality kicked in and back in 2016 the state of IPv6 and in kubernetes and Docker in particular wasn't quite there yet so yeah if we had to basically go back and Implement ipv4 support upon popular demand which probably a lot of people are are running sodium with um so yeah fast forward 2020 how does the situation look like today uh kubernetes has adopted IPv6 single stack for quite a while and uh dual stack also and the hyperscale has also made progress integrating IPv6 into the environment over most of it rather dual stack so if you look at for example the manage kubernetes offerings AKs eks gke they all offer you know various level of IPv6 support most of them dual stack there's one single stack so but that's already great um in terms of IPv6 like why do you want to why do users want to go there and a lot of times we hear they w
