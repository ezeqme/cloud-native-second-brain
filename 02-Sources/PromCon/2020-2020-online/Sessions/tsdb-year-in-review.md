---
type: promcon-talk
conference: PromCon
edition: "PromCon Online 2020"
edition_id: 2020-online
year: 2020
city: "Online"
country: "Online"
topics: ["Prometheus Core", "Remote Write Storage", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2020-online/talks/tsdb--year-in-review/
youtube_url: https://www.youtube.com/watch?v=K7R2xw4s-5o
youtube_search_url: https://www.youtube.com/results?search_query=TSDB%3A+Year+In+Review+PromCon+2020
video_match_score: 0.567
status: video-found
---

# TSDB: Year In Review

## Identificação

- Edição: PromCon Online 2020
- País/cidade: Online / Online
- Temas: [[Prometheus Core]], [[Remote Write Storage]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2020-online/talks/tsdb--year-in-review/
- YouTube: https://www.youtube.com/watch?v=K7R2xw4s-5o

## Resumo

Speaker: Ganesh Vernekar Prometheus’ storage engine has seen a lot of improvements and optimizations in the past 1 year since we had PromCon 2019 where I gave a review on TSDB developments since Prometheus 2.0. Similarly, in this talk, I will speak about all the new enhancements and features that have been added to TSDB since PromCon 2019 and will be added in the future. Some of the notable ones include: Various memory optimizations for loading blocks and compaction.

## Abstract oficial

Speaker: Ganesh Vernekar

Prometheus’ storage engine has seen a lot of improvements and optimizations in the past 1 year since we had PromCon 2019 where I gave a review on TSDB developments since Prometheus 2.0. Similarly, in this talk, I will speak about all the new enhancements and features that have been added to TSDB since PromCon 2019 and will be added in the future. Some of the notable ones include:


Various memory optimizations for loading blocks and compaction.
Isolation
M-map of Head chunks.
Faster restarts with a snapshot of chunks.
Lifting the block index size limit.


I will also talk about how each of these developments impacted Prometheus.

## Links

- Página oficial: https://promcon.io/2020-online/talks/tsdb--year-in-review/
- YouTube: https://www.youtube.com/watch?v=K7R2xw4s-5o
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=K7R2xw4s-5o
- YouTube title: PromCon Online 2020 - TSDB: Year In Review, Ganesh Vernekar @ Grafana Labs
- Match score: 0.567
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2020/tsdb-year-in-review/K7R2xw4s-5o.txt
- Transcript chars: 20330
- Keywords: memory, series, prometheus, actually, release, offset, optimizations, whenever, question, already, stored, headlock, another, postings, mapping, isolation, samples, posting

### Resumo baseado na transcript

[Music] welcome everyone to my talk tsd another year in so in the last prom con which happened in november 2019 i gave a similar talk called tsd one year in where i talked about what went into the tsb since the prometheus 2.0 release and in this talk i am going to talk what went into the tsdb since we had the last prop con which was in number 2019 so little about myself i am a software engineer at grafana labs and i am a prometheus member and is to move to 64 bit postings but it comes with it the problems in its own uh one of the problem is space on the disk like if you are just doubling the number of bits that is stored for posting it's going to take a lot of space on disk and not just that when you are storing a lot of data on disk fetching it is also slower and one of the thing prometheus aims is query performance so when the move to 64 bit postings come you have to take care of both performance and the space so we tried uh and tested lots of different uh compressions that we can do on this uh 64 bit postings and after lots of testing we decided to go with prefix compression where you store a common prefix and a list of suffixes and call it a bucket in 64-bit postings we chose 48 bits of prefix and 16 bits of the suffix which gives near equal performance of 32-bit postings and they actually take less space than

### Excerpt da transcript

[Music] welcome everyone to my talk tsd another year in so in the last prom con which happened in november 2019 i gave a similar talk called tsd one year in where i talked about what went into the tsb since the prometheus 2.0 release and in this talk i am going to talk what went into the tsdb since we had the last prop con which was in number 2019 so little about myself i am a software engineer at grafana labs and i am a prometheus member and i maintain the time series database part of the prometheus and i'll be sharing these slides after the talk so make sure you follow me on twitter i'll be sharing it there so let's see what happened in tsub since from con 2019 the outland outline of this talk is going to be first we start with what went into tcp already which are available in the prometheus releases and we will move on to what's coming up and we'll end with the features that were added for the downstream users like cortex thanos etc so what's already in isolation so isolation is finally in i talked about this even in the last prom con so the basic idea about this is earlier if you had like 1000 metrics that you are scraping and you use that in a histogram query and if the scrape is complete only up to like 500 metrics and if you query the tsdb you could see partial results like 500 metrics of the new script 500 matrix from the old script so this creates problems in various scenarios and isolation fixes it so this work was started by brian long ago and in the last prom con i mentioned gotham took it forward but that went stale again finally beyond who who is one of the earliest member of prometheus took the charge and finally finished the work which brian and gotham had started and isolation is finally in so if you are querying you won't see partial script so how this is implemented is we assign something called appender id for every append that comes into the tsdb and using this append id when we query we have a isolation state when we are iterating through the samples during the query we see if the append id that the sample corresponds to whether it's an active query like the active append which is not committed then we discard it so with some logic around that we have achieved the isolation now the next thing so i'm going to talk about a series of optimizations which brian put in in the 2.15 release so in the bottom right corner for of every slide i have the release number mentioned in which these optimizations are there for example isolation had 2.17
