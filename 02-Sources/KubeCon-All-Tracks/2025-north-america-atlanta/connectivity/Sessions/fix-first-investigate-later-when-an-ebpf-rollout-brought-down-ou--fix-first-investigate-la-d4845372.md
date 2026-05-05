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
themes: ["AI ML", "Networking"]
speakers: ["Zain Malik", "Exostellar", "Grzegorz Głąb", "Whatnot"]
sched_url: https://kccncna2025.sched.com/event/27FV7/fix-first-investigate-later-when-an-ebpf-rollout-brought-down-our-network-zain-malik-exostellar-grzegorz-glab-whatnot
youtube_search_url: https://www.youtube.com/results?search_query=Fix+First%2C+Investigate+Later%3A+When+an+eBPF+Rollout+Brought+Down+Our+Network+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Fix First, Investigate Later: When an eBPF Rollout Brought Down Our Network - Zain Malik, Exostellar & Grzegorz Głąb, Whatnot

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Connectivity]]
- Temas: [[AI ML]], [[Networking]]
- País/cidade: United States / Atlanta
- Speakers: Zain Malik, Exostellar, Grzegorz Głąb, Whatnot
- Schedule: https://kccncna2025.sched.com/event/27FV7/fix-first-investigate-later-when-an-ebpf-rollout-brought-down-our-network-zain-malik-exostellar-grzegorz-glab-whatnot
- Busca YouTube: https://www.youtube.com/results?search_query=Fix+First%2C+Investigate+Later%3A+When+an+eBPF+Rollout+Brought+Down+Our+Network+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Fix First, Investigate Later: When an eBPF Rollout Brought Down Our Network.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FV7/fix-first-investigate-later-when-an-ebpf-rollout-brought-down-our-network-zain-malik-exostellar-grzegorz-glab-whatnot
- YouTube search: https://www.youtube.com/results?search_query=Fix+First%2C+Investigate+Later%3A+When+an+eBPF+Rollout+Brought+Down+Our+Network+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=J-Zx64mJzVk
- YouTube title: Fix First, Investigate Later: When an eBPF Rollout Brought Down Our... Zain Malik & Grzegorz Głąb
- Match score: 0.944
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/fix-first-investigate-later-when-an-ebpf-rollout-brought-down-our-netw/J-Zx64mJzVk.txt
- Transcript chars: 27356
- Keywords: actually, retina, network, outage, workload, cluster, buffer, course, performance, kernel, context, happening, observability, configuration, disable, packet, ebpf, question

### Resumo baseado na transcript

How many of you uh it was caused by something in your cloud provider infrastructure? We would like to walk you through how one incident hit us hard and more importantly how we deal with that. update Kubernetes control plane and when we upgrade control plane as all of you may know we follow the procedure we check What happens? The other team was actually doing mitigation on their side and our plate was to investigate this network degradation and of course the first thing which we tried to do is to delete this demon set. When you look at retina demon set, you know that demon set selects the the nodes on which the ports uh needs to be scheduled and retina in this case was using match expression uh term which consists of several conditions. So in the result we have a demon set which doesn't span any ports on any nodes because nothing matches.

### Excerpt da transcript

Okay, I believe we can start. Welcome to our talk uh fix first investigate later. How an EBPF rollout brought out our network. First question is for you. How many of you were affected by uh production outage last year? Please raise your hands. Okay, great. Now, second question. How many of you uh it was caused by something in your cloud provider infrastructure? Just raise your hands. Okay, thank you. In in how many cases it took longer than 30 minutes to be mitigated? Okay. Longer sorry longer than 1 hour. Okay. Longer than few hours. Okay. Longer than one day. Okay. I believe that we are in good company. We would like to walk you through how one incident hit us hard and more importantly how we deal with that. So my name is Bish Gu. Um I am a cloud engineer and whatn not working mainly with cloud infrastructure and reliability >> and I'm Zan Malik working at accessor as a principal software engineer >> but our story started at cloud kitchens where we both uh were uh part of the core infrastructure team. >> Yeah.

Okay. Uh so at cloud kitchens we are part of small infrastructure team having like six people and we are managing a large scale cubernetes clusters. So you know thousands of nodes, ten of thousands of pots and supporting the whole company infrastructure. But first let me take a walk through like what we are going to be covering today. We covering through like some small cube kernel commands get diamond sets. Then we'll go through like some mutation web hooks, how to write them, CPU sets and go into the details of EBPF kernel to user space uh data transfer. Now you might be asking like why all of this technical like deep dive just for an outage and that's a good valid question to take you to more of that context. It's like over the years we learn how to operate that way. Usually when the outage happened in our case it was like a okay issue. So usually when we are having an issues like uh it would pose a risk to the business continuity and when that's happening it things try to escalate pretty quickly and our team naturally becomes the last line between the support between cloud providers and the whole arc.

Now the support ars do their best job sometime they can reproduce the issue and they will call it like how to which workload introduce that introduce it but on the other hand we have to play on the both sides. We have to find issues in the cloud provider infrastructure but we also have to find issues in the workload that the users are running in
