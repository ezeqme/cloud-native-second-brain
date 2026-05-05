---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Cloud Native Novice"
themes: ["Networking", "Kubernetes Core"]
speakers: ["Simone Rodigari", "Microsoft"]
sched_url: https://kccnceu2026.sched.com/event/2CW0A/demystifying-the-kubernetes-network-stack-from-pod-to-pod-simone-rodigari-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Demystifying+the+Kubernetes+Network+Stack+%28From+Pod+to+Pod%29+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Demystifying the Kubernetes Network Stack (From Pod to Pod) - Simone Rodigari, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Simone Rodigari, Microsoft
- Schedule: https://kccnceu2026.sched.com/event/2CW0A/demystifying-the-kubernetes-network-stack-from-pod-to-pod-simone-rodigari-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Demystifying+the+Kubernetes+Network+Stack+%28From+Pod+to+Pod%29+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Demystifying the Kubernetes Network Stack (From Pod to Pod).

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW0A/demystifying-the-kubernetes-network-stack-from-pod-to-pod-simone-rodigari-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Demystifying+the+Kubernetes+Network+Stack+%28From+Pod+to+Pod%29+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=fj5UQ0WBmAg
- YouTube title: Demystifying the Kubernetes Network Stack (From Pod to Pod) - Simone Rodigari, Microsoft
- Match score: 0.894
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/demystifying-the-kubernetes-network-stack-from-pod-to-pod/fj5UQ0WBmAg.txt
- Transcript chars: 18078
- Keywords: address, network, packet, cluster, destination, namespace, interface, provide, tables, communicate, source, networking, packets, virtual, inspect, balancing, container, capture

### Resumo baseado na transcript

My name is Simone Rodigari and I work as software engineer at Microsoft. Focusing particularly on pod-to-pod communication within a cluster and looking at packets. And generally speaking, those are the expectations that Kubernetes has in terms of networking. So, how is the pod networking configured if Kubernetes is not responsible for it? We know that in Kubernetes, if a pod is restarted the IP address could change. To solve this problem, Kubernetes is providing us with a resource called services which gives us a virtual IP called cluster IP and provides load balancing across ready pods.

### Excerpt da transcript

Good afternoon, everyone. Thank you for joining today. My name is Simone Rodigari and I work as software engineer at Microsoft. And today we'll be talking about Kubernetes networking. Focusing particularly on pod-to-pod communication within a cluster and looking at packets. Kubernetes networking can be invisible. We have a set of resources defined in a in a YAML file. We apply those resources. We can see pods are running. Services exist. Services provide load balancing between backing pods. So, everything seems to work. But what is really happening at the packet level? Clearly, there is a gap if we don't understand the packet path. And this presents a very big risk when something networking related breaks. Because, of course, troubleshooting would be very painful and not time efficient. The goal for the session today is to provide a mental model on how to trace packets in a Kubernetes cluster. We will focus in in-cluster communication from pod-to-pod. Today I will cover six different concepts starting from the pod itself.

The concept of Linux network namespaces and the importance for pods. The role of veth, virtual Ethernets. I'll move on to the connection between pod and node as well as touching base on the node data path. I will also discuss how pod can communicate to other pods cross node. Cover the role of Kubernetes services in providing DNAT and load balancing. And also briefly mention how DNS can make our life a little bit easier by mapping names to IP addresses. Finally, I will provide a debug approach that can be useful in a troubleshooting scenario. To start off, we need to provide some ground rules. And generally speaking, those are the expectations that Kubernetes has in terms of networking. Kubernetes is not responsible for the networking setup in full. Some of the ground rules include pods should have a unique IP address. There should be no network address translation between pods when pods are communicating to each other. And we should operate on a flat layer three network so that any pod can communicate to any other pods whether they are they are on the same node or across different nodes.

So, how is the pod networking configured if Kubernetes is not responsible for it? The process starts when the scheduler defines that the pod needs to run on a specific node. The kubelet on the chosen node will use the container runtime to create the sandbox for the pod. The container runtime is responsible for creating the Linux network namespace which
