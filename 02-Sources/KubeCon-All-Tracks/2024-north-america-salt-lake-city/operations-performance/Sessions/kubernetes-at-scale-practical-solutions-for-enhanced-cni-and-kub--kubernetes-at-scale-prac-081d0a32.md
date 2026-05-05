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
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Henrique Santana", "Amazon Web Services", "Bruno Gabriel da Silva", "Sysdig"]
sched_url: https://kccncna2024.sched.com/event/1i7mB/kubernetes-at-scale-practical-solutions-for-enhanced-cni-and-kubelet-performance-henrique-santana-amazon-web-services-bruno-gabriel-da-silva-sysdig
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+at+Scale%3A+Practical+Solutions+for+Enhanced+CNI+and+Kubelet+Performance+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Kubernetes at Scale: Practical Solutions for Enhanced CNI and Kubelet Performance - Henrique Santana, Amazon Web Services & Bruno Gabriel da Silva, Sysdig

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Henrique Santana, Amazon Web Services, Bruno Gabriel da Silva, Sysdig
- Schedule: https://kccncna2024.sched.com/event/1i7mB/kubernetes-at-scale-practical-solutions-for-enhanced-cni-and-kubelet-performance-henrique-santana-amazon-web-services-bruno-gabriel-da-silva-sysdig
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+at+Scale%3A+Practical+Solutions+for+Enhanced+CNI+and+Kubelet+Performance+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Kubernetes at Scale: Practical Solutions for Enhanced CNI and Kubelet Performance.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7mB/kubernetes-at-scale-practical-solutions-for-enhanced-cni-and-kubelet-performance-henrique-santana-amazon-web-services-bruno-gabriel-da-silva-sysdig
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+at+Scale%3A+Practical+Solutions+for+Enhanced+CNI+and+Kubelet+Performance+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=tKoxI-k7cu8
- YouTube title: Kubernetes at Scale: Practical Solutions for Enhanced CNI and Kubelet P... H. Santana, B.G. da Silva
- Match score: 0.912
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/kubernetes-at-scale-practical-solutions-for-enhanced-cni-and-kubelet-p/tKoxI-k7cu8.txt
- Transcript chars: 17358
- Keywords: cluster, basically, logs, everything, another, course, production, sometimes, configuration, usually, monday, networking, dashboard, called, everyone, customers, happen, working

### Resumo baseado na transcript

welcome everyone thank you for being here I know a long I know it's a long journey walking from their venue to you here so thank you so much for starting that before we start the presentation I would look to like some check who in here have a cluster a single cluster running at least with 50 notes 100 notes thousand notes some brave people here so today we're going to talk about kubernetes at scale or actually better say we going to talk problems when you scale and

### Excerpt da transcript

welcome everyone thank you for being here I know a long I know it's a long journey walking from their venue to you here so thank you so much for starting that before we start the presentation I would look to like some check who in here have a cluster a single cluster running at least with 50 notes 100 notes thousand notes some brave people here so today we're going to talk about kubernetes at scale or actually better say we going to talk problems when you scale and some tricks that you can use to enhance cni and CU blets I am Bruno Silva Senior Solutions engineer at cdic and I help customers on secure and compliance their workloads and kubernetes and the cloud and together with me my name is aiki s thank you for joining on our session and I work for AWS I support eks and ECS customers um for English speaker you can call me Ricky fine thank you for joining so a disclaimer uh the timeline that we going to present not necessarily represent the real thing how things happen we did a little bit of Shuffle to get a better flow and maybe not the same Multiverse that we are here so just be aware of that and of course we talk about Community safe no cluster were harm during the make of this presentation yeah just for context uh we had a we were working for a company that had a project that basically was to like save money have that c optimization project and for this project of course this affect our team and we need to uh provide some solutions to achieve the goal that they are looking for and one of the solution that we are thinking usually or likely that you are already using this is basically turning off and turning on your environment uh for the week weekends if you don't have workloads that receive traffic or or uh attend customers on weekend time so it's very common approach to reduce cost on cloud so basically the the goal is to like from between Friday and Saturday turn off all the nodes or maximum of the nodes that you have and at Monday time before the first Quest arve you start everything again to receive the be able to receive the traffic from your customers so for this we had just again to explain about the scale that we're talking about here for the test environment we had like 10000 nodes but for production we're talking about 1,00 1,200 nodes so for this we need to like do some maths because we could not test in production we need to do test environment make sure that it's working fine and after that okay let's do some math to make sure that we are
