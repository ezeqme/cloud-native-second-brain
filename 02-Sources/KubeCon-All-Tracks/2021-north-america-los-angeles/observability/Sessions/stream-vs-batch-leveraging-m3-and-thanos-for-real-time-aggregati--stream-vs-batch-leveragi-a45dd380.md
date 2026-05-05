---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Observability"
themes: ["Observability"]
speakers: ["Gibbs Cullen", "Chronosphere"]
sched_url: https://kccncna2021.sched.com/event/lV29/stream-vs-batch-leveraging-m3-and-thanos-for-real-time-aggregation-gibbs-cullen-chronosphere
youtube_search_url: https://www.youtube.com/results?search_query=Stream+vs.+Batch%3A+Leveraging+M3+and+Thanos+for+Real-Time+Aggregation+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Stream vs. Batch: Leveraging M3 and Thanos for Real-Time Aggregation - Gibbs Cullen, Chronosphere

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Los Angeles
- Speakers: Gibbs Cullen, Chronosphere
- Schedule: https://kccncna2021.sched.com/event/lV29/stream-vs-batch-leveraging-m3-and-thanos-for-real-time-aggregation-gibbs-cullen-chronosphere
- Busca YouTube: https://www.youtube.com/results?search_query=Stream+vs.+Batch%3A+Leveraging+M3+and+Thanos+for+Real-Time+Aggregation+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Stream vs. Batch: Leveraging M3 and Thanos for Real-Time Aggregation.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV29/stream-vs-batch-leveraging-m3-and-thanos-for-real-time-aggregation-gibbs-cullen-chronosphere
- YouTube search: https://www.youtube.com/results?search_query=Stream+vs.+Batch%3A+Leveraging+M3+and+Thanos+for+Real-Time+Aggregation+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=so_017-skv0
- YouTube title: Stream vs. Batch: Leveraging M3 and Thanos for Real-Time Aggregation - Gibbs Cullen, Chronosphere
- Match score: 0.915
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/stream-vs-batch-leveraging-m3-and-thanos-for-real-time-aggregation/so_017-skv0.txt
- Transcript chars: 17017
- Keywords: aggregation, metrics, prometheus, thanos, streaming, series, aggregated, recording, results, metric, overview, queries, remote, storage, database, coordinator, instances, stream

### Resumo baseado na transcript

okay well uh welcome everyone thank you for joining uh you know so i'll be talking today about stream versus batch leveraging m3 and thanos for real-time aggregation i guess i just had a quick intro but take the mask off all right sure that's good yeah no we want to be able to hear okay um yeah so just quick intro about myself so yeah developer advocate at chronosphere where i help out with the m3 open source community as a contributor and then i'm also a member of

### Excerpt da transcript

okay well uh welcome everyone thank you for joining uh you know so i'll be talking today about stream versus batch leveraging m3 and thanos for real-time aggregation i guess i just had a quick intro but take the mask off all right sure that's good yeah no we want to be able to hear okay um yeah so just quick intro about myself so yeah developer advocate at chronosphere where i help out with the m3 open source community as a contributor and then i'm also a member of the cncf of durability tag and prior to chronosphere i was a product manager over at aws okay so just running through the agenda for the talk today we're going to start out going through the problem statement and an overview of streaming versus batch aggregation then we'll go through stream aggregation with m3 followed by batch aggregation with thanos and then quick overview at the end kind of comparing the two so why does aggregation matter for real time looking here at this example of a c advisor dashboard you can see that so see advisor is a way to get your resource usage and performance metrics of all of your running pods or containers so kind of cpu memory kind of your infrastructure level metrics it runs as a damon set inside of a cubelet and then this particular dashboard we're looking at all of the um pods within our gateway application but essentially you're just able to get a quick uh 10 000 foot view of all of your of all your applications uh with this kind of with this dashboard so zooming in for this example we're going to look at the this particular panel here that's highlighted looking at cpu usage across all of your gateway pods or containers so you know you can see here that it's it's kind of showing an overview of all your pods but if we look at behind the scenes at what's what it takes to really produce these results you can see that it can it can lead to quite a bit of time for your queries to fully render these results so the way to advisor is is aggregating or pulling this metric this container cpu usage metric is it's pulling labels across all of your pods in your in your pod group so as a result you're getting roughly 51 000 time series and that's going to be taking over 20 seconds for your results to render so and that's just to query this this metric so if you did any sort of functions on top like summer max you can imagine it would take much longer but in most cases you typically don't want to you don't need to look at your your metrics at the per pod level and you rea
