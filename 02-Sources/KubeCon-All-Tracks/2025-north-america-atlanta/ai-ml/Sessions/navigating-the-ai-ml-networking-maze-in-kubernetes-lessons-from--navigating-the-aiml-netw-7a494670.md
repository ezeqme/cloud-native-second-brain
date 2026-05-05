---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "AI + ML"
themes: ["AI ML", "Networking", "Kubernetes Core"]
speakers: ["Antonio Ojea", "Google"]
sched_url: https://kccncna2025.sched.com/event/27FZW/navigating-the-aiml-networking-maze-in-kubernetes-lessons-from-the-trenches-antonio-ojea-google
youtube_search_url: https://www.youtube.com/results?search_query=Navigating+the+AI%2FML+Networking+Maze+in+Kubernetes%3A+Lessons+From+the+Trenches+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Navigating the AI/ML Networking Maze in Kubernetes: Lessons From the Trenches - Antonio Ojea, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Networking]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Antonio Ojea, Google
- Schedule: https://kccncna2025.sched.com/event/27FZW/navigating-the-aiml-networking-maze-in-kubernetes-lessons-from-the-trenches-antonio-ojea-google
- Busca YouTube: https://www.youtube.com/results?search_query=Navigating+the+AI%2FML+Networking+Maze+in+Kubernetes%3A+Lessons+From+the+Trenches+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Navigating the AI/ML Networking Maze in Kubernetes: Lessons From the Trenches.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FZW/navigating-the-aiml-networking-maze-in-kubernetes-lessons-from-the-trenches-antonio-ojea-google
- YouTube search: https://www.youtube.com/results?search_query=Navigating+the+AI%2FML+Networking+Maze+in+Kubernetes%3A+Lessons+From+the+Trenches+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=liHY_dy-W0w
- YouTube title: Navigating the AI/ML Networking Maze in Kubernetes: Lessons From the Trenches - Antonio Ojea, Google
- Match score: 0.964
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/navigating-the-ai-ml-networking-maze-in-kubernetes-lessons-from-the-tr/liHY_dy-W0w.txt
- Transcript chars: 20965
- Keywords: network, workloads, device, gpu, networking, another, basically, records, better, driver, plugins, create, talking, communicate, headless, performance, topology, multiple

### Resumo baseado na transcript

I mean you can work on Kubernetes on a IML on whatever thing and you cannot switch uh extended display. Let's get the thing going and let me try to tell you a a tale here an adventure that an adventure where that I had to go through in Kubernetes. >> [snorts] >> Then we have another projects that are implementing kubernetes networking right most of you use sirion or calico these days they use ebpf magic or nf tables spells to create services ingresses network policies and all these kind of things and we We you all can have 200 horror histories about Kubernetes networking but so far it was good enough right we were improving one thing at a time but one day this is a real character Vanessa Vanessa works in limor lab she open an isue in in Kubernetes she was saying oh I ran all this red park and they are not working well and because we are a community and somebody was working in NPI operator and okay it is they are saying there a network problem let's call Antonio and I started to to work with Vanessa on the problem the first thing is that I don't know what you're talking me about I mean you are telling me that this is the network but I don't know what you're what's the network

### Excerpt da transcript

Hello. Okay, sorry for being late. I mean you can work on Kubernetes on a IML on whatever thing and you cannot switch uh extended display. So apologies. So let's start. Let's get the thing going and let me try to tell you a a tale here an adventure that an adventure where that I had to go through in Kubernetes. Once upon a time like all the history start in the great kingdom of Kubernetes a new and terrifying maze appear. So my name is Antonio and as I say I'm going to try to go through this maze during the next minutes. Okay just to clarify this is real. This is not something that I'm putting a twist of adventure here but this you can follow all these things in the GitHub issues pull request and so so let me introduce myself I'm I'm not a knight I I work at Google I work in SIG network and I don't cast the spells or do all these magical runes of connectivity. I just try to make Kubernetes networking better for all of you. Okay, better means it is the less that you have to know of of Kubernet networking the better the most performant that it is without you having to tune anything the better.

So that's our work in Sign Network. Okay. So, but it's it's not that I work alone, right? There are other knights like Sir Tim or Sir Danquin or princess warriors like Sergia and and Nadia. And we have another friends too, right? We have the people in the networking pling group. They develop this multus that most of you know, right? You can attach multiple network interfaces. They also have a lot of uh other projects that use device plugins to attach RDMA n and all all these kind of things. >> [snorts] >> Then we have another projects that are implementing kubernetes networking right most of you use sirion or calico these days they use ebpf magic or nf tables spells to create services ingresses network policies and all these kind of things and we have another groups within sin network that are working in in developing new space right the gateway API people. This is people is focused more on the service. So we had ingress and and they evolved the the API to to handle more complex scenarios. Okay. But we live in in this world of I mean it's not ideal.

We you all can have 200 horror histories about Kubernetes networking but so far it was good enough right we were improving one thing at a time but one day this is a real character Vanessa Vanessa works in limor lab she open an isue in in Kubernetes she was saying oh I ran all this red park and they are not working well an
