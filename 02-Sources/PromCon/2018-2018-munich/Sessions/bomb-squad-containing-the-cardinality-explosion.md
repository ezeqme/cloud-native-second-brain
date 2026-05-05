---
type: promcon-talk
conference: PromCon
edition: "PromCon 2018"
edition_id: 2018-munich
year: 2018
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Remote Write Storage", "Alerting", "Scalability Reliability", "Cost Optimization"]
speakers: []
source_url: https://promcon.io/2018-munich/talks/bomb-squad-containing-the-cardinality-explosion/
youtube_url: https://www.youtube.com/watch?v=MHiXP5QW4_U
youtube_search_url: https://www.youtube.com/results?search_query=Bomb+Squad%3A+Containing+the+Cardinality+Explosion+PromCon+2018
video_match_score: 1.009
status: video-found
---

# Bomb Squad: Containing the Cardinality Explosion

## Identificação

- Edição: PromCon 2018
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Remote Write Storage]], [[Alerting]], [[Scalability Reliability]], [[Cost Optimization]]
- Speakers: N/A
- Página oficial: https://promcon.io/2018-munich/talks/bomb-squad-containing-the-cardinality-explosion/
- YouTube: https://www.youtube.com/watch?v=MHiXP5QW4_U

## Resumo

Speaker: Cody Boggs Series cardinality can be a large foot-gun that can take out a Prometheus instance quickly. It can have similar impacts to downstream systems when using remote write. Finding the offending series and recovering from such an event can cause a large downtime for your Prometheus installation.

## Abstract oficial

Speaker: Cody Boggs

Series cardinality can be a large foot-gun that can take out a Prometheus instance quickly. It can have similar impacts to downstream systems when using remote write. Finding the offending series and recovering from such an event can cause a large downtime for your Prometheus installation. In this talk I will show an implementation of a sidecar to Prometheus that automatically detects and squelches series whose cardinality is growing quickly. Using a combination of recording rules, dynamic metric relabel configs, and alerting, we can detect, throttle, and alert on any explosion in progress.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2018-munich/talks/bomb-squad-containing-the-cardinality-explosion/
- YouTube: https://www.youtube.com/watch?v=MHiXP5QW4_U
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=MHiXP5QW4_U
- YouTube title: PromCon 2018: Bomb Squad: Containing the Cardinality Explosion
- Match score: 1.009
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2018/bomb-squad-containing-the-cardinality-explosion/MHiXP5QW4_U.txt
- Transcript chars: 22484
- Keywords: cardinality, metric, prometheus, actually, series, little, values, exploding, config, metrics, moment, instance, explosion, hopefully, silence, pretty, quickly, labels

### Resumo baseado na transcript

all right thank you can you hear me okay excellent all right so actually to the last question for Julian's this is hopefully very very relevant so we'll see so yeah this is about bomb squad it's a project that we're working on to hopefully help tone down some bad events that we'll talk about in a moment first up Who am I so I'm Cody blogs nicknamed Choni if we have time we may tell that story I don't know it depends I'm an ops nerd for about the

### Excerpt da transcript

all right thank you can you hear me okay excellent all right so actually to the last question for Julian's this is hopefully very very relevant so we'll see so yeah this is about bomb squad it's a project that we're working on to hopefully help tone down some bad events that we'll talk about in a moment first up Who am I so I'm Cody blogs nicknamed Choni if we have time we may tell that story I don't know it depends I'm an ops nerd for about the last eight years been lead of ops for fresh tracks for about the last year a little bit more I'm obsessed with metrics and most other things observability related I like to pretend to write code my team is helping me to be less pretend II and more actual you know writing and I break all the things because that's apparently how I learn best so I'll go from there so what's on deck let's talk about what is cardinality we've heard it several times today but we should get a better feel for it what does it mean when it explodes it sounds bad and spoiler alert it is who cares we need charts and graphs so we can kind of back up some of my claims and then we'll see how well we get through a live demo of bomb squad so first what is cardinality we talk a lot about high cardinality and low cardinality it's it's simpler than it seems sometimes your birds are too high and sometimes they're too low so that's my talk thank you so much I hope that's the only bad joke in the talk we'll see how it goes more generally and more seriously it's just the count of a number of things in a group so in this little fake set of things of B 42 and tree we have a cardinality of 3 a little bit more scope to this talk we're gonna talk more specifically about how many discrete series there are for a given metric I know that as to Julian's point it is indeed series all the way down we're gonna flip that script a little bit and think about it more semantically as a metric is a thing that contains series so we'll talk more about that in a bit but for my little fake series here called CPU if I had one label called host and 3 distinct values for it I have a cardinality of 3 for my metric CPU so let's settle on terms back to the comment that I jumped ahead on so a series for anybody who's forgotten already is just a discrete pairing of label names and their values for the sake of this talk at least a metric is a set of series whose name special label match so for instance API requests CPU on the last slide so forth a cardinality explosion or a high cardin
