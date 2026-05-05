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
speakers: ["Jorge Turrado", "SCRM Lidl International Hub", "Zbynek Roubalik", "Kedify"]
sched_url: https://kccnceu2026.sched.com/event/2EF5k/unleashing-event-driven-capabilities-with-keda-jorge-turrado-scrm-lidl-international-hub-zbynek-roubalik-kedify
youtube_search_url: https://www.youtube.com/results?search_query=Unleashing+Event+Driven+Capabilities+With+KEDA+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Unleashing Event Driven Capabilities With KEDA - Jorge Turrado, SCRM Lidl International Hub & Zbynek Roubalik, Kedify

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jorge Turrado, SCRM Lidl International Hub, Zbynek Roubalik, Kedify
- Schedule: https://kccnceu2026.sched.com/event/2EF5k/unleashing-event-driven-capabilities-with-keda-jorge-turrado-scrm-lidl-international-hub-zbynek-roubalik-kedify
- Busca YouTube: https://www.youtube.com/results?search_query=Unleashing+Event+Driven+Capabilities+With+KEDA+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Unleashing Event Driven Capabilities With KEDA.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF5k/unleashing-event-driven-capabilities-with-keda-jorge-turrado-scrm-lidl-international-hub-zbynek-roubalik-kedify
- YouTube search: https://www.youtube.com/results?search_query=Unleashing+Event+Driven+Capabilities+With+KEDA+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=VCNxcBjVOIk
- YouTube title: Unleashing Event Driven Capabilities With KEDA - Jorge Turrado & Zbynek Roubalik
- Match score: 0.834
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/unleashing-event-driven-capabilities-with-keda/VCNxcBjVOIk.txt
- Transcript chars: 29580
- Keywords: scaling, metric, metrics, replicas, database, please, warload, another, perfect, autoscaling, define, scaled, object, trigger, seconds, interval, prometheus, possible

### Resumo baseado na transcript

I work as principal site reliability engineer at Digit, but I'm also get a maintainer and CNCF ambassador. The idea when we were thinking about the session, we thought that probably going to basics coming back to the beginning was a nice idea because even there are really nice features for them. Some rabbit com messages have been published and now we are seeing how they are scale. We depend on HPA which is the horizontal port autoscaler and there are few components in Ka. So it is like an adapter that connects to your Kubernetes cluster and you send the metrics to Kubernetes API server through this endpoint. So it will it will validate it and then we will try to open the connection in this case to Revit and Q uh to check the queue and based on that provide metrics to uh to to the to the Kubernetes.

### Excerpt da transcript

Thanks for joining us today. Thanks for being here. It's always nice to see the room packed. I'm going to introduce myself. I'm Horge Dorado there. The light the the marker. I work as principal site reliability engineer at Digit, but I'm also get a maintainer and CNCF ambassador. And my fellow maintainer is going to >> Hello everybody. My name is Beign, very hard to pronounce. Uh I'm from Czech Republic. I'm also Ka maintainer. I'm with the project since the beginning. Uh I'm the founder and CTO at company called Karify. We do like enterprise version of of Ka. We can continue. Right. >> Perfect. So what are we going to talk about today? The idea when we were thinking about the session, we thought that probably going to basics coming back to the beginning was a nice idea because even there are really nice features for them. You can contact us directly or our fellow maintainers sit on the first line but for the vast majority of the people probably go come to basics is nice. So what is keta? Ka kuber stands for kubernetes event driving autoscaling and our goal is super easy make the autoscaling in kubernetes that simple.

We are not aiming to do fancy stuff just making the things as simple as possible and we are a big community and the community grows day by day. So it's nice the main contributors are there and a lot of users it's nice seeing that we have adoption with the publicity effort that we do to be honest and the first point is okay scaling on Kubernetes does it work the first option before bothering you with 20 minutes more of h speed of the bits I'm going to show you how it works just to h without checking in detail terrible experience here. >> We still see the slides. Horge so. So until fix the fixed the stuff maybe there is some question I'm always getting like how to pronounce the name of the project. So uh you can use SCADA you can use SCADA. Please don't use SCADA. Uh and also please don't use SCADA that much because SCADA in Czech language and from Czech Republic has like a very bad connotation related to poop. So if possible please use SCADA. Thank you. >> So in this case I'm going to create the typical publisher and oh terrible apply.

Nice. It's applied. Perfect. Now I have the typical publisher and my consumer is starting to grow. No worries. We are going to go deep. We are going to go deeper in this point. But before bothering you I want to say that it work. Some rabbit com messages have been published and now we are seeing how they are s
