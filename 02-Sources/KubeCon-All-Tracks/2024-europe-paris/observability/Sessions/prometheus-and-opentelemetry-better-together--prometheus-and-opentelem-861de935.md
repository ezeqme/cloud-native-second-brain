---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Observability"
themes: ["Observability"]
speakers: ["Adriana Villela", "ServiceNow Cloud Observability", "Reese Lee", "New Relic"]
sched_url: https://kccnceu2024.sched.com/event/1YePz/prometheus-and-opentelemetry-better-together-adriana-villela-servicenow-cloud-observability-reese-lee-new-relic
youtube_search_url: https://www.youtube.com/results?search_query=Prometheus+and+OpenTelemetry%3A+Better+Together+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Prometheus and OpenTelemetry: Better Together - Adriana Villela, ServiceNow Cloud Observability & Reese Lee, New Relic

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: France / Paris
- Speakers: Adriana Villela, ServiceNow Cloud Observability, Reese Lee, New Relic
- Schedule: https://kccnceu2024.sched.com/event/1YePz/prometheus-and-opentelemetry-better-together-adriana-villela-servicenow-cloud-observability-reese-lee-new-relic
- Busca YouTube: https://www.youtube.com/results?search_query=Prometheus+and+OpenTelemetry%3A+Better+Together+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Prometheus and OpenTelemetry: Better Together.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YePz/prometheus-and-opentelemetry-better-together-adriana-villela-servicenow-cloud-observability-reese-lee-new-relic
- YouTube search: https://www.youtube.com/results?search_query=Prometheus+and+OpenTelemetry%3A+Better+Together+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=LJd1pJ0k28g
- YouTube title: Prometheus and OpenTelemetry: Better Together - Adriana Villela & Reese Lee
- Match score: 0.852
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/prometheus-and-opentelemetry-better-together/LJd1pJ0k28g.txt
- Transcript chars: 28667
- Keywords: prometheus, metrics, target, allocator, collector, operator, otel, basically, scrape, custom, monitor, resource, cluster, little, components, receiver, instance, targets

### Resumo baseado na transcript

all right it's 4:30 thank you all for being here um this is Prometheus and open Telemetry better together and we're really excited so before we start a couple brief introductions of ourselves yes hello my name is Adriana Vela and I am a cncf Ambassador I am a uh hashy Corp Ambassador a blogger podcaster my day job is as a senior staff developer Advocate at service now Cloud observability the artist formerly known as light step um by night I like to climb walls and fun fact I

### Excerpt da transcript

all right it's 4:30 thank you all for being here um this is Prometheus and open Telemetry better together and we're really excited so before we start a couple brief introductions of ourselves yes hello my name is Adriana Vela and I am a cncf Ambassador I am a uh hashy Corp Ambassador a blogger podcaster my day job is as a senior staff developer Advocate at service now Cloud observability the artist formerly known as light step um by night I like to climb walls and fun fact I really love capy badas as you can see from my t-shirt and I am ree Lee I'm a senior developer relations engineer at New Relic I work with the inimitable Adriana on the open tump end user working group where we are focused on connecting end users to each other through events and enablement content and we are also focused on creating a feedback loop between end users and maintainers to help improve the project and drive adoption and my fun fact is I love anything spooky and paranormal so open Telemetry and pereus they both help us monitor the health and U performance of our distribut systems they're both cncf open source projects but what role do they each play in observability so open Telemetry or oel for short is a vendor neutral observably framework and standard for um generating processing and exporting data Prometheus has been a fixture of the observability landscape for years it's widely relied upon um by many organizations for monitoring and um alerting and both Prometheus and open Telemetry whoops um generate metrics but the topic of similarities and differences between open TM metrics and Prometheus metrics is a vast topic it deserves its own session what we're going to talk about is how these two projects support each other and we're going to show you how we're going to show you the interoperability between these two projects so while you can Mo uh you can use Prometheus to monitor a wide variety of um application infrastructure metrics the piece that we're going to focus on is cuber dates monitoring so um oh and that's because it's arguably one of its most wide use one of the widest use cases um that's why we're going to be focusing on that so first we're going to start by learning about a few open t collector components you can use to collect Prometheus metrics um next we'll talk about the target uh Target allocator and how it can be used for sharting and and Prometheus service Discovery followed by a demo then we'll talk about some additional openet components you can use to
