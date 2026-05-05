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
themes: ["Observability", "Storage Data"]
speakers: ["Felix Geisendörfer", "Datadog", "Florian Lehner", "Elastic"]
sched_url: https://kccnceu2026.sched.com/event/2CW0V/the-fourth-pillar-arrives-opentelemetry-profiling-alpha-in-action-felix-geisendorfer-datadog-florian-lehner-elastic
youtube_search_url: https://www.youtube.com/results?search_query=The+Fourth+Pillar+Arrives%3A+OpenTelemetry+Profiling+Alpha+in+Action+CNCF+KubeCon+2026
slides: []
status: parsed
---

# The Fourth Pillar Arrives: OpenTelemetry Profiling Alpha in Action - Felix Geisendörfer, Datadog & Florian Lehner, Elastic

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[Storage Data]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Felix Geisendörfer, Datadog, Florian Lehner, Elastic
- Schedule: https://kccnceu2026.sched.com/event/2CW0V/the-fourth-pillar-arrives-opentelemetry-profiling-alpha-in-action-felix-geisendorfer-datadog-florian-lehner-elastic
- Busca YouTube: https://www.youtube.com/results?search_query=The+Fourth+Pillar+Arrives%3A+OpenTelemetry+Profiling+Alpha+in+Action+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre The Fourth Pillar Arrives: OpenTelemetry Profiling Alpha in Action.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW0V/the-fourth-pillar-arrives-opentelemetry-profiling-alpha-in-action-felix-geisendorfer-datadog-florian-lehner-elastic
- YouTube search: https://www.youtube.com/results?search_query=The+Fourth+Pillar+Arrives%3A+OpenTelemetry+Profiling+Alpha+in+Action+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=TKp2snmgvtQ
- YouTube title: The Fourth Pillar Arrives: OpenTelemetry Profiling Alpha in A... Felix Geisendörfer & Florian Lehner
- Match score: 0.872
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/the-fourth-pillar-arrives-opentelemetry-profiling-alpha-in-action/TKp2snmgvtQ.txt
- Transcript chars: 34194
- Keywords: profiling, actually, profile, function, little, profiler, program, information, signal, profiles, trace, calling, already, traces, probably, format, collector, ebpf

### Resumo baseado na transcript

Hello everybody and uh welcome to our presentation uh the fourth pillar arrives open telemetry profiles alpha in action. With me today is Florian Ler from Elastic and my name is Felix Gazender and I work at data dog and we're both members of the profiling special interest groups which is why we're talking today uh about profiling to you. I would say the three main use cases are incidents, costs, and performance. Maybe you have an alert on latency, but anyway, you find CPU usage has increased. You might just do roll back initially, but you still have to figure out which code was the problem and profiling can help you figure that out and then you can make a fix to roll forward again. Um you might find yourself uh spending at some point millions of dollars on the hyperscalers and so at that point it becomes very lucrative to actually ask yourself where's all my CPU time and all my memory going to and how can I optimize this in order to spend less and be more efficient.

### Excerpt da transcript

Hello everybody and uh welcome to our presentation uh the fourth pillar arrives open telemetry profiles alpha in action. With me today is Florian Ler from Elastic and my name is Felix Gazender and I work at data dog and we're both members of the profiling special interest groups which is why we're talking today uh about profiling to you. So to get started let's have a look at what profiles actually are. What is the essence of a profile? Um to to illustrate this I brought you a simple CPU profile in a text format here uh where you can see this particular stack trace main calling into surf request calling into get balance call into DB select was collected 30 times by a CPU profiler which is a sampling profiler. So we saw 30 of these samples and then for this stack trace we saw 20 samples five samples etc. And this is the simplest profiling format in existence. uh it's called the folded stack format by Brandon Craig who also invented the uh flame craft visualization and in a perfect world we would be done here this would be profiling and our job would be done we wouldn't have to do anything for open telemetry but the world is not perfect uh the world is complicated it expects efficiency uh with efficiency comp complexity and so for example we realized that for example many of these function names here that you see in this profile would be repeated multiple times so you would see main multiple times and that's not ideal.

In fact, in some cases, when you have not just an aggregation format, but you would include the timestamps for each individual sample, which there's many use cases for, you might have to repeat the entire stack trace that you've seen multiple times for each time stamp you want to associate with it. So, you have to think a little bit about how to make a profiling format efficiently um and and support other use cases such as timestamps, labels, etc., which the open telemetry profiling format does. Um, so let's talk about use cases for profiling. Why should you care about profiling? What can you use it for? I would say the three main use cases are incidents, costs, and performance. Uh for incidents, maybe one of the most common scenarios is that you're looking at a dashboard showing CPU usage, and you see a huge spike in CPU usage. Maybe that's what you have an alert on. Maybe you have an alert on latency, but anyway, you find CPU usage has increased. And profiling can be really useful for telling you which code that was maybe cold before has su
