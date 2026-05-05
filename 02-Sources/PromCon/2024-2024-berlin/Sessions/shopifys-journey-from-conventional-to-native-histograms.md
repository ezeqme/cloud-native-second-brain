---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2024"
edition_id: 2024-berlin
year: 2024
city: "Berlin"
country: "Germany"
topics: ["Metrics", "Remote Write Storage", "Alerting", "Kubernetes", "Scalability Reliability", "Visualization Dashboards"]
speakers: ["Sebastian Rabenhorst", "Pedro Tanaka"]
source_url: https://promcon.io/2024-berlin/talks/shopifys-journey-from-conventional-to-native-histograms/
youtube_url: https://www.youtube.com/watch?v=AeGOiSA4XRA
youtube_search_url: https://www.youtube.com/results?search_query=Shopify%27s+journey+from+conventional+to+native+histograms+PromCon+2024
video_match_score: 1.026
status: video-found
---

# Shopify's journey from conventional to native histograms

## Identificação

- Edição: PromCon EU 2024
- País/cidade: Germany / Berlin
- Temas: [[Metrics]], [[Remote Write Storage]], [[Alerting]], [[Kubernetes]], [[Scalability Reliability]], [[Visualization Dashboards]]
- Speakers: Sebastian Rabenhorst, Pedro Tanaka
- Página oficial: https://promcon.io/2024-berlin/talks/shopifys-journey-from-conventional-to-native-histograms/
- YouTube: https://www.youtube.com/watch?v=AeGOiSA4XRA

## Resumo

At Shopify, we've implemented a Thanos-based solution for monitoring hundreds of clusters and thousands of applications, which primarily use StatsD metrics with a heavy reliance on histograms. In this talk we will present how and why we migrated our backend, user dashboards and alerts from conventional to native histograms and we will highlight how the composition of our clients' metrics, primarily histograms, served as the driving force behind our migration. We will elaborate what problems the migration solved and the new challenges it presented to us and how we did it with minimal impact on our users.

## Abstract oficial

At Shopify, we've implemented a Thanos-based solution for monitoring hundreds of clusters and thousands of applications, which primarily use StatsD metrics with a heavy reliance on histograms.

In this talk we will present how and why we migrated our backend, user dashboards and alerts from conventional to native histograms and we will highlight how the composition of our clients' metrics, primarily histograms, served as the driving force behind our migration. We will elaborate what problems the migration solved and the new challenges it presented to us and how we did it with minimal impact on our users. 
Furthermore, we will provide insights into our contributions to Thanos, with a focus on the implementation of native histogram support.

## Links

- Página oficial: https://promcon.io/2024-berlin/talks/shopifys-journey-from-conventional-to-native-histograms/
- YouTube: https://www.youtube.com/watch?v=AeGOiSA4XRA
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=AeGOiSA4XRA
- YouTube title: PromCon 2024 - Shopify's journey from conventional to native histograms
- Match score: 1.026
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2024/shopifys-journey-from-conventional-to-native-histograms/AeGOiSA4XRA.txt
- Transcript chars: 17958
- Keywords: histograms, native, buckets, metrics, histogram, classic, metric, migration, cardinality, memory, series, precision, configuration, sebastian, pritus, dashboards, bucket, higher

### Resumo baseado na transcript

[Music] well thank you thank you for having us um at proncom thank you for the organizing committee as well so uh I will talk about today um Native histograms and how we migrated um from classic histograms to Native histograms at Shopify my name is Pedro I'm working as a senior software engineer um at chopy most specifically on the observability team and together with Sebastian we work on maintaining uh Shopify main um metric uh pipeline metric pipeline today I'll will talk about uh actually Sebastian will come

### Excerpt da transcript

[Music] well thank you thank you for having us um at proncom thank you for the organizing committee as well so uh I will talk about today um Native histograms and how we migrated um from classic histograms to Native histograms at Shopify my name is Pedro I'm working as a senior software engineer um at chopy most specifically on the observability team and together with Sebastian we work on maintaining uh Shopify main um metric uh pipeline metric pipeline today I'll will talk about uh actually Sebastian will come in virtually talking about uh a bit of context and how we do monitoring at Shopify and some of the um specifics that we have in our pipeline then I'll be talking about the migration work that we did and how we migrated the users to um start using um Native histograms and cut over from classic histograms to Native histograms then we talk about some Automation and some learnings that we had during our process there go thank you soas my name is Sebastian and I'm also part of the observability metrics team at Shopify I will give you some context on our migration to Native histograms but let's start with a recap of histograms in general in Prometheus histograms are used to observe and measure the distribution of values such as request Creations by categorizing them into buckets here you see an example of an histogram observing durations with three buckets conventional histograms or the old way of doing histograms in Prometheus consist of one time series for each bucket which you can query using using the Le label and a count time series which just counts the number of observations and the sometime series which sums up all values of each observation buckets for conventional histograms must be configured in advanced and are fixed capturing useful metrics requires choosing the right buckets which is hard without knowing the shape of your metrix in advanced this often results in a trade-off between low precision and high cardinality low Precision if you just Define a low number of buckets without knowing the shape of your metrix this might end in all observations going in one bucket for example or to increase the Precision if you don't know the shape of your data you just would Define a high number of buckets which might give you higher Precision but also increases the cardinality and this might impact your system negatively you will later see examples for this so here are native histograms which aim to solve this this issue about buckets they combine the co
