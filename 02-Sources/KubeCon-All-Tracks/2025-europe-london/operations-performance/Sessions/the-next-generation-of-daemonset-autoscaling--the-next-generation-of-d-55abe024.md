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
themes: ["SRE Reliability"]
speakers: ["Adam Bernot", "Google Cloud", "Bryan Boreham", "Grafana Labs"]
sched_url: https://kccnceu2025.sched.com/event/1tx8F/the-next-generation-of-daemonset-autoscaling-adam-bernot-google-cloud-bryan-boreham-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=The+Next+Generation+of+DaemonSet+Autoscaling+CNCF+KubeCon+2025
slides: []
status: parsed
---

# The Next Generation of DaemonSet Autoscaling - Adam Bernot, Google Cloud & Bryan Boreham, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Operations + Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Adam Bernot, Google Cloud, Bryan Boreham, Grafana Labs
- Schedule: https://kccnceu2025.sched.com/event/1tx8F/the-next-generation-of-daemonset-autoscaling-adam-bernot-google-cloud-bryan-boreham-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=The+Next+Generation+of+DaemonSet+Autoscaling+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre The Next Generation of DaemonSet Autoscaling.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx8F/the-next-generation-of-daemonset-autoscaling-adam-bernot-google-cloud-bryan-boreham-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=The+Next+Generation+of+DaemonSet+Autoscaling+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=yQQU8vDhj0o
- YouTube title: The Next Generation of DaemonSet Autoscaling - Adam Bernot & Bryan Boreham
- Match score: 0.852
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/the-next-generation-of-daemonset-autoscaling/yQQU8vDhj0o.txt
- Transcript chars: 27415
- Keywords: request, recommendation, logging, requests, actually, memory, cluster, resource, running, proposal, logs, resources, question, demons, behavior, problems, trying, general

### Resumo baseado na transcript

I work at Google Cloud on the Google Cloud managed service for Prometheus. Uh, my day job I work on massively scalable storage for, uh, metrics, logs, traces, and profiles. Uh, these uh what we mean by by demons here is is a computer program that runs in the background. uh the idea of a a demon being a kind of generally helpful thing that that that hangs out and uh does things for you. Um in Kubernetes terms, a demon set will run one pod on every node in your cluster. uh logging demon um something collecting logs from every node that that will run a metrics collection on every node is this kind of thing that we're talking about that that's what you would use a demon set for and um they they need to run everywhere.

### Excerpt da transcript

Hello, welcome. Uh, my name is Adam Berno. I work at Google Cloud on the Google Cloud managed service for Prometheus. Uh, hi, my name is Brian Borum. Uh, I am a distinguished engineer at Graphana Labs. Uh, my day job I work on massively scalable storage for, uh, metrics, logs, traces, and profiles. Uh, I'm also a Prometheus maintainer. Um, so if you like that, yeah, and uh feel free to uh follow us on our blue sky handles that are listed on the screen. Uh, we'd love to connect with you if you find this talk entertaining. Uh, we're going to be talking about how Damon sets run in Kubernetes and how to use autoscaling to make them more efficient and more effective. Um, yeah. So, uh, I show of hands, get get a bit of a audience participation going. Um, how many people have used a VPA, a vertical pod autoscaler? Okay, so that's about maybe maybe a fifth of the audience, something like that. And um, how many people have have used a demon set? Oh, nearly everyone. Um, how many people have used a VPA with a demon set?

Yeah, that guy. Well, uh, that's what our talk is about. Um, we, uh, we're going to kind of motivate the the problem that we see with this, uh, and then talk about what we did to try and solve it and hopefully give a demo. Yeah. And we're, uh, not we're the second last thing between you and free beer. So, uh, just, you know, chill, stay with us, and we'll take you on a journey. Oh, I Yeah. picture. Okay. Demons. Demons. Demons are not um coming from hell. Uh, these uh what we mean by by demons here is is a computer program that runs in the background. Um, and apparently this comes from from Greek mythology. uh the idea of a a demon being a kind of generally helpful thing that that that hangs out and uh does things for you. Um in Kubernetes terms, a demon set will run one pod on every node in your cluster. And uh why would you want to do this? Well, something like a like a network controller that that needs to run on every node. Um that will run a demon set. uh logging demon um something collecting logs from every node that that will run a metrics collection on every node is this kind of thing that we're talking about that that's what you would use a demon set for and um they they need to run everywhere.

Yeah. So just a little bit more level setting to before we get into the meat of the talk but uh let's talk about resource requests for a second since we'll be talking about them throughout. When you set up anything to run in Kubernetes, you can spec
