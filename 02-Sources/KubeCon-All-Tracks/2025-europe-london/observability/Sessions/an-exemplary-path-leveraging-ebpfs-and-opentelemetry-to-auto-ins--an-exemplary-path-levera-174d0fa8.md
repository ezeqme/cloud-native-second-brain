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
themes: ["Observability"]
speakers: ["Charlie Le", "Kruthika Prasanna Simha", "Apple"]
sched_url: https://kccnceu2025.sched.com/event/1txEI/an-exemplary-path-leveraging-ebpfs-and-opentelemetry-to-auto-instrument-for-exemplars-charlie-le-kruthika-prasanna-simha-apple
youtube_search_url: https://www.youtube.com/results?search_query=An+Exemplary+Path%3A+Leveraging+EBPFs+and+OpenTelemetry+To+Auto-instrument+for+Exemplars+CNCF+KubeCon+2025
slides: []
status: parsed
---

# An Exemplary Path: Leveraging EBPFs and OpenTelemetry To Auto-instrument for Exemplars - Charlie Le & Kruthika Prasanna Simha, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United Kingdom / London
- Speakers: Charlie Le, Kruthika Prasanna Simha, Apple
- Schedule: https://kccnceu2025.sched.com/event/1txEI/an-exemplary-path-leveraging-ebpfs-and-opentelemetry-to-auto-instrument-for-exemplars-charlie-le-kruthika-prasanna-simha-apple
- Busca YouTube: https://www.youtube.com/results?search_query=An+Exemplary+Path%3A+Leveraging+EBPFs+and+OpenTelemetry+To+Auto-instrument+for+Exemplars+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre An Exemplary Path: Leveraging EBPFs and OpenTelemetry To Auto-instrument for Exemplars.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txEI/an-exemplary-path-leveraging-ebpfs-and-opentelemetry-to-auto-instrument-for-exemplars-charlie-le-kruthika-prasanna-simha-apple
- YouTube search: https://www.youtube.com/results?search_query=An+Exemplary+Path%3A+Leveraging+EBPFs+and+OpenTelemetry+To+Auto-instrument+for+Exemplars+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=u-eUO3rIQV4
- YouTube title: An Exemplary Path: Leveraging EBPFs and OpenTelemetry To Aut... Charlie Le & Kruthika Prasanna Simha
- Match score: 0.806
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/an-exemplary-path-leveraging-ebpfs-and-opentelemetry-to-auto-instrumen/u-eUO3rIQV4.txt
- Transcript chars: 30322
- Keywords: exemplars, metrics, trace, metric, traces, instrument, cortex, exemplar, instrumentation, observability, ebpf, request, logs, information, application, kernel, actually, itself

### Resumo baseado na transcript

Thank you for being here and listening to us talk about leveraging EVPF and open telemetry to auto instrument exemplars. So before we get started um I just want to take a quick moment to introduce ourselves. But what if there is a way for me to go from metrics directly to traces? Exemplars are time series data points that essentially link metrics to traces and logs through the trace ID and span ID. And these are often stored alongside metrics in the metrics data store. They provide a lot of contextual information because it's not just the traces and logs.

### Excerpt da transcript

Good afternoon everyone. Thank you for being here and listening to us talk about leveraging EVPF and open telemetry to auto instrument exemplars. So before we get started um I just want to take a quick moment to introduce ourselves. Hi I'm Kitika and I'm a machine learning engineer at Apple. I uh work with the observability team and my experience is in observability uh machine learning and data science and I've been at Apple for about six years. U Charlie hi I'm Charlie I've uh worked at Apple for about 8 and a half years. Um I've had roles from SR DevOps and observability. Um, I'm a software engineer at Apple today and I'm also a maintainer for Cortex, a one of the projects in CNCF. All right. So, um, if you're here today and it doesn't matter what your background is, if you're an S, you're a developer, you're a DevOps engineer, you will take away how to use exemplars to supercharge your observability and your debugging abilities. So, what are we going to cover today? We'll talk a little bit about um what exemplars are and what eBPF is.

Uh we'll go into how you can use eBPF to auto instrument exemplars. And then we'll talk about projects that use open telemetry to create exemplars with eBPF. And we also have a demo for that. And finally, we'll talk about how you can okay um and how you can use machine learning to supercharge your exemplar observability. Okay. So, imagine this. Can you guys still hear me? Okay. Uh imagine this that I have a service and I'm noticing that the request latency there seems to be something off with that. So, what is the first thing I do? I go into my dashboard and I look at my request latency graph and indeed it looks like something is wrong. It seems to be going up. But I just cannot use only this metric to debug what's going wrong. I still need more information. So the next step that I do is I go to my distributed traces and now I have to sift through this plethora of traces to figure out which request path is that of the slow request. And obviously we all know how tedious that is. But what if there is a way for me to go from metrics directly to traces?

And the answer is there is a way to do it and that is through exemplars. Exemplars are time series data points that essentially link metrics to traces and logs through the trace ID and span ID. And these are often stored alongside metrics in the metrics data store. They provide a lot of contextual information because it's not just the traces and logs. You can add a lot of oth
