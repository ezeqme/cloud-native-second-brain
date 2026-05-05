---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2023"
edition_id: 2023-berlin
year: 2023
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2023-berlin/talks/observing-the-worlds-most-famous-3d-print-farm/
youtube_url: https://www.youtube.com/watch?v=PElyQobUZsk
youtube_search_url: https://www.youtube.com/results?search_query=Observing+the+world%27s+most+famous+3D+print+farm+PromCon+2023
video_match_score: 1.009
status: video-found
---

# Observing the world's most famous 3D print farm

## Identificação

- Edição: PromCon EU 2023
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2023-berlin/talks/observing-the-worlds-most-famous-3d-print-farm/
- YouTube: https://www.youtube.com/watch?v=PElyQobUZsk

## Resumo

Speaker(s): Pavel Strobl Using Prometheus in Cloud Native is obvious. Using it in IT is a sane default. But what if you have a spleen for observing the real, physical world?

## Abstract oficial

Speaker(s): Pavel Strobl

Using Prometheus in Cloud Native is obvious. Using it in IT is a sane default. But what if you have a spleen for observing the real, physical world?

Prusa Research is likely the best-known 3D printer manufacturer in the maker scene, and it started to aggressively modernize their software side. Join us on an end user journey of how Prometheus sits at the center of Prusa's new approach. From the shop to printables.com (of of the best known 3D print file repositories) all the way to individual printers and likely the best-known 3D print farm on Earth, it all ties back to Prometheus.

## Links

- Página oficial: https://promcon.io/2023-berlin/talks/observing-the-worlds-most-famous-3d-print-farm/
- YouTube: https://www.youtube.com/watch?v=PElyQobUZsk
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=PElyQobUZsk
- YouTube title: PromCon 2023 - Observing the world's most famous 3D print farm
- Match score: 1.009
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2023/observing-the-worlds-most-famous-3d-print-farm/PElyQobUZsk.txt
- Transcript chars: 15173
- Keywords: actually, printers, exporter, course, printer, printing, pretty, observability, metrics, promus, alerting, metric, points, sometimes, promes, cluster, source, single

### Resumo baseado na transcript

[Music] [Applause] okay hello I'm glad to see you there uh this is my second promcon I was uh first uh promon was in minic last year uh and I'm here to tell you how we observe not only world's most famous three part uh print Farm but also have we use promeo at Brer research yeah who am I my name is p strouble and I am devops engineer at pra research uh uh next uh I am Cloud native prodct organizer we organizing meetups about Cloud native uh

### Excerpt da transcript

[Music] [Applause] okay hello I'm glad to see you there uh this is my second promcon I was uh first uh promon was in minic last year uh and I'm here to tell you how we observe not only world's most famous three part uh print Farm but also have we use promeo at Brer research yeah who am I my name is p strouble and I am devops engineer at pra research uh uh next uh I am Cloud native prodct organizer we organizing meetups about Cloud native uh Technologies uh my main topic is Saran observability uh I sometimes do something about uh infrastructure here and there but uh that's not main uh thing I would like to do so I I'm more aaran observability guide uh besides that I also like to Homebrew my beer and did you know that you can observe process of fermentation of beer with promeo and graph and I play a lot with Hardware uh and iot 3D printers are my thing I like messing with my cars and uh and such something like that so how do we use prome uh if you think about PR will think okay these guys made three printers uh but it's not only that because we run multiple web services for example printable or eShop uh and we need to uh monitor some uh somehow this uh Services that's why we use promes uh this is our stack it's not complete of course uh we use uh gcp Google Cloud platform and we use Google kubernetes engine so it's much easier for us to manage our kubernetes instance and we have two clusters these are pretty small clusters but still there uh there are two of these we don't need de development cluster because there develop there own machines okay let's uh move to staging at staging you will see print tables and is as examples of applications and then there is running promes and lo lo is for logs but let's say let's talk about promeets we use T side cars because at our production cluster there is running tanos uh that can actually Flats our metrics to object storage that called Google bucket and even in production cluster we have uh prome with Thanos side car but you can actually access promeets and production directly we don't have a prod uh Ingress for uh prome at stage because it doesn't make sense we use uh tanos side car okay uh this is how alerting looks like because I think alerting is pretty uh uh difficult to set up and we use two approaches because we use uh two approaches in deployment we use two approaches of alerting uh let's say we have terraform now open t if you heard about that and uh used Argo CD with cross plane probably heard about that uh
