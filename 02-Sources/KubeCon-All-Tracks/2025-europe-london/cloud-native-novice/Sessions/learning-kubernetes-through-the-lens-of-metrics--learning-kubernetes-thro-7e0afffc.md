---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Cloud Native Novice"
themes: ["Observability", "Kubernetes Core"]
speakers: ["Priyanka Saggu", "SUSE", "Mario Jason Braganza", "Janusworx"]
sched_url: https://kccnceu2025.sched.com/event/1txG2/learning-kubernetes-through-the-lens-of-metrics-priyanka-saggu-suse-mario-jason-braganza-janusworx
youtube_search_url: https://www.youtube.com/results?search_query=Learning+Kubernetes+Through+the+Lens+of+Metrics+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Learning Kubernetes Through the Lens of Metrics - Priyanka Saggu, SUSE & Mario Jason Braganza, Janusworx

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[Observability]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Priyanka Saggu, SUSE, Mario Jason Braganza, Janusworx
- Schedule: https://kccnceu2025.sched.com/event/1txG2/learning-kubernetes-through-the-lens-of-metrics-priyanka-saggu-suse-mario-jason-braganza-janusworx
- Busca YouTube: https://www.youtube.com/results?search_query=Learning+Kubernetes+Through+the+Lens+of+Metrics+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Learning Kubernetes Through the Lens of Metrics.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txG2/learning-kubernetes-through-the-lens-of-metrics-priyanka-saggu-suse-mario-jason-braganza-janusworx
- YouTube search: https://www.youtube.com/results?search_query=Learning+Kubernetes+Through+the+Lens+of+Metrics+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=95NNuV-SUdg
- YouTube title: Learning Kubernetes Through the Lens of Metrics - Priyanka Saggu & Mario Jason Braganza
- Match score: 0.803
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/learning-kubernetes-through-the-lens-of-metrics/95NNuV-SUdg.txt
- Transcript chars: 19650
- Keywords: metrics, cluster, information, running, metric, cublet, container, hidden, version, enabled, control, giving, server, number, docker, prometheus, learning, learned

### Resumo baseado na transcript

So hello, good evening and welcome to the last talk of the first day of CubeCon London 2025. I serve as an independent consultant to small and medium businesses in Bombay, India. What this talk is not is a guide to metrics or to writing metrics efficiently. So what it is is about the interesting things we learned and the path of discovery we took to get there. Uh did you know that Kubernetes metrics can tell you which features are enabled in your cluster with alpha or beta or stable or reveal how many pods a a cublet is running, how many are waiting to be scheduled, how much byte space, container logs consume in your cluster. We're using the anecdotes themselves as guides and we'll walk through a few interesting metrics and the lessons we learned.

### Excerpt da transcript

So hello, good evening and welcome to the last talk of the first day of CubeCon London 2025. Uh I'm Jason Banza. I serve as an independent consultant to small and medium businesses in Bombay, India. Uh hi everyone, my name is Priyanka Sagu. I work at Souza as a Kubernetes integration engineer and uh I'm also part of the Kubernetes upstream project. I'm one of the technical leads for uh Kubernetes SIG contributor experience. So we're talking today about learning Kubernetes through the lens of metrics. It's all about what we learned about Kubernetes through the various uh as as we go about learning stuff like this talk is a spiritual kin to our last talk on CAPS where we spoke about uh what we learned about Kubernetes while uh going through the Kubernetes uh enhancement uh process documents. Uh you can find the recording here. Most of the footnotes and the links that we talk about if we say they're online, you can find them in a little thing there. So like I said, this is a new lens on learning Kubernetes uh and the stuff we learned tinkering with Kubernetes clusters.

What this talk is not is a guide to metrics or to writing metrics efficiently. It's more about what we groed uh exploring metrics. So what it is is about the interesting things we learned and the path of discovery we took to get there. So let's begin. Uh did you know that Kubernetes metrics can tell you which features are enabled in your cluster with alpha or beta or stable or reveal how many pods a a cublet is running, how many are waiting to be scheduled, how much byte space, container logs consume in your cluster. They can even track meods live go routines or the latest HCD compaction uh revision. So these seemingly small data points hold huge insights and that's just scratching the surface. Uh here's the thing. There's too many metrics out there in the world in the cube world. So and there's no good a toz guide to go through them. So all of this uh is basically the stuff that we found. We're using the anecdotes themselves as guides and we'll walk through a few interesting metrics and the lessons we learned.

So the structure of a metric itself as exposed by Kubernetes looks a little something like this. There's obviously the name uh as as we've seen but then it also com like we've kind of decomposed it into these four sections. The first one is the help section which gives us the definition of the metric when you look at it. Uh there's the type of the metric. Uh there are various types lik
