---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Observability"
themes: ["Observability"]
speakers: ["Ganesh Vernekar", "Grafana Labs"]
sched_url: https://kccnceu2022.sched.com/event/ytqF/prometheus-sparse-high-resolution-histograms-in-action-ganesh-vernekar-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=Prometheus+Sparse+High-Resolution+Histograms+in+Action+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Prometheus Sparse High-Resolution Histograms in Action - Ganesh Vernekar, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: Spain / Valencia
- Speakers: Ganesh Vernekar, Grafana Labs
- Schedule: https://kccnceu2022.sched.com/event/ytqF/prometheus-sparse-high-resolution-histograms-in-action-ganesh-vernekar-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Prometheus+Sparse+High-Resolution+Histograms+in+Action+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Prometheus Sparse High-Resolution Histograms in Action.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytqF/prometheus-sparse-high-resolution-histograms-in-action-ganesh-vernekar-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=Prometheus+Sparse+High-Resolution+Histograms+in+Action+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=T2GvcYNth9U
- YouTube title: Prometheus Sparse High-Resolution Histograms in Action - Ganesh Vernekar, Grafana Labs
- Match score: 0.868
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/prometheus-sparse-high-resolution-histograms-in-action/T2GvcYNth9U.txt
- Transcript chars: 25818
- Keywords: bucket, buckets, histograms, histogram, resolution, series, boundaries, prometheus, factor, number, precision, requests, second, boundary, running, latency, particular, higher

### Resumo baseado na transcript

hello hello i'm audible yeah so um yeah i guess no one is going so welcome everyone to my talk i'm going to talk about the shiny new histograms that's going to come in from india soon yeah so i am ganesh vernecker i am a software engineer at grafana labs i am a prometheus team member and i maintain the tsdb in the prometheus so before we talk about the shiny new histograms let's see what is a histogram a histogram lets you distribute your observations into multiple buckets you don't have to worry about this math you can just assume that it works and we will see soon how this solves all the remaining problems and if you see the color uh colors like once you go up like once you increase the

### Excerpt da transcript

hello hello i'm audible yeah so um yeah i guess no one is going so welcome everyone to my talk i'm going to talk about the shiny new histograms that's going to come in from india soon yeah so i am ganesh vernecker i am a software engineer at grafana labs i am a prometheus team member and i maintain the tsdb in the prometheus so before we talk about the shiny new histograms let's see what is a histogram a histogram lets you distribute your observations into multiple buckets let's take this example so in all the examples that i talk it's i am going to observe the latency of a request so on the y-axis it's the number of requests on the x-axis it's the request duration so in this particular histogram we can what we can get out of this is there are 15 requests that are less than 0.1 second latency there are 25 requests from 0.1 to one second and one to two seconds and the last bucket is special it encapsulates all the requests that were greater than two seconds into a single bucket so how do we store this in prometheus so in prometheus we give one time series for each bucket so we have a label for a series called l e which means less than or equal to and prometheus recognizes this special label as the bucket value for a time series so so for this particular histogram we have four bucket time series each mentioning here the bucket boundaries and if you notice it is less than or equal to so the first time series which is 0.1 includes all the count of all the requests that had latency less than 0.1 seconds which is 15 and the next one is less than or equal to 1 seconds which is all the requests that were before one second so it includes the first bar and the second bar similarly the third time series is the sum of first second and third bar and there is a plus infinity bucket which is everything before infinity basically the total count and we have two additional time series for the entire count and some so this is a problem the first problem is we have to pre-define these bucket boundaries even before instrumenting like when you write the instrumentation code you have to mention these bucket boundaries and it can get tricky and it can take some experimentation to get these bucket boundaries right and the buckets are cumulative if you see this particular example we have four buckets that are filled and i have changed the bucket boundaries a little bit but we have defined a whole lot of time bucket boundaries for this particular histogram so lots of time series are
