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
speakers: ["Bartłomiej Płotka", "Google", "Arianna Vespri", "Independent"]
sched_url: https://kccnceu2025.sched.com/event/1txHv/how-to-rename-metrics-without-impacting-somebodys-observability-bartlomiej-plotka-google-arianna-vespri-independent
youtube_search_url: https://www.youtube.com/results?search_query=How+To+Rename+Metrics+Without+Impacting+Somebody%E2%80%99s+Observability+CNCF+KubeCon+2025
slides: []
status: parsed
---

# How To Rename Metrics Without Impacting Somebody’s Observability - Bartłomiej Płotka, Google & Arianna Vespri, Independent

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United Kingdom / London
- Speakers: Bartłomiej Płotka, Google, Arianna Vespri, Independent
- Schedule: https://kccnceu2025.sched.com/event/1txHv/how-to-rename-metrics-without-impacting-somebodys-observability-bartlomiej-plotka-google-arianna-vespri-independent
- Busca YouTube: https://www.youtube.com/results?search_query=How+To+Rename+Metrics+Without+Impacting+Somebody%E2%80%99s+Observability+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre How To Rename Metrics Without Impacting Somebody’s Observability.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txHv/how-to-rename-metrics-without-impacting-somebodys-observability-bartlomiej-plotka-google-arianna-vespri-independent
- YouTube search: https://www.youtube.com/results?search_query=How+To+Rename+Metrics+Without+Impacting+Somebody%E2%80%99s+Observability+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Rw4c7lmdyFs
- YouTube title: How To Rename Metrics Without Impacting Somebody’s Observabili... Bartłomiej Płotka & Arianna Vespri
- Match score: 0.87
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/how-to-rename-metrics-without-impacting-somebodys-observability/Rw4c7lmdyFs.txt
- Transcript chars: 30399
- Keywords: metric, schema, actually, version, prometheus, change, metrics, course, client, changes, totally, already, matrix, renaming, application, ecosystem, storage, transformation

### Resumo baseado na transcript

Uh, looks like this topic of renaming metrics is really uh, you know, important. You have a counter metric that is exposed and scraped you know from some example application exporter or production application. Um and it it causes a lot of friction for both consumers of course users who have their queries broken suddenly out of nowhere but also for producers for maintainers like us who are afraid to rename metrics literally because it can cause possibly those kind of weak or not existing so We were kind of like okay this talk will be a little bit of moaning and sadness but actually it surprised even us that in the CNCF CNCF ecosystem both open telemetry and Prometheus communities worked on a already there are existing core fundamental pieces that combine together allows something truly truly magical right so imagine there is a way to pin your quer metrics to a certain version like you do with your code dependencies right? We want to show you a prototype of of a solution to this problem in Prometheio ecosystem um using several pieces uh from open telemetry project as well and and give you a chance to give us a feedback as a Prometheus maintainers developers uh

### Excerpt da transcript

Hello everyone. Um, welcome everyone to our talk. Let's start. It's really amazing to see so many people coming to our talk today. Uh, looks like this topic of renaming metrics is really uh, you know, important. Um, so it's very relevant and hopefully that's why you are here. Um, so yeah, we have really exciting content for you. So let's let's go. Let's not waste our time. So why we are here today? Uh, imagine the following scenario. You have a counter metric that is exposed and scraped you know from some example application exporter or production application. It's very important right this metric is very important you use it in on important alert dashboard maybe it's using you know are you are using it for autoscaling and you know and SLO tools and so on and if this query stops working you have essentially a production incident uh for example if you use it in autoscaling if this query is you know broken then you cannot scale your workloads for customers you cannot start things so it's super serious thing imagine that and it happens right suddenly after the underlying you know server application that was giving us those metrics.

Um, this application restarts and suddenly after that we don't have the query working again. So what happened after some stressful debugging you kind of like take a look and you realize that the application with this key metric was upgraded to a new version and this new version actually renamed a metric and made a small you know naming changes to the metric. Um, so what's worse is not only a metric name but actually a couple of labels, right? So it change you know integer to my number and um category to class and then label value change through you know to get uppercase just because maybe you know it was clearer and and easier to read. Um in our experience it's actually a very very common scenario. Um and it it causes a lot of friction for both consumers of course users who have their queries broken suddenly out of nowhere but also for producers for maintainers like us who are afraid to rename metrics literally because it can cause possibly those issues right and the honest truth about this talk is that when we proposed it in October um we maybe had a small vision how to fix it how to improve it um but we also knew that the current solutions to solve this are kind of weak or not existing so We were kind of like okay this talk will be a little bit of moaning and sadness but actually it surprised even us that in the CNCF CNCF ecosys
