---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2024"
edition_id: 2024-berlin
year: 2024
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Kubernetes", "Scalability Reliability"]
speakers: ["Krisztian Fekete"]
source_url: https://promcon.io/2024-berlin/talks/why-shipping-native-histograms-to-our-users-is-a-game-changer/
youtube_url: https://www.youtube.com/watch?v=jp7jAokH2P0
youtube_search_url: https://www.youtube.com/results?search_query=Why+Shipping+Native+Histograms+To+Our+Users+Is+a+Game+Changer+PromCon+2024
video_match_score: 1.034
status: video-found
---

# Why Shipping Native Histograms To Our Users Is a Game Changer

## Identificação

- Edição: PromCon EU 2024
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Metrics]], [[Kubernetes]], [[Scalability Reliability]]
- Speakers: Krisztian Fekete
- Página oficial: https://promcon.io/2024-berlin/talks/why-shipping-native-histograms-to-our-users-is-a-game-changer/
- YouTube: https://www.youtube.com/watch?v=jp7jAokH2P0

## Resumo

Traditional histograms in Prometheus have their shortcomings. Some of them are much more significant when you are building and shipping software than when you are and end user. Let's take deciding on bucket distribution for a histogram as an example.

## Abstract oficial

Traditional histograms in Prometheus have their shortcomings. Some of them are much more significant when you are building and shipping software than when you are and end user. Let's take deciding on bucket distribution for a histogram as an example. While a certain distribution might make sense in a local Kubernetes cluster, it might not make sense at scale, with 100s of clusters or nodes. Or how about being tired of losing visibility to the 100th percentile of your latency? Join Krisztian and learn about the benefits of using Native Histograms trough real-life examples with solo.io's Gloo products!

## Links

- Página oficial: https://promcon.io/2024-berlin/talks/why-shipping-native-histograms-to-our-users-is-a-game-changer/
- YouTube: https://www.youtube.com/watch?v=jp7jAokH2P0
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jp7jAokH2P0
- YouTube title: PromCon 2024 - Why Shipping Native Histograms to Our Users Is a Game Changer
- Match score: 1.034
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2024/why-shipping-native-histograms-to-our-users-is-a-game-changer/jp7jAokH2P0.txt
- Transcript chars: 20881
- Keywords: native, histograms, management, bucket, cluster, basically, histogram, buckets, actual, classic, primitives, another, application, actually, probably, already, metrics, layout

### Resumo baseado na transcript

[Music] hello everyone um thank you for having me thank you for the organizers and thank you for the creators of native histograms because they are great and uh in this talk I will talk about why they are great and why you should also probably use them my name is Christian F I'm working as a engineer at s.o uh that company is Building Products on applic to solve the application networking challenges uh we are one of the uh biggest contributor to to ISO who's using ISO by

### Excerpt da transcript

[Music] hello everyone um thank you for having me thank you for the organizers and thank you for the creators of native histograms because they are great and uh in this talk I will talk about why they are great and why you should also probably use them my name is Christian F I'm working as a engineer at s.o uh that company is Building Products on applic to solve the application networking challenges uh we are one of the uh biggest contributor to to ISO who's using ISO by the way not a lots of people but there's some if someone want to chat on chat about then feel free to to find me after the session um and you can see my uh content informations here if you have any followup questions afterward some interesting info uh this is my third time presenting during an emergency boarding System test uh this year so not sure what's what's happening this year but I think the first one was cucon the previous one was in NDC Oslo and yeah this is the third one I'm excited and I'm using PRI since around version 1.6 that was that was a while ago um so first let's take a look at what the uh classic original history Instagrams were and what was the problem with them I will try to do this first couple of slides uh pretty fast because there was yesterday already a talk uh on this topic from uh Pedro and his colleague um and you can also find lots of uh lots of talks from from be and julus and there are other great U presentations on this toic as well the documentation uh is also quite nice uh so feel free to uh check those out if you have further question on the U on the design and implementation so this is uh the original definition from PRI at I I think uh histogram is basically uh collects the samples and observations into buckets and you can visualize these um different ways and you have lots of helper metrics that you can use to to get the raate get the sum these kind of things um one important implementation detail is the is the fact that it uh it has configurable buckets the bad thing about them is that you need to configure them yourself um this is a standard um example of a classic histogram you can see that the buckets are basically the uh under the Le label um this is the this is the distribution that you need to uh come up with during development you can see that how these numbers are growing and that's not because the applic ation is getting SL smaller and smaller that's not how how promi works but that's because this is a cumulative histogram that means that not
