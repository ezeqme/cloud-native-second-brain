---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Observability"
themes: ["Observability"]
speakers: ["Jacek Migdal", "Quesma"]
sched_url: https://kccnceu2025.sched.com/event/1txI1/observability-pipeline-query-languages-present-and-the-future-jacek-migdal-quesma
youtube_search_url: https://www.youtube.com/results?search_query=Observability+Pipeline+Query+Languages%3A+Present+and+the+Future+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Observability Pipeline Query Languages: Present and the Future - Jacek Migdal, Quesma

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United Kingdom / London
- Speakers: Jacek Migdal, Quesma
- Schedule: https://kccnceu2025.sched.com/event/1txI1/observability-pipeline-query-languages-present-and-the-future-jacek-migdal-quesma
- Busca YouTube: https://www.youtube.com/results?search_query=Observability+Pipeline+Query+Languages%3A+Present+and+the+Future+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Observability Pipeline Query Languages: Present and the Future.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txI1/observability-pipeline-query-languages-present-and-the-future-jacek-migdal-quesma
- YouTube search: https://www.youtube.com/results?search_query=Observability+Pipeline+Query+Languages%3A+Present+and+the+Future+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=iiI91sUMtdg
- YouTube title: Observability Pipeline Query Languages: Present and the Future - Jacek Migdal, Quesma
- Match score: 0.939
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/observability-pipeline-query-languages-present-and-the-future/iiI91sUMtdg.txt
- Transcript chars: 29844
- Keywords: language, observability, actually, syntax, usually, companies, languages, another, write, vendor, metrics, operator, pretty, became, vendors, either, source, rather

### Resumo baseado na transcript

I would like to tell you a story about observability pipeline query languages. Uh and to be fair, it would be a little bit personal story because today I'm running like a small startup was doing database gateway. all of the text of your machine data keep them in centralized story and then you could like use similar syntax to query languages of course there's like one very major important difference why the Unix pipes were very like imperative so kind of like you know you pretty much execute one tractor after the other why this query language in distributed systems or like in is like declarative so it's kind of like SQL you tell it what needs to be done but actually the computers or system could maybe look for more specific errors or maybe group it by from which machine or Kubernetes spot they came. uh you know there was like you know once upon a time bork and out of bor came kubernetes and there was like also like a once upon a time in Google like a borgmon so system to monitor bork which later came to open

### Excerpt da transcript

Hello, I'm Yat Mindal. I would like to tell you a story about observability pipeline query languages. Uh and to be fair, it would be a little bit personal story because today I'm running like a small startup was doing database gateway. But previously I was working for 10 years and one of the observability vendors. So if you have to blame someone for that mess, that's me unfortunately. uh and uh before I also work at like Nvidia, Quran and Meta and where the history of pipe start they actually started with Unix. So even before Linux and computers were really slow at the time and the idea was like to write like a very specialized programs like just find if one word is in the text do this thing well but if you want to do anything more sophisticated you could like chain those programs together so you could redirect sadane or s either to file or either to another program and this was like it is like very core of unix philosophies that works surprisingly well. It stood the time of the time and even today if you have any Linux server you may just deal with your logs that way right like you could just one comment find files the other command to do like a grip on those file whether there is error sort them have unique them sort them by count and then do some head operations and if you don't run like operating systems just in your computer that may be enough but as we know system has evolved a lot and this idea of pipes was let brought by one of the first I would say full text commercial vendors plank that quickly realized that you know systems breaks all the time so what if we have like Google for this machine data so just ingest all of the text of your machine data keep them in centralized story and then you could like use similar syntax to query languages of course there's like one very major important difference why the Unix pipes were very like imperative so kind of like you know you pretty much execute one tractor after the other why this query language in distributed systems or like in is like declarative so it's kind of like SQL you tell it what needs to be done but actually the computers or system could optimize behind this and how this would work and this became quite popular and for those you you may not know it it's actually became popular and almost like every lock system has some version of that whether it's like Microsoft custo like uh EQL there's a lot of them but the idea is like pretty much the same you select some data either on type or either on
