---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Networking + Edge + Telco"
themes: ["Networking", "SRE Reliability"]
speakers: ["Daniel Borkmann", "Isovalent"]
sched_url: https://kccncna2023.sched.com/event/1R2s5/turning-up-performance-to-11-cilium-netkit-devices-and-going-big-with-tcp-daniel-borkmann-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=Turning+up+Performance+to+11%3A+Cilium%2C+NetKit+Devices%2C+and+Going+Big+with+TCP+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Turning up Performance to 11: Cilium, NetKit Devices, and Going Big with TCP - Daniel Borkmann, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Networking + Edge + Telco]]
- Temas: [[Networking]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Daniel Borkmann, Isovalent
- Schedule: https://kccncna2023.sched.com/event/1R2s5/turning-up-performance-to-11-cilium-netkit-devices-and-going-big-with-tcp-daniel-borkmann-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=Turning+up+Performance+to+11%3A+Cilium%2C+NetKit+Devices%2C+and+Going+Big+with+TCP+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Turning up Performance to 11: Cilium, NetKit Devices, and Going Big with TCP.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2s5/turning-up-performance-to-11-cilium-netkit-devices-and-going-big-with-tcp-daniel-borkmann-isovalent
- YouTube search: https://www.youtube.com/results?search_query=Turning+up+Performance+to+11%3A+Cilium%2C+NetKit+Devices%2C+and+Going+Big+with+TCP+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=AVEBcZc0YsQ
- YouTube title: Turning up Performance to 11: Cilium, NetKit Devices, and Going Big with TCP - Daniel Borkmann
- Match score: 0.981
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/turning-up-performance-to-11-cilium-netkit-devices-and-going-big-with/AVEBcZc0YsQ.txt
- Transcript chars: 32788
- Keywords: basically, kernel, device, packet, support, performance, devices, network, called, inside, actually, question, program, better, interesting, routing, header, traffic

### Resumo baseado na transcript

all right hello and welcome to my talk I'm uh Daniel Brookman I work at ISO veent I work on itself and ebpf in the Linux kernel I co maintain it there and have been cont contributing for a very long time um today the talk is about turning Up Performance to1 um I will talk about cium a new weef um device replacement uh that we built and yeah and going back with TCP so really the goal or experiment I had for this talk was basically I mean

### Excerpt da transcript

all right hello and welcome to my talk I'm uh Daniel Brookman I work at ISO veent I work on itself and ebpf in the Linux kernel I co maintain it there and have been cont contributing for a very long time um today the talk is about turning Up Performance to1 um I will talk about cium a new weef um device replacement uh that we built and yeah and going back with TCP so really the goal or experiment I had for this talk was basically I mean wouldn't it be nice to just turn on the volume knob and improve your performance unfortunately it's not always that nice but uh or always that easy um but the question was really like what would it take to really get to maximum performance and yeah first the question of why why is it relevant in the first place so the use use cases you might have might differ so for example one could be scale you're adding more workloads to your kubernetes environments you're adding you're connecting multiple clusters in a mesh and therefore also the the traffic uh that is being pushed around increases maybe maybe sustainability to better make use of your existing infrastructure or to reduce off for on Prem costs or performance uh performance-wise to reduce the RPC workload latencies or to better cope with potentially escalating bulk data demands that you have maybe from AI or machine learning workloads uh actually for the latter there's quite a big push in the industry right now uh we see new Nicks coming up with 800 gabit and Beyond um you know like a big uh hype around a Ai and and and machine learning to push uh data center Innovations uh the hyperscalers are uh you know increasing their capacity and we even see switches coming up to the market with 50 1.2 terabit per second which is really crazy um so the question here coming back to the kubernetes world is uh how would such a platform look like that would potentially be able to address those future demands and and the more practical question uh is how like what can we benefit from it today and especially without having to rewrite existing applications of course if you look at the standard kubernetes architecture or um setup so you have your host there's a CET running Cube proxy running and if you deploy celum as a cni for example there's a cium agent uh like the the demon itself and a cni plugin so whenever there's a new pod that is being spawned up it will basically give a handle of the network namespace of the part to the cni plugin the cni plugin will talk through RPC to the agent
