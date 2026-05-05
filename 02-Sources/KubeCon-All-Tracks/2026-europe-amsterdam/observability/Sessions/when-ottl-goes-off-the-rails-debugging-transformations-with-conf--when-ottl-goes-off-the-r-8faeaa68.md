---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Observability"
themes: ["AI ML", "Observability"]
speakers: ["Edmo Vamerlatti Costa", "Elastic", "Tyler Helmuth", "Honeycomb"]
sched_url: https://kccnceu2026.sched.com/event/2CVyH/when-ottl-goes-off-the-rails-debugging-transformations-with-confidence-edmo-vamerlatti-costa-elastic-tyler-helmuth-honeycomb
youtube_search_url: https://www.youtube.com/results?search_query=When+OTTL+Goes+Off+the+Rails%3A+Debugging+Transformations+with+Confidence+CNCF+KubeCon+2026
slides: []
status: parsed
---

# When OTTL Goes Off the Rails: Debugging Transformations with Confidence - Edmo Vamerlatti Costa, Elastic & Tyler Helmuth, Honeycomb

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Observability]]
- Temas: [[AI ML]], [[Observability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Edmo Vamerlatti Costa, Elastic, Tyler Helmuth, Honeycomb
- Schedule: https://kccnceu2026.sched.com/event/2CVyH/when-ottl-goes-off-the-rails-debugging-transformations-with-confidence-edmo-vamerlatti-costa-elastic-tyler-helmuth-honeycomb
- Busca YouTube: https://www.youtube.com/results?search_query=When+OTTL+Goes+Off+the+Rails%3A+Debugging+Transformations+with+Confidence+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre When OTTL Goes Off the Rails: Debugging Transformations with Confidence.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVyH/when-ottl-goes-off-the-rails-debugging-transformations-with-confidence-edmo-vamerlatti-costa-elastic-tyler-helmuth-honeycomb
- YouTube search: https://www.youtube.com/results?search_query=When+OTTL+Goes+Off+the+Rails%3A+Debugging+Transformations+with+Confidence+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=465RlwgsNHg
- YouTube title: When OTTL Goes Off the Rails: Debugging Transformations wit... Edmo Vamerlatti Costa & Tyler Helmuth
- Match score: 0.848
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/when-ottl-goes-off-the-rails-debugging-transformations-with-confidence/465RlwgsNHg.txt
- Transcript chars: 26374
- Keywords: logs, statement, collector, context, transform, metrics, important, resource, attributes, metric, statements, pretty, running, condition, string, execution, attribute, payload

### Resumo baseado na transcript

And today we're going to be going over how to debug OTTL with confidence. I want to be clear that this is an open or an intermediate open telemetry session. Metrics has a list of metrics and each metrics has a list of data points and traces have a list of spans and then spans can have a list of span events, span lengths and so on. So yeah, the debug tools we're going to be using today are three simple but very powerful tools which are the debug exporter, debug logs, and the OTL playground. If you're not seeing the data here, you probably have a problem and you need to take a look at that. So all those simple problems can be solved just by enabling this exported and looking at that output.

### Excerpt da transcript

Uh, welcome everyone. My name is Tyler Helmouth. I am a software engineer at Honeycomb. And >> my name is Aimo. I'm a software engineer at Elastiki. And today we're going to be going over how to debug OTTL with confidence. I want to be clear that this is an open or an intermediate open telemetry session. If you've never heard of open telemetry, if you've never used the open telemetry collector or if you've never used the open telemetry transformation language which we call OTTL, this is going to be a difficult session to follow. Uh we're going to talk about these topics assuming that you've used them before. The good news is if you're interested in these topics and this is your first time and you're looking for someone to explain them to you, there are a lot of talks this week at CubeCon about open telemetry, about the collector that you can go to. And there's also a lot of talks at previous CubeCons that have been uploaded online that you can find about these topics. So our agenda today is first we're going to review a couple important data models in open telemetry.

Uh as it's really really important to know the shape of your open telemetry data when you're using OTTL. Then we're going to review some of the tools that you can use to debug and we're going to go through some live debugging uh scenarios with you today. All right. First, let's review the open telemetry data model. Open telemetry has a very very structured data model that it uses to represent telemetry. The structure of each data model is broken down into different signals uh different types of data. So things like logs, metrics, traces are examples of signals. Each signal has a resource, a top level uh object in the data model that represents the application producing the telemetry. It has a set of attributes like service.name and they're set one time at the beginning when you are starting up your application. Each resource has an instrument a list of instrumentation scopes. Instrumentation scopes represent the thing producing telemetry. They have fields like a name, a version, more attributes and then each instrumentation scope has its own slice of items and those items are based on uh the type of signal that you're working with.

So for example uh logs has a log record. Metrics has a list of metrics and each metrics has a list of data points and traces have a list of spans and then spans can have a list of span events, span lengths and so on. Within each one of those items depending on the
