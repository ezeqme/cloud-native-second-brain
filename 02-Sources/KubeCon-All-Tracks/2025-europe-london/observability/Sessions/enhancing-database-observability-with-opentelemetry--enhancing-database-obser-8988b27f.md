---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Observability"
themes: ["Observability", "Storage Data"]
speakers: ["Marylia Gutierrez", "Grafana Labs"]
sched_url: https://kccnceu2025.sched.com/event/1txE9/enhancing-database-observability-with-opentelemetry-marylia-gutierrez-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=Enhancing+Database+Observability+With+OpenTelemetry+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Enhancing Database Observability With OpenTelemetry - Marylia Gutierrez, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[Storage Data]]
- País/cidade: United Kingdom / London
- Speakers: Marylia Gutierrez, Grafana Labs
- Schedule: https://kccnceu2025.sched.com/event/1txE9/enhancing-database-observability-with-opentelemetry-marylia-gutierrez-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Enhancing+Database+Observability+With+OpenTelemetry+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Enhancing Database Observability With OpenTelemetry.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txE9/enhancing-database-observability-with-opentelemetry-marylia-gutierrez-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=Enhancing+Database+Observability+With+OpenTelemetry+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Rf9NceXXRuw
- YouTube title: Enhancing Database Observability With OpenTelemetry - Marylia Gutierrez, Grafana Labs
- Match score: 0.847
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/enhancing-database-observability-with-opentelemetry/Rf9NceXXRuw.txt
- Transcript chars: 20834
- Keywords: database, attributes, create, instrumentation, databases, application, itself, semantic, operation, observability, actually, sending, convention, compare, define, everybody, postgress, looking

### Resumo baseado na transcript

Uh so yeah today I'm going to talk about how you can enhance database observability with open telemetry. I am a staff software engineer at Graphfana Labs focusing on open telemetry and within open telemetry I work in a couple of different groups. Then someone on the Java SDK say oh I want to create something too and they call it query time. And now when somebody want to use those SDKs, they have to learn the two different names for the things that are supposed to be the same. The second one are the metrics and the third one I'm calling here like specific because the mo even like we really try to say something that is going to encapsulate everybody. So here we have to define how we collect this metrics the units and if we are doing things like sanitization how you do the sanitization.

### Excerpt da transcript

H so yeah guess we can start now. Uh so thank you uh everyone for joining. See a lot of people here. So first I need to ask some questions. Who is Brazilian here? Uh so yeah today I'm going to talk about how you can enhance database observability with open telemetry. So to start let me introduce myself. My name is Maril Jes. I am a staff software engineer at Graphfana Labs focusing on open telemetry and within open telemetry I work in a couple of different groups. I am a maintainer for the contributor experience. So if you want to become a contributor to open telemetry and you have any challenges and you have some feedback, I'm happy to hear and improve your experience. Uh, I'm also approver for the JavaScript SDK, the database semantic conventions, which is something I'm going to talk about today, and also for the Portuguese localization. So to start talking about the database observability, I want to give you a little context of what this information that we are collecting where this is coming from.

So now you know if you want to give your opinion as well, make changes, you know exactly which point do you want to start. So everything here starts with semantic conventions. So what is exactly semantic conventions? This is like the long definitions that we have on our documentation. But what it basically is saying is that this is the place that we're going to define things like what are the span names, what are the metric names and why this is important. I can give two reasons. So the first one is because we define what is the same thing for everybody. Now we have the same baseline. So now everybody that we talk about spans we know everybody knows what should be a span and so on. And the other case is imagine it somebody say like oh I want to instrument for databases and then they go to the JavaScript SDK and then create a metric call it statement duration. Then someone on the Java SDK say oh I want to create something too and they call it query time. So now you have two different names to mean the same thing.

And now when somebody want to use those SDKs, they have to learn the two different names for the things that are supposed to be the same. And then when you are sending this to your observability vendor, what do you do is now you have two different names that you cannot easily combine. You can still combine but it's not so straightforward. So now when we define is a little more easy than everybody's on the same page. So how the creation of theatic co
