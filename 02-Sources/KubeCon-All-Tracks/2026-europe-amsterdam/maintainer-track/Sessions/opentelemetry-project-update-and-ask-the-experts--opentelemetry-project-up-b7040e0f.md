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
themes: ["AI ML", "Observability", "Storage Data", "Community Governance"]
speakers: ["Pablo Baeyens", "Datadog", "Juraci Paixão Kröhling", "OllyGarden", "Marylia Gutierrez", "Grafana Labs", "Severin Neumann", "Causely"]
sched_url: https://kccnceu2026.sched.com/event/2EF6i/opentelemetry-project-update-and-ask-the-experts-pablo-baeyens-datadog-juraci-paixao-krohling-ollygarden-marylia-gutierrez-grafana-labs-severin-neumann-causely
youtube_search_url: https://www.youtube.com/results?search_query=OpenTelemetry+Project+Update+and+%27Ask+the+Experts%27+CNCF+KubeCon+2026
slides: []
status: parsed
---

# OpenTelemetry Project Update and 'Ask the Experts' - Pablo Baeyens, Datadog; Juraci Paixão Kröhling, OllyGarden; Marylia Gutierrez, Grafana Labs; Severin Neumann, Causely

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Storage Data]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Pablo Baeyens, Datadog, Juraci Paixão Kröhling, OllyGarden, Marylia Gutierrez, Grafana Labs, Severin Neumann, Causely
- Schedule: https://kccnceu2026.sched.com/event/2EF6i/opentelemetry-project-update-and-ask-the-experts-pablo-baeyens-datadog-juraci-paixao-krohling-ollygarden-marylia-gutierrez-grafana-labs-severin-neumann-causely
- Busca YouTube: https://www.youtube.com/results?search_query=OpenTelemetry+Project+Update+and+%27Ask+the+Experts%27+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre OpenTelemetry Project Update and 'Ask the Experts'.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF6i/opentelemetry-project-update-and-ask-the-experts-pablo-baeyens-datadog-juraci-paixao-krohling-ollygarden-marylia-gutierrez-grafana-labs-severin-neumann-causely
- YouTube search: https://www.youtube.com/results?search_query=OpenTelemetry+Project+Update+and+%27Ask+the+Experts%27+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=mvSGusgcVuw
- YouTube title: OpenTelemetry Project Update and 'Ask the Experts' - Pablo B, Juraci P, Marylia G & Severin N
- Match score: 0.802
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/opentelemetry-project-update-and-ask-the-experts/mvSGusgcVuw.txt
- Transcript chars: 26063
- Keywords: stable, events, already, define, instrumentation, working, collector, specific, please, question, python, stability, environment, registry, browser, little, application, languages

### Resumo baseado na transcript

>> Uh, as you all know, open telemetry is the open start standard for telemetry. Uh, we have recently reflected that on our website with a along with a new redesign that you can check out right now. So it generates a a um a policy violation JSON that tells you what is wrong where uh and uh and you can get that information into a a another storage and you can alert on that. If you want to learn more about the injector, we also had a talk about this last year CubeCon on the observability day. Um so first I wanted to highlight uh some performance work that the Go SDK maintainers have been doing on the metric side. Um their benchmarks show between four and 30 times of performance improvements.

### Excerpt da transcript

Cool. All right. So, hello everyone. Uh, welcome to the open telemetry product updates. My name is Judas. >> I am Morelia. >> I'm Pablo. >> And I'm Severin. >> So, we have a clicker actually. >> Yes. >> Uh, as you all know, open telemetry is the open start standard for telemetry. Uh, we have recently reflected that on our website with a along with a new redesign that you can check out right now. Um and today we are first going to do things a little differently from other sessions. So we're going to do a deep dive into three different topics uh that we think should be interesting for you. >> Well, so the first one I'm going to talk about it is about declarative configuration which just reached a huge milestone. It is now stable. So yay, congratulations. So that that is a project that has been happening for a few years now. A lot of people working on it. So I know the people are here that also work on it. So thank you all for your work and this is going to be the the future how configuration is going to work on open telemetry.

So we are able now to configure complex attributes. You're not so dependent on environment variables that have a lot of limitation. Uh now is everything also the same. The configuration is the same language for all the places that you are using. In this case is a YAML file. So you have the same file that you can use for your Java application, your JavaScript, your Python, uh also for a collector. So doesn't matter which one. So you can have the same and just share around. And we have the data model that you can see all the options that exist which is very helpful because like today you have like so many environment variables. They're like, "Where do they all live? Which ones do you have?" So, you have to like keep researching, but now you have everything in a single file. So, that's gonna make your life easier. Uh here I want to show an example of a very simple file. Uh it's going to be two images. So, the first one just the file format to show that is the the version that is now stable. You have you can set up some resources.

Here I have an example that if you are used to using like environment variables and you want to start doing the migration, you can see here that you can put your environment variable on your config file if you still want to. We have propagators uh and then we also have like the providers or tracer uh meter and logger. So this is an example if you have this is a very basic one that you can already use to configu
