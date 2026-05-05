---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Eduardo Silva", "Chronosphere"]
sched_url: https://kccncna2025.sched.com/event/27Nmb/fluent-bit-smarter-telemetry-routing-faster-pipelines-eduardo-silva-chronosphere
youtube_search_url: https://www.youtube.com/results?search_query=Fluent+Bit%3A+Smarter+Telemetry+Routing%2C+Faster+Pipelines+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Fluent Bit: Smarter Telemetry Routing, Faster Pipelines - Eduardo Silva, Chronosphere

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Eduardo Silva, Chronosphere
- Schedule: https://kccncna2025.sched.com/event/27Nmb/fluent-bit-smarter-telemetry-routing-faster-pipelines-eduardo-silva-chronosphere
- Busca YouTube: https://www.youtube.com/results?search_query=Fluent+Bit%3A+Smarter+Telemetry+Routing%2C+Faster+Pipelines+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Fluent Bit: Smarter Telemetry Routing, Faster Pipelines.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Nmb/fluent-bit-smarter-telemetry-routing-faster-pipelines-eduardo-silva-chronosphere
- YouTube search: https://www.youtube.com/results?search_query=Fluent+Bit%3A+Smarter+Telemetry+Routing%2C+Faster+Pipelines+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=40gHwYn0bo4
- YouTube title: Fluent Bit: Smarter Telemetry Routing, Faster Pipelines - Eduardo Silva, Chronosphere
- Match score: 0.877
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/fluent-bit-smarter-telemetry-routing-faster-pipelines/40gHwYn0bo4.txt
- Transcript chars: 29246
- Keywords: fluent, routing, always, collector, configuration, sampling, actually, called, everything, certain, windows, question, performance, logs, traces, output, support, around

### Resumo baseado na transcript

I hope that you are enjoying the conference this second day and before getting started would like to know who's a fluent bit user and who's not so I can get a sense of how to drive the presentation. So, my name is Eduardo Silva, a creator and maintainer of this project and the focus of today's presentation is to get you into the widths of the the Fluent ecosystem and we can get started with that. More than 15 billion downloads, a ton of users, ton of bugs, ton of issues, but we're solving big problems. And thanks for everybody who has trust and this project sends really small contributors, users up to the hyperscalers. OpenAI give a a short keynote around about their use case of logging and how do they use fluent bit to scale the whole infrastructure and move the logs. is because it solves a real problem that moving data at scale it's a challenge and this project for 10 years has been driven by the same values high performance be vendor neutral that means that fully open source but also that we integrate with

### Excerpt da transcript

Well um still good morning everyone. I hope that you are enjoying the conference this second day and before getting started would like to know who's a fluent bit user and who's not so I can get a sense of how to drive the presentation. So please raise your hand if you're using fluent bit. Okay so like 80%. Okay. So, my name is Eduardo Silva, a creator and maintainer of this project and the focus of today's presentation is to get you into the widths of the the Fluent ecosystem and we can get started with that. First talking about the timeline of the project when we started very early in 2015 with fluent bit. Actually, Fluentd is around 14 years old and Fluent Bit was born just when the CNCF was created just after Kubernetes was donated from Google to this new foundation. And after time to time, Fluentd has been evolved as a solution in the cloud ecosystem and Fluent was always kind of the the small sibling around that was solving the problems at that era for embedded Linux. But at some point containers exploded.

They demanded more performance and fluent bit was pivot from embedded Linux to the cloud. But it can work from as really small Raspberry Pi to any type of server. And as of today after 10 years of the project actually we have our new character with Fifian friends that is called Bitsy with bit ZY. And I have to announce a little change that we have in the organization. For many years organization was always um name it as a project that was called fluentd and fluent bit was always under the umbrella of fluentd. So starting today the fluent the organization has been rename it to fluent right and well the github organization has always been fluent but this is just a cncf internal change where now fluent and fluent bit are both graduated projects at the same level there's no longer more sub project actually both belongs to the fluent organization and of course this is a good change after running this for 10 years and we We are celebrating 10 years, right? More than 15 billion downloads, a ton of users, ton of bugs, ton of issues, but we're solving big problems.

And that's why drive us here. And thanks for everybody who has trust and this project sends really small contributors, users up to the hyperscalers. I don't know if you were in the keynote this morning. You were there. OpenAI give a a short keynote around about their use case of logging and how do they use fluent bit to scale the whole infrastructure and move the logs. But the main use case here
