---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Frederic Branczyk", "Polar Signals"]
sched_url: https://kccnceu2021.sched.com/event/iE8c/intro-and-deep-dive-kubernetes-sig-instrumentation-frederic-branczyk-polar-signals
youtube_search_url: https://www.youtube.com/results?search_query=Intro+and+Deep+Dive%3A+Kubernetes+SIG+Instrumentation+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Intro and Deep Dive: Kubernetes SIG Instrumentation - Frederic Branczyk, Polar Signals

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Frederic Branczyk, Polar Signals
- Schedule: https://kccnceu2021.sched.com/event/iE8c/intro-and-deep-dive-kubernetes-sig-instrumentation-frederic-branczyk-polar-signals
- Busca YouTube: https://www.youtube.com/results?search_query=Intro+and+Deep+Dive%3A+Kubernetes+SIG+Instrumentation+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Intro and Deep Dive: Kubernetes SIG Instrumentation.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE8c/intro-and-deep-dive-kubernetes-sig-instrumentation-frederic-branczyk-polar-signals
- YouTube search: https://www.youtube.com/results?search_query=Intro+and+Deep+Dive%3A+Kubernetes+SIG+Instrumentation+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=4yTdJph2Knk
- YouTube title: Intro and Deep Dive: Kubernetes SIG Instrumentation - Frederic Branczyk, Polar Signals
- Match score: 0.838
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/intro-and-deep-dive-kubernetes-sig-instrumentation/4yTdJph2Knk.txt
- Transcript chars: 21364
- Keywords: metrics, essentially, prometheus, instrumentation, actually, within, already, logging, metric, interested, working, server, meetings, started, tracing, necessarily, couple, particular

### Resumo baseado na transcript

all right welcome everyone to the sick instrumentation session um i'm frederick i am uh the ceo and founder of polar signals um i've been working on kubernetes things for the past over five years now i am also a prometheus maintainer i generally do pretty much everything in the intersection of observability monitoring and kubernetes and so um if you've uh you're using any of the tools kind of in that intersection there's a good chance that i might have touched them um over the past five years um

### Excerpt da transcript

all right welcome everyone to the sick instrumentation session um i'm frederick i am uh the ceo and founder of polar signals um i've been working on kubernetes things for the past over five years now i am also a prometheus maintainer i generally do pretty much everything in the intersection of observability monitoring and kubernetes and so um if you've uh you're using any of the tools kind of in that intersection there's a good chance that i might have touched them um over the past five years um you can check out my github and uh if you want to chat uh feel free to hit me up on twitter um so in case you're new to kubernetes and kubernetes sigs essentially special interest groups sigs are essentially groups of people within kubernetes that have a common kind of desire that they want to improve kubernetes in some particular way and sick instrumentation as the name kind of implies is effectively about all kinds of instrumentation that we can add to kubernetes but also through sub projects to kind of allow kubernetes to be more observable so like we have several metrics projects we have several logging kind of libraries and projects and more recently we've started to to kind of dive into some tracing aspects as well but um organizationally uh special interest group sigs um are actually uh kind of well well organized i'd like to say and we have a charter and effectively it says we try to cover the best practices for cluster observability across all kubernetes components and develop relevant components so that's kind of the crisp kind of vision statement of our group uh some of the sub projects that you might have heard of are coop state matrix k log which is kind of the logging library that is used throughout the kubernetes ecosystem some hate it some love it um then the metric server which is uh a component that is very vital for uh for running kubernetes clusters but i'll dive a little bit deeper into metric server a little bit later and same with prometheus adapter but just to give you kind of a quick glimpse into what we do at uh within sick instrumentation um and again if you're if you're new here uh you it's very easy to kind of get started and talk to us we have regular meetings every two weeks at 9 30 a.m pacific time on thursdays so that's every second week and every other week essentially we on wednesdays have our triage meeting where we go through the latest issues and kind of assign them to folks that are in the in the call so if you're interested i
