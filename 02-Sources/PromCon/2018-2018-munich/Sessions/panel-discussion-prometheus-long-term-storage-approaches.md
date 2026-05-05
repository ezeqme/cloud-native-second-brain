---
type: promcon-talk
conference: PromCon
edition: "PromCon 2018"
edition_id: 2018-munich
year: 2018
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Remote Write Storage", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2018-munich/talks/panel-discussion-prometheus-long-term-storage-approaches/
youtube_url: https://www.youtube.com/watch?v=3pTG_N8yGSU
youtube_search_url: https://www.youtube.com/results?search_query=Panel+Discussion%3A+Prometheus+Long-Term+Storage+Approaches+PromCon+2018
video_match_score: 0.919
status: video-found
---

# Panel Discussion: Prometheus Long-Term Storage Approaches

## Identificação

- Edição: PromCon 2018
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Remote Write Storage]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2018-munich/talks/panel-discussion-prometheus-long-term-storage-approaches/
- YouTube: https://www.youtube.com/watch?v=3pTG_N8yGSU

## Resumo

In this panel, we will explore some of the emerging and competing approaches to Prometheus scalable long-term storage. Speakers: Julius Volz (moderator) Fabian Reinartz, Thanos Nikunj Aggarwal, M3DB Paul Dix, InfluxDB Tom Wilkie, Cortex Video link

## Abstract oficial

In this panel, we will explore some of the emerging and competing approaches to Prometheus scalable long-term storage.

Speakers:



Julius Volz (moderator)

Fabian Reinartz, Thanos

Nikunj Aggarwal, M3DB

Paul Dix, InfluxDB

Tom Wilkie, Cortex




Video link

## Links

- Página oficial: https://promcon.io/2018-munich/talks/panel-discussion-prometheus-long-term-storage-approaches/
- YouTube: https://www.youtube.com/watch?v=3pTG_N8yGSU
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3pTG_N8yGSU
- YouTube title: PromCon 2018: Panel Discussion - Long-Term Storage Approaches
- Match score: 0.919
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2018/panel-discussion-prometheus-long-term-storage-approaches/3pTG_N8yGSU.txt
- Transcript chars: 52298
- Keywords: storage, actually, prometheus, remote, question, basically, source, cortex, long-term, metrics, already, wanted, solution, database, format, thanos, support, answer

### Resumo baseado na transcript

so quiet thank you so the next thing actually is like really dear in new to my heart because I have been borrowing people for ages that we should have panel discussions and there's as a panel discussion so today's panel will be about long-term storage we have Fabian representing tennis we have tom representing cortex we have Julius doing the moderation we have good Nichkhun should be representing m3/d by uber and we have Paul from in flux thank you very much 0g thank you thought I was going like I think it's not just the blocks itself but the other pieces of like metadata that have to be standardized and like I said I'm particularly - arrow but the problem is arrow doesn't specify compressed types which is an issue so that's something

### Excerpt da transcript

so quiet thank you so the next thing actually is like really dear in new to my heart because I have been borrowing people for ages that we should have panel discussions and there's as a panel discussion so today's panel will be about long-term storage we have Fabian representing tennis we have tom representing cortex we have Julius doing the moderation we have good Nichkhun should be representing m3/d by uber and we have Paul from in flux thank you very much 0g thank you thought I was going to do the intros yep this is us you might be wondering how did we get into this situation so I'm joyous one of the initial like authors of Prometheus so I'll give some context about you know the history of storage Richie already introduced the others we'll get more details about their long-term storage approaches later on and basically you know the goal of the whole panel is to give people a bit of an idea of why do all these different storage solutions exist what are the differences between them which one might be the right one for you and yeah so let me start off by saying you know when we initially created promises at SoundCloud we didn't initially care so much about long-term storage we needed a tool to give us actionable alerts right now and maybe you know make it all so easy to make them highly available just by running - and it's nice thing that there's also some data that you can query nicely but we didn't care so much about you know keeping data for years and you know having gazillions of time series or you know just split up your primitive servers but then there were actual other users and they had all kinds of other different requirements so in the end we still said well we want to keep the primitive server itself simple because you know building a big clustered system with possibly consensus algorithms and so on that would be a bit of an antithesis to Prometheus which we want to keep simple and want to have a focus on the right now alerting and monitoring but we wanted to enable other people to build long-term storage use cases or even just you know even if you're not storing them maybe you want to ship every sample somewhere else and do something with it so we built a set of generic interfaces which is called the generic remote read and remote write interfaces where you can configure Prometheus to basically send on every sample that it scrapes to some remote URL endpoint and that could be a storage could be a stream process or whatever and for the reading t
