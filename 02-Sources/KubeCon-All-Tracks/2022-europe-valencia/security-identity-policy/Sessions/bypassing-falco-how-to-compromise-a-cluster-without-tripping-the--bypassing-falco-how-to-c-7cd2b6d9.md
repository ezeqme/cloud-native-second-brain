---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Security + Identity + Policy"
themes: ["Security", "Kubernetes Core"]
speakers: ["Shay Berkovich", "BlackBerry"]
sched_url: https://kccnceu2022.sched.com/event/ytl7/bypassing-falco-how-to-compromise-a-cluster-without-tripping-the-soc-shay-berkovich-blackberry
youtube_search_url: https://www.youtube.com/results?search_query=Bypassing+Falco%3A+How+to+Compromise+a+Cluster+without+Tripping+the+SOC+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Bypassing Falco: How to Compromise a Cluster without Tripping the SOC - Shay Berkovich, BlackBerry

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Shay Berkovich, BlackBerry
- Schedule: https://kccnceu2022.sched.com/event/ytl7/bypassing-falco-how-to-compromise-a-cluster-without-tripping-the-soc-shay-berkovich-blackberry
- Busca YouTube: https://www.youtube.com/results?search_query=Bypassing+Falco%3A+How+to+Compromise+a+Cluster+without+Tripping+the+SOC+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Bypassing Falco: How to Compromise a Cluster without Tripping the SOC.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytl7/bypassing-falco-how-to-compromise-a-cluster-without-tripping-the-soc-shay-berkovich-blackberry
- YouTube search: https://www.youtube.com/results?search_query=Bypassing+Falco%3A+How+to+Compromise+a+Cluster+without+Tripping+the+SOC+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2rSiSpaR6bI
- YouTube title: Bypassing Falco: How to Compromise a Cluster without Tripping the SOC - Shay Berkovich, BlackBerry
- Match score: 0.92
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/bypassing-falco-how-to-compromise-a-cluster-without-tripping-the-soc/2rSiSpaR6bI.txt
- Transcript chars: 26589
- Keywords: container, attacker, security, detection, cluster, docker, course, actually, trigger, interesting, scenario, running, typical, bypass, access, detect, create, connection

### Resumo baseado na transcript

hello everybody welcome to valencia thank you for joining this talk my name is shay and today we're going to talk about falcon by passing falco default rule set and perhaps even how to compromise a cluster without tripping the sock let's start let's start with the background what falco is for and what's container security is about and this is my view of container security you can sort of divide it into four areas so security cluster security pre-deployment and post deployment and of course how security is important

### Excerpt da transcript

hello everybody welcome to valencia thank you for joining this talk my name is shay and today we're going to talk about falcon by passing falco default rule set and perhaps even how to compromise a cluster without tripping the sock let's start let's start with the background what falco is for and what's container security is about and this is my view of container security you can sort of divide it into four areas so security cluster security pre-deployment and post deployment and of course how security is important because if host is compromised then it's really hard to reason about the workload security that runs on on the on this hubs pre-deployment is about building the base images in an efficient and secure way container scanning although some people call it a little bit scanning but i like to be more precise um scan for exposed secrets um static compliance basically everything that we can do with the static image file of the container cluster security it's all about kubernetes config and then there's a post deployment and that's where falco is coming into the picture runtime detection um there's also runtime prevention dynamic appliance and prevention is about existing um mostly about existing linux security kernel security mechanism that are sometimes given for free in the container context i've recently listened to the cloud what's the cloud security podcast and they suggested a bit different division uh into areas of container security so they were talking about build infrastructure and uh and runtime and that's sort of the way this this maps on to this view intro is cluster security and how security built is pre-deployment and the right time is actually post deployment so if that helps to think about it as well and we can see that where the falco belongs to runtime detection through the falco architecture falco is built on top of either kernel module or ebpf sensors running in the kernel space uh the events mostly syscalls and enriched syscalls are bubbling through the ring buffer up to the user space where a bunch of library focal libraries and more most importantly rule engine are taking them processing them and and decide whether the certain rules that are expressed as yaml files um they whether the rules should trigger given that event or shouldn't trigger and the if rolls trigger then one can integrate that with the typical cloud staff like cm or event in some kind of venting engine or grpc but for our first purpose we're going to use std out
