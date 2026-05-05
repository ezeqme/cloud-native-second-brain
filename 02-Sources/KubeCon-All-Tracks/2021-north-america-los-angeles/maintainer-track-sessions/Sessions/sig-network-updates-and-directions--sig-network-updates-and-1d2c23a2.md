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
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["Tim Hockin", "Bowei Du", "Google"]
sched_url: https://kccncna2021.sched.com/event/lV7K/sig-network-updates-and-directions-tim-hockin-bowei-du-google
youtube_search_url: https://www.youtube.com/results?search_query=SIG-NETWORK%3A+Updates+and+Directions+CNCF+KubeCon+2021
slides: []
status: parsed
---

# SIG-NETWORK: Updates and Directions - Tim Hockin & Bowei Du, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Tim Hockin, Bowei Du, Google
- Schedule: https://kccncna2021.sched.com/event/lV7K/sig-network-updates-and-directions-tim-hockin-bowei-du-google
- Busca YouTube: https://www.youtube.com/results?search_query=SIG-NETWORK%3A+Updates+and+Directions+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre SIG-NETWORK: Updates and Directions.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV7K/sig-network-updates-and-directions-tim-hockin-bowei-du-google
- YouTube search: https://www.youtube.com/results?search_query=SIG-NETWORK%3A+Updates+and+Directions+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=uZ0WLxpmBbY
- YouTube title: SIG-NETWORK: Updates and Directions - Tim Hockin & Bowei Du, Google
- Match score: 0.796
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/sig-network-updates-and-directions/uZ0WLxpmBbY.txt
- Transcript chars: 10242
- Keywords: network, policy, ingress, cluster, namespace, traffic, endpoint, gateway, within, support, second, topology, ranges, routes, resource, looking, policies, couple

### Resumo baseado na transcript

welcome to the sig network update and directions we will be going over major things that have changed in sig network from the last kubecon the sig network special interest group is responsible for kubernetes network components this includes things such as pod networking within and between nodes such as cni and ipam ingress and egress traffic service abstractions this includes service discovery load balancing l4 and l7 network policies and access control which is basically network security within a cluster and all of the apis associated with these functions path length in characters cannot exceed 2048 this is alpha so please try it out and let us know if you had any problems also in alpha is the ability for the node ipm controller to allocate ips from multiple non-contiguous sider ranges this allows what this means is that services and pods now support both ipv4 and ipv6 either in single or dual stack modes there are specific apis designed around migration of existing services between single stack and dual stack within some reasonable limits dual stack is also be enabled without breaking legacy apps dual stack api server endpoints will be published using endpoint slice the client code will be updated to understand dual stack but environment variables such as kubernetes service host will remain the same to avoid breaking existing applications the gateway api has also made...

### Excerpt da transcript

welcome to the sig network update and directions we will be going over major things that have changed in sig network from the last kubecon the sig network special interest group is responsible for kubernetes network components this includes things such as pod networking within and between nodes such as cni and ipam ingress and egress traffic service abstractions this includes service discovery load balancing l4 and l7 network policies and access control which is basically network security within a cluster and all of the apis associated with these functions which includes pod node endpoint and point slice service ingress gateway network policy to name a few we have a zoom meeting every other thursday as well as a very active slack channel in our community page link is shown below if you are new to kubernetes or need a refresher we have covered the basics in previous intro videos at kubecons this presentation will focus mostly on the cool stuff that has been happening in the past few months the sig has been paying special attention to our backlog we would like to make sure that proposals that are in alpha beta make it to ga and stable rather than staying in a half complete state for extended cycles the sig is also focused on a couple of major projects the first one is dual stack support which has landed in ga in 1 23 second project is gateway api for l4 and l7 and third are network policy improvements now let's take a look at some of the proposals and updates that have happened since 121 a couple of smaller improvements have graduated to stable disable lp node ports is now ga which lets the user avoid allocating node ports when creating a type load balancer service this is ga in 123.

ingress class can now reference a parameter object that is namespace scoped let's take care of some of the common use cases for in-cluster proxy deployments and self-service ingress deployments the new topology aware routing feature is now beta and along with this is a deprecation of the old topology keys based api the new topology hints is more flexible than the previous iteration and allows for implementations to have more leeway in determining traffic routing when the user specifies that they want their traffic to be topology aware the key thing here is to note that the topology keys field is now completely deprecated and renamed dns config now lets you specify more than five entries matching the behavior of modern libsy implementations the new limits are 32 search path elem
