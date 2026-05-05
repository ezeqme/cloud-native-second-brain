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
themes: ["Networking", "Kubernetes Core", "SRE Reliability"]
speakers: ["Marcel Zięba", "Isovalent", "Dorde Lapcevic", "Google"]
sched_url: https://kccncna2023.sched.com/event/1R2vB/scaling-kubernetes-networking-to-1k-5k-100k-nodes-marcel-zieba-isovalent-dorde-lapcevic-google
youtube_search_url: https://www.youtube.com/results?search_query=Scaling+Kubernetes+Networking+to+1k%2C+5k%2C+...+100k+Nodes%21%3F+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Scaling Kubernetes Networking to 1k, 5k, ... 100k Nodes!? - Marcel Zięba, Isovalent & Dorde Lapcevic, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Networking]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Marcel Zięba, Isovalent, Dorde Lapcevic, Google
- Schedule: https://kccncna2023.sched.com/event/1R2vB/scaling-kubernetes-networking-to-1k-5k-100k-nodes-marcel-zieba-isovalent-dorde-lapcevic-google
- Busca YouTube: https://www.youtube.com/results?search_query=Scaling+Kubernetes+Networking+to+1k%2C+5k%2C+...+100k+Nodes%21%3F+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Scaling Kubernetes Networking to 1k, 5k, ... 100k Nodes!?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2vB/scaling-kubernetes-networking-to-1k-5k-100k-nodes-marcel-zieba-isovalent-dorde-lapcevic-google
- YouTube search: https://www.youtube.com/results?search_query=Scaling+Kubernetes+Networking+to+1k%2C+5k%2C+...+100k+Nodes%21%3F+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=VWGB-NW800Y
- YouTube title: Scaling Kubernetes Networking to 1k, 5k, ... 100k Nodes!? - Marcel Zięba & Dorde Lapcevic
- Match score: 0.858
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/scaling-kubernetes-networking-to-1k-5k-100k-nodes/VWGB-NW800Y.txt
- Transcript chars: 28414
- Keywords: cluster, network, celium, clusters, identity, identities, mesh, policies, security, policy, question, second, number, points, ebpf, actually, propagation, interested

### Resumo baseado na transcript

hello everyone um super excited to see all of you interested in scalability so we will be talking about scaling kubernetes networking 2,000 5,000 and 100,000 nodes I'm marel Jumba I'm I work at isovalent and together with me we have d leich uh from Google so let's start with celum what is celum probably most of you heard about celium and most popular is cium cni which is secure scalable cni plugin that you can use for kubernetes um but then except for cni we also do have hble

### Excerpt da transcript

hello everyone um super excited to see all of you interested in scalability so we will be talking about scaling kubernetes networking 2,000 5,000 and 100,000 nodes I'm marel Jumba I'm I work at isovalent and together with me we have d leich uh from Google so let's start with celum what is celum probably most of you heard about celium and most popular is cium cni which is secure scalable cni plugin that you can use for kubernetes um but then except for cni we also do have hble in case you are interested in uh Network observability and last but not least tetragon so tetragon allows you to um to to basically secure your container runtime with policies similar to network policies and what all these projects have in common is that they use utilize ebpf so short introduction into ebpf um you can think of it as you can write small program that can be attached to different events within uh Linux kernel and what you can do with it is for example if you are interested in observability you can export some of the information from the kernel to ebpf map and then from user space you can access that data but it also works the other way around let's say that you want to implement um Service uh load balancing in kubernetes what you can do is actually take service take all the backends that are behind the service write those IPS into ebpf map and then have the ebpf program translate cluster IP into one of the backends and it's one of the most important parts of ebpf it's that it's way more efficient than other Alternatives so we'll be focusing today mostly on cium cni short summary what celum cni is um first of all efficient scalable kubernetes cni that also provides security kubernetes network policies but also more advanced cium Network policies um as mentioned before service load balancing so if you are um interested in Cube proxy replacement you can use cium to do the service load balancing instead of Cu proxy and last but not least which we'll be covering later on as well well is multicluster if you are interested in running multiple clusters and connectivity between different clusters then you can utilize as well um but let's start with even understanding what does the scalability even mean so our title mentions 100,000 nodes right but the scalability is not just the number of nodes it's way more than that so when we are thinking about scalability of kubernetes there are so many more dimensions that we care about noes is just one dimension that we care about but also
