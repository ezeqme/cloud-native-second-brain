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
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Yuan Tang", "Red Hat", "Mario Fahlandt", "Kubermatic", "Janet Kuo", "Google"]
sched_url: https://kccnceu2026.sched.com/event/2EF76/advancing-kubernetes-ai-conformance-current-state-and-roadmap-yuan-tang-red-hat-mario-fahlandt-kubermatic-janet-kuo-google
youtube_search_url: https://www.youtube.com/results?search_query=Advancing+Kubernetes+AI+Conformance%3A+Current+State+and+Roadmap+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Advancing Kubernetes AI Conformance: Current State and Roadmap - Yuan Tang, Red Hat; Mario Fahlandt, Kubermatic; Janet Kuo, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Yuan Tang, Red Hat, Mario Fahlandt, Kubermatic, Janet Kuo, Google
- Schedule: https://kccnceu2026.sched.com/event/2EF76/advancing-kubernetes-ai-conformance-current-state-and-roadmap-yuan-tang-red-hat-mario-fahlandt-kubermatic-janet-kuo-google
- Busca YouTube: https://www.youtube.com/results?search_query=Advancing+Kubernetes+AI+Conformance%3A+Current+State+and+Roadmap+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Advancing Kubernetes AI Conformance: Current State and Roadmap.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF76/advancing-kubernetes-ai-conformance-current-state-and-roadmap-yuan-tang-red-hat-mario-fahlandt-kubermatic-janet-kuo-google
- YouTube search: https://www.youtube.com/results?search_query=Advancing+Kubernetes+AI+Conformance%3A+Current+State+and+Roadmap+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=EdgyyJpauKU
- YouTube title: Advancing Kubernetes AI Conformance: Current State and Road... Yuan Tang, Mario Fahlandt & Janet Kuo
- Match score: 0.859
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/advancing-kubernetes-ai-conformance-current-state-and-roadmap/EdgyyJpauKU.txt
- Transcript chars: 14488
- Keywords: conformance, program, basically, requirements, standard, everyone, platform, actually, process, workloads, working, platforms, conformant, requirement, meetings, looking, started, running

### Resumo baseado na transcript

Uh as AI introduced as AI getting more and more uh adoption, we see that AI workloads are introducing new requirements and new challenges in Kubernetes. They have synchronously scaled workloads and there they require specialized hardware and networking and security and without a standard conformance and it's hard for us to um have a common standard for everyone to have the same experience. We want to make it uh interoperable so that you can get the same guarantee that you used to get with uh Kubernetes conformance that you can run you can write once and run it anywhere and with AI workloads too. So we are now transitioning we have transitioned into a a seek architecture official sub project. This is following the same path of Kubernetes conformance and you can uh take a look at the repo that we have. We have all the design and the requirements and discussion and all the code for and the automated test for the uh for the requirements there.

### Excerpt da transcript

Hi everyone, welcome to the uh Kubernetes AI conformance talk. We are going to talk about the current state and the road map. So these are the leads of AI conformance program and I'm Janet Quo. I work at Google. >> My name is Yan Tang. I work at Red Hat. >> I'm Mario Farland and I work for Curomedic. And we are missing one person who unfortunately couldn't make it here. uh which is uh Rita Sang for Microsoft. >> Cool. Uh I'll talk about the history of Kubernetes AI conformance. So how it started? Uh as AI introduced as AI getting more and more uh adoption, we see that AI workloads are introducing new requirements and new challenges in Kubernetes. There are GPUs. They are uh GPU intensive. They have synchronously scaled workloads and there they require specialized hardware and networking and security and without a standard conformance and it's hard for us to um have a common standard for everyone to have the same experience. So we figured that Kubernetes conformance is not enough. There are parts outside of Kubernetes core and we want to iterate faster than the Kubernetes because Kubernetes conformance care a lot about stability and being able to um have a stable release and a standard that everyone adopts.

But with AI we want to move faster. So we started the Kubernetes AI conformance working group in 20ou uh 2025 to solve this problem and this is sponsored by SIG architecture. We had a original proposal for what AI conformance could look like and we proposed the different requirements. We separate them by should and must. So should means that and this is a recommendation or a direction that the community want to go and must means that this is mandatory that all the platforms should follow this uh requirements. So what is included in the kubernetes a conformance? This is additional requirements on top of the existing kubernetes conformance. So basically uh a platform needs to be Kubernetes conformant first before they can be Kubernetes AI conformant and and also I got questions about oh does it does it tell me the best practice of how I run AI workloads on Kubernetes it actually doesn't we uh we only put uh the limitation or enforcement on the platforms so they should follow the standard to provide the capabilities or APIs in the platform so that it can cover most of the uh AI workflow use cases and users are free to choose however they want to use those clusters.

For example, they can just use the clusters for training or just for inferencing, but the p
