---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Project Opportunities"
themes: ["Observability"]
speakers: []
sched_url: https://kccncna2024.sched.com/event/1iW8S/jaeger-distributed-tracing-with-jaeger-and-opentelemetry-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=Jaeger%3A+Distributed+Tracing+with+Jaeger+and+OpenTelemetry+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Jaeger: Distributed Tracing with Jaeger and OpenTelemetry | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Observability]]
- País/cidade: United States / Salt Lake City
- Speakers: N/A
- Schedule: https://kccncna2024.sched.com/event/1iW8S/jaeger-distributed-tracing-with-jaeger-and-opentelemetry-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=Jaeger%3A+Distributed+Tracing+with+Jaeger+and+OpenTelemetry+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Jaeger: Distributed Tracing with Jaeger and OpenTelemetry | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1iW8S/jaeger-distributed-tracing-with-jaeger-and-opentelemetry-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=Jaeger%3A+Distributed+Tracing+with+Jaeger+and+OpenTelemetry+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=xpN0fuWEmX8
- YouTube title: Jaeger: Distributed Tracing with Jaeger and OpenTelemetry | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/jaeger-distributed-tracing-with-jaeger-and-opentelemetry-project-light/xpN0fuWEmX8.txt
- Transcript chars: 5217
- Keywords: application, version, jagger, within, better, metrics, distributed, joerger, visualize, search, database, prometheus, automatically, similar, jaeger, tracing, lightning, release

### Resumo baseado na transcript

hello everyone I'm here to talk to you today about joer and we have a big new release version too that I'll touch upon and explain the significance of this joerger is a graduated cncf project focused on observability we do distributed tracing it was donated by Uber to the cncf and was one of the first graduated projects my name is Jonah Cowell besides being a Jagger maintainer I also run product and design at p which is a monitoring company um and uh let's dive into the content

### Excerpt da transcript

hello everyone I'm here to talk to you today about joer and we have a big new release version too that I'll touch upon and explain the significance of this joerger is a graduated cncf project focused on observability we do distributed tracing it was donated by Uber to the cncf and was one of the first graduated projects my name is Jonah Cowell besides being a Jagger maintainer I also run product and design at p which is a monitoring company um and uh let's dive into the content so for those of you that haven't seen well first I love scuba diving so come to the Jagger Booth if you want to talk about diving that's what I do for fun um but jger uh really helps you debug distributed applications and pinpoint performance issues so this is how you would visualize different traces or executions within your application we've made a lot of enhancements in the user interface over the years being able to search and isolate problems and then drill into the actual execution of a single end to endend trace so you can see where the slow parts are how you can speed this up and optimize it so it really helps anyone that's building software do that better or operating software operate it better you can also visualize this instead of a timeline view you can look at it as a flame graph showing you where you can optimize where your CPU and your memory and your execution time is actually going um you can also drill into the database you can drill into Kafka just touching upon the last lightning talk here and and really dig in and see what's happening within the application itself visualize the views from end to end there's a lot of value for different stakeholders within your organization or if you're just doing this on your own so the other thing is that joer is closely tied to a couple of different projects one is Prometheus where we've uh built the capability to automatically get metrics into your Prometheus back end to automatically understand the request rate of your application the error rate and the duration uh so we have a really nice integration and visualization of these key metrics that let you know when something bad is starting to happen with your application uh you can also go deeper in your in your observability tool of choice that works with Prometheus uh folks like grafana or a new project called Percy that visualizes metrics as well uh so one of the big things we've done is Jagger version 2 this was about a 2-year project similar to some of the previous talks
