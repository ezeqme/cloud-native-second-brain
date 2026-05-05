---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Operations + Performance"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability"]
speakers: ["Alex Jones", "AWS", "Anais Urlichs", "JP Morgan Chase"]
sched_url: https://kccnceu2025.sched.com/event/1tx86/superpowers-for-humans-of-kubernetes-how-k8sgpt-is-transforming-enterprise-ops-alex-jones-aws-anais-urlichs-jp-morgan-chase
youtube_search_url: https://www.youtube.com/results?search_query=Superpowers+for+Humans+of+Kubernetes%3A+How+K8sGPT+Is+Transforming+Enterprise+Ops+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Superpowers for Humans of Kubernetes: How K8sGPT Is Transforming Enterprise Ops - Alex Jones, AWS & Anais Urlichs, JP Morgan Chase

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Alex Jones, AWS, Anais Urlichs, JP Morgan Chase
- Schedule: https://kccnceu2025.sched.com/event/1tx86/superpowers-for-humans-of-kubernetes-how-k8sgpt-is-transforming-enterprise-ops-alex-jones-aws-anais-urlichs-jp-morgan-chase
- Busca YouTube: https://www.youtube.com/results?search_query=Superpowers+for+Humans+of+Kubernetes%3A+How+K8sGPT+Is+Transforming+Enterprise+Ops+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Superpowers for Humans of Kubernetes: How K8sGPT Is Transforming Enterprise Ops.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx86/superpowers-for-humans-of-kubernetes-how-k8sgpt-is-transforming-enterprise-ops-alex-jones-aws-anais-urlichs-jp-morgan-chase
- YouTube search: https://www.youtube.com/results?search_query=Superpowers+for+Humans+of+Kubernetes%3A+How+K8sGPT+Is+Transforming+Enterprise+Ops+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=EXtCejkOJB0
- YouTube title: Superpowers for Humans of Kubernetes: How K8sGPT Is Transforming Enter... Alex Jones & Anais Urlichs
- Match score: 0.929
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/superpowers-for-humans-of-kubernetes-how-k8sgpt-is-transforming-enterp/EXtCejkOJB0.txt
- Transcript chars: 29076
- Keywords: knowledge, within, cluster, tooling, remediation, infrastructure, little, actually, effectively, result, deployment, platform, engineering, components, environments, excited, working, resources

### Resumo baseado na transcript

Um, too many CubeCons have been in other wonderful countries, but it's great to be here. If you're joining us from overseas, go to the barbec, go to the South Bank, go get some beer. We want to maximize developer developer efficiency and we want to maximize cost savings. So we want to scale ourselves out of our job to ultimately maximize efficiency within our workflows and not linearly scale our platform engineering team alongside of our workloads. If you've been here yesterday at AOCon you might have learned more about Argo CD as a GitOps tool. Now this all sounds amazing to basically build zero touch environments that just scale yourself out of the job so you can focus on your long-term goals.

### Excerpt da transcript

Hi everyone, welcome. Thank you so much for joining us today. It's a real pleasure to be in London. Um, too many CubeCons have been in other wonderful countries, but it's great to be here. If you're joining us from overseas, go to the barbec, go to the South Bank, go get some beer. It's a great place to to be, especially in this lovely weather. But I'm delighted you've joined us in this dark, cold room to talk about KGBT. It's a real testament to your effort. So, thank you very much for that. Um, we're really excited to talk to you about KCT today because there's going to be a portion of the room that's never heard of it. There'll be a segment of the room that might have heard of it and there'll be a few people that have probably used it in a bit of anger. What you probably don't know is there are a bunch of companies assisting us behind the scenes to make it better and better on prem in the cloud for single operators and for entire teams. and we believe that it's having a very subtle yet profound impact on the ecosystem for platform engineering and beyond.

So, let me introduce myself. Uh, my name is Alex Jones. I'm a a principal engineer at AWS, but I'm speaking about my u my my beloved project that I started two years ago out of frustration of being an S sur wanting to effectively codify go tests into slightly more integration-y tests and that eventually evolved into a set of a suite of behavioral tests that eventually was the uh the the start of case GBT. Good afternoon everyone. My name is Anesles. I'm a platform engineer at the accelerator at JP Morgan Chase here in London. Now, anything I'm sharing within this presentation has nothing to do with my employer or my day-to-day work. To get started, I want to ask you a few questions. Who here is using cloudnative open source technologies within their stack? Hands up. Okay. Most of you, I assume. I hope so. If you're at CubeCon. Um, now what technologies are you most excited about? Just scream. KGB. What else? Envoy, Prometheus, Kubernetes. What are you excited about? Tell me. Okay. I hope at the end of this presentation you will show the next time Kate's GBT.

Now, who here, last question. Who here is working or has experience working in a highly constrained regulated environment, an industry where you have to ensure that you are abiding by the the regulations within that industry. Okay. Several cool. Um now a lot of times when we as engineers identify new toolings that can help us within our job within
