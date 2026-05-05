---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "101 Track"
themes: ["101 Track"]
speakers: ["Betty Junod", "VMware", "Paul Burt", "HashiCorp"]
sched_url: https://kccncna2021.sched.com/event/lV4H/were-marketers-if-we-can-learn-distributed-systems-+-k8s-so-can-you-betty-junod-vmware-paul-burt-hashicorp
youtube_search_url: https://www.youtube.com/results?search_query=We%27re+Marketers.+If+we+can+Learn+Distributed+Systems+%2B+K8s%2C+so+can+you%21+CNCF+KubeCon+2021
slides: []
status: parsed
---

# We're Marketers. If we can Learn Distributed Systems + K8s, so can you! - Betty Junod, VMware & Paul Burt, HashiCorp

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[101 Track]]
- Temas: [[101 Track]]
- País/cidade: United States / Los Angeles
- Speakers: Betty Junod, VMware, Paul Burt, HashiCorp
- Schedule: https://kccncna2021.sched.com/event/lV4H/were-marketers-if-we-can-learn-distributed-systems-+-k8s-so-can-you-betty-junod-vmware-paul-burt-hashicorp
- Busca YouTube: https://www.youtube.com/results?search_query=We%27re+Marketers.+If+we+can+Learn+Distributed+Systems+%2B+K8s%2C+so+can+you%21+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre We're Marketers. If we can Learn Distributed Systems + K8s, so can you!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV4H/were-marketers-if-we-can-learn-distributed-systems-+-k8s-so-can-you-betty-junod-vmware-paul-burt-hashicorp
- YouTube search: https://www.youtube.com/results?search_query=We%27re+Marketers.+If+we+can+Learn+Distributed+Systems+%2B+K8s%2C+so+can+you%21+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=O3R1_88D5LY
- YouTube title: We're Marketers. If we can Learn Distributed Systems + K8s, so can you! - Betty Junod & Paul Burt
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/were-marketers-if-we-can-learn-distributed-systems-k8s-so-can-you/O3R1_88D5LY.txt
- Transcript chars: 34881
- Keywords: systems, distributed, failure, availability, containers, actually, network, everything, cluster, consistency, leader, docker, majority, networking, itself, compose, trying, interesting

### Resumo baseado na transcript

If we're marketers and if we can learn distributed systems, so can you. I am senior director of multi-cloud solutions at VMware and I'm here with my buddy Paul Burt. And it's not that there's it's someone's at fault for that, but it's a specific mindset that applies to your design. So if you accept that failure is inevitable in any layer of the stack, then what you do is you will design your systems to fundamentally handle that failure. It's not something that started, you know, just recently with you know, in the recent years because of Kubernetes. It's actually a problem that we've been trying to solve for a very long time.

### Excerpt da transcript

Hey everyone, thanks for joining us for our KubeCon session. If we're marketers and if we can learn distributed systems, so can you. My name is Betty Junod. I am senior director of multi-cloud solutions at VMware and I'm here with my buddy Paul Burt. Hi, I work at HashiCorp and I'm a senior PMM there working on open source stuff. Awesome. So we are super excited to talk to you about something that's near and dear to our hearts. Um first off, the slides and the reading list we've got an extensive reading list at the end of this can be found at this link and we'll make these slides available from to this CNCF so you all can download it. So first, let's start with why. Um we're all here because we're interested in Kubernetes, but have we thought about why? Why do we want Why do we want Kubernetes? Because everyone else does. It's there's FOMO, everyone's using it. Um but we really wanted to start with the question of why. Um why do we want Kubernetes? We really are thinking why it's it's why behind why we want distributed systems.

And really distributed systems are all about failure. So fundamentally accepting that systems will fail. Your applications will fail, your server will fail, your network will fail. Anything can fail at any given time. And it's not that there's it's someone's at fault for that, but it's a specific mindset that applies to your design. So if you accept that failure is inevitable in any layer of the stack, then what you do is you will design your systems to fundamentally handle that failure. And handling that means two things. Not only building your system so that it is more resistant to failure so that you can prevent it, but also doing that planning for when failures happen across the environment, how to handle that gracefully. So what will you optimize for in the event of a failure? So failure is inevitable and we know this because we used to live in a world where we deployed thing single app to a single server and we're like this is great now it's running. But we all knew that if that thing went down, the whole thing failed, right?

You can't get to the app anymore. So what do we do What do we do? We said we need more servers. So great, we went from one to three to five or whatever. Now we have a cluster of servers and so we have some fault tolerance built in. Um so that if one of them fails, we can route the traffic to another one. We can write some rules to route the traffic to another machine. And this is not a new problem. It's
