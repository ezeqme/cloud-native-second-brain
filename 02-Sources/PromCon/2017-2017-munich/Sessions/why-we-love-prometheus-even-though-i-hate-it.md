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
source_url: https://promcon.io/2017-munich/talks/why-we-love-prometheus-even-though-i-hate-it/
youtube_url: https://www.youtube.com/watch?v=Z-4XmQPBFn8
youtube_search_url: https://www.youtube.com/results?search_query=Why+We+Love+Prometheus+Even+Though+I+Hate+It+PromCon+2017
video_match_score: 0.869
status: video-found
---

# Why We Love Prometheus Even Though I Hate It

## Identificação

- Edição: PromCon 2017
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2017-munich/talks/why-we-love-prometheus-even-though-i-hate-it/
- YouTube: https://www.youtube.com/watch?v=Z-4XmQPBFn8

## Resumo

Speaker: Yaroslav Molochko At Anchorfree we had about 10 monitoring systems of different types. It was difficult to manage, we had 0 observability, as it was impossible to see whole picture. We decided to go with Prometheus full speed, migrated all the major and minor systems to it.

## Abstract oficial

Speaker: Yaroslav Molochko

At Anchorfree we had about 10 monitoring systems of different types. It was difficult to manage, we had 0 observability, as it was impossible to see whole picture. We decided to go with Prometheus full speed, migrated all the major and minor systems to it. This was not easy move, as we faced with a bunch of problems, fundamental misunderstandings, and resistance.

In this talk I would like to highlight the problems we faced, how we solved it. Answer why we still hate Prometheus and why we love it with all our hearts at the same time.



Video link

## Links

- Página oficial: https://promcon.io/2017-munich/talks/why-we-love-prometheus-even-though-i-hate-it/
- YouTube: https://www.youtube.com/watch?v=Z-4XmQPBFn8
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Z-4XmQPBFn8
- YouTube title: PromCon 2017: Why We Love Prometheus Even Though I Hate It - Yaroslav Molochko
- Match score: 0.869
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2017/why-we-love-prometheus-even-though-i-hate-it/Z-4XmQPBFn8.txt
- Transcript chars: 9344
- Keywords: actually, server, hadoop, prometheus, premises, promises, country, matrix, though, basically, blocked, decided, everything, discovered, platform, flux, telegraph, output

### Resumo baseado na transcript

[Music] next up if you love Moscow very good tell us why they love to missus but he doesn't yeah sense for having me and let me speak even though I have hate and permissions in the same sentence so Who am I I'm a System Architect and part time DevOps team lead a tanker free and what anchor phrase is our mission is to provide secure and anonymous access to Internet to or people in the pool basically we a VPN provider one was the biggest in why and

### Excerpt da transcript

[Music] next up if you love Moscow very good tell us why they love to missus but he doesn't yeah sense for having me and let me speak even though I have hate and permissions in the same sentence so Who am I I'm a System Architect and part time DevOps team lead a tanker free and what anchor phrase is our mission is to provide secure and anonymous access to Internet to or people in the pool basically we a VPN provider one was the biggest in why and we on a short list to be blocked on when our country decided to to block anything so we were using a lot of monitoring solution project our hospital shield project is like ten years old and we approached monitoring from different angles and I would say it is my click said it looks like a mess so we said a couple of requirements to our new age winter and solution it had to be highly available it had scaling up and down and out without data loss is maintenance lawn retention friendly community everything must be premises right and 2016 we discovered that it had zero don't don't kick me right now let me speak so about high-level beauty we discovered that even though you have you can have several premises servers you still have gaps in graphs and if you if you have stables stable platform it is may be acceptable to have one gap for one hour per month but when you are tuning and prior to 1.6 it was dark magic we were not able to like have continuous graph every day it was like some gaps and our management was driving crazy because our CEO is so questioned about this deliverances free internet to everyone that we have this white screens around the office and if it sees some gap he we should call an ambulance so we couldn't afford so horizontal scaling actually there is no such thing as scaling promises but there is a sharding and we discovered that host-based sharding doesn't work well and Federation server is actually it is not a single point of entrance to the data but it is basically yet another promise use with some limited amount of metrics and actually when we tried to shared our data by node we discovered that our herbs guys had a hard time figuring out figuring out where data is and actually this was we were not alone I am happy that we are not like the one who wants something strange so ease of maintenance back to 1.6 when we were actually we start with 1.4 it was a dark magic of tuning we had a lot of from we we were incrementing this ancient storage engine like it was like one Zen to and was like not really e
