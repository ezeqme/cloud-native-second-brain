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
themes: ["AI ML", "Observability"]
speakers: ["Johannes Tax", "Grafana Labs"]
sched_url: https://kccnceu2024.sched.com/event/1YeNV/disintegrated-telemetry-the-pains-of-monitoring-asynchronous-workflows-johannes-tax-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=Disintegrated+Telemetry%3A+The+Pains+of+Monitoring+Asynchronous+Workflows+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Disintegrated Telemetry: The Pains of Monitoring Asynchronous Workflows - Johannes Tax, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Observability]]
- Temas: [[AI ML]], [[Observability]]
- País/cidade: France / Paris
- Speakers: Johannes Tax, Grafana Labs
- Schedule: https://kccnceu2024.sched.com/event/1YeNV/disintegrated-telemetry-the-pains-of-monitoring-asynchronous-workflows-johannes-tax-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Disintegrated+Telemetry%3A+The+Pains+of+Monitoring+Asynchronous+Workflows+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Disintegrated Telemetry: The Pains of Monitoring Asynchronous Workflows.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeNV/disintegrated-telemetry-the-pains-of-monitoring-asynchronous-workflows-johannes-tax-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=Disintegrated+Telemetry%3A+The+Pains+of+Monitoring+Asynchronous+Workflows+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=GvF1ivr7RlA
- YouTube title: Disintegrated Telemetry: The Pains of Monitoring Asynchronous Workflows - Johannes Tax, Grafana Labs
- Match score: 0.923
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/disintegrated-telemetry-the-pains-of-monitoring-asynchronous-workflows/GvF1ivr7RlA.txt
- Transcript chars: 32221
- Keywords: trace, traces, single, message, instrumentation, conventions, semantic, workflows, messaging, workflow, solution, synchronous, scenarios, context, events, sampling, standards, support

### Resumo baseado na transcript

my name is johanes I am a software engineer at grafana Labs the team I'm working on uh our mission is it to make grafana users successfully with open dmetry instrumentation I'm involved in the open dmetry project for several years now I started out as a contributor to the open dmetry C++ project currently I'm mostly focusing on open Telemetry semantic conventions and and in particular semantic conventions for messaging that's also what prompted me to give this talk there is a lot of pain around monitoring a synchronous

### Excerpt da transcript

my name is johanes I am a software engineer at grafana Labs the team I'm working on uh our mission is it to make grafana users successfully with open dmetry instrumentation I'm involved in the open dmetry project for several years now I started out as a contributor to the open dmetry C++ project currently I'm mostly focusing on open Telemetry semantic conventions and and in particular semantic conventions for messaging that's also what prompted me to give this talk there is a lot of pain around monitoring a synchronous workflows way too much to put it all into this single talk it would be hard to bear so what we're going to do here we are going to focus on a single pain point that is the center piece here then first we will look where does this pain come from we will try to understand the source of this pain and then at the end we will look out for Hope is there any hope to alleviate this pain we will talk mostly about distributed tracing because this pain point that I picked it relates to distributed tracing also we will talk about distributed tracing here here because in my experience it is the area that causes the most pain when it comes to monitoring a synchronous Rock flows and to Define what we mean by synchronous workflows in the context of this talk we Define an as synchronous workflow as a workflow that involves a synchronous communication between different Services there can also be a synchronous communication inside a single service inside a single process and while many of the things we will see here also apply to those scenarios it's not what we are primarily focusing on these as synchronous Communications between different Services there also the terms messaging or Eventing used for it I will use the term messaging here a lot mainly because it rolls off the tongue much easier than the synchronous workflows so let's dive in let's talk about disintegration and let's look at some characteristics of a synchronous workflows what do we see here firstly we see that apparently I didn't go to art school but let's leave that aside for a moment we see a little comic here a little workflow described a little story we see two actors involved somebody pushes their bike to bike bike mechanic and says I need my bike repaired the bike mechanic says sure I'll text you when I'm done then the next day the owner of the bike receives a text message that says the bike is repaired he says great I will go there and pick it up right away and he goes there gets his bik
