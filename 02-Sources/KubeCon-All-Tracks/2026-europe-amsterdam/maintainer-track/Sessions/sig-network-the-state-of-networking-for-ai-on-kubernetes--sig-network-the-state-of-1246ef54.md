---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Networking", "Kubernetes Core", "Community Governance"]
speakers: ["David Martin", "Red Hat", "Haiyan Meng", "Bowei Du", "Kellen Swain", "Google", "Nadia Pinaeva", "NVIDIA"]
sched_url: https://kccnceu2026.sched.com/event/2EF4d/sig-network-the-state-of-networking-for-ai-on-kubernetes-david-martin-red-hat-haiyan-meng-bowei-du-kellen-swain-google-nadia-pinaeva-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=SIG+Network%3A+The+State+of+Networking+for+AI+on+Kubernetes+CNCF+KubeCon+2026
slides: []
status: parsed
---

# SIG Network: The State of Networking for AI on Kubernetes - David Martin, Red Hat; Haiyan Meng & Bowei Du & Kellen Swain, Google; Nadia Pinaeva, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Networking]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: David Martin, Red Hat, Haiyan Meng, Bowei Du, Kellen Swain, Google, Nadia Pinaeva, NVIDIA
- Schedule: https://kccnceu2026.sched.com/event/2EF4d/sig-network-the-state-of-networking-for-ai-on-kubernetes-david-martin-red-hat-haiyan-meng-bowei-du-kellen-swain-google-nadia-pinaeva-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=SIG+Network%3A+The+State+of+Networking+for+AI+on+Kubernetes+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre SIG Network: The State of Networking for AI on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF4d/sig-network-the-state-of-networking-for-ai-on-kubernetes-david-martin-red-hat-haiyan-meng-bowei-du-kellen-swain-google-nadia-pinaeva-nvidia
- YouTube search: https://www.youtube.com/results?search_query=SIG+Network%3A+The+State+of+Networking+for+AI+on+Kubernetes+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=DO1PVnly9cU
- YouTube title: SIG Network: The State of Networking for AI on Ku... David M, Haiyan M, Bowei D & Kellen S & Nadia P
- Match score: 0.792
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/sig-network-the-state-of-networking-for-ai-on-kubernetes/DO1PVnly9cU.txt
- Transcript chars: 27389
- Keywords: networking, gateway, inference, network, policy, workloads, working, actually, agentic, looking, observability, resource, access, questions, traffic, agents, request, question

### Resumo baseado na transcript

I'm from Google and uh I'm working on the cube agent networking project. So, this session will be basically an introduction to SIG network, kind of the scope that we cover. kind of basic problems and then how do they map to categories of say working groups or areas in sig network and just being very broad here right in AI we have you know how do you get the hardware like the GPUs accelerators and And then finally, we have this new category of workloads that's pretty special agentic workloads like how do you integrate that into your Kubernetes cluster. Um, if you're familiar with that part of the networking, it used to be mostly covered by group outside of Kubernetes, uh, which is called network plumbing, but now it is moving slightly more into the SIG network realm. And it all started with the introduction of dret which is a kubernetes network driver written by our good friend Antonio uh which uses dynamic resource allocation and it helps you deliver high performance networking.

### Excerpt da transcript

Okay, let's get started. Uh, welcome to the SIG network update. I know this is a very late session, so thank you for coming. Um, first we will introduce our panelists. So maybe introduce yourself from that end to here. >> Hey all, uh, I'm Kellen. I'm filling in for it. Uh, I work for Google on the GKE inference team. >> Hey, I'm David. work at Red Hat on MCP gateway. >> Hey, I'm Nadia. I work at Nvidia on Kubernetes networking. >> Hello, I'm Hyen. I'm from Google and uh I'm working on the cube agent networking project. >> And hi, I'm Bowie. I'm work at Google and I'm the Signet chair. So, this session will be basically an introduction to SIG network, kind of the scope that we cover. And then for particularly for this session, we want to kind of focus on what is happening in a IML. I don't know if you know it's kind of a big thing on everyone's mind. And then um we want to reserve a lot of time for Q&A. So probably like 15 minutes at the end for Q&A. First we have some canned questions but uh not too many and then you will basically be able to ask your own.

So first um introduction to SIG network. So what is SIG network? SIG network manages the components, interfaces and APIs for networking and Kubernetes. It maintains core code such as QRoxy and also the service API and those things and it defines APIs for many networking areas you know key among them ingress gateway API and we have a variety of sub projects just because the scope is so big. So we have a sub project in network policy, multi-et network and gateway API and of course the AI related uh sub projects as well and we work with lots of SIGs because you know networking kind of connects lots of things together. So we work with SIG node, SIG scheduling and multicluster and we participate in a lot of working groups you know AI gateway working group AI conformance working group so kind of in terms of a IML thinking about it it's like what are the kind of basic problems and then how do they map to categories of say working groups or areas in sig network and just being very broad here right in AI we have you know how do you get the hardware like the GPUs accelerators and so forth How do you integrate it into your training?

How do you serve inference workloads? And then finally, we have this new category of workloads that's pretty special agentic workloads like how do you integrate that into your Kubernetes cluster. So if you look at how it maps the SIG network, we have the gateway API project and the ga
