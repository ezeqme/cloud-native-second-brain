---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Observability", "Community Governance"]
speakers: ["Jan Fajerski", "Red Hat", "Bartłomiej Płotka", "Google"]
sched_url: https://kccnceu2026.sched.com/event/2EF4F/prometheus-v3-one-year-in-openmetrics-20-and-more-jan-fajerski-red-hat-bartlomiej-plotka-google
youtube_search_url: https://www.youtube.com/results?search_query=Prometheus+V3+One+Year+In%3A+OpenMetrics+2.0+and+More%21+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Prometheus V3 One Year In: OpenMetrics 2.0 and More! - Jan Fajerski, Red Hat & Bartłomiej Płotka, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jan Fajerski, Red Hat, Bartłomiej Płotka, Google
- Schedule: https://kccnceu2026.sched.com/event/2EF4F/prometheus-v3-one-year-in-openmetrics-20-and-more-jan-fajerski-red-hat-bartlomiej-plotka-google
- Busca YouTube: https://www.youtube.com/results?search_query=Prometheus+V3+One+Year+In%3A+OpenMetrics+2.0+and+More%21+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Prometheus V3 One Year In: OpenMetrics 2.0 and More!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF4F/prometheus-v3-one-year-in-openmetrics-20-and-more-jan-fajerski-red-hat-bartlomiej-plotka-google
- YouTube search: https://www.youtube.com/results?search_query=Prometheus+V3+One+Year+In%3A+OpenMetrics+2.0+and+More%21+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6vE9b6StC0g
- YouTube title: Prometheus V3 One Year In: OpenMetrics 2.0 and More! - Jan Fajerski & Bartłomiej Płotka
- Match score: 0.843
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/prometheus-v3-one-year-in-openmetrics-2-0-and-more/6vE9b6StC0g.txt
- Transcript chars: 31433
- Keywords: prometheus, metrics, already, storage, native, histograms, sample, better, promql, metric, actually, essentially, feedback, histogram, around, information, support, thanos

### Resumo baseado na transcript

We'll talk about what happened in Prometheus since V3, so about last year and a half, and where it's going. Um I work with Prometheus and around Prometheus and some other stuff uh and recently I moved to a forest with great internet connection, so I get to look at these things when I don't look into the magic box. Um it's uh TSDB at its center, um and it gives you a service discovery to discover scraping targets, where it gets all the metrics that it ingests into the TSDB. And then on the other side, it gives you a query interface with PromQL, um and you can define rules, which can be also alerts, but also recording rules. So, at the time, Prometheus 2 was like 2/3 of the lifetime of of Prometheus. Um if the histograms have been a part of Prometheus um for a long time, if not the beginning, um but native histograms basically improve all aspects of it, and you really want to use them.

### Excerpt da transcript

Great. Welcome everybody. Uh thanks for coming. We uh have a pretty jam-packed presentation. So, uh yeah, let's not spend too much time on intros and everything. We'll talk about what happened in Prometheus since V3, so about last year and a half, and where it's going. And um my name is Yan. Um I work with Prometheus and around Prometheus and some other stuff uh and recently I moved to a forest with great internet connection, so I get to look at these things when I don't look into the magic box. And with me is Bartek. Yeah, my name is Bartek. I work at Google. I'm responsible for Google managed service for Prometheus and generally observability at Google. And um I love, you know, open source. I maintain a bunch of stuff. I love mentoring. Um uh so, let's do some mentoring together if you want. And I also wrote a book called Efficient Go about optimizations, and I I love that stuff. And in my free time I tend to do motorcycling, but recently I have two little humans. So, it's a little bit more chaos, but it's definitely enjoyable anyway.

And but I miss my time with motorcycle as well. Let's go. All right. So, here's what we have planned for today. Um we'll we'll dive right into a little recap, uh then sort of the last year and a half, and then what's coming, couple of community updates, and then we have some requests to you guys, too. Okay. Um let's start. Who here doesn't know what Prometheus is? Oh, okay. More than I thought. Um who here runs Oh, sorry. Who here runs Prometheus? All right, keep your hands up. And uh lower your hands if you run 2.something. Okay. Okay. So, keep your hands up if you run three. All right. Pretty good. Not a whole lot, but maybe, I don't know, 6 7%. Um awesome. So, since we have uh more people than I thought who don't know what Prometheus is, here's what Prometheus is. Um it's uh TSDB at its center, um and it gives you a service discovery to discover scraping targets, where it gets all the metrics that it ingests into the TSDB. And then on the other side, it gives you a query interface with PromQL, um and you can define rules, which can be also alerts, but also recording rules.

And ultimately, you get out dashboards uh of your metrics and alerts. So, that's sort of the speed run. Uh since we don't have much time. Um Prometheus V3 uh was a pretty huge deal about 16 months ago. Uh the first major version in uh 7 years, I think. So, at the time, Prometheus 2 was like 2/3 of the lifetime of of Prometheus. Uh was time, and um it
