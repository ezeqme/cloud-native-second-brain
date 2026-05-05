---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2025"
edition_id: 2025-munich
year: 2025
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Remote Write Storage", "Scalability Reliability"]
speakers: ["Ruihang Xia"]
source_url: https://promcon.io/2025-munich/talks/engage-prometheus-in-rust-ecosystem/
youtube_url: https://www.youtube.com/watch?v=Q4-WDPtBcCQ
youtube_search_url: https://www.youtube.com/results?search_query=Engage+Prometheus+in+Rust+Ecosystem+PromCon+2025
video_match_score: 0.973
status: video-found
---

# Engage Prometheus in Rust Ecosystem

## Identificação

- Edição: PromCon EU 2025
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Remote Write Storage]], [[Scalability Reliability]]
- Speakers: Ruihang Xia
- Página oficial: https://promcon.io/2025-munich/talks/engage-prometheus-in-rust-ecosystem/
- YouTube: https://www.youtube.com/watch?v=Q4-WDPtBcCQ

## Resumo

Above 90% of Prometheus-related projects are in Go. For many years, other languages have only a client to expose Prometheus metrics, and nothing more. But we want to make some changes.

## Abstract oficial

Above 90% of Prometheus-related projects are in Go. For many years, other languages have only a client to expose Prometheus metrics, and nothing more.

But we want to make some changes. We've devoted years to building many useful yet fundamental basic Rust libraries that work with Prometheus, like a native PromQL parser or Prometheus Remote protocols, that have been used by hundreds of other projects with over 180k downloads.

And that's not the only aspect, we're also actively exploring the possibility to combine Prometheus with other widely used Rust projects in various ways, including arrow-rs, otlp-arrow, Parquet and DataFusion etc. Each of which can bring some new advantages in protocol, data storage, computation or more to the Prometheus economic system.

In this session I want to share our journey so far, the good, the bad and the sweet things when carving out Prometheus' way in Rust. We've learned so many lessons as well as sparked lots of inspiration. Looking forward to discovering a new world in hacking and using Prometheus with you.

## Links

- Página oficial: https://promcon.io/2025-munich/talks/engage-prometheus-in-rust-ecosystem/
- YouTube: https://www.youtube.com/watch?v=Q4-WDPtBcCQ
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Q4-WDPtBcCQ
- YouTube title: Promcon 2025 - Engage Prometheus in Rust Ecosystem
- Match score: 0.973
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2025/engage-prometheus-in-rust-ecosystem/Q4-WDPtBcCQ.txt
- Transcript chars: 19200
- Keywords: promises, another, languages, format, itself, second, language, premises, provide, actually, standard, choose, prometheus, ecosystem, rewrite, written, limited, storage

### Resumo baseado na transcript

Thank you and I'm honored to be first in the second day and my my talk today is about engaging promises in the Ras ecosystem the another language. Uh I'm currently a software engineer at grip uh which is another database uh startup. if you work using go I believe most of you are written in go if you are involved with promises you are mostly limited to ex exporting metrics only the SDKs to report data to promises not leverage your data visual system uh and to Actually I have done around one year of my job to trying to replace the underlying storage engine of prunes to another uh key value storage engine written in rust and um I think that's uh one of the best choices I have ever made. Uh have you ever think of written some plug-in in your njx layer and with lua script to intercept some prom query this is not uh I think this is not available in or not feible in if you are all in go but it's uh I'm not saying this is a good choice in some architecture but uh for us to build a infrastructure architecture it's always help if we have more choices and the other side is about uh another project open which is a you can think

### Excerpt da transcript

Thank you and I'm honored to be first in the second day and my my talk today is about engaging promises in the Ras ecosystem the another language. So first a few introduction about me. Uh I'm currently a software engineer at grip uh which is another database uh startup. Yeah. And I'm also a patch detusion PMC member and arrow committer. So um today today's talk I will also include much of them. And this is my GitHub ID. And I noticed that some talkers yesterday have have a unified theme and template, but I haven't noticed that. So this is not uh no permiss orange color here. And yeah, this is my first time being in the Europe. I'm not used to put my own selfish on the slides. So you can see me with your eyes. Okay. Today I will bring this topic in about three major parts like first why we take this why we bring Rust to Prometheus or bring premises to Rust and second uh what does this kind of action means to to me or to our company to the entire community and the sec the third is how how we achieve this in I will provide two examples with two totally different ways.

And before we start, let's uh give you some content warning. First uh uh this is about uh talking about Rust in a gocentric project. I'm not that kind of guest that who yielding of uh using rust to rewrite everything. Well, no. Uh I I do my day job with RS, but I'm not that kind of guy. And uh the second I I I got some cough. So and the third I I I will do some comparison but uh some of some of my code is on one side. So uh that would be expected biases but I would try to try my best to make them balanced and the first is uh broken English not very fluent. Okay, let's get started with uh a quick fact check. uh in the introduction I put on the website I said 19% of the projects are written in go but I realized I haven't do any formal investigation so I replace it with most of but I think that this state still stands that uh if you work using go I believe most of you are written in go if you are involved with promises you are mostly limited to ex exporting metrics only the SDKs to report data to promises not leverage your data visual system uh and to validate this I stand a picture that this is from the compliance test uh which is provided by prom labs I think yes but but this picture is pretty low about three years ago they haven't updated uh yes all of them are go some of these are like the first one is hosted by another cloud service and some of them are uh speaking promises languages or just
