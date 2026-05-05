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
themes: ["Observability"]
speakers: ["Endre Sara", "Causely", "Nikola Grcevski", "Grafana Labs"]
sched_url: https://kccnceu2026.sched.com/event/2CW5C/dns-tracing-metrics-via-ebpf-in-opentelemetry-endre-sara-causely-nikola-grcevski-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=DNS+Tracing+%26+Metrics+Via+eBPF+in+OpenTelemetry+CNCF+KubeCon+2026
slides: []
status: parsed
---

# DNS Tracing & Metrics Via eBPF in OpenTelemetry - Endre Sara, Causely & Nikola Grcevski, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Endre Sara, Causely, Nikola Grcevski, Grafana Labs
- Schedule: https://kccnceu2026.sched.com/event/2CW5C/dns-tracing-metrics-via-ebpf-in-opentelemetry-endre-sara-causely-nikola-grcevski-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=DNS+Tracing+%26+Metrics+Via+eBPF+in+OpenTelemetry+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre DNS Tracing & Metrics Via eBPF in OpenTelemetry.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW5C/dns-tracing-metrics-via-ebpf-in-opentelemetry-endre-sara-causely-nikola-grcevski-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=DNS+Tracing+%26+Metrics+Via+eBPF+in+OpenTelemetry+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YMqSK6uBhxU
- YouTube title: DNS Tracing & Metrics Via eBPF in OpenTelemetry- Endre Sara, Causely & Nikola Grcevski, Grafana Labs
- Match score: 0.732
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/dns-tracing-metrics-via-ebpf-in-opentelemetry/YMqSK6uBhxU.txt
- Transcript chars: 30442
- Keywords: actually, instrumentation, metrics, request, application, trace, capture, opentelemetry, traces, ebpf, process, kernel, client, trying, working, actual, server, requests

### Resumo baseado na transcript

I'm a maintainer at the OpenTelemetry BPF instrumentation project, also Grafana Labs employee. So, a while back, while we were working on OB, and Andras showed up at the SIG meeting and said, "You guys should do DNS." And it's really important, and eBPF is the perfect technology for doing that. And and you know, it would be so if we were to ask how many of you had DNS problems in the past 6 months? How how many of you had DNS problems in a way that you were trying to build your agentic pipeline and trying to look up your various SMTP servers? I Today I actually found out that apparently dot net has a built-in support that you can track some DNS metrics if you know how to connect with a trace program to get it out, but hey. Um it's actually quite often the problem without people knowing why it is a problem, and is it how is it even happening?

### Excerpt da transcript

Good, I know it's the end of the day. People probably tired, but yeah, here we are talking about DNS. Um Cool. So, my name is Nikola Grachevsky. I'm a maintainer at the OpenTelemetry BPF instrumentation project, also Grafana Labs employee. And I'm here with my co-presenter, Andras. Andras Szabo. I'm the co-founder at Causely. Has been working with Nikola on the OB project for a while. And I'm a co-founder at Causely. At Causely, we are building a causal layer for your agentic pipeline. Feel free to find me later if you want to know more about this. Here we are talking about DNS. It's very exciting to be back. I'm glad you guys are here. You could all be having a beer, and you came here. Thank you. >> [laughter] >> So Nikola Yeah. So, a while back, while we were working on OB, and Andras showed up at the SIG meeting and said, "You guys should do DNS." And it's really important, and eBPF is the perfect technology for doing that. So, show of hands here, who knows what eBPF is? Oh, everybody knows. All right, so I we don't have to talk about this.

>> [laughter] >> All right. Well, Andras, why don't you tell us about why you thought something didn't click over here? All right. Why don't you tell me about what was the problem, why you wanted us to actually implement this? So, so it's it's very interesting cuz I'm talking to a lot of customers, and even in our own environment um people [clears throat] are looking at their services, and they they they don't know what's going on with DNS. They see their services are slow, and they don't know why. And there isn't a really good observable layer for your your clients interacting with DNS services. Um so, um uh I thought that we should provide this visibility and make it as easy as possible. eBPF based auto instrumentation was a exciting opportunity to do this. Yeah. People always say this, like it's always DNS, right? Whenever you have a problem, I just never knew why it was so important. So, why [clears throat] don't we look at the actual issues? So, so what what what's actually interesting is that it's never DNS.

It's always DNS. But it turns out that it's not the DNS server, it's the DNS clients. People don't know what they're doing. Um and they make random DNS calls, they put in some random host name. Yeah. Um and then it may resolve. If it doesn't resolve, it's obvious. But it does resolve, but it takes a long time. It's really hard to know why because um if you just do, and I hope everybody here is doing auto
