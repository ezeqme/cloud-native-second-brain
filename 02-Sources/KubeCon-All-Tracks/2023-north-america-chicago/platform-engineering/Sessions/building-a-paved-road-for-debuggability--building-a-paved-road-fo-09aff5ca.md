---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Anusha Ragunathan", "Kevin Downey", "Intuit"]
sched_url: https://kccncna2023.sched.com/event/1R2nC/building-a-paved-road-for-debuggability-anusha-ragunathan-kevin-downey-intuit
youtube_search_url: https://www.youtube.com/results?search_query=Building+a+Paved+Road+for+Debuggability%21+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Building a Paved Road for Debuggability! - Anusha Ragunathan & Kevin Downey, Intuit

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: United States / Chicago
- Speakers: Anusha Ragunathan, Kevin Downey, Intuit
- Schedule: https://kccncna2023.sched.com/event/1R2nC/building-a-paved-road-for-debuggability-anusha-ragunathan-kevin-downey-intuit
- Busca YouTube: https://www.youtube.com/results?search_query=Building+a+Paved+Road+for+Debuggability%21+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Building a Paved Road for Debuggability!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2nC/building-a-paved-road-for-debuggability-anusha-ragunathan-kevin-downey-intuit
- YouTube search: https://www.youtube.com/results?search_query=Building+a+Paved+Road+for+Debuggability%21+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=bPa1PjY-Hg4
- YouTube title: Building a Paved Road for Debuggability! - Anusha Ragunathan & Kevin Downey, Intuit
- Match score: 0.752
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/building-a-paved-road-for-debuggability/bPa1PjY-Hg4.txt
- Transcript chars: 27592
- Keywords: actually, container, debugging, ephemeral, containers, specific, thread, application, access, basically, developer, orchestrator, platform, developers, network, workflow, little, running

### Resumo baseado na transcript

hello and welcome to our talk today we're going to be talking about how we built a debab paved Road at inate my name is Anusha ragunathan and with me is Kevin Downey and we're both software Engineers working at int on the kubernetes based platform infrastructure today we'll start off with giving a little bit of background of in it and our infrastructure at a glance and get into the problem statement why are we even giving this stock what are we solving why did we build a debuggability

### Excerpt da transcript

hello and welcome to our talk today we're going to be talking about how we built a debab paved Road at inate my name is Anusha ragunathan and with me is Kevin Downey and we're both software Engineers working at int on the kubernetes based platform infrastructure today we'll start off with giving a little bit of background of in it and our infrastructure at a glance and get into the problem statement why are we even giving this stock what are we solving why did we build a debuggability paveed road then we'll jump into how we built paved Road using two Technical Solutions the first one would be interactive debugging using ephemeral containers and the second one is the one click debugging that we built with Argo workflows and finish it off with some takeaway for you now into it is a fintech company that's built on an aid driven expert platform and um just to give you an idea of the scale at which we run our clusters we run about 315 plus and growing kubernetes clusters comprising of 28,000 name spaces that serves about 2,500 Production Services and these are just Production Services we have a whole bunch of preprod um Services as well and all of this serves uh development community of 7,000 Engineers that comprise about thousand development teams and to highlight our AI emphasis we actually do about 40 million AI Ops inferences per day to help our customers with their financial needs so what is the problem here we have about 7,000 developers at interet that we serve and one thing is common across all of their applications bugs we've all been there we write code pass a CI then we push it to prepr everything works and then we promote to prod and things break yeah and these can be very esoteric 5xx errors to transient timeouts and everything in between and we all know debugging distributor systems is a pretty hard problem and traditionally developers use metrics logs and distributed traces to observe their systems and try and debug root cause and fix the issues but sometimes this is not sufficient what if you need to actually do deeper debugging and observability in your service environments what if you have to actually run a memory profiler what you what if you have to capture your network packets what if you have to do some homegrown debugging tools that you need to run or even just Network traces what do you do and in this in in this scenario and any friction that you have during this deeper debugging experience will increase your meantime to detect and resol
