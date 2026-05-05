---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2022"
edition_id: 2022-munich
year: 2022
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Alerting", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2022-munich/talks/best-practices-and-pitfalls-of-i/
youtube_url: https://www.youtube.com/watch?v=B6Ds2myOIRc
youtube_search_url: https://www.youtube.com/results?search_query=Best+Practices+and+Pitfalls+of+Instrumenting+Your+Cloud-Native+Application+PromCon+2022
video_match_score: 1.032
status: video-found
---

# Best Practices and Pitfalls of Instrumenting Your Cloud-Native Application

## Identificação

- Edição: PromCon EU 2022
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Alerting]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2022-munich/talks/best-practices-and-pitfalls-of-i/
- YouTube: https://www.youtube.com/watch?v=B6Ds2myOIRc

## Resumo

Speaker(s): Jéssica Lins & Kemal Akkoyun Observability is the key to understanding how your application runs and behaves in action. Among many other observability signals like logs, traces and continuous profiling, metrics play the most substantial role. Sampled measurements observed throughout the system are crucial for ensuring service quality, improving performance, scalability, debuggability, security, and enabling real-time, actionable alerting.

## Abstract oficial

Speaker(s): Jéssica Lins & Kemal Akkoyun

Observability is the key to understanding how your application runs and behaves in action. Among many other observability signals like logs, traces and continuous profiling, metrics play the most substantial role. Sampled measurements observed throughout the system are crucial for ensuring service quality, improving performance, scalability, debuggability, security, and enabling real-time, actionable alerting. 

The act of building observable applications starts with instrumentation. Although the tools in the Prometheus ecosystem make life a lot easier, there are still numerous possibilities to make mistakes or misuse them.

During this talk, Jéssica and Kemal will present several useful patterns, best practices and idiomatic methods for instrumenting critical services. They will discuss common pitfalls, failure cases and instrumentation strategies while sharing useful insights and methods to avoid those mistakes. They will give tips for writing simple, maintainable and robust instrumentation facilities using several real-life examples. Moreover, they will demonstrate how to enrich metrics by correlating them with other observability signals. Last, they will discuss how to make the best usage of recent changes in the client_golang, a Go client library for Prometheus.

## Links

- Página oficial: https://promcon.io/2022-munich/talks/best-practices-and-pitfalls-of-i/
- YouTube: https://www.youtube.com/watch?v=B6Ds2myOIRc
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=B6Ds2myOIRc
- YouTube title: PromCon EU 2022: Best Practices and Pitfalls of Instrumenting Your Cloud-Native Application
- Match score: 1.032
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2022/best-practices-and-pitfalls-of-instrumenting-your-cloud-native-applica/B6Ds2myOIRc.txt
- Transcript chars: 21160
- Keywords: metrics, client, registry, function, prometheus, actually, instrumentation, examples, applications, create, request, application, metric, handle, buckets, systems, handler, practices

### Resumo baseado na transcript

[Music] foreign [Music] yes awesome okay yeah hi everyone so welcome to our talks today um yeah today we want to talk about best practices and also pitfalls of instrumenting your Cloud native application my name is Jessica I'm a software engineer at Red Hat I'm also a contributor and approver for Portuguese content at the cncf glossary I'm a maintainer of the observe historian project and I'm currently working with go and I'm also interested in distributed systems and in observability as well and my name is Kamai and

### Excerpt da transcript

[Music] foreign [Music] yes awesome okay yeah hi everyone so welcome to our talks today um yeah today we want to talk about best practices and also pitfalls of instrumenting your Cloud native application my name is Jessica I'm a software engineer at Red Hat I'm also a contributor and approver for Portuguese content at the cncf glossary I'm a maintainer of the observe historian project and I'm currently working with go and I'm also interested in distributed systems and in observability as well and my name is Kamai and this is how I look in the internet I work as a software engineer for Polar sickness if it's not obvious enough we are building an open source project called parka which is an ebpf based profiler and continuous profiling solution if you are interested you can check it out I'm also a maintainer of Thanos and Prometheus client calling cool so what can you expect from our thoughts today so first we want to understand why do we need instrumentation in general we will also talk about best practices of instrumental application like using some examples examples mainly using the client gold link library but that you can also apply to other languages as well yeah and then see some tips see different types of applications so online applications offline applications bad jobs and also check about slos and slis but yeah but first let's try to understand why do you need instrumentation right I think yeah with instrumentation uh it gives you gives you insights about your application so for example when you have a black box monitoring maybe you don't have so many insights as on the other hand if you have white box monitoring so with instrumentation um and once you have your applications instrumented then you make your monitoring better right because then you are adding metrics to your applications you get more insights and as a consequence your monitoring also gets better and with better monitoring then you have better user experience and also it helps you with troubleshooting your application so I think the short answer here is to really instrument intentionally so think about your users right let the slos guide your instrumentation and yeah like think about the user experience and how can you improve that so for those who don't know slos they mean service level objectives and with slos it has a really user-centric approach it motivates collaboration among stakeholders so you are not only work with people from your team but you are also working yeah with othe
