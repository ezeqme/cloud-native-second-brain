---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2022"
edition_id: 2022-munich
year: 2022
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Remote Write Storage", "Scalability Reliability", "Cost Optimization"]
speakers: []
source_url: https://promcon.io/2022-munich/talks/native-histograms-in-prometheus/
youtube_url: https://www.youtube.com/watch?v=AcmABV6NCYk
youtube_search_url: https://www.youtube.com/results?search_query=Native+Histograms+in+Prometheus+PromCon+2022
video_match_score: 0.925
status: video-found
---

# Native Histograms in Prometheus

## Identificação

- Edição: PromCon EU 2022
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Remote Write Storage]], [[Scalability Reliability]], [[Cost Optimization]]
- Speakers: N/A
- Página oficial: https://promcon.io/2022-munich/talks/native-histograms-in-prometheus/
- YouTube: https://www.youtube.com/watch?v=AcmABV6NCYk

## Resumo

Speaker(s): Ganesh Vernekar Histograms in Prometheus have worked reliably for years, but they have had a few downsides when it came to storage efficiency, accuracy of histogram queries, and flexibility in using histograms. Making histograms efficient and easy to use is a highly complex problem, and given the position of Prometheus we needed to get it right. After years of research by Björn Rabenstein, we have designed a new native histogram that is supported starting with Prometheus v2.40.0.

## Abstract oficial

Speaker(s): Ganesh Vernekar

Histograms in Prometheus have worked reliably for years, but they have had a few downsides when it came to storage efficiency, accuracy of histogram queries, and flexibility in using histograms.

Making histograms efficient and easy to use is a highly complex problem, and given the position of Prometheus we needed to get it right. After years of research by Björn Rabenstein, we have designed a new native histogram that is supported starting with Prometheus v2.40.0.

This talk is accompanied by a brief introduction to native histograms and how they are better. We will see how to start using this and migrate from the old histograms. The talk will end with what to expect in v2.40.0, current limitations, and the future roadmap for native histograms.

## Links

- Página oficial: https://promcon.io/2022-munich/talks/native-histograms-in-prometheus/
- YouTube: https://www.youtube.com/watch?v=AcmABV6NCYk
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=AcmABV6NCYk
- YouTube title: PromCon EU 2022: Native Histograms in Prometheus
- Match score: 0.925
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2022/native-histograms-in-prometheus/AcmABV6NCYk.txt
- Transcript chars: 19496
- Keywords: buckets, histograms, bucket, resolution, native, schema, histogram, client, prometheus, series, number, support, format, boundaries, boundary, previous, observations, seconds

### Resumo baseado na transcript

[Music] foreign [Music] I'm going to speak about the new native histograms in Prometheus I am Ganesh vanekar I'm a Prometheus team member and I work as a software engineer at grafana labs before starting work to see what are native histograms let's see what are histograms first histograms is a distribution of all your observations in specified time ranges we call them buckets in this particular example the First Column tells you there are 15 requests that took less than 0.1 seconds similarly there's a blue column tells you series is now combined into a single time series uh all this time Prometheus just stored a float value with the time series The timestamp was end the value was float now we are overhauling the entire storage to support this new data structure where

### Excerpt da transcript

[Music] foreign [Music] I'm going to speak about the new native histograms in Prometheus I am Ganesh vanekar I'm a Prometheus team member and I work as a software engineer at grafana labs before starting work to see what are native histograms let's see what are histograms first histograms is a distribution of all your observations in specified time ranges we call them buckets in this particular example the First Column tells you there are 15 requests that took less than 0.1 seconds similarly there's a blue column tells you like 25 requests were between 0.1 to 1 seconds and last bucket is a special one which encloses everything that was more than two seconds and this is how we store it in Prometheus right now we have a separate time series for each individual bucket and the last book and we use something called the Le label which means less than or equal to and all the time series are cumulative for example uh if you look at the time series which says L E equals to 1 it says 40 and not 25 which means it's everything that's less than one so if you want the count between 0.1 to 1 you have to subtract 40 with the previous time series and we have two more time series for this which is the overall count and the overall sum of observations so this is how it is done in Prometheus right now but this is how Native histograms will be stored it's a single data structure with everything that has to do with histograms uh we will take an exam I will show an example of how the native histogram looks like but to go over these very briefly the histogram has count and some like before it has a schema which defines uh what the bucket boundaries will be the 0.1 seconds and one second all those things we call as bucket boundaries and yeah schema defines what the bucket boundaries can be the positive spans and negative spans are just something which tells you which buckets are filled and positive spans are for positive observations negatives fans are for negative observations and positive buckets and negative buckets hold the actual observations in them we'll ignore the other two parameters for this talk but now let's see what how do we store these native histograms let's start with schema because that's where everything starts so with schema we get something called a ratio who's formula is 2 power of 2 power of minus schema we'll see why this 2 power of 2 power is uh required later and this ratio defines uh what's the ratio between a bucket boundary and the bucket boundary of a
