---
type: session
event: "Observability Day 2025 - Europe"
year: 2025
kind: session
youtube_url: "https://www.youtube.com/watch?v=P3e9JQWta_g"
youtube_id: "P3e9JQWta_g"
playlist: "Observability Day 2025 - Europe"
playlist_id: "PLj6h78yzYM2O7PaLWCNCE5wKhzmzF4b6A"
playlist_index: 2
speakers: ["Why Not Both? Margaret Dawson"]
topics: ["OpenTelemetry", "Collectors", "Metrics", "Tracing", "Logging", "Profiling", "Kubernetes", "AI Observability"]
keywords: ["collector", "fluent", "logs", "metrics", "tracing", "logging", "opentelemetry", "kubernetes", "collectors", "agents", "agent", "profiles", "otlp", "otel", "pipeline", "telemetry", "ecosystem", "fluentbit", "projects", "source", "little", "working", "started", "questions"]
transcript_file: "_sources/transcripts/youtube-playlists/observability-day-2025-europe/sponsored-keynote-fluent-bit-vs-opentelemetry-collector/P3e9JQWta_g.txt"
transcript_chars: 6683
status: "transcript-downloaded"
match_score: 1.08
---

# Sponsored Keynote: Fluent Bit vs. OpenTelemetry Collector - Why Not Both? Margaret Dawson

## Metadata

- YouTube: https://www.youtube.com/watch?v=P3e9JQWta_g
- Playlist: Observability Day 2025 - Europe
- Speakers: Why Not Both? Margaret Dawson
- Topics: [[OpenTelemetry]], [[Collectors]], [[Metrics]], [[Tracing]], [[Logging]], [[Profiling]], [[Kubernetes]], [[AI Observability]]

## Transcript

Good morning. I hope you're having a good morning. Uh I'm here to talk to you about a couple of the open source projects you've heard a little bit about today already. Jose did a great job of giving you an overview of Fluent Bit and most of you already know the hotel collector and you heard some more about the updates to open telemetry. So I've been working in open source about 20 years. Um I don't know if that's longer or shorter because I can't see your faces at all, but Linux, OpenStack, any other OpenStack fanboys out there? um most recently Kubernetes and Anzible. I was with Red Hat for many years and I joined Chronosphere about a year ago and started learning all the new technologies surrounding um this ecosystem. And I found myself asking a lot of questions about when to use what. There's so many collectors and agents and two that I looked a lot at were Fluent Bit of course because we are the maintainers of that project and the hotel collector.

So, I thought I'd just share my learnings and how I'm thinking about these two and hopefully it'll help you. So, one of the things that I realized was the versus one versus the other was kind of the wrong framing. And yes, I love really fast cars, so I just put this for the hell of it. Um, because in fact, these competitive projects that a lot of people are trying to figure out which one to use are very complimentary. And in fact, we're seeing more and more organizations start to use them together. And so, um, I started looking more and more at that. And I wanted to first look at what do these have in common? Why do we have both of these projects? And first of all, I think one of the things we do to both of these is put them in a box. So we tend to use the term protocol, collector, agent, which are all true, but really if you look at these projects, they've expanded to be much more of a framework or a portfolio than just purely collecting the telemetry data.

Um, both have expanded to include all the core telemetry types. So they came from different origins. They now both support logs, traces, and metrics. Um and they do this as part of a broader observability architecture. Um both are of course open- source and both are vendor agnostic mostly which we can talk about for hours over drinks later. I have a lot of opinions about that. Um and both have a really vibrant community. So you've heard about the communities here. You've heard about updates. Um last I checked Fluent Bit was at about 15 billion downloads and around 350 contributors. I'm sure the hotel guys can give you the latest things with that. So, that's what they have in common. Let's back up a little bit and see what they do uniquely for themselves. So, Fluent Bid, as you might know, was purpose-built for logs. Um, so that is its sweet spot, but it now has expanded, as I said, to metrics and traces.

Fluent bit is written in C. Um, and it turns out some people find that very complex. I'm old enough that I actually learned C in school. Um, any other C people out there? C language. Okay, a few. All right, so old people, we can all, you know, go sit in the other part of the room. Um, I guess there's some challenges, but with that, it brings its superpower, which is it is incredibly lightweight, fast, and resource efficient. So, Fluent Bit sweet spot is for any environments where you need high throughput, low latency. So, think containerized environments at scale. It works great at the edge. Um, so it was really made for those environments. Um, Fluentbit supports a huge plug-in ecosystem. You heard some of that from Jose. Um, in addition to all the standard plugins, uh, he mentioned it does you can extend Fluentbit to Lua to Go to Wasom and then now to Zigg. Okay. So, what's sweet spot? The hotel collector started with distributed tracing.

As you probably know, it's still its most mature signal, but it now does metrics and logs. Hotel, of course, is written in Go, which is a language very familiar in the CNCF ecosystem. A little bit easier to learn. Um, it also supports a lot of plug plugins. I think its real secret sauce is, you know, the rich collection of components and tools that it brings in from the community and from vendors that work with it. Um, and it's also really strong at resource detection. And I love how with that ecosystem, it's constantly updating features um such as profiles. So how do they work best together? What I've seen is when you're kind of using the best of each of those in your work. So um fluent bit for example has fully conformed to hotel specification and schema and you can hear a lot more about that. But we play nice with hotel very much. Chronosphere as a company encourages many of its uh customers to move to the hotel standard.

Uh Fluentbit offers OTLP endpoints to ingest hotel formatted data from your SDKs, your libraries, uh your different instrumentation. And if you're already invested in the hotel ecosystem, Fluentbit actually can turn any arbitrary collection into hotel logging schema. And then hotel for its uh has a receiver and exporter that enables you to ingest or route fluent bit based on its forward protocol. So they're really working hard to make it easy for you to use them together. Um in a lot of organizations, especially larger ones, what I see is they'll kind of use Fluentbit for logging and OTEL for tracing. Um, if you're a Google Cloud user, their ops engine does an amazing job of bringing this all together and processing in one place. And again, it uses both Fluent Bit and Hotel Collector to do that. I always try to come up with some criteria or questions to ask. So, here are the questions that I would go through for you to figure out which is right for you or if both are.

Um, you know, what are your core competencies? Do you have folks already that are using Fluent Bit or Hotel Collector? They're contributing to the um organizations. Do you have a vendor you're already working with that supports you in that or maybe can influence those communities with features you need? Um what are your data sources and destinations? What's your environment? Do you need something that's really resource efficient? Um and really looking at your telemetry data volume and and velocity. And finally, that's just the start. I hope this was interesting. I'd love to keep the discussion going. We have a table out front uh with the new Fluent BIT t-shirts, which I haven't gotten one yet, so I will have one soon. Um but you can talk to us about Fluent Bit. We have a telemetry pipeline and an observability platform. I did not talk about our products, but you can do so at our booth. Thank you so much and I hope you have a great


## Related keywords

[[collector]] [[fluent]] [[logs]] [[metrics]] [[tracing]] [[logging]] [[opentelemetry]] [[kubernetes]] [[collectors]] [[agents]] [[agent]] [[profiles]]

## Notes

- Raw note imported from CNCF YouTube playlist. Promote durable insights to topic notes under `03-Topics/`.
