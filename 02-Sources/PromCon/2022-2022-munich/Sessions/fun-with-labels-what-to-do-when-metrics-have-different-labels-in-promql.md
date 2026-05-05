---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2022"
edition_id: 2022-munich
year: 2022
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2022-munich/talks/fun-with-labels!-what-to-do-when/
youtube_url: https://www.youtube.com/watch?v=wjukmbi0I58
youtube_search_url: https://www.youtube.com/results?search_query=Fun+with+labels%21+What+to+Do+When+Metrics+Have+Different+Labels+in+PromQL+PromCon+2022
video_match_score: 1.046
status: video-found
---

# Fun with labels! What to Do When Metrics Have Different Labels in PromQL

## Identificação

- Edição: PromCon EU 2022
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2022-munich/talks/fun-with-labels!-what-to-do-when/
- YouTube: https://www.youtube.com/watch?v=wjukmbi0I58

## Resumo

Speaker(s): Jaime Yera Hidalgo PromQL is great for combining and doing math between different metrics. However, one of the most recurring nightmares of every engineer operating Prometheus is when two or more metrics in the same PromQL expression don't share the same labels. PromQL offers different functions and ways to cover all the possible use cases for these kinds of situations.

## Abstract oficial

Speaker(s): Jaime Yera Hidalgo

PromQL is great for combining and doing math between different metrics. However, one of the most recurring nightmares of every engineer operating Prometheus is when two or more metrics in the same PromQL expression don't share the same labels.

PromQL offers different functions and ways to cover all the possible use cases for these kinds of situations. In this talk, Jaime will go through some of the most common scenarios, from the easiest to the more tricky ones, giving examples and showing the underlying logic behind each solution.

In this talk, you will learn about:


How PromQL combines different metrics
PromQL functions for solving label conflicts
PromQL functions to modify labels at query time

## Links

- Página oficial: https://promcon.io/2022-munich/talks/fun-with-labels!-what-to-do-when/
- YouTube: https://www.youtube.com/watch?v=wjukmbi0I58
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=wjukmbi0I58
- YouTube title: PromCon 2022: Fun with labels! What to Do When Metrics Have Different Labels in PromQL
- Match score: 1.046
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2022/fun-with-labels-what-to-do-when-metrics-have-different-labels-in-promq/wjukmbi0I58.txt
- Transcript chars: 8119
- Keywords: labels, metrics, information, metric, obviously, simple, create, select, inside, syntax, another, combine, decided, combination, matrix, details, levels, operation

### Resumo baseado na transcript

[Music] foreign [Music] and I'm also a maintainer of the open source project.io today I'm here to talk about of the different challenges that we can find with labels when we try to combine different metrics I began to work a series deck five months ago and then I entered in this work of monitoring uh where you can retrieve information from your application of your environments thanks to Prometheus metrics I discovered that I could create these dashboards and alerts metrics give us that useful data to the users

### Excerpt da transcript

[Music] foreign [Music] and I'm also a maintainer of the open source project.io today I'm here to talk about of the different challenges that we can find with labels when we try to combine different metrics I began to work a series deck five months ago and then I entered in this work of monitoring uh where you can retrieve information from your application of your environments thanks to Prometheus metrics I discovered that I could create these dashboards and alerts metrics give us that useful data to the users and he can't use it in a blink of an eye so I thought how can I do that how can I turn all that metrics into that in dashboards and alert and I began to work with a brinkual I was very excited and I decided to build this huge combination of metrics and in order to create these dashboards and maybe it was very naive because I thought that matches were only a name and that was all bad obviously not so I realized that behind of that Matrix were that details that enriched metrics and give them all that powerful details and those Dark Horse um with labels I began to work when they've also and discovered that all combination between my matches who applied that and allocate those levels between my metrics so for this talk I prepare three different use cases very basic but very useful when you are beginning to work in this world with Prometheus metrics and unless labels from scratch so let's work with some math class with primeql 101 and for this first example when I begin to work with with Matrix and these combinations I thought that I can enter in my Prometheus and tap my both metrics and that will be enough but that's not true because when I try to recover the information for a simple combination I just was in my in front of my screen with nothing on it so actually realized that I had to combine my Matrix using those labels I begin to see between this simple theoretical example and realized that I have some labels that matching between the metrics and if I have a combination this means you have to point and allocate those levels inside the syntax of my printql and that is enough for this for example the first use case when you are working with pronql and for this one this first example I use this maybe different case instead of a simple one with two metrics because obviously we have our rates and some other operators but in the basics you have two different blocks and one operation between them so I will have to have one time series in this in this case t
