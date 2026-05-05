---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Keynote Sessions"
themes: ["AI ML", "SRE Reliability"]
speakers: ["Fabian Ponce", "Member of Technical Staff", "OpenAI"]
sched_url: https://kccncna2025.sched.com/event/29Kgb/keynote-how-one-line-of-code-freed-30000-cpu-cores-deep-diving-fluent-bit-at-petabyte-scale-fabian-ponce-member-of-technical-staff-openai
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+How+One+Line+of+Code+Freed+30%2C000+CPU+Cores%3A+Deep-Diving+Fluent+Bit+at+Petabyte+Scale+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Keynote: How One Line of Code Freed 30,000 CPU Cores: Deep-Diving Fluent Bit at Petabyte Scale - Fabian Ponce, Member of Technical Staff, OpenAI

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Fabian Ponce, Member of Technical Staff, OpenAI
- Schedule: https://kccncna2025.sched.com/event/29Kgb/keynote-how-one-line-of-code-freed-30000-cpu-cores-deep-diving-fluent-bit-at-petabyte-scale-fabian-ponce-member-of-technical-staff-openai
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+How+One+Line+of+Code+Freed+30%2C000+CPU+Cores%3A+Deep-Diving+Fluent+Bit+at+Petabyte+Scale+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Keynote: How One Line of Code Freed 30,000 CPU Cores: Deep-Diving Fluent Bit at Petabyte Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/29Kgb/keynote-how-one-line-of-code-freed-30000-cpu-cores-deep-diving-fluent-bit-at-petabyte-scale-fabian-ponce-member-of-technical-staff-openai
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+How+One+Line+of+Code+Freed+30%2C000+CPU+Cores%3A+Deep-Diving+Fluent+Bit+at+Petabyte+Scale+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=pbOvWxuYPIU
- YouTube title: Keynote: How One Line of Code Freed 30,000 CPU Cores: Deep-Diving Fluent Bit at Petabyte... F. Ponce
- Match score: 1.037
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/keynote-how-one-line-of-code-freed-30-000-cpu-cores-deep-diving-fluent/pbOvWxuYPIU.txt
- Transcript chars: 8916
- Keywords: fluent, source, logs, compute, notify, software, information, performance, fluentbit, surprising, result, results, openai, process, little, capacity, resources, cluster

### Resumo baseado na transcript

Hi everyone, I'm Fabian and I'm a member of technical staff at OpenAI on their applied observability team. Um, super excited to be here and share with you how we're using open source technology to process logs at scale and some of the interesting things that we've found. Then I'll share the unique challenges that we're trying to meet and how those business problems force us to look for performance wins. We run Fluent Bbit on every Kubernetes node in our fleet and it's responsible for ingesting log files, performing any sampling, enriching those logs with metadata that comes from Kubernetes, formatting them into the right schema, and then routing them to the appropriate data stores that those logs can be queried. In the aggregate, we emit just shy of 10 pabytes of logs per day using this architecture. A fluent bit process that exceeds its CPU quota and gets throttled could ends up losing logs or worse, uh it could degrade the performance of a different application.

### Excerpt da transcript

Hi everyone, I'm Fabian and I'm a member of technical staff at OpenAI on their applied observability team. Um, super excited to be here and share with you how we're using open source technology to process logs at scale and some of the interesting things that we've found. So, it's only been three years since the original chat GPT release, and I think it's fair to say that AI has already completely changed the way that we work and the way that we access information. With GPT5, the model is not just generating text. It's seeing and creating images, writing and running code, and orchestrating increasingly complex tool chains. And each step up in capability doesn't just mean more compute. It means more Kubernetes clusters, more user traffic, and orders of magnitude more telemetry to keep it all running and ensure that we're successful in our mission to make AGI beneficial to all of humanity. Our role on applied observability is to make sure that every engineer at OpenAI has the tools that they need to prevent SES hopefully before they happen, but also to effectively fight them when they do.

And that means ingesting absolutely massive amounts of telemetry and making it fast, queriable, and actionable at scale. So to set the scene for you, I'm first going to share with you highle architecture of what our logging solution looks like. Then I'll share the unique challenges that we're trying to meet and how those business problems force us to look for performance wins. And lastly, I'll share the Eureka moment that saved us a ton of compute and what I think is the most important thing to take away from this experience. So the ingestion pipeline starts with Fluent Bit. We run Fluent Bbit on every Kubernetes node in our fleet and it's responsible for ingesting log files, performing any sampling, enriching those logs with metadata that comes from Kubernetes, formatting them into the right schema, and then routing them to the appropriate data stores that those logs can be queried. In the aggregate, we emit just shy of 10 pabytes of logs per day using this architecture. And since Fluent bit runs on every node, its performance is critical.

A fluent bit process that exceeds its CPU quota and gets throttled could ends up losing logs or worse, uh it could degrade the performance of a different application. So, we'd prefer it to just use as little CPU as possible to get the job done. So, if you follow the news, I'm sure you've heard about our absolutely insatiable appetite fo
