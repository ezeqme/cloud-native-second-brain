---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Observability", "Community Governance"]
speakers: ["Eduardo Silva", "Anurag Gupta", "Calyptia"]
sched_url: https://kccnceu2023.sched.com/event/1Ikk4/observability-with-fluent-bit-logs-metrics-traces-eduardo-silva-anurag-gupta-calyptia
youtube_search_url: https://www.youtube.com/results?search_query=Observability+with+Fluent+Bit%3A+Logs%2C+Metrics+%26+Traces+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Observability with Fluent Bit: Logs, Metrics & Traces - Eduardo Silva & Anurag Gupta, Calyptia

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Eduardo Silva, Anurag Gupta, Calyptia
- Schedule: https://kccnceu2023.sched.com/event/1Ikk4/observability-with-fluent-bit-logs-metrics-traces-eduardo-silva-anurag-gupta-calyptia
- Busca YouTube: https://www.youtube.com/results?search_query=Observability+with+Fluent+Bit%3A+Logs%2C+Metrics+%26+Traces+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Observability with Fluent Bit: Logs, Metrics & Traces.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Ikk4/observability-with-fluent-bit-logs-metrics-traces-eduardo-silva-anurag-gupta-calyptia
- YouTube search: https://www.youtube.com/results?search_query=Observability+with+Fluent+Bit%3A+Logs%2C+Metrics+%26+Traces+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=PP8vlQBRtts
- YouTube title: Observability with Fluent Bit: Logs, Metrics & Traces - Eduardo Silva & Anurag Gupta, Calyptia
- Match score: 0.811
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/observability-with-fluent-bit-logs-metrics-traces/PP8vlQBRtts.txt
- Transcript chars: 27758
- Keywords: metrics, matrix, logs, fluent, prometheus, output, support, metric, application, traces, information, windows, labels, everyone, getting, environment, actually, configuration

### Resumo baseado na transcript

hey welcome everyone I Thanks for for coming in I know it's a little packed but uh you know thankfully these will be recorded and and everyone can also see it uh otherwise as well uh so I'm I'm on a rug I'm joined with Eduardo uh and we're our maintainers of the fluent fit project and I guess some questions to to kick it off how many folks here know what fluent fit is or and keep your hand raised are using it today okay a couple less hands

### Excerpt da transcript

hey welcome everyone I Thanks for for coming in I know it's a little packed but uh you know thankfully these will be recorded and and everyone can also see it uh otherwise as well uh so I'm I'm on a rug I'm joined with Eduardo uh and we're our maintainers of the fluent fit project and I guess some questions to to kick it off how many folks here know what fluent fit is or and keep your hand raised are using it today okay a couple less hands good uh awesome so what we'll do today we're going to go over the project a little bit and then we'll run through some of the updates that we've done you know specifically talking about some of the Integrations that have come in the latest version released yesterday uh and then last but not least we'll we'll save some good time for for demo here so again yeah I'm one of the maintainers on rug and then I'm joined with Eduardo uh we both work for the company colyptia uh and so we've been here doing fluent D fluent bit uh and and very much in the space of telemetry logs metrics traces for for quite a while so really excited to get to chat with everyone here and you know kind of starting at a very high level what is the the complexity of telemetry data right the the idea behind all of this data that we're getting it's really so we can go do some data analytics data analysis what's going wrong troubleshooting have a really nice understanding of what's happening within the environment and ideally when you understand what's happening you're able to make better decisions whether those are business related whether those are for operational purposes uh and and to do this really we look at the challenges that occur with this you have multiple sources you know everyone here might have a different logging Library you might be logging XYZ you might be instrumenting your application in a certain way there's different languages and we have tons and tons of different data formats so the more that we continue to produce and create the software we are continually expounding and increasing the challenges in order to understand what's what's going on and you know a lot of folks might say oh there's there's profiling there's others but really let's if we focus on the three major verticals of telemetry data you have your logs things that have been there for for long long periods of time metrics as well things that kind of detail how a specific application might be running could be custom metrics about something within the business and more rec
