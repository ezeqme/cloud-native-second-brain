---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Observability"
themes: ["Observability", "Storage Data"]
speakers: ["Juliano Costa", "Datadog", "Yuri Oliveira", "OllyGarden"]
sched_url: https://kccnceu2026.sched.com/event/2CW3A/how-manual-otel-instrumentation-saves-more-than-just-money-juliano-costa-datadog-yuri-oliveira-ollygarden
youtube_search_url: https://www.youtube.com/results?search_query=How+Manual+OTel+Instrumentation+Saves+More+Than+Just+Money+CNCF+KubeCon+2026
slides: []
status: parsed
---

# How Manual OTel Instrumentation Saves More Than Just Money - Juliano Costa, Datadog & Yuri Oliveira, OllyGarden

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[Storage Data]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Juliano Costa, Datadog, Yuri Oliveira, OllyGarden
- Schedule: https://kccnceu2026.sched.com/event/2CW3A/how-manual-otel-instrumentation-saves-more-than-just-money-juliano-costa-datadog-yuri-oliveira-ollygarden
- Busca YouTube: https://www.youtube.com/results?search_query=How+Manual+OTel+Instrumentation+Saves+More+Than+Just+Money+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre How Manual OTel Instrumentation Saves More Than Just Money.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW3A/how-manual-otel-instrumentation-saves-more-than-just-money-juliano-costa-datadog-yuri-oliveira-ollygarden
- YouTube search: https://www.youtube.com/results?search_query=How+Manual+OTel+Instrumentation+Saves+More+Than+Just+Money+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=13Lyvy48Y6A
- YouTube title: How Manual OTel Instrumentation Saves More Than Just Money - Juliano Costa & Yuri Oliveira
- Match score: 0.886
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/how-manual-otel-instrumentation-saves-more-than-just-money/13Lyvy48Y6A.txt
- Transcript chars: 21036
- Keywords: instrumentation, application, information, manual, instrumented, business, request, database, important, collector, forest, memory, question, observability, actually, connect, filter, everything

### Resumo baseado na transcript

uh some crackling from some leaves from the wind or I don't know animals walking around you don't know and but there is no waterway you need to cross this forest like again really dark maybe a bit scary and you look at the side and there is a light switch you think like what the heck a light switch in the middle of the forest. So if you think about you can control the incoming request or you control the the server side of your application and the database is the database query is where you would improve the query and the the performance of the query. And in manual instrumentation, we could say, hey, I would like to have just the incoming request and database query. we just uh show like gradually here how to what is what is increasing but let's say in express we are having uh 75 MB extra just to add the auto instrument we can argue again this is not much but maybe in a scale out scenario where you have a lot of services that are auto instrumented maybe that may be something cool uh so let's investigate a bit on the cost of lightning the forest list.

### Excerpt da transcript

Uh hello everyone. I I not even have clothes to be on this stage. Uh thanks for joining. Before we start, I'd like to propose an exercise to everyone. Um imagine we we are in a dark forest like really really dark. We can barely see anything. You can hear some O's in the at the back. uh some crackling from some leaves from the wind or I don't know animals walking around you don't know and but there is no waterway you need to cross this forest like again really dark maybe a bit scary and you look at the side and there is a light switch you think like what the heck a light switch in the middle of the forest. Well, it's dark. It's scary. I'll turn it on. And then two flood lights, one on each of the each side of the the forest. And suddenly you can see everything. You can cross the forest as it was daylight. But now all the animals are disturbed. And do you even need all that light? How much energy are you consuming on that? In your observability journey, your application is this dark forest. It's a black black box.

You can cannot see anything on it. And you hear about all the instrumentation and you give a try. Once you deploy on your application, you can see everything. And I would I would even say that maybe you can see too much. Do you need all the spans that you are getting? Do you need every single hop that your application is doing within this each service within the span? Do you need all the attributes that you are cons that you are um ingesting runtime description really? Well, today we're going to learn how auto instrumentation can save more than just money and the pros and cons of auto and manual instrumentation. Hopefully by the end of the talk you'll also get some sanity back. I'm Juliano Costa. I'm a developer advocate at Data Dog and a CNCF ambassador and I'm here today with my friend Yuri. Thank you Juliano. Yeah, I'm Yuri. I'm a co-founder at Olig Garden and I hope you enjoy. >> Cool. So again one more thing that we want to say before we start actually the the talk. Um the community the the open telemetry community which we are both part of uh work really hard on trying to impact the least as possible on your application.

We are not here to bash on anything of uh uh any work that the community is doing. We are just here to shed some light pun intended into the vantage and advantage of auto and manual instrumentation. Having said that, let's discuss a bit of what motivated us to get started on this talk. So you and I we were talking and uh on
