---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "AI + ML"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability"]
speakers: ["Nic Vermande", "ScaleOps"]
sched_url: https://kccnceu2026.sched.com/event/2CVza/to-swap-or-not-to-swap-memory-management-design-patterns-for-ai-workloads-in-kubernetes-134+-nic-vermande-scaleops
youtube_search_url: https://www.youtube.com/results?search_query=To+Swap+or+Not+To+Swap%3A+Memory+Management+Design+Patterns+for+AI+Workloads+in+Kubernetes+1.34%2B+CNCF+KubeCon+2026
slides: []
status: parsed
---

# To Swap or Not To Swap: Memory Management Design Patterns for AI Workloads in Kubernetes 1.34+ - Nic Vermande, ScaleOps

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Nic Vermande, ScaleOps
- Schedule: https://kccnceu2026.sched.com/event/2CVza/to-swap-or-not-to-swap-memory-management-design-patterns-for-ai-workloads-in-kubernetes-134+-nic-vermande-scaleops
- Busca YouTube: https://www.youtube.com/results?search_query=To+Swap+or+Not+To+Swap%3A+Memory+Management+Design+Patterns+for+AI+Workloads+in+Kubernetes+1.34%2B+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre To Swap or Not To Swap: Memory Management Design Patterns for AI Workloads in Kubernetes 1.34+.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVza/to-swap-or-not-to-swap-memory-management-design-patterns-for-ai-workloads-in-kubernetes-134+-nic-vermande-scaleops
- YouTube search: https://www.youtube.com/results?search_query=To+Swap+or+Not+To+Swap%3A+Memory+Management+Design+Patterns+for+AI+Workloads+in+Kubernetes+1.34%2B+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Go3JMhvAhlc
- YouTube title: To Swap or Not To Swap: Memory Management Design Patterns for AI Workloads in Kuber... Nic Vermande
- Match score: 0.989
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/to-swap-or-not-to-swap-memory-management-design-patterns-for-ai-worklo/Go3JMhvAhlc.txt
- Transcript chars: 26980
- Keywords: memory, gpu, request, workloads, second, limited, latency, inference, workload, capacity, everything, scenario, cgroup, enable, essentially, configuration, utilization, container

### Resumo baseado na transcript

Second day for almost all, first day for some of you, second day for other who were already there yesterday for the KubeCon event. Eight times latency degradation every inference request can be eight times slower, 1.6 GB of memory thrashing between RAM and disk on a single misconfigured Kubernetes nodes. So quickly ScaleOps may help you with a lot of things we're going to see today. I really I didn't run everything at super large large scale, but when it's not the case, I will have, you know, I will tell you, "Okay, this is small scale most small scale. At large scale, this is what you will see, right?" So I run control experiments with swap on GP nodes, different workload types, different storage backends, different QoS configuration. Um so I'm going to show you three main scenario and give you a decision framework when swap swap helps, when it destroys performance, um and when actually bad sizing swap is worse than having no swap at all, right?

### Excerpt da transcript

Okay. Hi everyone. Hopefully you had a good lunch. Very happy to be here. Second day for almost all, first day for some of you, second day for other who were already there yesterday for the KubeCon event. So hope you guys enjoying your time. So let's get started. Eight times latency degradation every inference request can be eight times slower, 1.6 GB of memory thrashing between RAM and disk on a single misconfigured Kubernetes nodes. So quick show of hands, uh who here has been told by your ops team or platform team that they should never enable swap on a Kubernetes nodes? Yeah, or yourself. All right. What about the rest? Like you guys think you can enable swap and everything is going to be magic or All right. No, it's not going to be magic. Uh I would say like now who, you know, keep your hands up for some people but not enough of you have their hands up. So I'm just going to tell you something. You're going to face this problem if you're going to enable enable swap and GPU in one to run LLM workloads in Kubernetes.

Obviously at some point to save you some bad time in terms of OOM kills, the first thing that you would want to do is increase the number of nodes or increase GPU resources to manage LLM workloads. Why is that? We're going to see it, but at some point the biggest risk is OOM kill. Not necessarily OOM kill in terms of setting a limit, but also just filling up a whole node. So some people they say, "Okay, now I'll just have, you know, more node so it's, you know, I will have more space. Therefore wasting money." So the goal of today is really about that. How can swap enable you to run LLM workloads in a way that is more, you know, smarter. And we're going to go through different use case when it's good to do it, when it's bad to do it, all those kind of things. So here swap versus LLM workloads, it's essentially the contradiction I spent the last couple of month, I would say, investigating. So my name is Nick. I'm a DevRel at ScaleOps. So quickly ScaleOps may help you with a lot of things we're going to see today.

We are do doing resource optimization at Scale. We can help you with GPU, CPU. For some of the use cases I'm going to mention how it would do like without us and quick the value we can add to make your life easier, right? That's essentially the idea here. Um so I uh it's mainly a lot of benchmarks, a lot of number because usually I like to talk about thing I test myself for a long period of time. So this is essentially the results
