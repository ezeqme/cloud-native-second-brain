---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Operations + Performance"
themes: ["Storage Data", "SRE Reliability"]
speakers: ["Jef Spaleta", "Isovalent at Cisco"]
sched_url: https://kccncna2024.sched.com/event/1i7r8/the-key-value-of-etcd-over-custom-resources-scalability-jef-spaleta-isovalent-at-cisco
youtube_search_url: https://www.youtube.com/results?search_query=The+Key+Value+of+etcd+Over+Custom+Resources%3A+Scalability+CNCF+KubeCon+2024
slides: []
status: parsed
---

# The Key Value of etcd Over Custom Resources: Scalability - Jef Spaleta, Isovalent at Cisco

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Storage Data]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Jef Spaleta, Isovalent at Cisco
- Schedule: https://kccncna2024.sched.com/event/1i7r8/the-key-value-of-etcd-over-custom-resources-scalability-jef-spaleta-isovalent-at-cisco
- Busca YouTube: https://www.youtube.com/results?search_query=The+Key+Value+of+etcd+Over+Custom+Resources%3A+Scalability+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre The Key Value of etcd Over Custom Resources: Scalability.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7r8/the-key-value-of-etcd-over-custom-resources-scalability-jef-spaleta-isovalent-at-cisco
- YouTube search: https://www.youtube.com/results?search_query=The+Key+Value+of+etcd+Over+Custom+Resources%3A+Scalability+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=H3NYupSNMnA
- YouTube title: The Key Value of etcd Over Custom Resources: Scalability - Jef Spaleta, Isovalent at Cisco
- Match score: 0.86
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/the-key-value-of-etcd-over-custom-resources-scalability/H3NYupSNMnA.txt
- Transcript chars: 31551
- Keywords: cilium, cluster, server, actually, scalability, clusters, across, inside, watchers, resources, ebpf, mesh, testing, access, talking, custom, projects, critical

### Resumo baseado na transcript

You know, I want to give the extra minute for the people to find the room. But Like I was saying, thanks everyone for finding this meeting room now that they shut down the gates from the exhibit hall. Um so, Cilium is an eBPF-powered connectivity, observability, and security platform for Kubernetes clusters. Like I said, I'm not going to go into the details of eBPF, but eBPF is a basically makes your kernel the Linux kernel programmable and Cilium takes advantage of that to do enhanced networking performance inside your Kubernetes nodes, right? So, the other project that's the key player in the story is the actual Kubernetes API server, right? It we all interact with this when we are maintaining or customizing our Kubernetes clusters.

### Excerpt da transcript

Hey, everybody. We are live. I'll start I'll start on time in a minute. You know, I want to give the extra minute for the people to find the room. But Like I was saying, thanks everyone for finding this meeting room now that they shut down the gates from the exhibit hall. Um It's an adventure getting here. So, here we go. We're starting. Um Welcome to my talk. My name is Jess Balleta. I'm actually a technical community advocate at Isovalent, now Cisco. And I'm here to talk to you. I'm going to read the title. The key value of etcd over custom resources, scalability for now. So, why am I talking about scalability? I am not a practitioner. I do not run Kubernetes clusters. I'm not a maintainer for any of the projects I'm going to talk about. I am associated with Cilium um um as a technical advocate. And so, that means I am concerned about making sure end users and the project are aligning, right? And I am talking about this because there is an opportunity for practitioners, people with technical expertise running clusters, to help all the CNCF projects tackle the issue of scalability by providing testing.

And I'm going to use Cilium as an example of what I'm talking about. This is a Cilium uh state scalability story. I'm not talking about eBPF or the superpower that it is to provide performance inside your nodes. I'm talking about how you how the state of Cilium state impacts scalability um inside a cluster and across multiple clusters. So, this is mostly for the people watching the video and not for everyone here. This is the cast of characters. These are the things I'll be mentioning that impact the scalability story for Cilium and probably much of it will impact other projects. Um so, Cilium is an eBPF-powered connectivity, observability, and security platform for Kubernetes clusters. Like I said, I'm not going to go into the details of eBPF, but eBPF is a basically makes your kernel the Linux kernel programmable and Cilium takes advantage of that to do enhanced networking performance inside your Kubernetes nodes, right? So, from that you're able to get transparent encryption, advanced load balancing, transparent observability.

All of that stuff falls out of the fact that we are using eBPF underneath and building capabilities on top of it. If you're not familiar with Cilium, it is not a sales pitch, but please check out the project if you're not familiar with it. But I'm talking about it here because that's the project I'm most familiar with and I'm goi
