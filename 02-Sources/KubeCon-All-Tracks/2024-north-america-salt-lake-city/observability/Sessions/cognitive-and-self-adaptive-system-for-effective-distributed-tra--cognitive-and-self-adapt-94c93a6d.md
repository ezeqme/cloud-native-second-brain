---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Observability"
themes: ["AI ML", "Observability"]
speakers: ["Mitul Tandon", "Akash Gusain"]
sched_url: https://kccncna2024.sched.com/event/1i7nb/cognitive-and-self-adaptive-system-for-effective-distributed-tracing-in-applications-mitul-tandon-akash-gusain
youtube_search_url: https://www.youtube.com/results?search_query=Cognitive+and+Self-Adaptive+System+for+Effective+Distributed-Tracing+in+Applications+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Cognitive and Self-Adaptive System for Effective Distributed-Tracing in Applications - Mitul Tandon & Akash Gusain

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Observability]]
- Temas: [[AI ML]], [[Observability]]
- País/cidade: United States / Salt Lake City
- Speakers: Mitul Tandon, Akash Gusain
- Schedule: https://kccncna2024.sched.com/event/1i7nb/cognitive-and-self-adaptive-system-for-effective-distributed-tracing-in-applications-mitul-tandon-akash-gusain
- Busca YouTube: https://www.youtube.com/results?search_query=Cognitive+and+Self-Adaptive+System+for+Effective+Distributed-Tracing+in+Applications+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Cognitive and Self-Adaptive System for Effective Distributed-Tracing in Applications.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7nb/cognitive-and-self-adaptive-system-for-effective-distributed-tracing-in-applications-mitul-tandon-akash-gusain
- YouTube search: https://www.youtube.com/results?search_query=Cognitive+and+Self-Adaptive+System+for+Effective+Distributed-Tracing+in+Applications+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9V_iLfYsScY
- YouTube title: Cognitive and Self-Adaptive System for Effective Distributed-Tracing in Appl... M. Tandon, A. Gusain
- Match score: 0.979
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/cognitive-and-self-adaptive-system-for-effective-distributed-tracing-i/9V_iLfYsScY.txt
- Transcript chars: 19786
- Keywords: traces, trace, sampling, tracing, cluster, distributed, adaptive, approach, feature, observability, request, interesting, aggregator, sampler, vector, events, entire, systems

### Resumo baseado na transcript

hey hi everyone thank you for joining us today my name is Akash I'm currently working at BTO uh in BTO we build tools powered by llm to increase engineering efficiency and uh boost developer productivity previously I was working as an S at VMware okay I'm mthal I'm working as a s art Property Guru currently and I've also worked with vmw previously yeah so the title for the talk today is cognitive and self adaptive system for Effective distributed tracing so as the topic is based upon distributed

### Excerpt da transcript

hey hi everyone thank you for joining us today my name is Akash I'm currently working at BTO uh in BTO we build tools powered by llm to increase engineering efficiency and uh boost developer productivity previously I was working as an S at VMware okay I'm mthal I'm working as a s art Property Guru currently and I've also worked with vmw previously yeah so the title for the talk today is cognitive and self adaptive system for Effective distributed tracing so as the topic is based upon distributed tracing which is part of observability so we figured we will talk about a bit about observability as well so I recently stumbled upon this quote which it really struck with me in a world where software observability is the new Norm observability is our superp power turning chaos into Clarity it's rightfully true uh we we see there are dozens of you know open source tools based on observability there are hundreds of organization we are working on observability so what really does it mean and why do we need it so as of now as we adopt uh distributed architecture we are moving into container containers I guess we are into containers and communities that's why we are here the systems are becoming more and more complicated the it's becoming more and more hard to you know know what is going on at every corner of your software systems so this is where we need observability and uh there is some set of data which is part of observability which we usually look at it and this is the data that provides us the insightful information that we we usually look at it and uh find a problem and then probably stumble upon the solution as well so this data exist in four forms mainly metrics events logs and traces and for this talk we will only focus upon the tracing and what problems did we face while implementing it and how did we propose to solve it yeah over to you uh yeah so as mentioned earlier for this talk we'll be mainly focusing on distributed tracing uh which is is one of the important pillars of observability Stack uh before we proceed any further let's try to just understand what distributed tracing is and why do we need it so uh distributed tracing is a method of tracking application request when this request spans over M multiple services and uh span across multiple servers uh this is a crucial tool in troubleshooting uh request when there's a high latency or there's a fault in one of the components uh some important terms associated with distributed tracing are one is Tra
