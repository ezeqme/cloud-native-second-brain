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
speakers: ["Vijay Samuel", "Aishwarya Yandapalli", "eBay"]
sched_url: https://kccnceu2024.sched.com/event/1YeNu/from-configurations-to-conclusions-lessons-from-fine-tuning-open-telemetrys-collector-for-tracing-vijay-samuel-aishwarya-yandapalli-ebay
youtube_search_url: https://www.youtube.com/results?search_query=From+Configurations+to+Conclusions%3A+Lessons+from+Fine-Tuning+Open+Telemetry%E2%80%99s+Collector+for+Tracing+CNCF+KubeCon+2024
slides: []
status: parsed
---

# From Configurations to Conclusions: Lessons from Fine-Tuning Open Telemetry’s Collector for Tracing - Vijay Samuel & Aishwarya Yandapalli, eBay

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Observability]]
- Temas: [[AI ML]], [[Observability]]
- País/cidade: France / Paris
- Speakers: Vijay Samuel, Aishwarya Yandapalli, eBay
- Schedule: https://kccnceu2024.sched.com/event/1YeNu/from-configurations-to-conclusions-lessons-from-fine-tuning-open-telemetrys-collector-for-tracing-vijay-samuel-aishwarya-yandapalli-ebay
- Busca YouTube: https://www.youtube.com/results?search_query=From+Configurations+to+Conclusions%3A+Lessons+from+Fine-Tuning+Open+Telemetry%E2%80%99s+Collector+for+Tracing+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre From Configurations to Conclusions: Lessons from Fine-Tuning Open Telemetry’s Collector for Tracing.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeNu/from-configurations-to-conclusions-lessons-from-fine-tuning-open-telemetrys-collector-for-tracing-vijay-samuel-aishwarya-yandapalli-ebay
- YouTube search: https://www.youtube.com/results?search_query=From+Configurations+to+Conclusions%3A+Lessons+from+Fine-Tuning+Open+Telemetry%E2%80%99s+Collector+for+Tracing+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=RSJwv1jOdTg
- YouTube title: From Configurations to Conclusions: Lessons from Fine-Tuning Open Telemetry’s... - Vijay & Aishwarya
- Match score: 0.91
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/from-configurations-to-conclusions-lessons-from-fine-tuning-open-telem/RSJwv1jOdTg.txt
- Transcript chars: 30449
- Keywords: sampling, trace, tracing, metrics, metric, collector, traces, basically, sample, platform, applications, framework, exemplars, application, second, instrumentation, memory, latency

### Resumo baseado na transcript

good evening everyone uh my name is Vijay Samuel uh I am a principal architect at eBay and uh I help build the observability platform um you might notice that my co-speaker is missing uh aishwaria just had her baby boy and uh she's back in the US right now but uh [Applause] yes congratulations Aishwarya uh we did manage to get a recording of her portion of the talk uh which play when when those slides come uh we've been uh using open Telemetry collector and in the past

### Excerpt da transcript

good evening everyone uh my name is Vijay Samuel uh I am a principal architect at eBay and uh I help build the observability platform um you might notice that my co-speaker is missing uh aishwaria just had her baby boy and uh she's back in the US right now but uh [Applause] yes congratulations Aishwarya uh we did manage to get a recording of her portion of the talk uh which play when when those slides come uh we've been uh using open Telemetry collector and in the past we have talked about uh metrics in previous ccon uh this time we're going to talk about tracing um how we have been playing around with various uh configurations of the open telary collector um and uh where we are at right now uh so various configurations and the conclusions that we were able to make while fine-tuning open Telemetry collector for tracing that said uh uh we'll do an introduction of what tracing is uh how uh it looks like inside of eBay uh what's the problem we faced uh how we soled some of the lessons that we learned along the way and if time permits let's do some questions so what is what is tracing uh open Telemetry the the website defines tracing as uh traces give us the big picture of what happens when a request is made to an application whether your application is a monolith with a single database or a sophisticated mesh of services traces are essential to understanding the full path request takes in your application um so why is it important inside of eBay we have um call chains that can have like tens of databases uh several microservices to the point where knowing what exactly the customer saw when uh a request was being served uh tracing is very critical for that what is our scale we have a 14-day retention um with uh 190 billion spans that we process every day uh which roughly translates to 2.2 million per second uh which is served by 3.6k provision computes and uh 150 terabyt in U uh storage and from an architecture perspective uh every kubernetes cluster has three kinds of applications that run uh some of them are what we like to call generic applications um so these are typically I wrote a program in an arbitrary language uh it it doesn't I just deploy it on kubernetes um uh it's basically free flow uh on the other hand we have managed uh applications that are there uh managed meaning they have full support in terms of uh developer life cycle and whatnot uh and they have uh sdks into which we bundle the open Elementary SDK so uh generic applications would need to
