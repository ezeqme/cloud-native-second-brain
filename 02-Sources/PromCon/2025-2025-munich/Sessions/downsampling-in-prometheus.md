---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2025"
edition_id: 2025-munich
year: 2025
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Scalability Reliability"]
speakers: ["Jan Fajerski"]
source_url: https://promcon.io/2025-munich/talks/downsampling-in-prometheus/
youtube_url: https://www.youtube.com/watch?v=yDNClMnFqe8
youtube_search_url: https://www.youtube.com/results?search_query=Downsampling+in+Prometheus+PromCon+2025
video_match_score: 0.93
status: video-found
---

# Downsampling in Prometheus

## Identificação

- Edição: PromCon EU 2025
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Scalability Reliability]]
- Speakers: Jan Fajerski
- Página oficial: https://promcon.io/2025-munich/talks/downsampling-in-prometheus/
- YouTube: https://www.youtube.com/watch?v=yDNClMnFqe8

## Resumo

Downsampling of TSDB data has been requested repeatedly in the past. In this session we will first take brief look at the history of this feature requests and I will outline common use cases. Then we'll look at examples of how downsampling use cases can be solved today with Prometheus.

## Abstract oficial

Downsampling of TSDB data has been requested repeatedly in the past. In this session we will first take brief look at the history of this feature requests and I will outline common use cases. Then we'll look at examples of how downsampling use cases can be solved today with Prometheus. Last but not least we'll explore some upcoming features and undecided feature requests that could open up new setups, as well as scenarios that will forever stay outside of Prometheus' scope.

## Links

- Página oficial: https://promcon.io/2025-munich/talks/downsampling-in-prometheus/
- YouTube: https://www.youtube.com/watch?v=yDNClMnFqe8
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=yDNClMnFqe8
- YouTube title: PromCon 2025 - Downsampling in Prometheus
- Match score: 0.93
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2025/downsampling-in-prometheus/yDNClMnFqe8.txt
- Transcript chars: 19644
- Keywords: sample, prometheus, samples, downsampling, pretty, already, little, algorithm, usually, recording, second, basically, actually, signal, processing, interesting, wanted, probably

### Resumo baseado na transcript

Actually bit too excited as it turns thought I got a little carried away. I read my proposal after the fact and I needed to make sure that I'm actually um talking about what I promised I would talk about, but I think it's close enough. Um we will talk a little bit about what works in Prometheus today already, what everybody can do. of the goal is usually um fewer samples that could be a reduction in bandwidth um so you know if you think Prometheus think labels um or sample rate, right? Um and if you ever look at any graphs, be it in Prometheus UI or in Graphana, there's definitely downsampling going on there. Um so yeah, really you Prometheus is already a what they call a multi- rate uh digital processing system if you want a nice term for it.

### Excerpt da transcript

[music] this two. All right, there we are finally. Um, welcome everybody. Sorry for the slight delay. Um, I hope you can hear me all right. I know that sounds kind of tricky. Um, so yeah. Hi, I'm Yan. Uh, today I want to talk about downsampling in Prometheus. Um, I'm quite excited about this talk. Actually bit too excited as it turns thought I got a little carried away. I read my proposal after the fact and I needed to make sure that I'm actually um talking about what I promised I would talk about, but I think it's close enough. Um so downsampling I think in Prometheus um is pretty old feature request, right? Um I think uh first came up in 2017 and the answer was yeah, we don't do it. Um but it's a pretty interesting topic. Um uh that's sort of I think one of the main motivations here um to talk about this and u I also can talk a little bit about signal processing which is super cool um so why not right um and as you can see there's another topic I can relate this to that I'm reasonably excited about so uh yeah that was sort of the motivation and um I recently did some work with this um at my day job at Red Hat which unfortunately uh doesn't leave me too much time to work on Prometheus so you was a nice nice coincidence to take this here.

So yeah, that goes to say um I'm quite excited about this talk. All right. Um what are we going to do today? So uh we'll we'll talk about downsampling. Um sort of what that actually means. It's a pretty broad term. Um and when it's requested in sort of Prometheus and systems like that, um it usually means a subset of what it could mean. So we need to sort of define what we want to talk about, right? Um we will talk a little bit about what works in Prometheus today already, what everybody can do. Um and then I will well I wanted to show you a little example uh the experiment I was trying to do. Um it's there is still a bug so I don't have too much to show but uh there's a couple of things I can uh I can already sort of tell you about. Um okay so downsampling um what do we mean when we say uh downsampling or you know what others what might others mean? So this is a um term that comes from the land of signal processing specifically digital signal processing or discrete signal processing. Um and it's really uh super ubiquitous right here in this room all these machines uh there's probably tens if not hundreds of um sample rate conversion processes going on right now right the sound all the video um it's really everywhere um
