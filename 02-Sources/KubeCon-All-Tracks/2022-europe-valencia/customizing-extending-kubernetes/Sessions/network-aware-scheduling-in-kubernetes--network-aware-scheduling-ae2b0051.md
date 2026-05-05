---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Customizing + Extending Kubernetes"
themes: ["Networking", "Kubernetes Core"]
speakers: ["José Santos", "Ghent University"]
sched_url: https://kccnceu2022.sched.com/event/ytlA/network-aware-scheduling-in-kubernetes-jose-santos-ghent-university
youtube_search_url: https://www.youtube.com/results?search_query=Network-aware+Scheduling+in+Kubernetes+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Network-aware Scheduling in Kubernetes - José Santos, Ghent University

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: José Santos, Ghent University
- Schedule: https://kccnceu2022.sched.com/event/ytlA/network-aware-scheduling-in-kubernetes-jose-santos-ghent-university
- Busca YouTube: https://www.youtube.com/results?search_query=Network-aware+Scheduling+in+Kubernetes+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Network-aware Scheduling in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytlA/network-aware-scheduling-in-kubernetes-jose-santos-ghent-university
- YouTube search: https://www.youtube.com/results?search_query=Network-aware+Scheduling+in+Kubernetes+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=E4cP275_OCs
- YouTube title: Network-aware Scheduling in Kubernetes - José Santos, Ghent University
- Match score: 0.811
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/network-aware-scheduling-in-kubernetes/E4cP275_OCs.txt
- Transcript chars: 25379
- Keywords: network, application, cluster, workloads, latency, framework, scheduling, currently, deploy, topology, essentially, bandwidth, scheduler, typically, dependencies, online, boutique, plugins

### Resumo baseado na transcript

hi so i'm currently a postdoc researcher at kent university i'm jose sanchez i just recently graduated last month and this talk summarizes the latest work during my dissertation which is trying to bring network aware information to the scheduling process in kubernetes trying to find better decisions uh focus on this information to allocate workloads in kubernetes unfortunately uh my collaborator my co-speaker shen was not able to be here today so i'll be doing the the presentation this work is a joint collaboration between ghent university and ibm

### Excerpt da transcript

hi so i'm currently a postdoc researcher at kent university i'm jose sanchez i just recently graduated last month and this talk summarizes the latest work during my dissertation which is trying to bring network aware information to the scheduling process in kubernetes trying to find better decisions uh focus on this information to allocate workloads in kubernetes unfortunately uh my collaborator my co-speaker shen was not able to be here today so i'll be doing the the presentation this work is a joint collaboration between ghent university and ibm today i'll talk about more about the motivation why do we need network aware scheduling in current kubernetes clusters i'll try to show you the main building blocks that we currently have in our network aware framework i'll try to explain you some of the implementation details and some of the considerations that we have in our framework and i'll try to show you a complete example on how you can use our framework to deploy your applications in a kubernetes cluster trying to find better decisions in terms of network aware placement then if the demo gods and the wi-fi help me i'll try to show you a live demo by deploying the online boutique application which is a typical application used in microservice research so it's a web-based application with several workloads and by deploying this application with the default scheduler and with our approach our network aware framework you will see the differences that you get by deploying this application in kubernetes cluster then i'll talk about the challenges and the lessons learned and finally acknowledgements so typically when we started working on network aware scheduling we noticed that the kubernetes scheduler typically mainly focuses on resource efficiency so typically you as a developer you try to set up cpu and memory requests and limitations so that the scheduler can find better decisions for your pods and that's particularly important when you are focusing on energy efficiency but for certain applications like latency sensitive iot applications and video streaming applications low latency plays a major role because you want to reduce the the applications response time trying to give pleasant experiences to your end users so currently there are very few plugins scheduling plugins in the kubernetes architecture that you can use with contextual awareness so for instance when you have several workloads in your application typically the scheduler allocates these workl
