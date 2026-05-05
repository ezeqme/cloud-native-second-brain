---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2025"
edition_id: 2025-munich
year: 2025
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Scalability Reliability"]
speakers: ["Attila Szakács"]
source_url: https://promcon.io/2025-munich/talks/counting-what-you-care-about-in-your-security-data-pipeline/
youtube_url: https://www.youtube.com/watch?v=lapPsiWVBzU
youtube_search_url: https://www.youtube.com/results?search_query=Counting+What+You+Care+About+in+Your+Security+Data+Pipeline+PromCon+2025
video_match_score: 1.031
status: video-found
---

# Counting What You Care About in Your Security Data Pipeline

## Identificação

- Edição: PromCon EU 2025
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Scalability Reliability]]
- Speakers: Attila Szakács
- Página oficial: https://promcon.io/2025-munich/talks/counting-what-you-care-about-in-your-security-data-pipeline/
- YouTube: https://www.youtube.com/watch?v=lapPsiWVBzU

## Resumo

Traditional syslog systems have long been opaque — exporting minimal, fixed-format metrics that rarely reflect what users actually care about. AxoSyslog, a high-performance fork of syslog-ng, has taken a different path: not only adopting native Prometheus metrics, but also enabling metric emission directly from the user’s log processing logic. In this talk, I’ll share how we transitioned from CSV-style global and per-driver metrics to full Prometheus integration.

## Abstract oficial

Traditional syslog systems have long been opaque — exporting minimal, fixed-format metrics that rarely reflect what users actually care about. AxoSyslog, a high-performance fork of syslog-ng, has taken a different path: not only adopting native Prometheus metrics, but also enabling metric emission directly from the user’s log processing logic.

In this talk, I’ll share how we transitioned from CSV-style global and per-driver metrics to full Prometheus integration. But more importantly, I’ll explore a less common mindset: treating metrics not as static artifacts of a system, but as programmable, user-defined views of what matters. Users can emit fine-grained, label-rich metrics from log routing logic itself — for example, tracking per-tenant message volume, labeling metrics with custom log or environment related info, or observing how often certain fields are missing.

We’ll walk through:
* What syslog metrics looked like historically (and why they fell short).
* Our journey to integrating Prometheus natively.
* How update_metric() works and why it's powerful.
* Real-world use cases where dynamic metrics made debugging and policy enforcement dramatically easier.

If you want to make observability accessible in deeply traditional parts of the stack — or want to let users code their own metrics — this talk is for you.

## Links

- Página oficial: https://promcon.io/2025-munich/talks/counting-what-you-care-about-in-your-security-data-pipeline/
- YouTube: https://www.youtube.com/watch?v=lapPsiWVBzU
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=lapPsiWVBzU
- YouTube title: Promcon 2025 - Counting What You Care About in Your Security Data Pipeline
- Match score: 1.031
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2025/counting-what-you-care-about-in-your-security-data-pipeline/lapPsiWVBzU.txt
- Transcript chars: 17230
- Keywords: metrics, logs, syslog, labels, itself, pipeline, information, available, logging, prometheus, events, agency, sislog, called, fallback, coming, probably, processing

### Resumo baseado na transcript

Uh and I will yeah I will tell you about uh metrics about logs in your observability pipeline or as the title says counting what you care about in your security data pipeline. I'm a founding engineer and tech lead uh at Exoflow uh which is a startup uh where we develop a logging pipeline on steroids uh or uh how that's how I would uh introduce it. Uh if you have not heard about it before uh what metrics looked like in syslog uh previously and how we transition transition to prometheus time metrics. Uh which I think is interesting to see because sislog was not developed in prometheus in mind and we had to retrofit uh this. Um then we will talk about what other limitations uh system entries metrics have and uh how we think that log driven metrics solve those issues. Um and then we will see some examples and the case study uh of these metrics in action.

### Excerpt da transcript

[music] Okay, can you hear me? Cool. Uh so hello everyone. Uh my name is Aila Sakage. Uh and I will yeah I will tell you about uh metrics about logs in your observability pipeline or as the title says counting what you care about in your security data pipeline. So quick intro introduction uh my name is Aila Satchet. I'm a founding engineer and tech lead uh at Exoflow uh which is a startup uh where we develop a logging pipeline on steroids uh or uh how that's how I would uh introduce it. Uh I'm doing uh software engineering here. Uh I'm the tech lead of uh the data plane team. Um actually I had the privilege uh to develop syslog for uh more than seven years now. Uh and I'm also a logging operator maintainer which is uh CNCF sandbox CNCF sandbox uh project. Uh so I'm coming from mainly a logging background uh and from the developer side uh not strictly as the user of lo pipelines. Uh so my introduction to metrics uh was probably very different from uh the rest of you or most of you uh more similar to the uh approach uh in the next uh or uh in the previous presentation.

So most of the time I looked at matrix to uh debug uh the logging pipeline uh I was developing and maintaining uh but I hope because of this uh I can give you a slightly different perspective to logs and metrics. uh maybe one uh you you have not really heard about or maybe nothing new will come from this uh and and uh every one of you uh knows this but at least you can see a different path of uh learning about metrics. Uh also I'm a first-time conference speaker. Uh I'm very honored to be here. So I must thank uh prom uh from having me and starting on this journey. Okay. Okay. So what will we hear about today? Uh first we will talk about what syslog is. Uh if you have not heard about it before uh what metrics looked like in syslog uh previously and how we transition transition to prometheus time metrics. Uh which I think is interesting to see because sislog was not developed in prometheus in mind and we had to retrofit uh this. Um then we will talk about what other limitations uh system entries metrics have and uh how we think that log driven metrics solve those issues.

Um and then we will see some examples and the case study uh of these metrics in action. So uh how many of you have heard about syslog before? Wow, that's that's quite a lot of hands. Uh more than I expected. Cool. Uh so those of you who don't know uh syslog is an old school lock processing service. Uh it is older than Prometh
