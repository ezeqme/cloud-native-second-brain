---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2025"
edition_id: 2025-munich
year: 2025
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Remote Write Storage", "Kubernetes", "Scalability Reliability", "Visualization Dashboards", "Community"]
speakers: ["Saswata Mukherjee", "Hélia Barroso"]
source_url: https://promcon.io/2025-munich/talks/no-jsonnet-no-problem-prometheus-in-perses-powered-by-go/
youtube_url: https://www.youtube.com/watch?v=fImIhZYXpfM
youtube_search_url: https://www.youtube.com/results?search_query=No+Jsonnet%3F+No+Problem%21+Prometheus+in+Perses%2C+Powered+by+Go+PromCon+2025
video_match_score: 1.026
status: video-found
---

# No Jsonnet? No Problem! Prometheus in Perses, Powered by Go

## Identificação

- Edição: PromCon EU 2025
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Remote Write Storage]], [[Kubernetes]], [[Scalability Reliability]], [[Visualization Dashboards]], [[Community]]
- Speakers: Saswata Mukherjee, Hélia Barroso
- Página oficial: https://promcon.io/2025-munich/talks/no-jsonnet-no-problem-prometheus-in-perses-powered-by-go/
- YouTube: https://www.youtube.com/watch?v=fImIhZYXpfM

## Resumo

Perses, the newly minted CNCF open dashboard platform, has already started to help SRE teams get the most out of their Prometheus instances. Not only is metric visualisation its strong suit, but with Perses Go SDKs, type-safe PromQL builder interfaces, and well-thought-out Dashboard As Code libraries, it packs a tremendous punch when it comes to open configuration. In this session, Hélia and Saswata will take you through the nitty-gritty details of how the Perses Go configuration and Prometheus integration have evolved.

## Abstract oficial

Perses, the newly minted CNCF open dashboard platform, has already started to help SRE teams get the most out of their Prometheus instances. Not only is metric visualisation its strong suit, but with Perses Go SDKs, type-safe PromQL builder interfaces, and well-thought-out Dashboard As Code libraries, it packs a tremendous punch when it comes to open configuration.

In this session, Hélia and Saswata will take you through the nitty-gritty details of how the Perses Go configuration and Prometheus integration have evolved. They will also introduce the community-dashboards initiative, which provides importable Go modules containing methods to generate your favourite mixin dashboards for projects like Kubernetes, Prometheus, Thanos, and more. 

You will also learn how to easily adopt these open standards via the kube-prometheus stack, which includes the Perses Operator and community-dashboard CRDs, offering an alternative visualisation layer. Discover how Perses + Prometheus can elevate your dashboard experience and streamline Observability workflows.

## Links

- Página oficial: https://promcon.io/2025-munich/talks/no-jsonnet-no-problem-prometheus-in-perses-powered-by-go/
- YouTube: https://www.youtube.com/watch?v=fImIhZYXpfM
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=fImIhZYXpfM
- YouTube title: Promcon 2025 - No Jsonnet? No Problem! Prometheus in Perses, Powered by Go
- Match score: 1.026
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2025/no-jsonnet-no-problem-prometheus-in-perses-powered-by-go/fImIhZYXpfM.txt
- Transcript chars: 22441
- Keywords: dashboards, prometheus, dashboard, builder, mixins, already, operator, basically, actually, jsonet, monitoring, panels, directly, promql, itself, queries, plugins, generate

### Resumo baseado na transcript

Um, super excited to see all of you here at Promcon today and glad to be chatting about um, Percy's with you. Now, let's be honest, the title of the talk is a little bit of rage bait for those who really love JSONet. So from metrics with Prometheus and Prometheus like long strings, but also I had already has support for traces, logs and profiles. But from the beginning, Persist was first and foremost fully compatible with Prometheus. Not only you can build your dashboards, but also get detail information about all your metrics and prom queries pretty much the same way you are used to do in the Prometheus UI itself. And for example, one of the latest releases of Percy's also brought the quick query viewer that as you can see mimics the view that you have in Prometheus for when you're running your queries.

### Excerpt da transcript

Uh, okay. So, good morning everyone. Um, super excited to see all of you here at Promcon today and glad to be chatting about um, Percy's with you. Now, let's be honest, the title of the talk is a little bit of rage bait for those who really love JSONet. Um, but does that mean we actually hate JSONet? probably not. Um I think JSONET certainly has its uses as a templating language. It allows for some higher order functional abstractions. Um which definitely reduces this uh sprawl of JSON or YAML config that you might have especially for things like um Kubernetes manifests. JSONET might actually be a step up from tools like customizer Helm when it comes to templating. However, maybe JSONet isn't meant to handle all types of config. So for things like monitoring dashboards um and rules, we felt that we could just do a whole lot better, especially in ways that would um end up making the dashboard construction process much more end user friendly and much more um durable. So what's a better way? That's what Helia and I are here to answer.

But before that, some short introduction. Hi everyone. I'm very happy to be here. This is my first prom. So I'm Ellie Buzz. I work as an observability engineer at 59. I'm also open source contributor primarily towards Prometheus operator and the persist project. I'm also a community organizer at my local cloud native community group. And when I'm offline I like to do what I call granny hobbies. So kneading, stitching and also reading books and music. >> And yeah this is my first promcon as well and my name is Saswat Mukerji. I'm a senior software engineer at Red Hat where I mostly work on multicluster observability systems. I'm also a maintainer of a few projects you might have heard of like Tannas and Percy's itself um and several other adjacent tools and libraries. Um you can find me online as update SAS time code pretty much anywhere and I occasionally love to do some photography sometimes. >> So let's intro into Percis then. And what is Persis? For those who aren't familiar, Persis is an open source visualization tool that allows you to explore and your telemetry data and build dashboards with the main focus of being cloud native and GitHubs friendly.

This project join CNCF sandbox in 2024 and it currently supports all your telemetry uh signals. So from metrics with Prometheus and Prometheus like long strings, but also I had already has support for traces, logs and profiles. But from the beginning, Persist was first and fo
