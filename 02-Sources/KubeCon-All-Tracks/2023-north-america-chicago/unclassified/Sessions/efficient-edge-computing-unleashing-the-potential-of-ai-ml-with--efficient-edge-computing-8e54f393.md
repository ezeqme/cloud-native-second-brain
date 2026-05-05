---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Unclassified"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Ricardo Noriega De Soto", "Red Hat", "Alex Mevec", "Lockheed Martin"]
sched_url: https://kccncna2023.sched.com/event/1R2vK/efficient-edge-computing-unleashing-the-potential-of-aiml-with-lightweight-kubernetes-ricardo-noriega-de-soto-red-hat-alex-mevec-lockheed-martin
youtube_search_url: https://www.youtube.com/results?search_query=Efficient+Edge+Computing%3A+Unleashing+the+Potential+of+AI%2FML+with+Lightweight+Kubernetes+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Efficient Edge Computing: Unleashing the Potential of AI/ML with Lightweight Kubernetes - Ricardo Noriega De Soto, Red Hat & Alex Mevec, Lockheed Martin

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Chicago
- Speakers: Ricardo Noriega De Soto, Red Hat, Alex Mevec, Lockheed Martin
- Schedule: https://kccncna2023.sched.com/event/1R2vK/efficient-edge-computing-unleashing-the-potential-of-aiml-with-lightweight-kubernetes-ricardo-noriega-de-soto-red-hat-alex-mevec-lockheed-martin
- Busca YouTube: https://www.youtube.com/results?search_query=Efficient+Edge+Computing%3A+Unleashing+the+Potential+of+AI%2FML+with+Lightweight+Kubernetes+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Efficient Edge Computing: Unleashing the Potential of AI/ML with Lightweight Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2vK/efficient-edge-computing-unleashing-the-potential-of-aiml-with-lightweight-kubernetes-ricardo-noriega-de-soto-red-hat-alex-mevec-lockheed-martin
- YouTube search: https://www.youtube.com/results?search_query=Efficient+Edge+Computing%3A+Unleashing+the+Potential+of+AI%2FML+with+Lightweight+Kubernetes+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=11CzoVex7rU
- YouTube title: Efficient Edge Computing: Unleashing the Potential of AI/ML... Ricardo Noriega De Soto & Alex Mevec
- Match score: 0.829
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/efficient-edge-computing-unleashing-the-potential-of-ai-ml-with-lightw/11CzoVex7rU.txt
- Transcript chars: 15751
- Keywords: devices, running, little, operating, device, computing, models, update, basically, microshift, llm, trying, memory, applications, approach, health, manage, looking

### Resumo baseado na transcript

thank you very much for attending is one of the last uh sessions of the conference I know it's hard for all of you um my name is Ricardo Nora I'm a principal software engineer uh working in the emerging Technologies organization in the office of the CTO in bread and that's I'm Alex mevik I work over at locked Martin I'm a senior inops engineer working primarily on AI devices so in this presentation we are going to talk about well how to run efficiently AI models at the

### Excerpt da transcript

thank you very much for attending is one of the last uh sessions of the conference I know it's hard for all of you um my name is Ricardo Nora I'm a principal software engineer uh working in the emerging Technologies organization in the office of the CTO in bread and that's I'm Alex mevik I work over at locked Martin I'm a senior inops engineer working primarily on AI devices so in this presentation we are going to talk about well how to run efficiently AI models at the edge uh of course you seen uh kubernetes this talk is meant for you know infrastructure people it's not meant for data scientist but I think uh you know uh we'll explain what we've been doing and I think I hope you find it interesting so uh for you know to give you a little bit of background um what is h Computing it's uh that work can mean uh lot of things for for different people um and in our industry we've been trying to centralize workloads for for decades we have built data centers with thousands of servers we have built you know distributed computing platforms that we call the cloud but however uh more and more devices are connected to the internet uh smart lights uh IP cameras sensors Etc and they are all generating huge amounts of data that have been transferred to the cloud and across the globe right um all these industries that you see in the slid uh medical automotive industrial defense for example FYI that is one of the Lo lockit Martin goodies um they are all generating huge amounts of data so for us the definition of edge Computing is basically putting computing power closer to where the data is is been generated especially when we talk about running AI models at the edge uh we want to do the inferencing process closer to where the data is generated imagine you want to run an anomaly detection uh algorithm uh we cannot afford to send video streams back to the cloud to do that that process we need to put the gpus closer to to that data so as you can see in the slides there are um these are the type of devices that we are talking about uh these are usually single board computers or system some chip uh that have certain limitations or characteristics that need to be taken into account uh limited resources in terms in terms of CPU memory storage um they are not extensible as servers we are used to servers right like they have uh PCI Express slots to plug accelerators more memory you know uh they are extensible um usually they don't have outof band management interfaces which might
