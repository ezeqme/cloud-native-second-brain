---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Platform Engineering"
themes: ["AI ML", "Platform Engineering"]
speakers: ["Abhishek Malvankar", "Olivier Tardieu", "IBM"]
sched_url: https://kccnceu2024.sched.com/event/1YeO0/unleashing-the-power-of-dra-dynamic-resource-allocation-for-just-in-time-gpu-slicing-abhishek-malvankar-olivier-tardieu-ibm
youtube_search_url: https://www.youtube.com/results?search_query=Unleashing+the+Power+of+DRA+%28Dynamic+Resource+Allocation%29+for+Just-in-Time+GPU+Slicing+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Unleashing the Power of DRA (Dynamic Resource Allocation) for Just-in-Time GPU Slicing - Abhishek Malvankar & Olivier Tardieu, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]]
- País/cidade: France / Paris
- Speakers: Abhishek Malvankar, Olivier Tardieu, IBM
- Schedule: https://kccnceu2024.sched.com/event/1YeO0/unleashing-the-power-of-dra-dynamic-resource-allocation-for-just-in-time-gpu-slicing-abhishek-malvankar-olivier-tardieu-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=Unleashing+the+Power+of+DRA+%28Dynamic+Resource+Allocation%29+for+Just-in-Time+GPU+Slicing+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Unleashing the Power of DRA (Dynamic Resource Allocation) for Just-in-Time GPU Slicing.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeO0/unleashing-the-power-of-dra-dynamic-resource-allocation-for-just-in-time-gpu-slicing-abhishek-malvankar-olivier-tardieu-ibm
- YouTube search: https://www.youtube.com/results?search_query=Unleashing+the+Power+of+DRA+%28Dynamic+Resource+Allocation%29+for+Just-in-Time+GPU+Slicing+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hk2R51pw-Xg
- YouTube title: Unleashing the Power of DRA (Dynamic Resource Allocation) for Just-in-Time GPU Slicing
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/unleashing-the-power-of-dra-dynamic-resource-allocation-for-just-in-ti/hk2R51pw-Xg.txt
- Transcript chars: 32616
- Keywords: gpu, resource, cluster, claims, placement, workload, controller, allocation, object, nvidia, resources, immediate, dynamic, changes, change, operator, scheduler, instance

### Resumo baseado na transcript

good morning uh Welcome to our s session um my name is Olivia T I'm a principal uh research scientist and manager at IBM and today I'm joined with by abishek malvankar who is a senior software developer at IBM research and the two of us are very excited to tell you uh about our experience about the lessons we learned trying to use Dynamic resource allocation for improving GPU utilizations on our uh kuties clusters so uh in this talk I'll start by briefly uh talking about motivations uh

### Excerpt da transcript

good morning uh Welcome to our s session um my name is Olivia T I'm a principal uh research scientist and manager at IBM and today I'm joined with by abishek malvankar who is a senior software developer at IBM research and the two of us are very excited to tell you uh about our experience about the lessons we learned trying to use Dynamic resource allocation for improving GPU utilizations on our uh kuties clusters so uh in this talk I'll start by briefly uh talking about motivations uh inference servers the the the workload that you know led us on this journey towards using Dynamic resource allocation I'll talk about multi-instance gpus and then we'll dive into Dynamic resource allocation I'll talk about what it changes from the perspective of kuani users uh or cluster owners and I'll introduce insta slice which is a piece of code work contributing to the community that is you know par paradoxically trying to make sure that nothing changes uh that will become clear in a second and after that abishek will walk you through uh not just uh What uh jir is doing but how it's working its mechanics and what we've been trying to do to improve on the outof thebox experience with scheduling latencies and placement strategies so in the last couple of years at IBM research we've been developing uh an inference server service a large you know inference service that I think today is ranging over about 100 he100 Nvidia gpus and we use the service as a platform for experimentation with models with serving technology and so on and it serves uh constantly varying evolving collection of machine learning models some of them very big with you know hundreds of billions of parameters and some of them relatively small by today's standards with just a let's say a couple million parameters we've talked already twice this week about this uh inference service here's one of the talk on the slides there's another one if you want more uh specifics more details about this workload and this service you can find a lot more statistics in these stocks but from the purpose of these stocks what is of interest uh to me today is that some of these models are small they can uh they only require a fraction of a GPU to run and so of course in order to maximize GP utilization we like to uh pack many models on uh the same GPU and you have different ways to go after that but this is cubec Con So today we're going to talk about kubernetes Native mechanism to do that hi he how can I run multiple containe
