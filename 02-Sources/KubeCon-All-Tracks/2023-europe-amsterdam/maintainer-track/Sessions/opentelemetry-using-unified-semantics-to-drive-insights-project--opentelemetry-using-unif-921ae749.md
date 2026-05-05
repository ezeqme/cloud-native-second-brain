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
speakers: ["Morgan McLean", "Splunk", "Alolita Sharma", "Apple", "Daniel Dyla", "Dynatrace", "Ted Young", "Lightstep"]
sched_url: https://kccnceu2023.sched.com/event/1HyS5/opentelemetry-using-unified-semantics-to-drive-insights-+-project-update-morgan-mclean-splunk-alolita-sharma-apple-daniel-dyla-dynatrace-ted-young-lightstep
youtube_search_url: https://www.youtube.com/results?search_query=OpenTelemetry%3A+Using+Unified+Semantics+to+Drive+Insights+%2B+Project+Update+CNCF+KubeCon+2023
slides: []
status: parsed
---

# OpenTelemetry: Using Unified Semantics to Drive Insights + Project Update - Morgan McLean, Splunk; Alolita Sharma, Apple; Daniel Dyla, Dynatrace; Ted Young, Lightstep

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Morgan McLean, Splunk, Alolita Sharma, Apple, Daniel Dyla, Dynatrace, Ted Young, Lightstep
- Schedule: https://kccnceu2023.sched.com/event/1HyS5/opentelemetry-using-unified-semantics-to-drive-insights-+-project-update-morgan-mclean-splunk-alolita-sharma-apple-daniel-dyla-dynatrace-ted-young-lightstep
- Busca YouTube: https://www.youtube.com/results?search_query=OpenTelemetry%3A+Using+Unified+Semantics+to+Drive+Insights+%2B+Project+Update+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre OpenTelemetry: Using Unified Semantics to Drive Insights + Project Update.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyS5/opentelemetry-using-unified-semantics-to-drive-insights-+-project-update-morgan-mclean-splunk-alolita-sharma-apple-daniel-dyla-dynatrace-ted-young-lightstep
- YouTube search: https://www.youtube.com/results?search_query=OpenTelemetry%3A+Using+Unified+Semantics+to+Drive+Insights+%2B+Project+Update+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=dFKpbfGJVxI
- YouTube title: OpenTelemetry: Using Unified Semantics to Drive Insights + Project... - Morgan, Alolita, Daniel, Ted
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/opentelemetry-using-unified-semantics-to-drive-insights-project-update/dFKpbfGJVxI.txt
- Transcript chars: 35856
- Keywords: logs, metrics, actually, working, logging, instrumentation, collector, profiling, feedback, projects, probably, conventions, implementations, stable, languages, please, tracing, semantic

### Resumo baseado na transcript

uh so welcome to the maintainers track talk on open Telemetry thank you for coming I wish we had a larger room because it looks like there are other people trying to come in um my name is Morgan McLean I'm one of the co-founders of open Telemetry and like my colleagues here I'm on the governance committee and I'll let them introduce themselves and then we'll get started uh yeah I am Daniel dyla um I work for dynatrace I'm also on the governance committee and I maintain open

### Excerpt da transcript

uh so welcome to the maintainers track talk on open Telemetry thank you for coming I wish we had a larger room because it looks like there are other people trying to come in um my name is Morgan McLean I'm one of the co-founders of open Telemetry and like my colleagues here I'm on the governance committee and I'll let them introduce themselves and then we'll get started uh yeah I am Daniel dyla um I work for dynatrace I'm also on the governance committee and I maintain open Telemetry Js very happy to be here I'm Alita Sharma I'm on the open Telemetry governance committee as well as work on the collector as well as the go library and again uh I'm from Apple and also lead the observability for AIML there hi my name is Ted I work at lightstep and I am also on the governance committee and I mostly heard cats around the specification working group and I forgot to mention I work at the Splunk um so it's been a big year or two for open Telemetry the project has gotten even bigger than it was before it's it's the impact is quite considerable I think we've been coming in various incarnations to kubecon sense I mean country was announced in 2019 and certainly there was open census and open tracing prior to that like Ted I'm trying to remember like when the first time you would have come to cube probably 2016 2017 something like that yeah so like there's been a long journey in in these projects uh to to success but like we're we're really proud of what the community has achieved so we're going to start by giving people a brief overview of where open Telemetry is right now and then the road map and then we're going to dive into the semantic conventions as promised uh so as I mentioned we were announced in 2019 in mid-2020 uh tracing the tracing specification and implementations hit uh stable in open Telemetry that's when the project really started to gain adoption last year we announced at kubecon EU that the metric specifications of the second signal type in open Telemetry had reached 1.0 status and then in kubecon Detroit last year in October we had the announcement that a number of our major languages had achieved their 1.0 implementations and metrics and since then we've seen the adoption of that really grow but we've achieved a lot more than that as a community there's other data types coming in uh it's probably pretty well known to this point that logging is being added as a new signal to open Telemetry and you can see here on this on this timeline when we start
