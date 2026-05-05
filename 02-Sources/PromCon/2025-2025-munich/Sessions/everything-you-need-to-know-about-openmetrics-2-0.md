---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2025"
edition_id: 2025-munich
year: 2025
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "OpenTelemetry", "Scalability Reliability"]
speakers: ["György Krajcsovits", "Bartłomiej Płotka"]
source_url: https://promcon.io/2025-munich/talks/everything-you-need-to-know-about-openmetrics-20/
youtube_url: https://www.youtube.com/watch?v=KTdhXHY-Hqo
youtube_search_url: https://www.youtube.com/results?search_query=Everything+you+need+to+know+about+OpenMetrics+2.0%21+PromCon+2025
video_match_score: 1.013
status: video-found
---

# Everything you need to know about OpenMetrics 2.0!

## Identificação

- Edição: PromCon EU 2025
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[OpenTelemetry]], [[Scalability Reliability]]
- Speakers: György Krajcsovits, Bartłomiej Płotka
- Página oficial: https://promcon.io/2025-munich/talks/everything-you-need-to-know-about-openmetrics-20/
- YouTube: https://www.youtube.com/watch?v=KTdhXHY-Hqo

## Resumo

The ability to look at metrics exposed by an application in text, use that as the input to Prometheus compatible systems and “what you see is what you query” paradigm has been central to the design of Prometheus. The Prometheus format and OpenMetrics 1.0 standards have been around for a number of years to define how metrics are exposed in text format, however there are a set of challenges that motivates a new version of OpenMetrics. In this talk, you will learn about those challenges, how we plan to address those and how you can join our working group for this effort!.

## Abstract oficial

The ability to look at metrics exposed by an application in text, use that as the input to Prometheus compatible systems and “what you see is what you query” paradigm has been central to the design of Prometheus. The Prometheus format and OpenMetrics 1.0 standards have been around for a number of years to define how metrics are exposed in text format, however there are a set of challenges that motivates a new version of OpenMetrics.

In this talk, you will learn about those challenges, how we plan to address those and how you can join our working group for this effort!. On the way we will deep dive into more complex concepts like native histograms in the text exposition, OpenTelemetry compatibility, created timestamp improvements, and more! Show some of the concepts being worked on and give a deep dive into complex data types, in particular for native histograms.

## Links

- Página oficial: https://promcon.io/2025-munich/talks/everything-you-need-to-know-about-openmetrics-20/
- YouTube: https://www.youtube.com/watch?v=KTdhXHY-Hqo
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KTdhXHY-Hqo
- YouTube title: Promcon 2025 - Everything you need to know about OpenMetrics 2.0!
- Match score: 1.013
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2025/everything-you-need-to-know-about-openmetrics-2-0/KTdhXHY-Hqo.txt
- Transcript chars: 27713
- Keywords: metric, format, actually, already, native, matrix, histograms, protobuff, suffixes, metrics, exposition, prometheus, promuse, complex, efficient, readable, aspect, series

### Resumo baseado na transcript

Um hello everyone we are super excited to be here and chat about openmetrics and its potential future. We all know know the core aspect of Promeigu's ecosystem depends on the fact it scrapes metrics. Well first thing is that there are different flavors of you can use uh in Prometheus to collect your metrics notably multiple versions of text and a protoraph. For example, this is a snippet of Prometheus configuration kind of recently added that allows you to configure um the preferences of straight format from the scraper perspectively globally or per scraper. So for example in this example if we reach an application and it doesn't support protobuff it should and supports openmetrics it should kind of respond with openmetrics. So just by looking on this config um there are some decisions to make right as a user when I configure Prometheus like what what format should I prefer and also as an application exporter developer what to implement what what you know I should

### Excerpt da transcript

Um hello everyone we are super excited to be here and chat about openmetrics and its potential future. Let's dive in. We all know know the core aspect of Promeigu's ecosystem depends on the fact it scrapes metrics. Uh for that it requires some sort of transport which we call the exposition. uh in this context you know the exposition format is essentially an HTTP uh response content describer for example primitives can use to periodically collect the current metric values from the exposer. So for example your application for instance you are probably familiar with the text exposition format which is what you typically see when you just you know hit this /metric endpoint um and it became a prime use signature at this point right and it's really one of the main reasons why prime use is so widely adopted you probably heard also about openmetrics 10 that came in 2020 standardizing primeuse text format and added bunch of stuff on the way well around a year ago uh produced project started a new working group to deliver open matrix 20 to zero.

Um and since then we form a solid goals and ideas on what 20 zero could should solve and we are here um today with cryo to share it all with you. Um so make sure you fasten your seat belt because you know there are some ideas that are very ambitious but we think they really uh represent what Prometheus is slowly evolving into. Um and it's still open page so don't worry if you don't agree with things um if you don't like things so please we are making this talk exactly to hear your feedback so let us know after the talk what do you think what would you improve or maybe you like it so at the end of this talk I want you to know what exposition formats we have in the ecosystem and how to navigate them which one I don't know what should you choose uh I want you to know what optric 200 changes are what what we are thinking about and how you can join and help our effort but let's start with a short introduction I'm here with Cryo. >> Yeah, my name is Derek Kachchovich Cryo for short. Uh I'm I work at Graphana and I'm a maintainer in Promeus Graphana Mimir and coowner in open country and I specialize in native histograms.

>> And my name is Bart Podka. I work at Google. I'm responsible for Google management and service and I maintain um lots of stuff usually in go uh in open source. I'm also mentoring. I wrote a book called efficient go and I also you know last year in my free time I started motorcycleycling but this year I had ext
