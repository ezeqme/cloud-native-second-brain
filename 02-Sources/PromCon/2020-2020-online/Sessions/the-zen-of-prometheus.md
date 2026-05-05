---
type: promcon-talk
conference: PromCon
edition: "PromCon Online 2020"
edition_id: 2020-online
year: 2020
city: "Online"
country: "Online"
topics: ["Prometheus Core", "Metrics", "Alerting", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2020-online/talks/the-zen-of-prometheus/
youtube_url: https://www.youtube.com/watch?v=Nqp4fjw_omU
youtube_search_url: https://www.youtube.com/results?search_query=The+Zen+of+Prometheus+PromCon+2020
video_match_score: 0.63
status: video-found
---

# The Zen of Prometheus

## Identificação

- Edição: PromCon Online 2020
- País/cidade: Online / Online
- Temas: [[Prometheus Core]], [[Metrics]], [[Alerting]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2020-online/talks/the-zen-of-prometheus/
- YouTube: https://www.youtube.com/watch?v=Nqp4fjw_omU

## Resumo

Speaker: Kemal Akkoyun In modern days, we run our applications as loosely coupled microservices on distributed, elastic infrastructure as (mostly) stateless workloads. Under these circumstances, observability is the key to understanding how our applications run and behave in action to deliver highly available and resilient service. Prometheus is born in such an atmosphere as a solution to satisfy the observability needs of the cloud-native era.

## Abstract oficial

Speaker: Kemal Akkoyun

In modern days, we run our applications as loosely coupled microservices on distributed, elastic infrastructure as (mostly) stateless workloads. Under these circumstances, observability is the key to understanding how our applications run and behave in action to deliver highly available and resilient service.

Prometheus is born in such an atmosphere as a solution to satisfy the observability needs of the cloud-native era. Among many other observability signals like logs and traces, metrics play the most substantial role. Sampled measurements observed throughout the system are crucial for monitoring the health of the applications and they enable real-time, actionable alerting. Although the tools in the Prometheus ecosystem make life a lot easier, there are still numerous possibilities to make mistakes or misuse them.

During this talk, Kemal will present several valuable patterns, best practices and idiomatic methods for instrumenting critical services. He will discuss common pitfalls and failure cases while sharing useful insights and methods to avoid those mistakes. Last but not least, he will give tips for writing simple, maintainable and robust alerts that derived from real-life experiences. By doing so he will propose “the Zen of Prometheus”.

## Links

- Página oficial: https://promcon.io/2020-online/talks/the-zen-of-prometheus/
- YouTube: https://www.youtube.com/watch?v=Nqp4fjw_omU
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Nqp4fjw_omU
- YouTube title: PromCon Online 2020 - The Zen of Prometheus, Kemal Akkoyun, Red Hat
- Match score: 0.63
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2020/the-zen-of-prometheus/Nqp4fjw_omU.txt
- Transcript chars: 19471
- Keywords: labels, actually, alerts, questions, practices, question, systems, problems, proverbs, prometheus, instrumentation, create, already, mentioned, started, others, important, always

### Resumo baseado na transcript

[Music] hello everyone I hope you are enjoying the conference so far so this will be a yet another best practice talk on instrumentation and alerting using Prometheus and I'm sure you have seen similar talks and perhaps better ones but anyhow this will be my take on it so I have collected a couple of best practices as set of rules and I'm gonna share those with you in this presentation so before I start I want to make something clear none of these are like mine the only

### Excerpt da transcript

[Music] hello everyone I hope you are enjoying the conference so far so this will be a yet another best practice talk on instrumentation and alerting using Prometheus and I'm sure you have seen similar talks and perhaps better ones but anyhow this will be my take on it so I have collected a couple of best practices as set of rules and I'm gonna share those with you in this presentation so before I start I want to make something clear none of these are like mine the only noble thing I am gonna be presenting here is the mere collection of these metrics these ideas so first Who I am so my name is Claire mine and I work for reddit as a software engineer I work OpenType observability platform team and in this team we are building a platform to collect observability signals like such as metrics logs tracing and profile also as a team we are we have a sri responsibilities and meaningly we are on call for the platform that we are building so the rules that I'm gonna share with you today we are actually applying that in our daily lives on production systems I'm also a ton of maintainer and recently started to contribute to parameters yeah achievement unlocked for me besides the observer ability and monitoring topics I am also passionate about distributed systems and data raises and by the way in this picture I'm on location and like normally I don't look that much happy so let's start so what is that when you check the dictionary or in this case of Wikipedia you get a definition so then emphasize the rigorous self restraint meditation practice practice inside into the nature of the mind and nature of the things and the personal expression of this insides daily life especially for the benefit of others that's the formal definition so from this formal definition to use in our context I have derived a simpler one a Zen is a collection of insights gathered from the daily life to benefit others so I'm sure you have heard similar than ideas before so in this talk I'm gonna try to come up with a set of rules to fulfill this definition the first and probably the most popular of designs in software systems is the Zen of Python it's created 20 years ago as a Python an enhancement proposal Feb 20 believed by Tim Peters in this document he captured the engineering the others behind Titan in some humorous way you can access these you can access these through the website or through the Python interpreter there is the Easter Egg in Python interpreter so if you open up an interpre
