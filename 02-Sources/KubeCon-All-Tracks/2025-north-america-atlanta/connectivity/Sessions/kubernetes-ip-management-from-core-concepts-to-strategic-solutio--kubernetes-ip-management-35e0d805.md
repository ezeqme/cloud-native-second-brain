---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Connectivity"
themes: ["Kubernetes Core"]
speakers: ["Ivy Zhuang", "Whitney Jenkins", "Google"]
sched_url: https://kccncna2025.sched.com/event/27FW8/kubernetes-ip-management-from-core-concepts-to-strategic-solutions-ivy-zhuang-whitney-jenkins-google
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+IP+Management%3A+From+Core+Concepts+To+Strategic+Solutions+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Kubernetes IP Management: From Core Concepts To Strategic Solutions - Ivy Zhuang & Whitney Jenkins, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Connectivity]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Ivy Zhuang, Whitney Jenkins, Google
- Schedule: https://kccncna2025.sched.com/event/27FW8/kubernetes-ip-management-from-core-concepts-to-strategic-solutions-ivy-zhuang-whitney-jenkins-google
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+IP+Management%3A+From+Core+Concepts+To+Strategic+Solutions+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Kubernetes IP Management: From Core Concepts To Strategic Solutions.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FW8/kubernetes-ip-management-from-core-concepts-to-strategic-solutions-ivy-zhuang-whitney-jenkins-google
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+IP+Management%3A+From+Core+Concepts+To+Strategic+Solutions+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=EXxa7Qxdveg
- YouTube title: Kubernetes IP Management: From Core Concepts To Strategic Solutions - Ivy Zhuang & Whitney Jenkins
- Match score: 0.91
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/kubernetes-ip-management-from-core-concepts-to-strategic-solutions/EXxa7Qxdveg.txt
- Transcript chars: 23896
- Keywords: cluster, ranges, network, feature, addresses, additional, subnet, features, address, clusters, little, observability, perspective, support, exhaustion, actually, within, utilization

### Resumo baseado na transcript

Hi, my name is Whitney Jenkins and I am a product manager at Google working on GKE IPAM and this is my colleague Ivy. >> And today we are going to talk about Kubernetes IP management and talk about some of the core concepts and strategic solutions. This is a big deal because it um is um high performance, is more secure, it has built-in securities and better observability. So we talked a lot about the core kind of Kubernetes concepts, but I kind of hinted at a little bit. Um, in addition, there are a few features that Ivy will be talking about later that will allow you to add additional ranges to existing clusters with that additional range being one of these to give you more scale. Um, and then if you have any like kind of advanced configurations with load balancing or interested in external internal destinations, there are ways that you can also leverage this range to make your um custom architecture work for you.

### Excerpt da transcript

Hi, my name is Whitney Jenkins and I am a product manager at Google working on GKE IPAM and this is my colleague Ivy. >> Hello everyone, my name is Ivy. I am a software engineer from Google and then I mainly work on GKIPAM. >> And today we are going to talk about Kubernetes IP management and talk about some of the core concepts and strategic solutions. Uhoh. It's okay. Um, so let's dive into some of the core Kubernetes concepts. So in GKE, we have a flat network that is fully integrated. What this means is that every pod receives a unique routable IP that is part of the VPC's IP range. There is direct native integration with GCP services like load balancing, service mesh, VPC peering and shared VPC. Pod IP addresses are visible throughout the network. So this is really important for observability. Uh this enhances telemetry and simplifies debugging. Um pod IP address ranges can be made accessible for onrem through GCP tools like cloudVPN or cloud interconnect. Kubernetes has a flat network model but uh Kubernetes itself does not handle this uh for the implementation details.

Instead it delegates the entire responsibility to a set of plugins. So CN CNI is a CNCF project that creates a simple pluggable interface between container runtime and the network plugins. So this diagram shows the workflow when a pod is scheduling and when CNI comes into play. So at first the kubalot will decide to start a pod. Then it'll cause the container runtime to um create a pause sandbox. The runtime then will look at the CNI plugins file at -etci-net.d file. It will execute the specific CNI plugins and execute the add command that is defined in the interface. The CNI will does all the work including create the network interface and assign the IPs or manage the routes. After that the pod is now live and then it will be able to uh communicate. It is on the network. GK's default networking mode is VPC and it is standard. Uh the pod will get a real IP address from the secondary ranges from the uh cloud the uh cloud VPC. Um GK is use a standard C9 plugin where it merely it is something called local um host that it merely just look at the preconfigured ranges.

It assigns the port IP ranges every time it needs one. But this um plug-in is able to actually u redefine your own logics and for example talk to your cloud container, your own cloud APIs to decide which IPs to allocate to the pod. Uh for the DPV2, GKE um uses a psyllium or eBPF for its CNI um plugin. This is a big deal beca
