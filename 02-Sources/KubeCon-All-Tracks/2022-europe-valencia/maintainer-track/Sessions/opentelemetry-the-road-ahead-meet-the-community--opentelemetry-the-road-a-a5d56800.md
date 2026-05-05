---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Maintainer Track"
themes: ["AI ML", "Observability", "Community Governance"]
speakers: ["Morgan McLean", "Splunk", "Alolita Sharma", "Amazon", "Ted Young", "Lightstep", "Daniel Dyla", "Dynatrace"]
sched_url: https://kccnceu2022.sched.com/event/ytns/opentelemetry-the-road-ahead-+-meet-the-community-morgan-mclean-splunk-alolita-sharma-amazon-ted-young-lightstep-daniel-dyla-dynatrace
youtube_search_url: https://www.youtube.com/results?search_query=OpenTelemetry%3A+The+Road+Ahead+%2B+Meet+the+Community+CNCF+KubeCon+2022
slides: []
status: parsed
---

# OpenTelemetry: The Road Ahead + Meet the Community - Morgan McLean, Splunk; Alolita Sharma, Amazon; Ted Young, Lightstep; Daniel Dyla, Dynatrace

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: Morgan McLean, Splunk, Alolita Sharma, Amazon, Ted Young, Lightstep, Daniel Dyla, Dynatrace
- Schedule: https://kccnceu2022.sched.com/event/ytns/opentelemetry-the-road-ahead-+-meet-the-community-morgan-mclean-splunk-alolita-sharma-amazon-ted-young-lightstep-daniel-dyla-dynatrace
- Busca YouTube: https://www.youtube.com/results?search_query=OpenTelemetry%3A+The+Road+Ahead+%2B+Meet+the+Community+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre OpenTelemetry: The Road Ahead + Meet the Community.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytns/opentelemetry-the-road-ahead-+-meet-the-community-morgan-mclean-splunk-alolita-sharma-amazon-ted-young-lightstep-daniel-dyla-dynatrace
- YouTube search: https://www.youtube.com/results?search_query=OpenTelemetry%3A+The+Road+Ahead+%2B+Meet+the+Community+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2uuqGuKpyQ8
- YouTube title: OpenTelemetry: The Road Ahead + Meet the Co... Morgan McLean, Alolita Sharma, Ted Young, Daniel Dyla
- Match score: 0.747
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/opentelemetry-the-road-ahead-meet-the-community/2uuqGuKpyQ8.txt
- Transcript chars: 29737
- Keywords: logging, questions, collector, metrics, logs, already, question, instrumentation, started, probably, information, ebpf, application, effectively, feedback, security, maintainers, working

### Resumo baseado na transcript

so welcome everybody to the maintainers track session uh for open telemetry uh so we'll introduce ourselves and we'll get started uh with a very quick background on the project because i'm assuming most people here are pretty familiar with open telemetry at this point uh followed by our current status then we'll talk about the road ahead uh and we'll wrap up with uh a q a amongst maintainers so once we finish the road ahead section we'll invite the maintainers to come on stage we've got a hand

### Excerpt da transcript

so welcome everybody to the maintainers track session uh for open telemetry uh so we'll introduce ourselves and we'll get started uh with a very quick background on the project because i'm assuming most people here are pretty familiar with open telemetry at this point uh followed by our current status then we'll talk about the road ahead uh and we'll wrap up with uh a q a amongst maintainers so once we finish the road ahead section we'll invite the maintainers to come on stage we've got a hand mic here and then we'll take questions from the audience until they give us the boot uh out of here um so to start with introductions my name is morgan mclean i'm a director of product management at splunk i've been with open telemetry since the beginning and open sentence before that uh as have i guess both my my uh co-stars up here um and uh yeah i i don't do a lot of code contributions but uh i run the weekly maintainers call and i'm involved in a lot of the spec work and other work that's going on hi yeah my name's ted young i work at lightstep also one of the co-founders of open telemetry and spend most of my time working on that project making it go uh i'm daniel daila i work for dynatrace i've been the maintainer of open telemetry.js for about two years and on the governance committee as well for about the same amount of time nice all right all right yeah so just a a briefest of overviews of the project and uh what it consists of i assume most people know but just as a reminder this green blob is your app and if you would like to observe your app you install the open telemetry sdk the open telemetry sdk observes your various libraries uh either by having those libraries natively instrument themselves or by installing an instrumentation plugin you then export that data from the sdk to a collector either running as a side car or as a pool behind the load balancer and you send that data through otlp which is open telemetry's native protocol the collector itself is a really awesome swiss army knife it takes input from a huge variety of sources not just otlp connects all of that data into uh complex processing pipelines that you can write in order to do things like data scrubbing and enrichment and all that fun stuff and then outputs it again in otlp or a variety of other formats and what makes open telemetry special beyond just being very friendly uh standard that's adopted by many different organizations is it takes all these different signals tracing metrics log
