---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2024"
edition_id: 2024-berlin
year: 2024
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Scalability Reliability"]
speakers: ["Owen Williams"]
source_url: https://promcon.io/2024-berlin/talks/why-not-just-dots-utf8-support-in-prometheus-30/
youtube_url: https://www.youtube.com/watch?v=POSFqCBLH-o
youtube_search_url: https://www.youtube.com/results?search_query=Why+Not+Just+Dots%3F+UTF-8+Support+in+Prometheus+3.0+PromCon+2024
video_match_score: 1.013
status: video-found
---

# Why Not Just Dots? UTF-8 Support in Prometheus 3.0

## Identificação

- Edição: PromCon EU 2024
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Metrics]], [[Scalability Reliability]]
- Speakers: Owen Williams
- Página oficial: https://promcon.io/2024-berlin/talks/why-not-just-dots-utf8-support-in-prometheus-30/
- YouTube: https://www.youtube.com/watch?v=POSFqCBLH-o

## Resumo

An overview of the design and implementation of UTF-8 support for metric and label names in Prometheus. The talk will detail the genesis of the new quoting syntax, as well as why the chosen approach didn't simply add dots as a new valid character. The talk will also cover how Prometheus maintains compatibility with older systems and will support metric name migrations.

## Abstract oficial

An overview of the design and implementation of UTF-8 support for metric and label names in Prometheus. The talk will detail the genesis of the new quoting syntax, as well as why the chosen approach didn't simply add dots as a new valid character. The talk will also cover how Prometheus maintains compatibility with older systems and will support metric name migrations.

## Links

- Página oficial: https://promcon.io/2024-berlin/talks/why-not-just-dots-utf8-support-in-prometheus-30/
- YouTube: https://www.youtube.com/watch?v=POSFqCBLH-o
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=POSFqCBLH-o
- YouTube title: PromCon 2024 - Why Not Just Dots? UTF-8 Support in Prometheus 3.0
- Match score: 1.013
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2024/why-not-just-dots-utf-8-support-in-prometheus-3-0/POSFqCBLH-o.txt
- Transcript chars: 26389
- Keywords: metric, prometheus, characters, character, escaping, quotes, syntax, implementation, around, operator, format, underscore, legacy, support, metrics, validation, scrape, change

### Resumo baseado na transcript

[Music] hello um can we get these yay slides on the screen uh hi my name is Owen Williams uh I'm a software engineer at grafana labs and I've been uh working with the Prometheus Community for the past couple years on utf8 support in Prometheus uh 3 know um this is something that has been uh I thank the previous speakers for teasing this in the uh in their in their talk so now we get the big payoff um so I wanted to give some background um about

### Excerpt da transcript

[Music] hello um can we get these yay slides on the screen uh hi my name is Owen Williams uh I'm a software engineer at grafana labs and I've been uh working with the Prometheus Community for the past couple years on utf8 support in Prometheus uh 3 know um this is something that has been uh I thank the previous speakers for teasing this in the uh in their in their talk so now we get the big payoff um so I wanted to give some background um about character support in Prometheus um this this talk is mostly not technical because this is not uh an incredibly difficult like the actual technical part of it is not as um complicated as sort of the reasoning behind uh the change and uh the way we went about doing it so the traditional uh allowed character set in Prometheus is this Rex which people may have seen in code in one place or the other letters numbers underscores and colons uh in Prometheus the concept was to try to keep the metric names predictable um and and have a pretty strict set of standards for how they would be formed so there's all these rules about uh it's got to be you know these characters it the word should be like this it should have a unit it should have um a suffix uh and so the idea was to create the set of rules and with the set of rules you would avoid the problem of every team in your organization creating metrics with different uh naming schemes um while this was while this is a great approach um it turns out to have not worked out in the long term because other observability systems did not choose the same set of constraints uh so one of the things you know Prometheus famously doesn't use dots and then open Telemetry does and many other systems do graphite Etc um and in fact dots sort of started to gain favor as a way of doing hierarchical separation um and then this created problems with uh feature par first of all so just familiarity people come over to Prometheus if they're familiar with something else and they might say well what do you mean I can't even use a DOT um and then migrations if you're trying to move from one system to another having your uh metric names not be compatible is a big sticking point and what do you do with about that uh and so thus began the ground swell of the people want dots um and can't we just start start with this Rex and just put you know a period in there and then call it a day uh so let's do that okay great now we've added dots and now we're done thank you very much uh not so simple um as the discus
