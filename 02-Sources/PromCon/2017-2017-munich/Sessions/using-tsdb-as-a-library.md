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
source_url: https://promcon.io/2017-munich/talks/using-tsdb-as-a-library/
youtube_url: https://www.youtube.com/watch?v=AYnXeMGAZes
youtube_search_url: https://www.youtube.com/results?search_query=Using+TSDB+as+a+library+PromCon+2017
video_match_score: 0.691
status: video-found
---

# Using TSDB as a library

## Identificação

- Edição: PromCon 2017
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2017-munich/talks/using-tsdb-as-a-library/
- YouTube: https://www.youtube.com/watch?v=AYnXeMGAZes

## Resumo

Speaker: Goutham Veeramachaneni This talk will be an introductory talk about using the new datastore as a library. It will be based on this blog: https://geekon.tech/content/post/tsdb-embeddable-timeseries-database/ with clearer and more verbose examples and a simple REST based timeseries demo at the end. People will leave with: A clear understanding of how to use tsdb.

## Abstract oficial

Speaker: Goutham Veeramachaneni

This talk will be an introductory talk about using the new datastore as a library. It will be based on this blog: https://geekon.tech/content/post/tsdb-embeddable-timeseries-database/ with clearer and more verbose examples and a simple REST based timeseries demo at the end.

People will leave with:


A clear understanding of how to use tsdb.
The fundamentals that are needed to start contributing to the tsdb <--> Prometheus layer.




Video link -
Slides

## Links

- Página oficial: https://promcon.io/2017-munich/talks/using-tsdb-as-a-library/
- YouTube: https://www.youtube.com/watch?v=AYnXeMGAZes
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=AYnXeMGAZes
- YouTube title: PromCon 2017: Using TSDB as a library - Goutham Veeramachaneni
- Match score: 0.691
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2017/using-tsdb-as-a-library/AYnXeMGAZes.txt
- Transcript chars: 17533
- Keywords: series, prometheus, actually, database, create, essentially, values, labels, matches, weather, points, prompt, fabian, anyways, basically, insert, expression, databases

### Resumo baseado na transcript

[Music] all right so now welcome Gotham who is a new contributor he started noticing Prometheus when fabian built the new TST beat for Prometheus - and like record speed learned how it all works and is already know improving it in various ways and he's going to now tell you how to use the TST B package outside of Prometheus for other purposes hello hi I'm Gautam I'm currently a bachelor student at IIT Hyderabad until exactly 10 days back I was an intern with core OS where I

### Excerpt da transcript

[Music] all right so now welcome Gotham who is a new contributor he started noticing Prometheus when fabian built the new TST beat for Prometheus - and like record speed learned how it all works and is already know improving it in various ways and he's going to now tell you how to use the TST B package outside of Prometheus for other purposes hello hi I'm Gautam I'm currently a bachelor student at IIT Hyderabad until exactly 10 days back I was an intern with core OS where I got to work on the two-pointer engine with Fabian so I have a question how many of you here are students Wow ok nice so yeah PSDB so this is the DSD B repo and this is Prometheus 2.0 storage engine and it's actually a library rendered by Prometheus this is was a conscious design decision which means you guys can embed it in your golang applications but why would you want to do that type I think time series is everywhere and I think this is a very nice API to deal with large data sets for example take weather data all of weather data is just time series and we probably want to do correlation and a lot of other data science stuff and you might be like oh I have big data I need a Hadoop cluster but from fabian stock we know that we can compress 1 billion points into one point just 1 point 2 GB so I don't think your big data is that big if you use tsdp so anyways so I'm gonna take you through so some people launch products at a conference I'm launching a startup I'm gonna take you through a crazy startup idea Prometheus with push so how many of you when you initially configured Prometheus thought why just Prometheus need to discover my services why can't I just push data oh my god service discovery reliable complex how many of you friend that oops how many of you are stupid enough to write an aggregator well you can push your data I did that anyways anyways we get a lot of requests for this at least are you when I was looking into it there were some requests so Prometheus has a lot of users if I capture 5% of those users I have a multi-million dollar startup introducing ROM flux so you you you in just influx line protocol which means all your client libraries are there and you query using chrome QL which we all know how cool it is and I'm not joking I even made a logo so no that is not how Prometheus works and I I spent it's been a long time since I touched a production Prometheus so all these terms are being products done by an amateur don't do it in production but the real reason I'm not
