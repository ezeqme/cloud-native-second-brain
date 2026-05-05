---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Emerging + Advanced"
themes: ["AI ML", "SRE Reliability"]
speakers: ["Ganeshkumar Ashokavardhanan", "Microsoft", "Bernie Wu", "MemVerge"]
sched_url: https://kccnceu2025.sched.com/event/1tx7u/transparent-infra-level-checkpoint-and-restore-for-resilient-aiml-workloads-ganeshkumar-ashokavardhanan-microsoft-bernie-wu-memverge
youtube_search_url: https://www.youtube.com/results?search_query=Transparent%2C+Infra-Level+Checkpoint+and+Restore+for+Resilient+AI%2FML+Workloads+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Transparent, Infra-Level Checkpoint and Restore for Resilient AI/ML Workloads - Ganeshkumar Ashokavardhanan, Microsoft & Bernie Wu, MemVerge

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[AI ML]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Ganeshkumar Ashokavardhanan, Microsoft, Bernie Wu, MemVerge
- Schedule: https://kccnceu2025.sched.com/event/1tx7u/transparent-infra-level-checkpoint-and-restore-for-resilient-aiml-workloads-ganeshkumar-ashokavardhanan-microsoft-bernie-wu-memverge
- Busca YouTube: https://www.youtube.com/results?search_query=Transparent%2C+Infra-Level+Checkpoint+and+Restore+for+Resilient+AI%2FML+Workloads+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Transparent, Infra-Level Checkpoint and Restore for Resilient AI/ML Workloads.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx7u/transparent-infra-level-checkpoint-and-restore-for-resilient-aiml-workloads-ganeshkumar-ashokavardhanan-microsoft-bernie-wu-memverge
- YouTube search: https://www.youtube.com/results?search_query=Transparent%2C+Infra-Level+Checkpoint+and+Restore+for+Resilient+AI%2FML+Workloads+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3oWODC2mdk0
- YouTube title: Transparent, Infra-Level Checkpoint and Restore for Resil... Ganeshkumar Ashokavardhanan & Bernie Wu
- Match score: 0.786
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/transparent-infra-level-checkpoint-and-restore-for-resilient-ai-ml-wor/3oWODC2mdk0.txt
- Transcript chars: 33920
- Keywords: checkpoint, checkpointing, gpu, running, application, memory, workloads, process, restore, distributed, training, checkpointed, continue, maintenance, address, checkpoints, workload, actually

### Resumo baseado na transcript

Great to see you all on a Friday afternoon towards the end of the conference uh when you could be out in London enjoying the beautiful weather. Hi everyone, I'm with uh Bernie here and I'm Ganesh and we are going to be talking about intralevel transparent checkpointing for resilient a IML workloads. Uh on a personal note, I I live uh part-time in uh Hawaii, and I noticed that the culture of the Kubernetes community in Hawaii is very similar. In today's talk, we'll start off with a brief poll, then talk about the motivation for why we want to do this approach, and what are the other current approaches that people are taking to address these problems. Then we'll define what intralevel transparent checkpointing is, talk about uh use cases and limitations, and then Bernie will share about how it works and show some cool demos to see this in action. So about a third of users have less than or equal to 30% of GPU usage according to this uh survey and but how do we address these challenges um today and how can we make it better today many users are running GPU health

### Excerpt da transcript

Great to see you all on a Friday afternoon towards the end of the conference uh when you could be out in London enjoying the beautiful weather. Hi everyone, I'm with uh Bernie here and I'm Ganesh and we are going to be talking about intralevel transparent checkpointing for resilient a IML workloads. Uh believe it or not that is me uh without a beard and I am a software engineer in the Azure Kubernetes service team at Microsoft. Uh at AKS we run a managed uh Kubernetes service platform which allows you to run a variety of compute workloads uh including lots of ML training and inference workloads and we have users running these workloads at extremely large scales. I particularly work on GPU provisioning and making it easier to run a variety of GPU workloads on the platform. I've also previously worked on speeding up pod start time through a feature called artifact streaming. Yeah, my name is Birdie Woo. I'm the VP of technology partnerships for a company called Meverge. Mever is a uh Silicon Valley based uh startup uh that has software uh that we've developed that uh helps on memory virtualization and also checkpointing software.

Uh and so we're hoping to bring those two kinds of capabilities into the A IML area. Uh on a personal note, I I live uh part-time in uh Hawaii, and I noticed that the culture of the Kubernetes community in Hawaii is very similar. There's a there's a a very friendly culture uh uh one that helps each other. And uh and it's almost like an extended family or what we call Ohana in Hawaii. And uh we also in Hawaii, we like to welcome new people. That's called the Aloa spirit. So, one of these days I hope we'll have CubeCon over in in Hawaii. Anyway, back to you. Thank you. In today's talk, we'll start off with a brief poll, then talk about the motivation for why we want to do this approach, and what are the other current approaches that people are taking to address these problems. Then we'll define what intralevel transparent checkpointing is, talk about uh use cases and limitations, and then Bernie will share about how it works and show some cool demos to see this in action. And we'll also talk about some open areas that we could address together as a community.

For this part, I would really really love your participation. There'll be three questions. First one, how many of you have run GPU workloads in Kubernetes? Please raise your hands. Wow, that's great. Almost everyone here has done that uh as expected. And then uh how many of you
