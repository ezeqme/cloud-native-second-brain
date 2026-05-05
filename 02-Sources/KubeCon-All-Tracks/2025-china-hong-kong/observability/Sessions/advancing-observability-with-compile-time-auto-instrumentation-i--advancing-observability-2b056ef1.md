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
speakers: ["Liu Ziming", "Alibaba Cloud", "Przemek Delewski", "Quesma"]
sched_url: https://kccncchn2025.sched.com/event/1x5iC/advancing-observability-with-compile-time-auto-instrumentation-in-golang-liu-ziming-alibaba-cloud-przemek-delewski-quesma
youtube_search_url: https://www.youtube.com/results?search_query=Advancing+Observability+With+Compile-Time+Auto-Instrumentation+in+Golang+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Advancing Observability With Compile-Time Auto-Instrumentation in Golang - Liu Ziming, Alibaba Cloud & Przemek Delewski, Quesma

## Identificação

- Edição: KubeCon + CloudNativeCon China 2025 - Hong Kong, China
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: China / Hong Kong
- Speakers: Liu Ziming, Alibaba Cloud, Przemek Delewski, Quesma
- Schedule: https://kccncchn2025.sched.com/event/1x5iC/advancing-observability-with-compile-time-auto-instrumentation-in-golang-liu-ziming-alibaba-cloud-przemek-delewski-quesma
- Busca YouTube: https://www.youtube.com/results?search_query=Advancing+Observability+With+Compile-Time+Auto-Instrumentation+in+Golang+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Advancing Observability With Compile-Time Auto-Instrumentation in Golang.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncchn2025.sched.com/event/1x5iC/advancing-observability-with-compile-time-auto-instrumentation-in-golang-liu-ziming-alibaba-cloud-przemek-delewski-quesma
- YouTube search: https://www.youtube.com/results?search_query=Advancing+Observability+With+Compile-Time+Auto-Instrumentation+in+Golang+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=xEsVOhBdlZY
- YouTube title: Advancing Observability With Compile-Time Auto-Instrumentation in G... Liu Ziming & Przemek Delewski
- Match score: 0.918
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/advancing-observability-with-compile-time-auto-instrumentation-in-gola/xEsVOhBdlZY.txt
- Transcript chars: 18447
- Keywords: instrumentation, compile, function, context, language, compilation, request, instrument, trace, framework, observability, related, runtime, server, instance, modify, languages, native

### Resumo baseado na transcript

This might be a hard name for non-polish speaker and together with seemingly we would like to tell you uh about go compile time instrumentation. I am also founding member of go compai uh instrumentation and Zimigo is recent engineer at Alibaba cloud. So it's it's very easy to learn and it has very strong support for concurrency. it it was originally written in Typescript and they achieved 10x performance improvement improvements. So mostly uh uh today's systems are growing and also uh we are uh very often addicting uh accidental complexity which is not related to the problem itself. It's a kind of uh designed pattern where you can inject some code uh be before some call and after some call uh in in the in Java you can use it is statically typed language from the uh type system perspective but from the

### Excerpt da transcript

Okay, good afternoon. My name is Pamed Devski. This might be a hard name for non-polish speaker and together with seemingly we would like to tell you uh about go compile time instrumentation. So shortly about us uh I am a founding engineer at Quasma. It's a startup working at in dite space. I am also founding member of go compai uh instrumentation and Zimigo is recent engineer at Alibaba cloud. Uh everybody knows what Alibaba cloud is so it doesn't need introduction. So that's our plan for for today. So first we would like to do some intro introduction and motivation behind the the project. Then we will go through uh different approaches to uh observability. Then we would like to dive into go compile instrumentation. And uh last but not least I would like to uh tell you more about community. Uh yeah so introduction. So as you know probably uh Golang is uh very popular. it's its popularity is growing. So according to Top Index, it's currently at seventh place on on the list of the most popular programming languages.

This is mostly related to the cloud native uh stuff. So uh and some features that uh or properties that this language has. So first of all, it's in natively compiled language which means that the binaries are very small. So you can uh u copy or install your application without some kind of runtime that is needed like in the context of Java or or Python. Uh also it is a very small language so very very limit with very limited numbers of features. So it's it's very easy to learn and it has very strong support for concurrency. So it's very good for uh as I said cloud native application server side kind of application but also there are more examples uh of uh uh of usability of this language. So for instance recently uh Microsoft ported its TypeScript compiler to the uh Golang. it it was originally written in Typescript and they achieved 10x performance improvement improvements. So this is partially due to uh native compilation and partially due to the uh concurrency. Uh now uh that's how the to software systems mostly looks like.

So on the right you can see uh a picture that shows the uh software system it's taken from the Netflix. So the dots represents uh different services and the edges represent uh connections between them. So these services communicates between each other and it's it's very hard generally to uh understand the systems today because the uh the teams are changing people are coming and uh and going h also systems evolve. So most
