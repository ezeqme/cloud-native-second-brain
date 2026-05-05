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
speakers: ["Arthur Sens", "Grafana", "Juraj Michálek", "Swiss RE"]
sched_url: https://kccnceu2025.sched.com/event/1txIA/the-state-of-prometheus-and-opentelemetry-interoperability-arthur-sens-grafana-juraj-michalek-swiss-re
youtube_search_url: https://www.youtube.com/results?search_query=The+State+of+Prometheus+and+OpenTelemetry+Interoperability+CNCF+KubeCon+2025
slides: []
status: parsed
---

# The State of Prometheus and OpenTelemetry Interoperability - Arthur Sens, Grafana & Juraj Michálek, Swiss RE

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United Kingdom / London
- Speakers: Arthur Sens, Grafana, Juraj Michálek, Swiss RE
- Schedule: https://kccnceu2025.sched.com/event/1txIA/the-state-of-prometheus-and-opentelemetry-interoperability-arthur-sens-grafana-juraj-michalek-swiss-re
- Busca YouTube: https://www.youtube.com/results?search_query=The+State+of+Prometheus+and+OpenTelemetry+Interoperability+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre The State of Prometheus and OpenTelemetry Interoperability.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txIA/the-state-of-prometheus-and-opentelemetry-interoperability-arthur-sens-grafana-juraj-michalek-swiss-re
- YouTube search: https://www.youtube.com/results?search_query=The+State+of+Prometheus+and+OpenTelemetry+Interoperability+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=JFS0lSfHtMI
- YouTube title: The State of Prometheus and OpenTelemetry Interoperability - Arthur Sens & Juraj Michálek
- Match score: 0.891
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/the-state-of-prometheus-and-opentelemetry-interoperability/JFS0lSfHtMI.txt
- Transcript chars: 22040
- Keywords: prometheus, resource, attributes, metrics, metric, remote, deltas, support, memory, experience, collector, change, native, application, instead, series, accept, definitely

### Resumo baseado na transcript

Okay, we are talking about the state of Prometheus and open telemetry interoperability. Uh besides that, I also do mentorships through CNCF mentorship programs, Google center of code, LFX, and I graph pays me to make sure that Prometheus and open telemetry work well. Um, we won't go into the nitty-gritty details of things, but Prometheus is also very much designed uh for pull and regular intervals. Um also um uh without lowering the uh look back delta in Prometheus uh you can also keep getting the basically last data point for your application that away that went away for up to 5 minutes. And I I'm not proud to say uh I've been a Prometheus user for almost a decade now. Uh but if we compare the two like why do we see them as competitors like Prometheus is a time series database focused on metrics uh and it has a lot of features that allows monitoring and alerting systems while the open telemetry is not a backend.

### Excerpt da transcript

Okay, we are talking about the state of Prometheus and open telemetry interoperability. First of all, show of hands. Who is using Prometheus or open telemetry? Um, who is using Prometheus and open telemetry? And who is liking the experience? Okay, I'm sorry. Um I'm Arthur. I work for Graphana Labs. I'm a maintainer of From Meus for a few years now. I joined Open Telemetry recently. I've been contributing for like six, seven months. I got approver status in the collector. Uh besides that, I also do mentorships through CNCF mentorship programs, Google center of code, LFX, and I graph pays me to make sure that Prometheus and open telemetry work well. Apparently, I'm not doing a good job. Uh, but I hope uh we improve over time. Hi, so I'm Uray. Um, I'm an SR with a focus on observability in SW3. Uh, and I'm also hotel and the looks good to me stack contributor. I'm also an active member of the open telemetry and Prometheus uh special interest group and um last year I also became a graphana champion. So, so um with um Prometheus and openmetry they sort of got off at the wrong foot and at least partially that's due to philosophical differences um around how to collect metrics right whereas uh Prometheus is predominantly a pullbased model.

Open telemetry at least in its current implementation is predominantly a pushbased model. Um so uh what's the differences? what are the pros and cons uh with the pool based Prometheus model um Prometheus relies on service discovery to know what's uh supposed to be monitored and it also allows us um to have uh metrics such as the app metric in Prometheus we can which we can use to monitor for failed scrapes. Uh however there are some disadvantages to this approach. Um apps need to keep the metrics in memory. uh and if you if your metrics don't change frequently um uh if they keep the same value for a period of time we're wasting CPU and uh network to collect uh the same data over and over uh whereas with the pushbased model uh yeah whereas with the pushbased model uh we don't need to keep the metrics in memory and um we can only push when there's actual data to push however we don't have the service discovery uh so the promeus can't tell what's being monitored. And even if it knew what's being monitored, it can't tell easily the difference between an application that went away versus an application that's just unavailable due to, for example, a network issue.

Um, we won't go into the nitty-gritty details of things, but Prometh
