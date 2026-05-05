---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2025"
edition_id: 2025-munich
year: 2025
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "OpenTelemetry", "Scalability Reliability"]
speakers: ["Julius Volz"]
source_url: https://promcon.io/2025-munich/talks/why-i-recommend-native-prometheus-instrumentation-over-opentelemetry/
youtube_url: https://www.youtube.com/watch?v=Clh2Q1GHiTo
youtube_search_url: https://www.youtube.com/results?search_query=Why+I+Recommend+Native+Prometheus+Instrumentation+over+OpenTelemetry+PromCon+2025
video_match_score: 1.043
status: video-found
---

# Why I Recommend Native Prometheus Instrumentation over OpenTelemetry

## Identificação

- Edição: PromCon EU 2025
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[OpenTelemetry]], [[Scalability Reliability]]
- Speakers: Julius Volz
- Página oficial: https://promcon.io/2025-munich/talks/why-i-recommend-native-prometheus-instrumentation-over-opentelemetry/
- YouTube: https://www.youtube.com/watch?v=Clh2Q1GHiTo

## Resumo

With all the hype around OpenTelemetry, you may be tempted to use OpenTelemetry and its SDKs for all of your application instrumentation needs. However, when it comes to generating metrics for usage in Prometheus, you should at least think twice before going all in on OTel. Not only do you risk throwing away some of the core features that define Prometheus as a monitoring system, but you'll also end up with awkward metrics translation and escaping issues, as well as other inefficiencies and complexities.

## Abstract oficial

With all the hype around OpenTelemetry, you may be tempted to use OpenTelemetry and its SDKs for all of your application instrumentation needs. However, when it comes to generating metrics for usage in Prometheus, you should at least think twice before going all in on OTel. Not only do you risk throwing away some of the core features that define Prometheus as a monitoring system, but you'll also end up with awkward metrics translation and escaping issues, as well as other inefficiencies and complexities. That's why I still recommend using Prometheus's own native instrumentation client libraries over the OTel SDKs if you want to get the best possible Prometheus monitoring experience. In this talk, I'm going to lay out some of the major reasons that led me to this opinion.

## Links

- Página oficial: https://promcon.io/2025-munich/talks/why-i-recommend-native-prometheus-instrumentation-over-opentelemetry/
- YouTube: https://www.youtube.com/watch?v=Clh2Q1GHiTo
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Clh2Q1GHiTo
- YouTube title: PromCon 2025 - Why I Recommend Native Prometheus Instrumentation over OpenTelemetry
- Match score: 1.043
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2025/why-i-recommend-native-prometheus-instrumentation-over-opentelemetry/Clh2Q1GHiTo.txt
- Transcript chars: 25086
- Keywords: prometheus, metrics, metric, server, discovery, actually, usually, promql, attributes, instrumentation, target, labels, metadata, resource, everyone, client, probably, little

### Resumo baseado na transcript

I'm just a one person company doing trainings and courses around Prometheus. Um, and uh because I saw some issues with, you know, people using open telemetry with Prometheus and then I joked and said like, hey, I could do a promcon talk about it and the joke was accepted and now I'm doing the talk. We're also going to have more talks today and uh tomorrow about open telemetry and Prometheus. As probably most people in this room will know um you know Prometheus aims to be an entire monitoring system. gives you tools to track metrics in your systems, then get them out of your processes, store them, query them, even have like alerting facilities, dashboarding, although that's usually done with Graphana, but it aims to give you like a tool chain for the entire In the contrast, open telemetry only cares about generating the signals and then processing them a little bit and just passing them on to some kind of third party backend system, but it does it for more than one signal types, logs, metrics, traces, and now also profiles is pretty new, I think.

### Excerpt da transcript

Good morning. Does it work? Everyone can hear me? >> Nice. Okay, so >> Oh, it doesn't matter. >> Let's see. Richie, how do I even move your cursor? There's no mouse. >> It's on the right hand side. >> Huh? >> Is it trimmer? >> You are moving the mouse. >> Ah, okay. See, I'm just not uh smart enough. Okay. >> Wow. >> Okay. I always mirror, so I'm not used to this. Okay. Perfect. So, welcome to Promcon H first talk. Um I'm Julius, one of the co-founders of Prometheus. And now I'm just Prom Labs. I'm just a one person company doing trainings and courses around Prometheus. And a while ago I uh what do I hit? Ah, okay. Ah, okay. Interesting. It doesn't. Ah, okay. I need to actually Can I not mirror then? >> Ah, there it is. Okay, perfect. So, I'm testing the room for you. Okay, so originally I wrote a blog post in July. Um, and uh because I saw some issues with, you know, people using open telemetry with Prometheus and then I joked and said like, hey, I could do a promcon talk about it and the joke was accepted and now I'm doing the talk.

Um so you could also read the blog post for more detail if you want to. Um so open telemetry is here in full force. I would say it's not going to go away. Uh people want to use it with Prometheus, right? Like they want to instrument their services uh with open telemetry and then the metrics part of it they want to send to Prometheus. But honestly, I have to say there are plenty of downsides in comparison to using Prometheus's own native instrumentation client libraries. So I want to talk a bit about those downsides and you should at least be aware of them before choosing to go down the hotel route if you mostly care about matrix and Prometheus. Disclaimers, I'm a Prometheus co-founder, so I'm like super duper biased towards Prometheus, of course, towards the Prometheus way. Um, and there can still be valid reasons potentially for using open telemetry with Prometheus even. Um, but there are plenty of other talks and PR start pieces and every everything on the internet talking about why you want to do that.

So this talk is just not going to cover that again. We're also going to have more talks today and uh tomorrow about open telemetry and Prometheus. And I want to commend everyone on working on this that compatibility and making that work as good as possible. Um it's just this talk isn't that. So but still props to everyone working on that and making that good. So quick contrast between the two systems. As probably most peopl
