---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["Bowei Du", "Tim Hockin", "Google"]
sched_url: https://kccnceu2021.sched.com/event/iE8K/sig-network-updates-and-future-directions-bowei-du-tim-hockin-google
youtube_search_url: https://www.youtube.com/results?search_query=SIG-network%3A+Updates+and+Future+Directions+CNCF+KubeCon+2021
slides: []
status: parsed
---

# SIG-network: Updates and Future Directions - Bowei Du & Tim Hockin, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Bowei Du, Tim Hockin, Google
- Schedule: https://kccnceu2021.sched.com/event/iE8K/sig-network-updates-and-future-directions-bowei-du-tim-hockin-google
- Busca YouTube: https://www.youtube.com/results?search_query=SIG-network%3A+Updates+and+Future+Directions+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre SIG-network: Updates and Future Directions.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE8K/sig-network-updates-and-future-directions-bowei-du-tim-hockin-google
- YouTube search: https://www.youtube.com/results?search_query=SIG-network%3A+Updates+and+Future+Directions+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Nn-qrp0TRnM
- YouTube title: SIG-network: Updates and Future Directions - Bowei Du & Tim Hockin, Google
- Match score: 0.832
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/sig-network-updates-and-future-directions/Nn-qrp0TRnM.txt
- Transcript chars: 15910
- Keywords: network, cluster, endpoint, policy, traffic, support, balancer, policies, gateway, topology, single, actually, feature, external, slices, networking, finally, protocol

### Resumo baseado na transcript

welcome to the sig network deep dive this has been a collaborative set of slides from the members of the kubernetes sig network community including myself franz j ricardo rob emmanuel so what is the area that is covered by sig network well it touches on all of the networking aspects of the kubernetes ecosystem this includes pod networking within in between nodes including interfaces such as cni and ipam cluster networking in and out of the cluster network service abstractions such as load balancing of l4 l7 and service so big and therefore scaling was difficult with this new feature this becomes finally easy again endpoint slices support ipv4 ipv6 and fqdns finally there is an important security related update around the service external ips feature use of the service external ips feature allows users to specify an ip directly as a way to integrate with manually configured external load balancers unfortunately it is impossible for kubernetes to determine whether or not the ip specified actually belongs to the user or is an internet ip that they might be

### Excerpt da transcript

welcome to the sig network deep dive this has been a collaborative set of slides from the members of the kubernetes sig network community including myself franz j ricardo rob emmanuel so what is the area that is covered by sig network well it touches on all of the networking aspects of the kubernetes ecosystem this includes pod networking within in between nodes including interfaces such as cni and ipam cluster networking in and out of the cluster network service abstractions such as load balancing of l4 l7 and service discovery so using systems such as dns network policies i.e security and access control basically how you secure your pods and workloads and of course the apis associated with these functions and these apis include pod node endpoint endpoint slice service ingress gateway and network policy for those of you who are interested we have a well-attended zoom meeting every other thursday and a busy slack channel and don't worry we will put this information back up at the end of this presentation as we only have a 35-minute slot and there are many excellent intro videos here are some previous intros and deep dives the links shown here we would like to take our 20 minutes to give an update about exciting things that have been happening in the sig things that have landed things that the sig is actively working on and future directions okay so what has been happening in the sig there are many smaller improvements features that people have requested and apis have gone ga that have been covered in detail before such as endpoint slice and also there are a couple of big items dual stack which is support for ipv4 in ipv6 gateway api which is the next iteration of l4 l7 service apis rethinking how to support network topology in network routing and finally network policy working group which has already landed some features and are looking as well at a potential version two of the api let's talk about some of the improvements to kubernetes networking that have landed first we have loosened the restriction that a service type load balancer can only support a single protocol this is the multi-protocol services cap and the link is there in the slide basically before this improvement you could only have a single protocol service as part of your load balancer definition with the new changes you can actually have multiple protocols supported as part of your load balancer service for example in this case you see a mixed protocol service that actually uses both udp a
