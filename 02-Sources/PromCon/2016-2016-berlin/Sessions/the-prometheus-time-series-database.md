---
type: promcon-talk
conference: PromCon
edition: "PromCon 2016"
edition_id: 2016-berlin
year: 2016
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Remote Write Storage", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2016-berlin/talks/the-prometheus-time-series-database/
youtube_url: https://www.youtube.com/watch?v=HbnGSNEjhUc
youtube_search_url: https://www.youtube.com/results?search_query=The+Prometheus+Time+Series+Database+PromCon+2016
video_match_score: 0.83
status: video-found
---

# The Prometheus Time Series Database

## Identificação

- Edição: PromCon 2016
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Remote Write Storage]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2016-berlin/talks/the-prometheus-time-series-database/
- YouTube: https://www.youtube.com/watch?v=HbnGSNEjhUc

## Resumo

Speaker: Björn Rabenstein Various time series databases (TSDBs) have been implemented on top of key-value stores with BigTable semantics. The TSDB that sits at the core of the Prometheus monitoring system started with a similar approach and was built on top of LevelDB. The Prometheus server as we know it today, however, uses a highly optimized custom storage layer for bulk sample data, enabling a single server to sustain an ingestion rate of 500,000 samples per second belonging to millions of time series.

## Abstract oficial

Speaker: Björn Rabenstein

Various time series databases (TSDBs) have been implemented on top of
key-value stores with BigTable semantics. The TSDB that sits at the core of
the Prometheus monitoring system started with a similar approach and was built
on top of LevelDB. The Prometheus server as we know it today, however, uses a
highly optimized custom storage layer for bulk sample data, enabling a single
server to sustain an ingestion rate of 500,000 samples per second belonging to
millions of time series. Very recent improvements of the in-memory
representation of sample data resulted in an outstanding compression level of
1.3 bytes per sample in a typical production setup. A journey from fundamental
challenges of TSDB design to details of the Prometheus storage layer.

## Links

- Página oficial: https://promcon.io/2016-berlin/talks/the-prometheus-time-series-database/
- YouTube: https://www.youtube.com/watch?v=HbnGSNEjhUc
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=HbnGSNEjhUc
- YouTube title: PromCon 2016: The Prometheus Time Series Database - Björn Rabenstein
- Match score: 0.83
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2016/the-prometheus-time-series-database/HbnGSNEjhUc.txt
- Transcript chars: 40438
- Keywords: prometheus, series, gorilla, chunks, memory, actually, sample, encoding, storage, pretty, single, double, write, samples, always, better, serious, spinning

### Resumo baseado na transcript

welcome come back everyone from lunch so we'll be continuing on now with the uh afternoon session Richie we're continuing on with the afternoon session uh so when lots of people uh come to Prometheus they uh ask about the clustering and they're shocked that we don't have it and it turns out normally that they're used to systems which you know can handle a thousand machines with like two metrics each remember actually once in IRC we had someone a graphite set up and uh they were worried pritus

### Excerpt da transcript

welcome come back everyone from lunch so we'll be continuing on now with the uh afternoon session Richie we're continuing on with the afternoon session uh so when lots of people uh come to Prometheus they uh ask about the clustering and they're shocked that we don't have it and it turns out normally that they're used to systems which you know can handle a thousand machines with like two metrics each remember actually once in IRC we had someone a graphite set up and uh they were worried pritus couldn't handle their uh 6,000 metrics and that's not per second that's just 6,000 metrics um so the thing is though the pritus is so efficient that you don't need clustering or distrib distribution most of the time and a lot of that is due to Bjorn and his optimizations of the storage system so that we can get up to 800,000 samples per second so B's not going to tell us about it how works okay thank you um actually only some parts of the storage system are done optimized by me um so many people ask me how is the storage lay and the Prometheus the Prometheus server working um and this is finally the talk I always wanted to give to explain everybody how that works and it's recorded for posteriority and everything um the um Prometheus is not a Time Zer database Prometheus happens to use an embedded time series database somewhere at its core and that's source of confusion because many like high-profile monitoring projects are sometimes just a Time serious database like open TSB for example so um Prometheus can't really compare or compete with that so much because it's way more in a way because it deals with all aspects of monitoring and alerting but on the other hand the TSB functionality is actually way less but it's still pretty neat and optimized and so totally worth the talk so this is just about a tiny tiny fraction of the Prometheus ecosystem and it will still be quite a right um I even have to um narrow this down even more this is just about raw sample storage this is totally not about indexing so basically a tstv or the tsv we use for Prometheus has two sides the one is Al a promql expression I want to find out which time series am I actually dealing with and that is an indexing problem and then once I know which time Ser I'm dealing with please give me those time series with all their samples um the indexing we had planned to give a talk about indexing but then there were too many interesting topics to talk about so I guess next year at promcon we will have an i
