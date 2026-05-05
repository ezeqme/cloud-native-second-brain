---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Application Development"
themes: ["Kubernetes Core"]
speakers: ["Christian Schlotter", "Broadcom", "Fabrizio Pandini", "VMware by Broadcom"]
sched_url: https://kccnceu2025.sched.com/event/1tx6k/kubernetes-crd-design-for-the-long-haul-tips-tricks-and-lessons-learned-christian-schlotter-broadcom-fabrizio-pandini-vmware-by-broadcom
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+CRD+Design+for+the+Long+Haul%3A+Tips%2C+Tricks%2C+and+Lessons+Learned+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Kubernetes CRD Design for the Long Haul: Tips, Tricks, and Lessons Learned - Christian Schlotter, Broadcom & Fabrizio Pandini, VMware by Broadcom

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Application Development]]
- Temas: [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Christian Schlotter, Broadcom, Fabrizio Pandini, VMware by Broadcom
- Schedule: https://kccnceu2025.sched.com/event/1tx6k/kubernetes-crd-design-for-the-long-haul-tips-tricks-and-lessons-learned-christian-schlotter-broadcom-fabrizio-pandini-vmware-by-broadcom
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+CRD+Design+for+the+Long+Haul%3A+Tips%2C+Tricks%2C+and+Lessons+Learned+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Kubernetes CRD Design for the Long Haul: Tips, Tricks, and Lessons Learned.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx6k/kubernetes-crd-design-for-the-long-haul-tips-tricks-and-lessons-learned-christian-schlotter-broadcom-fabrizio-pandini-vmware-by-broadcom
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+CRD+Design+for+the+Long+Haul%3A+Tips%2C+Tricks%2C+and+Lessons+Learned+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7IA-Vw1K7eg
- YouTube title: Kubernetes CRD Design for the Long Haul: Tips, Tricks, and... Christian Schlotter & Fabrizio Pandini
- Match score: 0.828
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/kubernetes-crd-design-for-the-long-haul-tips-tricks-and-lessons-learne/7IA-Vw1K7eg.txt
- Transcript chars: 20310
- Keywords: cluster, version, create, object, machine, change, fields, consider, evolve, breaking, mistake, instead, controller, adding, simple, binary, mistakes, writing

### Resumo baseado na transcript

Um, yeah, we're talking about Kubernetes here designing for the long haul where we want to try to share tips and tricks and um, stuff we learned in our journey with cluster API and designing APIs. I'm also a cluster API maintainer and I work in the same team of Christian in in Broadcom. Before talking about mistakes, let's have a a quick refresher on how we develop APIs or CRD in Kubernetes. But what could possibly go wrong when you keep a good developer and you ask him to develop a Kubernetes API? So let's start looking what mistake we we could happen by going through some of the lesson learned in the la in the last few years. So if you take a look for example before v1.29 29 Kubernetes QBAM used the vivon beta 3 version of their cluster configuration.

### Excerpt da transcript

Hi everyone. Um, welcome to our talk and thanks for coming. Um, yeah, we're talking about Kubernetes here designing for the long haul where we want to try to share tips and tricks and um, stuff we learned in our journey with cluster API and designing APIs. Before we start, we want to introduce ourselves. I'm Christian. I'm a maintainer in cluster API and a software engineer at Broadcom. Hello everyone. Thank you for being here. I'm Fitza Pandini. I'm also a cluster API maintainer and I work in the same team of Christian in in Broadcom. So the long haul. So let's start with a pool. How many of you are maintaining a project software contributed to a project software no matter if upstream or downstream open source or not? Let's raise hand please. Okay. some good developer vibes in the room. So you all probably know that every software project keep evolving. As soon as users start using your project, you start getting feedback. You start getting a request for improvement. And so also your API or your CRD have to improve.

But your API, your CRD is slightly different than your binary. You need a a strategy to make sure that your CRD evolve nicely in the long run. In the Kubernetes ecosystem, let me say the most common strategy to make your API to evolve is based by two complimentary ideas. The first one is that you want to pick to keep evolving your current API version. If you think about it, this is what they are doing in Kubernetes. Kubernetes is V1 since a couple of year now and it keeps evolving. But sometime what you can do with a single API version is limited. So you cannot do breaking change. So sometime you also want to create new API version. But the key point here is that you want to create API version only after a careful and deliberate decision. This is the key. So today talk is about avoiding making mistakes that will force you to create unplanned version. Okay. Before talking about mistakes, let's have a a quick refresher on how we develop APIs or CRD in Kubernetes. So the process started by writing a go types.

You write a go types. Then what you do? you run a uh a generator from controller gen and this generator create a CRD where the most important part in of the CRD is the open API spec that reflect your types. Finally, you apply this CRD to the API server and the user can interact with your API by writing YAML. So if you look at the at this process where do you think mistakes will happen? So on the right side there are the users. User by defa
