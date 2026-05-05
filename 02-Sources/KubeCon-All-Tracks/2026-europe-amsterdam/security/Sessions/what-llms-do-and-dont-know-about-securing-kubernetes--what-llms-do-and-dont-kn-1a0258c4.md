---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Security"
themes: ["AI ML", "Security", "Storage Data", "Kubernetes Core"]
speakers: ["Rory McCune", "Datadog"]
sched_url: https://kccnceu2026.sched.com/event/2CVyo/what-llms-do-and-dont-know-about-securing-kubernetes-rory-mccune-datadog
youtube_search_url: https://www.youtube.com/results?search_query=What+LLMs+Do%2C+and+Don%27t%2C+Know+About+Securing+Kubernetes+CNCF+KubeCon+2026
slides: []
status: parsed
---

# What LLMs Do, and Don't, Know About Securing Kubernetes - Rory McCune, Datadog

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]], [[Storage Data]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Rory McCune, Datadog
- Schedule: https://kccnceu2026.sched.com/event/2CVyo/what-llms-do-and-dont-know-about-securing-kubernetes-rory-mccune-datadog
- Busca YouTube: https://www.youtube.com/results?search_query=What+LLMs+Do%2C+and+Don%27t%2C+Know+About+Securing+Kubernetes+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre What LLMs Do, and Don't, Know About Securing Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVyo/what-llms-do-and-dont-know-about-securing-kubernetes-rory-mccune-datadog
- YouTube search: https://www.youtube.com/results?search_query=What+LLMs+Do%2C+and+Don%27t%2C+Know+About+Securing+Kubernetes+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jgx4J1z7POM
- YouTube title: What LLMs Do, and Don't, Know About Securing Kubernetes - Rory McCune, Datadog
- Match score: 0.919
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/what-llms-do-and-dont-know-about-securing-kubernetes/jgx4J1z7POM.txt
- Transcript chars: 31247
- Keywords: security, models, actually, cluster, question, interesting, container, answer, results, winner, wanted, clusters, fairly, create, manifest, arbback, skills, thought

### Resumo baseado na transcript

Good afternoon everyone and welcome along uh to this talk about LLMs and Kubernetes security. The more keen eyed of you might have noticed if you've looked at the schedule or been out on the booths, there's the odd mention of LLMs and Agentic AI and whenever we get a new technology there's a question of well how well does it work in reality? I'm also one of the authors of the OASP Kubernetes top 10 which we only just released last week. So if you're interested in OASP top 10s uh and the Kubernetes top 10, please come along to the SIG security session. we have on Thursday where we'll be talking more about it and obviously yeah I'm also a member of Kubernetes SIG security so when I wanted to work out this answer you know how good are these things at Kubernetes security I had to think Can you say to an agent hey could you harden my Kubernetes cluster for me?

### Excerpt da transcript

Good afternoon everyone and welcome along uh to this talk about LLMs and Kubernetes security. The more keen eyed of you might have noticed if you've looked at the schedule or been out on the booths, there's the odd mention of LLMs and Agentic AI and whenever we get a new technology there's a question of well how well does it work in reality? And I wanted to try and take a shot at answering that question for LLMs and Kubernetes security. So what I want to do today is just talk you through uh some experiments that I came up with to try and answer that question. some examples of where the tools work, where they succeed. Possibly more interesting, some examples of where they fail and how they fail, but also to give you some practical advice for if you are going to use this kind of tool for Kubernetes security related tasks. What should you think about? How should you approach it? So, before I get into it, just a very quick about me. Why am I up here talking about this? Uh, I've been in security, whatever we're calling it these days, for a bit over 25 years now.

last 10 or 11 of those focusing on Kubernetes and container security. Uh I'm a senior security researcher and advocate for data dog and I do a couple of things to help out in the container security community. I'm one of the authors of the CIS benchmarks for Docker and Kubernetes. I'm also one of the authors of the OASP Kubernetes top 10 which we only just released last week. So if you're interested in OASP top 10s uh and the Kubernetes top 10, please come along to the SIG security session. we have on Thursday where we'll be talking more about it and obviously yeah I'm also a member of Kubernetes SIG security so when I wanted to work out this answer you know how good are these things at Kubernetes security I had to think of well how am I going to prove that what could I do that would help me establish some ideas on where they work and where they fail so I gave it some thought and came up with some ideas and I came up with four different types of tests the first thing I thought of is nobody likes writing YAML, right?

So, we're probably going to try and get LLM to do that for us so we don't have to write YAML anymore. How well does that work? Do these tools write YAML well? Do they do well with the security of the manifest they generate? The second thing I had an idea of was a quiz. Everyone loves a quiz. What could we do in terms of creating a quiz that told us where the borders of their knowledge was?
