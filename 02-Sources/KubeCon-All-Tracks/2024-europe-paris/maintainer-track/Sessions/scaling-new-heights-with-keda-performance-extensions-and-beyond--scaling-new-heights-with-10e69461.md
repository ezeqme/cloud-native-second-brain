---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "SRE Reliability", "Community Governance"]
speakers: ["Jorge Turrado", "SCRM Lidl International Hub", "Zbynek Roubalik", "Kedify"]
sched_url: https://kccnceu2024.sched.com/event/1YhgO/scaling-new-heights-with-keda-performance-extensions-and-beyond-jorge-turrado-scrm-lidl-international-hub-zbynek-roubalik-kedify
youtube_search_url: https://www.youtube.com/results?search_query=Scaling+New+Heights+with+KEDA%3A+Performance%2C+Extensions%2C+and+Beyond+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Scaling New Heights with KEDA: Performance, Extensions, and Beyond - Jorge Turrado, SCRM Lidl International Hub & Zbynek Roubalik, Kedify

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Jorge Turrado, SCRM Lidl International Hub, Zbynek Roubalik, Kedify
- Schedule: https://kccnceu2024.sched.com/event/1YhgO/scaling-new-heights-with-keda-performance-extensions-and-beyond-jorge-turrado-scrm-lidl-international-hub-zbynek-roubalik-kedify
- Busca YouTube: https://www.youtube.com/results?search_query=Scaling+New+Heights+with+KEDA%3A+Performance%2C+Extensions%2C+and+Beyond+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Scaling New Heights with KEDA: Performance, Extensions, and Beyond.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YhgO/scaling-new-heights-with-keda-performance-extensions-and-beyond-jorge-turrado-scrm-lidl-international-hub-zbynek-roubalik-kedify
- YouTube search: https://www.youtube.com/results?search_query=Scaling+New+Heights+with+KEDA%3A+Performance%2C+Extensions%2C+and+Beyond+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_5_njiPr5vg
- YouTube title: Scaling New Heights with KEDA: Performance, Extensions, and Beyond - Jorge Turrado & Zbynek Roubalik
- Match score: 0.888
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/scaling-new-heights-with-keda-performance-extensions-and-beyond/_5_njiPr5vg.txt
- Transcript chars: 28241
- Keywords: scaling, metrics, object, metric, basically, application, promethus, interceptor, request, thanks, custom, please, trigger, events, source, scaler, important, resource

### Resumo baseado na transcript

hi hello I think that we can start maybe not anyone from the organization can we start probably yes okay no problem leaving on edge okay first of all thanks to everybody for joining us today just for hearing us talking about kada so let's introduce ourself I'm Jorge D I work in SCM little plus a part of asbar group as as principal SRE and I'm one of the maintainers of kada I'm cncf Ambassador and I'm also Microsoft MVP and he is my assistant no I'm joking go

### Excerpt da transcript

hi hello I think that we can start maybe not anyone from the organization can we start probably yes okay no problem leaving on edge okay first of all thanks to everybody for joining us today just for hearing us talking about kada so let's introduce ourself I'm Jorge D I work in SCM little plus a part of asbar group as as principal SRE and I'm one of the maintainers of kada I'm cncf Ambassador and I'm also Microsoft MVP and he is my assistant no I'm joking go ahead introduce yourself hello everybody it's a pleasure to be here with you all and with my dear friend and boss hor uh my name is B grobal League I know the name is hard to pronounce so don't feel about it don't feel bad about this kind of stuff I'm also I'm also K maintainer I'm with the project since the beginning so basically we started couple years ago it was a PC it was a PC to try to solve Autos scaling problem it's uh it was a good solution so we donated the project to cncf as a Sandbox project and after a couple years uh K graduated project so this is really great uh and I'm also founder and CTO at kifi it's a company built around kada uh we try to provide Enterprise Autos scaring platform for our customers so to to solve the special needs for for Enterprises anyway let's talk about K so we have a lot of stuff to cover today so I will try to be quick uh first we will do some introduction uh to K so maybe there are some people that knows SCA maybe there are people that don't know what K is so we will try to do very quick intro then we will talk about some cool features and about the future so let me start uh actually I will try to do uh K in 5 minutes which is kind of challenging but anyway let's start so what is ska uh what is the problem that we are trying to solve imagine that you have an application and the application is doing some some important tasks important job and this application for example is consuming data from some external Source in this case it could be rabid mq and because the you know the data uh they are not stable you know it's not constant uh flow of data so sometimes we need to you know uh process more data sometimes less data maybe sometimes there are no data at all so what we can do we can plug Autos scaling in the solution so we have the dynamicity in the application right so the first knife approach would be uh to plug HPA the building kubernetes autoscaler uh it is a great tool but it has some limitations and espcially in this in this specific use case because what
