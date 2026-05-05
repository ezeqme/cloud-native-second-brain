---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Observability"
themes: ["Observability", "SRE Reliability"]
speakers: ["Joel Verezhak", "Open Systems"]
sched_url: https://kccncna2023.sched.com/event/1R2tz/thanos-unleashed-mastering-the-challenges-of-production-scale-metrics-joel-verezhak-open-systems
youtube_search_url: https://www.youtube.com/results?search_query=Thanos+Unleashed%3A+Mastering+the+Challenges+of+Production-Scale+Metrics+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Thanos Unleashed: Mastering the Challenges of Production-Scale Metrics - Joel Verezhak, Open Systems

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Joel Verezhak, Open Systems
- Schedule: https://kccncna2023.sched.com/event/1R2tz/thanos-unleashed-mastering-the-challenges-of-production-scale-metrics-joel-verezhak-open-systems
- Busca YouTube: https://www.youtube.com/results?search_query=Thanos+Unleashed%3A+Mastering+the+Challenges+of+Production-Scale+Metrics+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Thanos Unleashed: Mastering the Challenges of Production-Scale Metrics.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2tz/thanos-unleashed-mastering-the-challenges-of-production-scale-metrics-joel-verezhak-open-systems
- YouTube search: https://www.youtube.com/results?search_query=Thanos+Unleashed%3A+Mastering+the+Challenges+of+Production-Scale+Metrics+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Q3qOZ7SEgcM
- YouTube title: Thanos Unleashed: Mastering the Challenges of Production-Scale Metrics - Joel Verezhak, Open Systems
- Match score: 0.916
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/thanos-unleashed-mastering-the-challenges-of-production-scale-metrics/Q3qOZ7SEgcM.txt
- Transcript chars: 36859
- Keywords: thanos, metrics, actually, storage, receiver, series, prometheus, receive, course, controller, receives, hashing, blocks, basically, coming, tenant, cardinality, number

### Resumo baseado na transcript

so my name is Joel verac I'm a senior system engineer at open systems um and I work in the observability team and what does open systems do so we are actually uh let's say a managed uh connectivity company so we offer um managed Network Solutions and so it's quite interesting I think to be here at cucon which is a kubernetes conference um and we actually ship mostly we work with these kind of boxes these kind of devices and we don't run kubernetes on these devices so we have there is a bit of a let's say there is a bit of crossover time or a bit of uncertainty between when the kubernetes API recognizes or when the kuet rep recognizes that the pot is unhealthy it of course depends on how many series we can manage you know based on our resources which we've deployed in the in the receives um and what we need to do is we just need to query what the current metric value is for for that head series each of the receives like Prometheus has a metric called um head series Prometheus time series head or head time series something like that pops up later so we can actually count that um live and then it's we just need to tell the rooting receiver to current head series values and it's a query which looks exactly like this this is exactly the query which is run and so in this example for example you can see the sdp tenant has 28 million um head series the van tenant has 23

### Excerpt da transcript

so my name is Joel verac I'm a senior system engineer at open systems um and I work in the observability team and what does open systems do so we are actually uh let's say a managed uh connectivity company so we offer um managed Network Solutions and so it's quite interesting I think to be here at cucon which is a kubernetes conference um and we actually ship mostly we work with these kind of boxes these kind of devices and we don't run kubernetes on these devices so maybe it's interesting to think you know why are we here in the first place um we run quite a lot of these hosts currently we have just over 10,000 um situated all over the world so they plug into all our customers infrastructure um but today I'm not going to talk about how we monitor these hosts is sort of another topic entirely if it sounds interesting and it is interesting um there's a link here to a to a talk I gave um at cucon EU um back in April uh where I go into more sort of details about this um but today uh we're going to talk about Thanos at least I hope that's what everyone is expecting um otherwise I wrote my my abstract very wrongly um in particular what I would like to talk about is scalability resilience and performance of the right path so for us all of our metrics are sort of customer facing so if there are problems with the metrics it comes back to us very very quickly you know customers complain um so we're really really focused on making sure that we get every metric which is shipped to us from all of those devices um and at the end if there's time um this sort of one weird trick that reduced storage costs for us by quite a significant number um it was kind of an interesting uh Journey let's say debugging Journey um as to what was going wrong um so hopefully we can get around to that as well so hopefully most of you are aware of what Thanos is if not you will know what Prometheus is um otherwise I'll do my best to accomodate for everybody um so Thanos is a framework which is built around Prometheus okay so it's um it's you know Prometheus of course is the the the sort of deao metrics back end for most kubernetes clusters I think if you spin up a kubernetes cluster today uh one of the first things you do is you go and install Cube prom stack to just get basic monitoring in place um so Thanos is sort of wrapping around Prometheus and extending its capabilities so it offers a global query view um so this is really nice if you have multiple uh you know maybe tens or hundreds o
