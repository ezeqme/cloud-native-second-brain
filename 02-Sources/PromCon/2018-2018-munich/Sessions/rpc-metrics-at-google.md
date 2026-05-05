---
type: promcon-talk
conference: PromCon
edition: "PromCon 2018"
edition_id: 2018-munich
year: 2018
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Alerting", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2018-munich/talks/rpc_metrics_at_google/
youtube_url: https://www.youtube.com/watch?v=Dm3r0Siu7PU
youtube_search_url: https://www.youtube.com/results?search_query=RPC+Metrics+at+Google+PromCon+2018
video_match_score: 0.894
status: video-found
---

# RPC Metrics at Google

## Identificação

- Edição: PromCon 2018
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Alerting]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2018-munich/talks/rpc_metrics_at_google/
- YouTube: https://www.youtube.com/watch?v=Dm3r0Siu7PU

## Resumo

Speaker: Jaana B. Dogan Collecting and alerting on RPC metrics is a fundamental part of Google's reliability story. In this talk, we will go through what we have learned in the last two decades and why we are trying to flex our instrumentation stack to cooperate with Prometheus.

## Abstract oficial

Speaker: Jaana B. Dogan

Collecting and alerting on RPC metrics is a fundamental part of Google's reliability story. In this talk, we will go through what we have learned in the last two decades and why we are trying to flex our instrumentation stack to cooperate with Prometheus.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2018-munich/talks/rpc_metrics_at_google/
- YouTube: https://www.youtube.com/watch?v=Dm3r0Siu7PU
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Dm3r0Siu7PU
- YouTube title: PromCon 2018: RPC Metrics at Google
- Match score: 0.894
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2018/rpc-metrics-at-google/Dm3r0Siu7PU.txt
- Transcript chars: 17411
- Keywords: metrics, actually, google, understand, latency, infrastructure, export, client, hundred, enough, across, little, primitives, source, instrumentation, questions, anything, request

### Resumo baseado na transcript

yeah it's super bad news for me because I missed a party last night and I'm so jealous but you know don't be judgmental if I mess up things I really prepared this talk last night I'm JB D as a Julius mentioned I work at Google main on the instrumentation side of the thing so I don't understand everything end to end but I understand my stuff if you have questions I may need to you know reroute you to the right people if I don't know anything about

### Excerpt da transcript

yeah it's super bad news for me because I missed a party last night and I'm so jealous but you know don't be judgmental if I mess up things I really prepared this talk last night I'm JB D as a Julius mentioned I work at Google main on the instrumentation side of the thing so I don't understand everything end to end but I understand my stuff if you have questions I may need to you know reroute you to the right people if I don't know anything about it so today's talk is about RPC metrics and to be honest RPC is just basic G RPC at Google now pretty much so it's going to be more about G RPC metrics well if you don't like JR pieces that's fine because you know these concepts work regardless of the protocol so you can see it as a talk on request metrics so why do we care about metrics is the first question I think because we care about availability and you know we as an industry like to trivialize and you know use simple descriptions of what availability is this is our VP of asari on reliability a hundred percent is the wrong reliable to target basically for anything just because you know a hundred percent just doesn't exist it's so complex and expensive to hu hundred percent that it's not practical to set it as a goal and it's not achievable at all so maybe we should you know try to understand what is good availability what is good reliability or you know let's ask first what is availability to begin with so we see available there's a as is about you know whether a service is performing is user expects or not in simpler terms we say that like a services available if users cannot tell it's there was a knowledge so failure can happen and might happen but it should be rare enough and rare enough here it just really depends on the business you know how much your users can tolerate failure and so on so you need to set your you know failure in when we you know it depends on the system so I just want to reiterate the key here is not like a hundred percent reliability because it's you know just not possible we are more of a principled way of saying things like you know what type of what kind what what is the level of downtown which is acceptable for our service lots of people have mentioned you know Isolators Eliza solos so we define and use this we have this common language all across the organization we write several objectives to tell everybody hey this is you know what is acceptable downtown and there are two major categories we care about our PC especially but yo
