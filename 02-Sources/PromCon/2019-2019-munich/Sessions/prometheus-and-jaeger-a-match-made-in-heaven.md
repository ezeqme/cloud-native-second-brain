---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2019"
edition_id: 2019-munich
year: 2019
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Remote Write Storage", "Kubernetes", "Scalability Reliability", "Visualization Dashboards"]
speakers: []
source_url: https://promcon.io/2019-munich/talks/prometheus-and-jaeger-a-match-made-in-heaven/
youtube_url: https://www.youtube.com/watch?v=EvzTFUMqCXY
youtube_search_url: https://www.youtube.com/results?search_query=Prometheus+and+Jaeger%3A+A+Match+Made+in+Heaven%21+PromCon+2019
video_match_score: 0.976
status: video-found
---

# Prometheus and Jaeger: A Match Made in Heaven!

## Identificação

- Edição: PromCon EU 2019
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Remote Write Storage]], [[Kubernetes]], [[Scalability Reliability]], [[Visualization Dashboards]]
- Speakers: N/A
- Página oficial: https://promcon.io/2019-munich/talks/prometheus-and-jaeger-a-match-made-in-heaven/
- YouTube: https://www.youtube.com/watch?v=EvzTFUMqCXY

## Resumo

Speaker: Goutham Veeramachaneni Jaeger is an OSS distributed tracing solution, also part of the CNCF. Standalone, it can add immense value but when coupled with Prometheus, there is a lot more to gain. We have leveraged Prometheus and Jaeger together to make Cortex 10x faster and we will be sharing our journey and key learnings.

## Abstract oficial

Speaker: Goutham Veeramachaneni

Jaeger is an OSS distributed tracing solution, also part of the CNCF. Standalone, it can add immense value but when coupled with Prometheus, there is a lot more to gain. We have leveraged Prometheus and Jaeger together to make Cortex 10x faster and we will be sharing our journey and key learnings. With Prometheus, we have our RED dashboards that highlight which services are slow, and we then use Jaeger to drill down and investigate which functions are taking how long, if we’re making too many calls, if we could batch calls together, etc. We then verify the impact using Jaeger and Prometheus after rolling out the changes. Without our RED dashboards, it would be shooting in the dark to find out which spans/services we should look at in Jaeger. Usually the slowness occurs in only one cluster. To enable filtering of traces to only that cluster/env, we enrich the traces with the same metadata that prometheus has. We were also seeing very slow queries once in a while that weren’t very obvious when using only dashboards. We then started logging the trace ID in our request logs. We picked the requests that took too long, and used their trace IDs to probe for issues with that particular request. While this approach works, you need a solid log aggregation system, and even then it’s not exactly easy to find the interesting traces (longest/shortest requests). We will show you how Prometheus helps by providing us exemplars that can let us directly jump to the right traces from the latency dashboards. We will end the talk by demo-ing everything discussed.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2019-munich/talks/prometheus-and-jaeger-a-match-made-in-heaven/
- YouTube: https://www.youtube.com/watch?v=EvzTFUMqCXY
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=EvzTFUMqCXY
- YouTube title: PromCon EU 2019: Prometheus and Jaeger: A Match Made in Heaven!
- Match score: 0.976
- Transcript file: N/A
- Transcript chars: 0
- Keywords: prometheus, jaeger, dashboards, traces, together, cluster, trace, request, requests, heaven, speaker, goutham, veeramachaneni, distributed, tracing, solution, standalone, immense

### Resumo baseado na transcript

_Transcript indisponível; enriquecimento baseado apenas em metadados._

### Excerpt da transcript

_Sem transcript disponível._
