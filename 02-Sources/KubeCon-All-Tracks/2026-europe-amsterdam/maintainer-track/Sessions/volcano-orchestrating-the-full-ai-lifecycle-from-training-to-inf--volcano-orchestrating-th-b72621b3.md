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
themes: ["AI ML", "Community Governance"]
speakers: ["Chen Zicong", "Huawei Technologies", "Hajnal Máté", "Aumovio"]
sched_url: https://kccnceu2026.sched.com/event/2EF5S/volcano-orchestrating-the-full-ai-lifecycle-from-training-to-inference-and-agents-chen-zicong-huawei-technologies-hajnal-mate-aumovio
youtube_search_url: https://www.youtube.com/results?search_query=Volcano%3A+Orchestrating+the+Full+AI+Lifecycle+%E2%80%93+From+Training+To+Inference+and+Agents+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Volcano: Orchestrating the Full AI Lifecycle – From Training To Inference and Agents - Chen Zicong, Huawei Technologies; Hajnal Máté, Aumovio

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Chen Zicong, Huawei Technologies, Hajnal Máté, Aumovio
- Schedule: https://kccnceu2026.sched.com/event/2EF5S/volcano-orchestrating-the-full-ai-lifecycle-from-training-to-inference-and-agents-chen-zicong-huawei-technologies-hajnal-mate-aumovio
- Busca YouTube: https://www.youtube.com/results?search_query=Volcano%3A+Orchestrating+the+Full+AI+Lifecycle+%E2%80%93+From+Training+To+Inference+and+Agents+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Volcano: Orchestrating the Full AI Lifecycle – From Training To Inference and Agents.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF5S/volcano-orchestrating-the-full-ai-lifecycle-from-training-to-inference-and-agents-chen-zicong-huawei-technologies-hajnal-mate-aumovio
- YouTube search: https://www.youtube.com/results?search_query=Volcano%3A+Orchestrating+the+Full+AI+Lifecycle+%E2%80%93+From+Training+To+Inference+and+Agents+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=mzA0yuZ4QuY
- YouTube title: Volcano: Orchestrating the Full AI Lifecycle – From Training To Inferen... Chen Zicong & Hajnal Máté
- Match score: 0.917
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/volcano-orchestrating-the-full-ai-lifecycle-from-training-to-inference/mzA0yuZ4QuY.txt
- Transcript chars: 23123
- Keywords: volcano, scheduling, workloads, topology, cluster, network, platform, schedule, training, scheduler, actually, unified, support, latency, native, picture, multicluster, decode

### Resumo baseado na transcript

Thanks for joining us today on the on the maintainer tech uh maintainers track. Uh we will speak about volcano um how it's orchestrating the full uh AI life cycle. It has a queue management um system which uh which is able to handle multi-level cues uh in a in a in a Kubernetes cluster and uh also uh it has a really unique feature which is called workloads collocation. A few years ago um we had uh batch training um uh workloads mainly dominated on the Kubernetes ecosystem um which we were actually uh handling and uh recently in 2023 uh we started seeing these massive LLM distributed training workloads on the clusters and with that the ca the agentic workloads uh came into the picture which are short-lived latency sensitive and extremely bursty um yeah so these these uh these different characteristics uh bring new challenges and and uh we can't really uh optimize both for uh latency It's it's a really really hard challenge and and to tackle these challenges we we need to evolve fast.

### Excerpt da transcript

Hello. Hello everyone. So um let's uh let's get started. Thanks for joining us today on the on the maintainer tech uh maintainers track. Uh we will speak about volcano um how it's orchestrating the full uh AI life cycle. Uh our focus here won't be just one product in isolation. It is a the full AI life cycle from training to inference and uh and highly bursty agents in the end. But uh before we start uh a quick uh speaker introduction uh let us introduce ourselves. My colleague here is uh Chong. >> Yeah. >> You can call me Jesse. Yeah. >> Yeah. I will call him Jesse too because that's what that's his GitHub handle. Um he's an R&D engineer and volcano maintainer from Huavi Technologies. Um and I'm myself uh is Matty Hel a senior machine learnings engineer at Movio and a core working a contributor recently uh we have worked worked together on a lot of features um let's move uh to the agenda what we will have today um I will cover uh the big picture uh the volcano evolution uh we will start with that that how we evolved uh evolved to a unified batch scheduling system uh scheduling platform from just being a simple simple uh batch scheduler.

After that we will jump uh into the scalable and efficient foundation we tried to lay down in volcano in general in uh into the past few years and uh uh we will extend that knowledge uh with the the topology of our uh section. Uh so I will cover these parts and uh the next uh part will be about kina an enterprisegrade uh llm serving platform um and the agent cube a cloudnative agent and code inter interpreter platform and volcano global the component that's capable of multicluster federation and these uh these these will be covered by Jesse so uh volcano as I said earlier evolved from uh The cube batch project uh it was developed throughout the years uh from being just a standard batch system to be a greater unified scheduling platform. Um just a little history uh it became part of the CNCF volcan the CNCF volcano became part of uh the CNCF ecosystem in uh 2020 and uh two years after it's reached a maturity level of being an incubating project uh in the CNCF foundation and in 2026 this year we really want to achieve a graduated status.

Um so uh some listeners may not be familiar with the volcano in general but uh uh let's just uh go through a little bit that what it's capable of doing. So uh it's a unified scheduling platform. It's it's it it supports just a wide variety of workloads. uh we can we are integrated with Ten
