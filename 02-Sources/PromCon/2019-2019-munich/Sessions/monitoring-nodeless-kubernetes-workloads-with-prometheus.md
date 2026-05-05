---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2019"
edition_id: 2019-munich
year: 2019
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Kubernetes", "Cost Optimization"]
speakers: []
source_url: https://promcon.io/2019-munich/talks/monitoring-nodeless-kubernetes-workloads-with-prometheus/
youtube_url: https://www.youtube.com/watch?v=JcVOuCBRN8s
youtube_search_url: https://www.youtube.com/results?search_query=Monitoring+Nodeless+Kubernetes+Workloads+with+Prometheus+PromCon+2019
video_match_score: 1.005
status: video-found
---

# Monitoring Nodeless Kubernetes Workloads with Prometheus

## Identificação

- Edição: PromCon EU 2019
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Kubernetes]], [[Cost Optimization]]
- Speakers: N/A
- Página oficial: https://promcon.io/2019-munich/talks/monitoring-nodeless-kubernetes-workloads-with-prometheus/
- YouTube: https://www.youtube.com/watch?v=JcVOuCBRN8s

## Resumo

Speaker: Madhuri Yechuri Emerging Nodeless Kubernetes solutions like virtual-kubelet and Kiyot simplify public cloud k8s node management, save cost, and improve multi-tenant security. This talk explores how Prometheus can be used to monitor Nodeless Kubernetes workloads on public cloud. Demo included.

## Abstract oficial

Speaker: Madhuri Yechuri

Emerging Nodeless Kubernetes solutions like virtual-kubelet and Kiyot simplify public cloud k8s node management, save cost, and improve multi-tenant security. This talk explores how Prometheus can be used to monitor Nodeless Kubernetes workloads on public cloud. Demo included.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2019-munich/talks/monitoring-nodeless-kubernetes-workloads-with-prometheus/
- YouTube: https://www.youtube.com/watch?v=JcVOuCBRN8s
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=JcVOuCBRN8s
- YouTube title: PromCon EU 2019: Monitoring Nodeless Kubernetes Workloads with Prometheus
- Match score: 1.005
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2019/monitoring-nodeless-kubernetes-workloads-with-prometheus/JcVOuCBRN8s.txt
- Transcript chars: 13639
- Keywords: worker, compute, running, capacity, prometheus, virtual, launch, control, applications, cluster, provision, single, deployment, public, notice, matrix, itself, monitoring

### Resumo baseado na transcript

[Music] and everybody my name is Madhuri I am the founder makers of nodelist kubernetes prior to that I've been a systems engineer for 20 years worked on Flocka which some of you might remember from the early container ecosystem days where we helped run stateful applications inside containers and prior to that worked on resource management for the investig-- on initial placement load balancing of virtual machines you know VMware truster and also VMware hypervisor product prior to that worked on oracle database server technologies in cluster way software

### Excerpt da transcript

[Music] and everybody my name is Madhuri I am the founder makers of nodelist kubernetes prior to that I've been a systems engineer for 20 years worked on Flocka which some of you might remember from the early container ecosystem days where we helped run stateful applications inside containers and prior to that worked on resource management for the investig-- on initial placement load balancing of virtual machines you know VMware truster and also VMware hypervisor product prior to that worked on oracle database server technologies in cluster way software so mostly systems and distributed systems engineering how many of you use kubernetes currently with prometheus Wow kubernetes capacity planning on public cloud is super hard when you take a regular kubernetes cluster instead of focusing on your applications your pods your resource manifests you as the DevOps and asari folks spend a lot of time on hand curating the worker nodes you have to select the base worker node type and what price point of the worker node you want to select whether it's on demand pre-emptive spot or forget kind of of compute launch types and also you have to hand curate the auto scaling knobs and maintain monitor and update the auto scaling knobs based on your applications workload changes and also when a worker node dies it is a pet worker node so you have to someone has to be on on-call rotation to make sure that the the compute capacity is still enough to run your worker nodes the compute capacity on public cloud is ephemeral and it doesn't have the same static sticky qualities of server blades on on-premise data centers so why are we continuing to to manage and provision compute on public cloud as if we owned the machines is sitting in a private datacenter so with the over-provision the compute capacity nodes we are wasting resources we are wasting money if we under provision the parts will be in pending state and won't have the compute node available when it wants to run and unexpected spikes during rolling up upgrades and horizontal part of scaling will be very lazy to react no less kubernetes is flavor of kubernetes which basically makes sure that you consume public cloud capacity as and when it is needed for your kubernetes clusters and focus on your kubernetes applications instead of focusing on managing the operational complexity of your kubernetes cluster worker nodes so what noodle s communities does is that the control plane looks down and sees a worker node which advertis
