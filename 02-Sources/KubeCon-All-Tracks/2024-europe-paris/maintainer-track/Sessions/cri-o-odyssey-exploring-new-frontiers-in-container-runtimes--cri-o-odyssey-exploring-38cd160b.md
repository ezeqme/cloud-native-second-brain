---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Runtime Containers", "Community Governance"]
speakers: ["Julien Ropé", "Sohan Kunkerkar", "Red Hat"]
sched_url: https://kccnceu2024.sched.com/event/1Yhgj/cri-o-odyssey-exploring-new-frontiers-in-container-runtimes-julien-rope-sohan-kunkerkar-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=CRI-O+Odyssey%3A+Exploring+New+Frontiers+in+Container+Runtimes+CNCF+KubeCon+2024
slides: []
status: parsed
---

# CRI-O Odyssey: Exploring New Frontiers in Container Runtimes - Julien Ropé & Sohan Kunkerkar, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Julien Ropé, Sohan Kunkerkar, Red Hat
- Schedule: https://kccnceu2024.sched.com/event/1Yhgj/cri-o-odyssey-exploring-new-frontiers-in-container-runtimes-julien-rope-sohan-kunkerkar-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=CRI-O+Odyssey%3A+Exploring+New+Frontiers+in+Container+Runtimes+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre CRI-O Odyssey: Exploring New Frontiers in Container Runtimes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1Yhgj/cri-o-odyssey-exploring-new-frontiers-in-container-runtimes-julien-rope-sohan-kunkerkar-red-hat
- YouTube search: https://www.youtube.com/results?search_query=CRI-O+Odyssey%3A+Exploring+New+Frontiers+in+Container+Runtimes+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=mDPLioNIIjo
- YouTube title: CRI-O Odyssey: Exploring New Frontiers in Container Runtimes - Julien Ropé & Sohan Kunkerkar
- Match score: 0.894
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/cri-o-odyssey-exploring-new-frontiers-in-container-runtimes/mDPLioNIIjo.txt
- Transcript chars: 27625
- Keywords: container, runtime, containers, confidential, support, running, trying, security, information, change, request, advisor, download, future, inside, cluster, actually, snapshot

### Resumo baseado na transcript

good morning everyone thank you so much for joining this session I hope you are enjoying the cube con my name is Sohan kerker I work at Red Hat as a senior software engineer I'm working on cryo and signote specific projects today along with me we have so um I'm Julian R I'm working for reddat as a software developer I'm also a contributor to cryo and I am involved to uh the Kata containers and the confidential container projects too so um today we want to talk about

### Excerpt da transcript

good morning everyone thank you so much for joining this session I hope you are enjoying the cube con my name is Sohan kerker I work at Red Hat as a senior software engineer I'm working on cryo and signote specific projects today along with me we have so um I'm Julian R I'm working for reddat as a software developer I'm also a contributor to cryo and I am involved to uh the Kata containers and the confidential container projects too so um today we want to talk about what happened in cryo in the past months following our graduation uh within the cncf um we will talk about uh how the project behave at the community level here uh so this is showing uh the number of stars that we have on the GitHub project uh this is a steady incline as you can see over the years uh it is showing uh uh growing interest into the project and follows uh all the work we do to keep having more contributors and contributions to the project um as part of it the work we are doing to get more contributors include uh working with uh mentorship programs with uh like the lfix mentorship so we had successful contribution following that uh so yeah we we see we see a steady number of commits and contributors going on uh at the community level so we can say the project is in good good shape uh and is seeing a traction um next uh so just a glimpse of what we are going to release in the next release 1.30 um so this is just a a small number of the things that are going into that release so first we are going to have an easier way to deploy seom profiles using go artifacts um we're going to release uh support for the s390 uh AR tecture and uh the enablement for split image file system which is something that soan is going to talk about a little more uh later on uh so also we added uh the ability to give time zone information for the Pod and containers to for them to be able to process the local time and um more internal is instrumentation of calls with the in plugin so it's just a way to give visualization of internal processes within the cryo uh components uh so this is it for that okay so more technical Pro projects um so this is we want to talk about what we did to integrate uh confidential containers support into cryo so um confidential containers is about running uh your workloads uh in a trusted environment and we are doing that by using um a virtual machine which is running on a hypervisor with uh the ability to encrypt the memory while it is in use uh the goal is that well we already encr
