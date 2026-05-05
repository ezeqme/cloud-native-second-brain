---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2023"
edition_id: 2023-berlin
year: 2023
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Alerting", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2023-berlin/talks/when-my-counter-restarted-addressing-decade-old-counter-limitation-with-created-timestamps/
youtube_url: https://www.youtube.com/watch?v=nWf0BfQ5EEA
youtube_search_url: https://www.youtube.com/results?search_query=When+my+Counter+Restarted%3F+Addressing+Decade-Old+Counter+Limitation+With+Created+Timestamps+PromCon+2023
video_match_score: 1.018
status: video-found
---

# When my Counter Restarted? Addressing Decade-Old Counter Limitation With Created Timestamps

## Identificação

- Edição: PromCon EU 2023
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Metrics]], [[Alerting]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2023-berlin/talks/when-my-counter-restarted-addressing-decade-old-counter-limitation-with-created-timestamps/
- YouTube: https://www.youtube.com/watch?v=nWf0BfQ5EEA

## Resumo

Speaker(s): Arthur Silva Sens & Bartłomiej Płotka Prometheus counters are one of the most useful metric types. Thanks to cumulative characteristics and simple semantics, they allow cheap and reliable rate calculations, even with missed scrapes. But what if we tell you that your rates sometimes might deceive you?

## Abstract oficial

Speaker(s): Arthur Silva Sens & Bartłomiej Płotka

Prometheus counters are one of the most useful metric types. Thanks to cumulative characteristics and simple semantics, they allow cheap and reliable rate calculations, even with missed scrapes. But what if we tell you that your rates sometimes might deceive you?

Fear not! In this talk, the audience will learn about the latest development in the Prometheus ecosystem that fixes these decade-old precision issues with counters. By supporting created timestamp, Prometheus can now accurately deduce the start times for each stream of samples.

Arthur and Bartek will explain how created timestamps are integrated with Prometheus and how you can leverage them in your production systems. Increase the reliability of queries and alerts against counter today!

## Links

- Página oficial: https://promcon.io/2023-berlin/talks/when-my-counter-restarted-addressing-decade-old-counter-limitation-with-created-timestamps/
- YouTube: https://www.youtube.com/watch?v=nWf0BfQ5EEA
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=nWf0BfQ5EEA
- YouTube title: PromCon 2023 - When my Counter Restarted? Addressing Old Counter Limitations With Created Timestamps
- Match score: 1.018
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2023/when-my-counter-restarted-addressing-decade-old-counter-limitation-wit/nWf0BfQ5EEA.txt
- Transcript chars: 22993
- Keywords: counter, pritus, rabbit, turtle, actually, created, google, little, training, already, metric, important, sample, essentially, finish, samples, thanks, scrape

### Resumo baseado na transcript

oh my God all right hello everyone uh I hope everybody is still energized oh thank you energized after a very long day of conference um our talk will be about a limitation in peritus actually it's a Precision issue uh but I don't want to spoil the the talk too much um I also wanted to say that this is really an honor to be here I've been following promom for years and this is the first time that I'm actually here so thanks for having me uh I

### Excerpt da transcript

oh my God all right hello everyone uh I hope everybody is still energized oh thank you energized after a very long day of conference um our talk will be about a limitation in peritus actually it's a Precision issue uh but I don't want to spoil the the talk too much um I also wanted to say that this is really an honor to be here I've been following promom for years and this is the first time that I'm actually here so thanks for having me uh I am very nervous as you might see but uh that's why I'm actually talking a lot at the beginning just to talk it off are you less nervous now not really we try yeah yeah well let's start with a short introduction cool um hello my name is BK putka I work at Google I specifically work on Google manage promit in Google Cloud uh I also wrote a book called efficient go um I'm active in the cncf I maintain prit use I co-founded tanos and also I started recently a podcast called optimize all the things it's about optimizations to your life infrastructure work everything um yeah is a a little bit hard to compete against that um oh nice somebody got it yeah I'm just [Applause] [Music] Arthur seriously I I'm a devops engineer at K Logics uh I'm recently become a maintainer of Peres operator I used to be an SRE at gitpod and back in 2020 I was a mentee for cubber and right now I'm a mentee for pritus uh under the Google summer of code program and actually what we are going to talk about is what we've been doing in this ship amazing um I wanted to make a joke that I didn't get the barie joke as you but you get it so um good job nevertheless we are here today and we're super excited to be on promcon on our favorite conference uh to discuss quite discuss quite old counter limitation and no it's not about ability to decrease counter values that's not limitation uh that's a feature uh but let me start with some uh short quick refresher about counters um hopefully you know that but you know it's probably the first thing that somebody learns when they came into prome how counters works but essentially counter type in prome represents a cumulative uh count of something for example aror count right uh as we can see on the graph for example uh yeah you can see the row counter value here which represents you know a total number of Errors uh that occurred on some server the counter values um should be always monotonically increasing that's very important thanks of that property whenever it decreases we are sure that the counter was rested uh f
