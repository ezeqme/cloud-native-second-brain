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
speakers: ["João Duarte", "Elastic"]
sched_url: https://kccnceu2026.sched.com/event/2CW4H/enriching-telemetry-signals-through-lookups-in-the-otel-collector-joao-duarte-elastic
youtube_search_url: https://www.youtube.com/results?search_query=Enriching+Telemetry+Signals+Through+Lookups+in+the+OTel+Collector+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Enriching Telemetry Signals Through Lookups in the OTel Collector - João Duarte, Elastic

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: João Duarte, Elastic
- Schedule: https://kccnceu2026.sched.com/event/2CW4H/enriching-telemetry-signals-through-lookups-in-the-otel-collector-joao-duarte-elastic
- Busca YouTube: https://www.youtube.com/results?search_query=Enriching+Telemetry+Signals+Through+Lookups+in+the+OTel+Collector+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Enriching Telemetry Signals Through Lookups in the OTel Collector.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW4H/enriching-telemetry-signals-through-lookups-in-the-otel-collector-joao-duarte-elastic
- YouTube search: https://www.youtube.com/results?search_query=Enriching+Telemetry+Signals+Through+Lookups+in+the+OTel+Collector+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=OVffupWFEtw
- YouTube title: Enriching Telemetry Signals Through Lookups in the OTel Collector - João Duarte, Elastic
- Match score: 0.947
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/enriching-telemetry-signals-through-lookups-in-the-otel-collector/OVffupWFEtw.txt
- Transcript chars: 20890
- Keywords: source, processor, collector, lookup, signal, course, within, enrichment, attribute, sources, specify, understand, already, either, signals, enough, information, useful

### Resumo baseado na transcript

Uh we're here to talk to talk today about enriching telemetry signals using the open telemetry collector. Uh I say that my main hobby is to collect hobbies and then not spend enough time on them and therefore I'm bad at them. It can be useful for your organization to understand uh to which cost center this signal is affected to or even to see which uh if a certain IP that is hitting your endpoint is a malicious IP using a threat feed. So the idea again is to take this raw signal and adding more to it so that you can then use it on alerts. so you're able to understand where it lives within your Kubernetes cluster where the which cloud provider that signal is coming through etc. So what I did was to take a lot of these discussions, a lot of these learnings, a lot of these proposals and try to come up with something that would be useful for everyone and try to satisfy the needs that were described in these issues.

### Excerpt da transcript

Hello everyone. This is not yet the last talk of the day. So I hope you still have some energy in you. Uh we're here to talk to talk today about enriching telemetry signals using the open telemetry collector. So my name is Jan. I live in Portugal, Lisbon. I work at Elastic at the uh inest observability team. Uh I say that my main hobby is to collect hobbies and then not spend enough time on them and therefore I'm bad at them. So if you want to talk about any of these hobbies or about the contents of this presentation, uh yeah, hit me up after the session. So before we talk about enrichment, we need to understand what enrichment is. So of course I went to the dictionary and enrichment is the process of making someone wealthy or the action of improving the enhancing the quality or value of something. And I got to say, I'm sorry, but we're not going to necessarily make anyone rich in this presentation as we're going to be focusing mostly on the second definition of the action of improving or enhancing the quality or value of something.

And here the something is or are the signals that are traveling through your hotel collector. And why do we need to talk about this? So signals by themselves are already valuable pieces of information. They capture a moment in time, an occurrence, a measurement. However, often enough they lack enough context or even structure for you to use them properly. So here enhancing the value will come from adding more context to the signals. This context can be useful for your S sur practitioners for example to understand where the signal is coming from from within your uh infrastructure. It can be useful for your organization to understand uh to which cost center this signal is affected to or even to see which uh if a certain IP that is hitting your endpoint is a malicious IP using a threat feed. So the idea again is to take this raw signal and adding more to it so that you can then use it on alerts. You can use it on dashboards. You can even use it to do better model inference for what you need. Another thing that we need when we talk about enrichment is to understand what kinds of enrichment there are.

And I came up with a set of categories of enrichment. You can also put it differently, but essentially I came up with these six types. And the first one is the most simple one. You already have a piece of data and you're just either taking that piece of data and just splitting into more information or just taking two pieces of inform
