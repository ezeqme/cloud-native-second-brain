---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Damien Grisonnet", "Red Hat"]
sched_url: https://kccnceu2023.sched.com/event/1HyRq/sig-instrumentation-introduction-and-deep-dive-damien-grisonnet-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=SIG+Instrumentation+Introduction+and+Deep+Dive+CNCF+KubeCon+2023
slides: []
status: parsed
---

# SIG Instrumentation Introduction and Deep Dive - Damien Grisonnet, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Damien Grisonnet, Red Hat
- Schedule: https://kccnceu2023.sched.com/event/1HyRq/sig-instrumentation-introduction-and-deep-dive-damien-grisonnet-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=SIG+Instrumentation+Introduction+and+Deep+Dive+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre SIG Instrumentation Introduction and Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyRq/sig-instrumentation-introduction-and-deep-dive-damien-grisonnet-red-hat
- YouTube search: https://www.youtube.com/results?search_query=SIG+Instrumentation+Introduction+and+Deep+Dive+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=BYQxStXTqeA
- YouTube title: SIG Instrumentation Introduction and Deep Dive - Damien Grisonnet, Red Hat
- Match score: 0.866
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/sig-instrumentation-introduction-and-deep-dive/BYQxStXTqeA.txt
- Transcript chars: 30048
- Keywords: metrics, server, logging, metric, logs, support, request, matrix, traces, tracing, pretty, better, instrumentation, software, anything, expose, change, primitives

### Resumo baseado na transcript

all right welcome everyone and I hope you've had a great kubecon so far I guess it will be kind of one of the last talks you will attend and I hope it will be fine and not that boring as well um so what I will go through today is seek instrumentation uh and a quick introduction and a deep dive as well as kind of an update about our group um and who am I to to presenting instrumentation so I'm Deborah grizone um I'm a software engineer way to have structured logs but with a context so when you would the idea was that when you would produce a log you could attach to the logger a certain contact let's say a value or any kind of data that you want and propagate it through your calls in order to make sure that you set a value through the audio called sites this was adding kubernetes as Alpha in 124 and it's currently planned to become better in 128. your logs already contain this information and there was no way to ensure that so that's the goal of contextual logging and one more futuristic goal would be to also attach let's say a span ID for tracing our Trace ID in order to have correlation between logging and tracing made super easily um and yeah now the goal is to really migrate the code base to both structure logging and contextual logging and we are actively looking for contributors to help us do that um so there is a

### Excerpt da transcript

all right welcome everyone and I hope you've had a great kubecon so far I guess it will be kind of one of the last talks you will attend and I hope it will be fine and not that boring as well um so what I will go through today is seek instrumentation uh and a quick introduction and a deep dive as well as kind of an update about our group um and who am I to to presenting instrumentation so I'm Deborah grizone um I'm a software engineer for Reddit and I'm also the kubernetes instrumentation technique or at least one of the two tech leads of the group and I also maintain projects such as cube State metric metric server and parameters adapter that you may know and you can reach out to me on this available or LinkedIn um you know my handles um and so like um I don't know how much you are aware about six in general and singing instrumentation as well so I will go through what is this again what we are doing in C instrumentation what are the sub project that we own the different signals that we own as well as part of our group how you could help us and contribute and where then you can find us and just chat about anything really so what do we do so is Sig in kubernetes is a group that has a definite task and a definite area of expertise in our case we have a charter that tells us that we have to cover the best practices for cluster observability across all the kubernetes component and develop the relevant components that we need in order to spread those practices so we don't own the signals as such so we don't own Matrix for all the components but what we own is the libraries that we then provide to the different developers to help them improve their signal and build a better obserability as a whole so to do that we first have our sub project that we also support maintain as well as kind of oversee so er like the three main ones I would say cubesat metric uh State metric is to get any kind of metrics about your kubernetes resources klog is the logging library that we use to produce any kind of logging kubernetes and metrics of it is what you would use for auto scaling and we have many more I will go a bit more in through the details of a couple of them later but that's what we do as part of our sub projects and then the various signals that you can see on the daily basis in obserability uh we try to cover metrics in kubernetes as well as logging and events events are some kind of logs a bit more structure we could say and in logging like we nowadays do more on st
