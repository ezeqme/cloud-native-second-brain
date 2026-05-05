---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2024"
edition_id: 2024-berlin
year: 2024
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Scalability Reliability"]
speakers: ["Carrie Edwards", "Fiona Liao"]
source_url: https://promcon.io/2024-berlin/talks/implementing-outoforder-native-histograms-in-prometheus/
youtube_url: https://www.youtube.com/watch?v=VlTtwCWnRjg
youtube_search_url: https://www.youtube.com/results?search_query=Implementing+Out-of-Order+Native+Histograms+in+Prometheus+PromCon+2024
video_match_score: 1.028
status: video-found
---

# Implementing Out-of-Order Native Histograms in Prometheus

## Identificação

- Edição: PromCon EU 2024
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Metrics]], [[Scalability Reliability]]
- Speakers: Carrie Edwards, Fiona Liao
- Página oficial: https://promcon.io/2024-berlin/talks/implementing-outoforder-native-histograms-in-prometheus/
- YouTube: https://www.youtube.com/watch?v=VlTtwCWnRjg

## Resumo

Support for out-of-order ingestion of float samples was introduced in Prometheus v2.39.0. With the introduction of native histograms in Prometheus 2.41.0, it was necessary to adapt the TSDB’s handling of out-of-order samples in order to support native histograms. In this talk, we will tell the story of how we made our first substantial contribution to Prometheus by adding support for out-of-order ingestion of native histograms, and dive into the challenges and changes required in the TSDB to make this happen.

## Abstract oficial

Support for out-of-order ingestion of float samples was introduced in Prometheus v2.39.0. With the introduction of native histograms in Prometheus 2.41.0, it was necessary to adapt the TSDB’s handling of out-of-order samples in order to support native histograms.

In this talk, we will tell the story of how we made our first substantial contribution to Prometheus by adding support for out-of-order ingestion of native histograms, and dive into the challenges and changes required in the TSDB to make this happen.

The audience will learn the internals of out-of-order ingestion, native histograms and the challenges of the implementation of ingesting OOO native histograms. We will also share our process of getting familiarized with the TSDB, and hopefully encourage others to contribute to Prometheus.

## Links

- Página oficial: https://promcon.io/2024-berlin/talks/implementing-outoforder-native-histograms-in-prometheus/
- YouTube: https://www.youtube.com/watch?v=VlTtwCWnRjg
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=VlTtwCWnRjg
- YouTube title: PromCon 2024 - Implementing Out-of-Order Native Histograms in Prometheus
- Match score: 1.028
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2024/implementing-out-of-order-native-histograms-in-prometheus/VlTtwCWnRjg.txt
- Transcript chars: 21198
- Keywords: samples, chunks, counter, histograms, native, prometheus, sample, histogram, resets, another, single, ingestion, written, values, buckets, incoming, always, already

### Resumo baseado na transcript

[Music] uh hi everyone Welcome to our talk uh my name is Carrie Edwards and I'm a senior software engineer at grafana labs and I'm Fiona I'm also a senior software engineer at grafana labs and so as a bit of background to this talk we have both done some small PRS in Prometheus before but out of order native histograms was the first significant contribution made so we'll be talking about what we did what we learned and hopefully encourage you all to contribute to Prometheus um but before

### Excerpt da transcript

[Music] uh hi everyone Welcome to our talk uh my name is Carrie Edwards and I'm a senior software engineer at grafana labs and I'm Fiona I'm also a senior software engineer at grafana labs and so as a bit of background to this talk we have both done some small PRS in Prometheus before but out of order native histograms was the first significant contribution made so we'll be talking about what we did what we learned and hopefully encourage you all to contribute to Prometheus um but before we go into all the scary out of order details let's first introduce a few key Prometheus Concepts first uh so I know there's already been a lot of really great talks on Native histograms so you've already heard a lot about them but I'm going to quickly summarize them again um so native histograms are similar to Classic histograms they store distribution of data points rather than raw data uh they frequently used for quantile estimations um the data is recorded in counts of values that fall into certain ranges and these are called buckets so in this example we have five values in the range of 1 to two uh three values in the range of 2 to 4 0 from 4 to 8 and seven from 8 to 12 um the main difference between classic histograms and Native histograms is that for classic histograms you have to define the bucket boundaries yourself ahead of time this can be difficult to determine what the proper boundary should be and this might might change over time so uh Native histograms fixes uh that issue because the buckets are pre-computed uh and exponentially increasing over time so I'm not going to get into all the details of the structure but some of the properties are important to know for this talk so the first would be the count which is the overall count of obser observations in the native histogram and then there's also the positive buckets and negative buckets which store the counts um that fall into the buckets and then there's the zero count which is the count of values that are zero or close to zero and the zero count combined with the positive and negative buckets should sum to the overall count uh what is out of order ingestion so um originally Prometheus only accepted in ordered samples which worked well uh with a pool-based system but there's situations where you could have samples arrive out of order Um this can happen for a variety of reasons such as network issues uh loss of network connection but another possible reason is uh push-based metric systems are more likely t
