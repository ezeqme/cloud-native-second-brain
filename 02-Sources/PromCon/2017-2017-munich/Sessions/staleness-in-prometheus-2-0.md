---
type: promcon-talk
conference: PromCon
edition: "PromCon 2017"
edition_id: 2017-munich
year: 2017
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2017-munich/talks/staleness-in-prometheus-2-0/
youtube_url: https://www.youtube.com/watch?v=GcTzd2CLH7I
youtube_search_url: https://www.youtube.com/results?search_query=Staleness+in+Prometheus+2.0+PromCon+2017
video_match_score: 0.704
status: video-found
---

# Staleness in Prometheus 2.0

## Identificação

- Edição: PromCon 2017
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2017-munich/talks/staleness-in-prometheus-2-0/
- YouTube: https://www.youtube.com/watch?v=GcTzd2CLH7I

## Resumo

Speaker: Brian Brazil The biggest semantic change in Prometheus 2.0 is the new staleness handling. This long awaited feature means there's no longer a fixed 5 minute staleness. Now time series go stale when they're no longer exposed, and targets that no longer exist don't hang around for a full 5 minutes.

## Abstract oficial

Speaker: Brian Brazil

The biggest semantic change in Prometheus 2.0 is the new staleness handling. This long awaited feature means there's no longer a fixed 5 minute staleness. Now time series go stale when they're no longer exposed, and targets that no longer exist don't hang around for a full 5 minutes. Learn about how it works and how to take advantage of it.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2017-munich/talks/staleness-in-prometheus-2-0/
- YouTube: https://www.youtube.com/watch?v=GcTzd2CLH7I
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=GcTzd2CLH7I
- YouTube title: PromCon 2017: Staleness and Isolation in Prometheus 2.0 - Brian Brazil
- Match score: 0.704
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2017/staleness-in-prometheus-2-0/GcTzd2CLH7I.txt
- Transcript chars: 48751
- Keywords: scrape, series, basically, actually, minutes, federation, already, markers, equals, target, isolation, seconds, marker, timestamps, prometheus, change, pretty, gateway

### Resumo baseado na transcript

[Music] now we will have brine Brazil he's the founder of robbers perception a promises core developer and most well-known for proving that prawn koalas turing-complete and he's going to tell you about staleness in prometheus 2.0 so I presume you will kind of know who I am by now and you know I may have done some inadvisable things that prompt you out of my time but what I want to talk about here is that you already had some fabian the awesome changes were happening in from idiots

### Excerpt da transcript

[Music] now we will have brine Brazil he's the founder of robbers perception a promises core developer and most well-known for proving that prawn koalas turing-complete and he's going to tell you about staleness in prometheus 2.0 so I presume you will kind of know who I am by now and you know I may have done some inadvisable things that prompt you out of my time but what I want to talk about here is that you already had some fabian the awesome changes were happening in from idiots to zero with a storage engine and which is the biggest change so i'm gonna talk about the second biggest change which is a semantic change and which also conveniently is one of the things for pull wins over push so sorry butum your startup just can't handle this so this is a bug this is a feature we've talked about for a long time like I filed a bug in July 2014 just basically three years ago soon after I got involved in form 8 he smokes like me and so we're gonna look at basically what permit freebies previous versions did with stainless and the problems with that and basically how I fixed it or improved it so the thing is before 2.0 ik anywhere up to well Prometheus won 8-1 and probably the last one and if you value a range vector like looking at a counter for 10 minutes it's always going to return all data points in that range inclusive nice simple not gonna change great if you evaluate an inspector like a gauge right it'll return the latest value before the evaluation time looking back to five minutes which is to say that if a time series gets no updated data points for five minutes it goes stale and is no longer returned for instant vectors now there is a flag you can use to control this setting you shouldn't change it because most people have asked about this flag we're trying to do event log and if you're going to do that well you can use influx DB or DL expect something else which is better designed for that use case so there are several problems that come from the old stainless semantics the first one people come across most common is the few alerts on up equals zero and you can imagine you have something running on kubernetes it starts failing it has optical zero at least once and then it's rescheduled but up equals zero is still there and will be there for five minutes even though it's been rescheduled somewhere else and is now happy so if you have created a hair-trigger alert that's put a fire before like five minutes against recommendations as Julius earlier then yea
