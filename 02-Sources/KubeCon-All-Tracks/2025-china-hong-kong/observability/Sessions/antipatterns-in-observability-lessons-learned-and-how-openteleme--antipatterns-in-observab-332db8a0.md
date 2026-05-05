---
type: kubecon-session
event: "KubeCon + CloudNativeCon China 2025 - Hong Kong, China"
event_id: kccncchn2025
year: 2025
region: "China"
city: "Hong Kong"
country: "China"
event_date: "2025"
track: "Observability"
themes: ["Observability"]
speakers: ["Steve Flanders", "Splunk"]
sched_url: https://kccncchn2025.sched.com/event/1x5i3/antipatterns-in-observability-lessons-learned-and-how-opentelemetry-solves-them-steve-flanders-splunk
youtube_search_url: https://www.youtube.com/results?search_query=Antipatterns+in+Observability%3A+Lessons+Learned+and+How+OpenTelemetry+Solves+Them+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Antipatterns in Observability: Lessons Learned and How OpenTelemetry Solves Them - Steve Flanders, Splunk

## Identificação

- Edição: KubeCon + CloudNativeCon China 2025 - Hong Kong, China
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: China / Hong Kong
- Speakers: Steve Flanders, Splunk
- Schedule: https://kccncchn2025.sched.com/event/1x5i3/antipatterns-in-observability-lessons-learned-and-how-opentelemetry-solves-them-steve-flanders-splunk
- Busca YouTube: https://www.youtube.com/results?search_query=Antipatterns+in+Observability%3A+Lessons+Learned+and+How+OpenTelemetry+Solves+Them+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Antipatterns in Observability: Lessons Learned and How OpenTelemetry Solves Them.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncchn2025.sched.com/event/1x5i3/antipatterns-in-observability-lessons-learned-and-how-opentelemetry-solves-them-steve-flanders-splunk
- YouTube search: https://www.youtube.com/results?search_query=Antipatterns+in+Observability%3A+Lessons+Learned+and+How+OpenTelemetry+Solves+Them+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2xX3Fx_WVSo
- YouTube title: Antipatterns in Observability: Lessons Learned and How OpenTelemetry Solves Them - Steve Flanders
- Match score: 0.993
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/antipatterns-in-observability-lessons-learned-and-how-opentelemetry-so/2xX3Fx_WVSo.txt
- Transcript chars: 36470
- Keywords: instrumentation, observability, actually, symmetry, collector, environment, another, platform, vendor, basically, everything, instrumented, trace, metrics, metadata, supports, probably, anti-attern

### Resumo baseado na transcript

Hello everyone and welcome to this talk, antiatterns and observability, lessons learned and how open telemetry helps you solve them. Uh love talking about these two topics, observability and open telemetry. This could be problem isolation, root cause analysis, remediation, but you basically have everything necessary to do it in your observability platform. Have you added observability so you can actually make sure you can monitor the health and performance of your system? That's great, but if you don't also have endtoend testing, it may not work properly in the environment that's going to cause problems for you. For example, if you're building a new service, you may not have to solve for massive scale immediately, but as the customer demand grows, you're going to have to find a way to scale that platform or service that you've built.

### Excerpt da transcript

All right. Hello everyone and welcome to this talk, antiatterns and observability, lessons learned and how open telemetry helps you solve them. I'm super excited to be here at CubeCon Hong Kong. Uh love talking about these two topics, observability and open telemetry. Uh but when it really comes to like pitfalls and antiatterns and environments, I don't think it's something that's talked about enough. It's more about the technology and how to leverage it. Uh but if you don't leverage it correctly, you can actually run into issues. And that's what I'd like to talk about today. First, a quick introduction. My name is Steve Flanders. I've been part of the open telemetry project since the very beginning. Uh I've been in the monitoring and observability space for over a decade working on logs, metrics, uh and tracing distributed uh systems for observability platforms. Uh I'm also the author of a book called Mastering Open Symmetry and Observability. And I hope you'll take a look at it. All right. So before we get started, I want to define the terminology that's being used here just to make sure that we're all on the same page.

Uh and then we'll get into some examples of what they all mean. The first is well, what is an anti-attern? An anti-attern is basically a behavior that if you do it will have consequences. They could be consequences now, they could be consequences in the future, but they basically don't help you realize or be as efficient as you could possibly be. Now, we're going to be talking about antiatterns in the context of observability. And so, when you have an anti-attern in observability, it basically means that you will not be able to successfully implement it or fully utilize it because of the pattern or behavior that's being leveraged. Now, the next term is observability. And many people have different definitions for this. I like to refer to it as being able to answer unknown unknowns in your environments. What do I mean? Maybe you've experienced a problem for the first time. You've never seen it before. Well, if you're collecting the right amount of telemetry data and you have the right observability platform, you should be able to answer any question using the platform and the data that you have to solve that.

This could be problem isolation, root cause analysis, remediation, but you basically have everything necessary to do it in your observability platform. And then finally, open symmetry. How many people have heard of open symmetry? Sh
