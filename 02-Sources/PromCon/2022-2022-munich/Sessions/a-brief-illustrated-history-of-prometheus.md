---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2022"
edition_id: 2022-munich
year: 2022
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Community"]
speakers: []
source_url: https://promcon.io/2022-munich/talks/a-brief-illustrated-history-of-p/
youtube_url: https://www.youtube.com/watch?v=VSg3YYUbEDI
youtube_search_url: https://www.youtube.com/results?search_query=A+Brief+Illustrated+History+of+Prometheus+PromCon+2022
video_match_score: 0.967
status: video-found
---

# A Brief Illustrated History of Prometheus

## Identificação

- Edição: PromCon EU 2022
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Community]]
- Speakers: N/A
- Página oficial: https://promcon.io/2022-munich/talks/a-brief-illustrated-history-of-p/
- YouTube: https://www.youtube.com/watch?v=VSg3YYUbEDI

## Resumo

Speaker(s): Martin Chodúr Prometheus is here with us for some time now, and we take it for granted how it "just works" with all its features. But it wasn't always this way, and it took a huge amount of work from maintainers and community to get it where it is now. Let me take you through the history of how it got there, with images of course!

## Abstract oficial

Speaker(s): Martin Chodúr

Prometheus is here with us for some time now, and we take it for granted how it "just works" with all its features. But it wasn't always this way, and it took a huge amount of work from maintainers and community to get it where it is now. Let me take you through the history of how it got there, with images of course!

## Links

- Página oficial: https://promcon.io/2022-munich/talks/a-brief-illustrated-history-of-p/
- YouTube: https://www.youtube.com/watch?v=VSg3YYUbEDI
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=VSg3YYUbEDI
- YouTube title: PromCon EU 2022: A Brief Illustrated History of Prometheus
- Match score: 0.967
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2022/a-brief-illustrated-history-of-prometheus/VSg3YYUbEDI.txt
- Transcript chars: 15139
- Keywords: prometheus, remote, discovery, actually, instances, parameters, nowadays, started, already, alerting, available, collection, definitely, version, features, global, feature, yesterday

### Resumo baseado na transcript

[Music] foreign [Music] good morning everyone I hope you enjoyed the social even yesterday I did that's great and I hope today I will have no technical difficulties like yesterday uh my name is Martin Peru and I work at susanon.cz I'm building observability stick in that company we are so-called check Google and I will like to talk or walk you through the brief history of Prometheus with the videos so we will start easy in the morning right there are just images and some talking so okay yeah and this service discovery of Prometheus native support for kubernetes was uh was the thing so yeah that was definitely very useful and also first prom con happened in Berlin I wasn't there but yeah the I found out that it was 2016. so it's a few years back and the community group because all of these nice features that came how it was useful the people started to use Primitives and and the community the exporters started to show up and Prometheus got to the point of incubation in cncf it was actually a second project to incubate I think after kubernetes so that was even made it even more popular in that year also Prometheus operator was first started so I was actually surprised it's that old also uh and as I said all those things led to even more and more adaption of Prometheus we see it in production we used it actually from the 1.0 in production successfully and it was like yeah...

### Excerpt da transcript

[Music] foreign [Music] good morning everyone I hope you enjoyed the social even yesterday I did that's great and I hope today I will have no technical difficulties like yesterday uh my name is Martin Peru and I work at susanon.cz I'm building observability stick in that company we are so-called check Google and I will like to talk or walk you through the brief history of Prometheus with the videos so we will start easy in the morning right there are just images and some talking so okay yeah I'll just start a timer so I have the idea how it all started or where you can track it back this is the first comet in the Primitive repository you could find uh it's year two to 2012 and the commit message says in Translation it's Zeus cover up your Skype and it was done in a SoundCloud where the parameters were was born actually so there's some new kid and observability town it was a bit of different than the other Solutions available as I said born in SoundCloud was a bit similar to Bergman from Google and Spark and why it was different the different was the data collection approach the pull versus push there was lots of set about it already so but I'm not sure if there was any other solution except the Boardman using pool based approach so this is definitely a different thing about Prometheus back then also there was the approach was open box monitoring like you are really uh looking what's happening in the in the application it tells you raw data not just I'm okay but you know what's happening in there and the multi-dimensional modal uh using labels allowing you to aggregate data As You Wish on the Fly and also powerful query language from ql which is loved by some hated by others but yeah it's powerful I personally like it and it tried to keep things simple it was like single binary and it just works it's like uh yeah no no moving Parts it was built to withstand so as I said it was like all in one solution you have collection of data you have visualization of the data and alerting this is all done in one single binary the database is included it's like you just run it and it's that's it right it just works uh also it came with some uh best practices how how to deploy it so you should deploy it as close to your applications as possible so the data collection is reliable that already already heard the highly available setup two parameters instances next to each other so you always deploy two of those and the idea of exporters you need the applications to support t
