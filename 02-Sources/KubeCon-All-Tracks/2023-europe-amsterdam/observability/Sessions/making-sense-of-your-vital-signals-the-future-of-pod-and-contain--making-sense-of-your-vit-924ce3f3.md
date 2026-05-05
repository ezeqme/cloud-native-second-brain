---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Observability"
themes: ["AI ML", "Observability", "Runtime Containers"]
speakers: ["David Porter", "Google", "Peter Hunt", "Red Hat"]
sched_url: https://kccnceu2023.sched.com/event/1HydJ/making-sense-of-your-vital-signals-the-future-of-pod-and-containers-monitoring-david-porter-google-peter-hunt-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Making+Sense+of+Your+Vital+Signals%3A+The+Future+of+Pod+and+Containers+Monitoring+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Making Sense of Your Vital Signals: The Future of Pod and Containers Monitoring - David Porter, Google & Peter Hunt, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Observability]]
- Temas: [[AI ML]], [[Observability]], [[Runtime Containers]]
- País/cidade: Netherlands / Amsterdam
- Speakers: David Porter, Google, Peter Hunt, Red Hat
- Schedule: https://kccnceu2023.sched.com/event/1HydJ/making-sense-of-your-vital-signals-the-future-of-pod-and-containers-monitoring-david-porter-google-peter-hunt-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Making+Sense+of+Your+Vital+Signals%3A+The+Future+of+Pod+and+Containers+Monitoring+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Making Sense of Your Vital Signals: The Future of Pod and Containers Monitoring.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HydJ/making-sense-of-your-vital-signals-the-future-of-pod-and-containers-monitoring-david-porter-google-peter-hunt-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Making+Sense+of+Your+Vital+Signals%3A+The+Future+of+Pod+and+Containers+Monitoring+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=w6PeNpPhIF8
- YouTube title: Making Sense of Your Vital Signals: The Future of Pod and Containers Mo... David Porter & Peter Hunt
- Match score: 0.94
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/making-sense-of-your-vital-signals-the-future-of-pod-and-containers-mo/w6PeNpPhIF8.txt
- Transcript chars: 31782
- Keywords: advisor, metrics, actually, container, containers, metric, milliseconds, understand, endpoint, monitoring, little, application, basically, running, resource, around, performance, request

### Resumo baseado na transcript

okay hello everyone uh thank you so much for for coming to our session uh you know it's the last session of the day so hope you've had a great kubecon so far my name is David Porter uh I'm a software engineer on the Google kubernetes team uh I focus on node uh I work in Upstream signode community and I'm also the maintainer of sea advisor which we'll talk about in this presentation which is a monitoring Library used in the kubernetes ecosystem hey everyone my name is

### Excerpt da transcript

okay hello everyone uh thank you so much for for coming to our session uh you know it's the last session of the day so hope you've had a great kubecon so far my name is David Porter uh I'm a software engineer on the Google kubernetes team uh I focus on node uh I work in Upstream signode community and I'm also the maintainer of sea advisor which we'll talk about in this presentation which is a monitoring Library used in the kubernetes ecosystem hey everyone my name is Peter hunt I'm a senior software engineer at Red Hat primarily working on the container runtime cryo but I also work in Upstream Sig node and on podman and run C and other container related Technologies today we're going to talk about making sense of your vital signals the future of pod and container monitoring so let me start this presentation with I hope a situation you haven't been during kubecon but for anyone who's been on call it's probably faced you suddenly get paged right and maybe you get page then you have an alert you know maybe it's your chatbot application or your other LM thing and it says that the latency of application is too high right what just happened and what do you do well first thing you probably act in right but then after that you figure out how do we actually resolve this that's what we hope to describe in this presentation so what is kind of the monitoring observability space and why is it important so observability it's really important to understand how your applications are performing right you want to understand if you roll out new versions of your application how is the resource changes changing is there kind of a regression in your application is it using too much resources too little Etc right so you want to be able to identify issues and unexpected Behavior with your apps and maybe you also want to learn them right so we've alerted for example on our latency and we got that alert or maybe we want to alert on other scenarios like using too much memory or something like that additionally maybe you have slos or slis for your internal customers or external customers and you need observability to understand if you're adhering to those slos or slis and lastly not just for for kind of you as the you know cluster admin or application developer but also the internal kubernetes components also need monitoring and Metric data to perform its core functions so a good example here kubelet which is the worker agent running on every single node in your cluster it needs moni
