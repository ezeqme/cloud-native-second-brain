---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "AI + ML"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Xiao Zhang", "DaoCloud", "Mengxuan Li", "The 4th paradigm", "Ltd"]
sched_url: https://kccnceu2025.sched.com/event/1txAf/unlocking-how-to-efficiently-flexibly-manage-and-schedule-seven-ai-chips-in-kubernetes-xiao-zhang-daocloud-mengxuan-li-the-4th-paradigm-ltd
youtube_search_url: https://www.youtube.com/results?search_query=Unlocking+How+To+Efficiently%2C+Flexibly%2C+Manage+and+Schedule+Seven+AI+Chips+in+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Unlocking How To Efficiently, Flexibly, Manage and Schedule Seven AI Chips in Kubernetes - Xiao Zhang, DaoCloud & Mengxuan Li, The 4th paradigm, Ltd

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Xiao Zhang, DaoCloud, Mengxuan Li, The 4th paradigm, Ltd
- Schedule: https://kccnceu2025.sched.com/event/1txAf/unlocking-how-to-efficiently-flexibly-manage-and-schedule-seven-ai-chips-in-kubernetes-xiao-zhang-daocloud-mengxuan-li-the-4th-paradigm-ltd
- Busca YouTube: https://www.youtube.com/results?search_query=Unlocking+How+To+Efficiently%2C+Flexibly%2C+Manage+and+Schedule+Seven+AI+Chips+in+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Unlocking How To Efficiently, Flexibly, Manage and Schedule Seven AI Chips in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txAf/unlocking-how-to-efficiently-flexibly-manage-and-schedule-seven-ai-chips-in-kubernetes-xiao-zhang-daocloud-mengxuan-li-the-4th-paradigm-ltd
- YouTube search: https://www.youtube.com/results?search_query=Unlocking+How+To+Efficiently%2C+Flexibly%2C+Manage+and+Schedule+Seven+AI+Chips+in+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=VAWw5CujiR8
- YouTube title: Unlocking How To Efficiently, Flexibly, Manage and Schedule Seven AI Chi... Xiao Zhang & Mengxuan Li
- Match score: 0.907
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/unlocking-how-to-efficiently-flexibly-manage-and-schedule-seven-ai-chi/VAWw5CujiR8.txt
- Transcript chars: 15179
- Keywords: gpu, device, memory, nvidia, resource, schedule, scheduling, inside, scheduleuler, support, priority, container, utilization, multiple, extender, sharing, specify, volcano

### Resumo baseado na transcript

Hello everyone, welcome to our session and and this session is about unlocking how to efficiently flexibility and manage the seven AI chips in Kubernetes. It is a rather abstract title but uh in one in one sentence it can be sound like how to improve your GPU utilization in Kubernetes. This will cause the performance of the Kubernetes scheduling is very poor. It is stabled in 1.32 version in Kubernetes and it is um and you need to set a resource claim and the resource class and every device vendor need to implement their own resource DRA driver and it communicate with Kublet to do the uh device sharing and uh uh scheduling and allocating but it has many restrictions. The first is it has it it requires the Kubernetes version must be the latest. It means 132i uh Kubernetes and it has to and it has happens to me that not many device vendors implements DIA driver for now.

### Excerpt da transcript

Hello everyone, welcome to our session and and this session is about unlocking how to efficiently flexibility and manage the seven AI chips in Kubernetes. It is a rather abstract title but uh in one in one sentence it can be sound like how to improve your GPU utilization in Kubernetes. Yes, this session is brought is brought to you by two software engineers. My name is Lemon. This is my colleague Junga. We are both from a new founded company called Dynamia Point AI. And here are the Let me let me first introduce to you the background. The first background is the burst requirement for computing power. The global GPU marketing growth is over 60% than last year. The mo majority is majority growth is Nvidia and the heterogeneous is over 20% as you can see in in this figure it has been rather boost after the emergence of large language models and uh you may guess we are from the mainland China so so uh in our country the highspec Nvidia can't can't be imported very easily so we have to use uh alternative cards like these device vendors.

They are they are all some alternative plan for Nvidia cards and of course they are not as highspec as Nvidia and the user pre user experiences may not be as good as Nvidia but they but it is very cheap so it so we can use them in the production level as well and it has a decent performance. Yes. But we here we meet a challenge is that the GPU can't be shared in a traditional Kubernetes and suppose you have five GPUs each with the capacity of 40 40G device memory and it is all running uh 2G little mode small model and it will cause the all the device be not not be able to fit more ports other than this one. So the other part which uses CPU are in a pending state which cause the utilization of GPU in the cluster is very low. And another challenge is the management of heterogeneous clusters. As you can see, there are multiple device vendors in China and many of them imple implement their own scheduleuler extender and it hijacked the filter hijack the score process and you have and you have a and if you have a cluster composed of multiore AI cards then you have to install their schedule extenders and you have a more sc scheduling pipeline and if you enter the filter you have first go through the multiple extenders and go back to the filter.

computer and then into the score process you you still need to go through all the extenders and return to the score. This will cause the performance of the Kubernetes scheduling is very poor.
