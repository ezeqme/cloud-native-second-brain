---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2025"
edition_id: 2025-munich
year: 2025
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Alerting", "Scalability Reliability", "Visualization Dashboards"]
speakers: ["Jorge Creixell", "Manoj Acharya"]
source_url: https://promcon.io/2025-munich/talks/saafe--a-prioritized-alerting-model-to-troubleshoot-your-incidents/
youtube_url: https://www.youtube.com/watch?v=YoTafH7-OpA
youtube_search_url: https://www.youtube.com/results?search_query=SAAFE+-+A+prioritized+alerting+model+to+troubleshoot+your+incidents+PromCon+2025
video_match_score: 1.039
status: video-found
---

# SAAFE - A prioritized alerting model to troubleshoot your incidents

## Identificação

- Edição: PromCon EU 2025
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Alerting]], [[Scalability Reliability]], [[Visualization Dashboards]]
- Speakers: Jorge Creixell, Manoj Acharya
- Página oficial: https://promcon.io/2025-munich/talks/saafe--a-prioritized-alerting-model-to-troubleshoot-your-incidents/
- YouTube: https://www.youtube.com/watch?v=YoTafH7-OpA

## Resumo

Existing taxonomies for time-series data, including the Four Golden Signals, the RED, and the USE Method, are most concerned with the nature of each type of series. The SAAFE - Saturation, Amend, Anomaly, Failure, and Error alerting model helps you focus on what they imply and not the type. At Grafana Labs, we have built a scalable, fully automated alerting system that analyzes the data using its domain knowledge.

## Abstract oficial

Existing taxonomies for time-series data, including the Four Golden Signals, the RED, and the USE Method, are most concerned with the nature of each type of series. The SAAFE - Saturation, Amend, Anomaly, Failure, and Error alerting model helps you focus on what they imply and not the type. 

At Grafana Labs, we have built a scalable, fully automated alerting system that analyzes the data using its domain knowledge. These alerts are categorized into the SAAFE model based on their implications for the system. Combined with severity levels - info, warning, critical, no of instances, and firing duration, the SAAFE alerts are scored and ranked. When our on-call engineers troubleshoot incidents, they use the SAAFE categorization and ranking to prioritize, filter, and infer causality. 

In this talk, we will introduce the SAAFE method with real-world examples of how this has been useful. We will also share the open-source framework built purely using PromQL and Grafana that you can adopt.

## Links

- Página oficial: https://promcon.io/2025-munich/talks/saafe--a-prioritized-alerting-model-to-troubleshoot-your-incidents/
- YouTube: https://www.youtube.com/watch?v=YoTafH7-OpA
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YoTafH7-OpA
- YouTube title: Promcon 2025 - SAAFE - A prioritized alerting model to troubleshoot your incidents
- Match score: 1.039
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2025/saafe-a-prioritized-alerting-model-to-troubleshoot-your-incidents/YoTafH7-OpA.txt
- Transcript chars: 21601
- Keywords: basically, actually, assertion, important, probably, alerts, metric, specific, assertions, anomaly, metrics, dashboard, framework, detect, already, visualize, recording, happening

### Resumo baseado na transcript

Uh but he's a VP of engineering in the department also at Grafana Labs. Uh Manus basically has been traveling for the last two months and uh he really wanted to spend the valley with his family. So, you typically get paid and if you're like me, the first thing that you do is probably you jump to dashboard uh related to the alert and you try to analyze, you know, okay, what happened? And usually what you're seeing is just a symptom of a cost that is probably happening elsewhere. And so what you do is usually try to go up, you know, zoom out and create a view of the world of your system of what's happening in your system at the global level and try to infer the cost out of the symptom. And there's another way that is complimentary that you can actually look at this problem and it's basically a top-down approach where when you get paid the first thing that you see is you go to the system overview and hopefully the system overview is

### Excerpt da transcript

[music] Hello everyone. Uh my name is Jorge and I'm a software engineer at Graphana Labs. And as you can see, Manus is not here with me today. Uh but he's a VP of engineering in the department also at Grafana Labs. Uh Manus basically has been traveling for the last two months and uh he really wanted to spend the valley with his family. So it's going to be just me today. Uh but let's get started. Um, I want to talk about alerting and how you could make it more useful during your uh troubleshooting. But first of all, I wanted to know raise your hand if you attended Promcon 2024 last year. All right, quite a few hands. And uh raise your hand if you have tried this anomaly detection framework from last year. Okay, quite a few. All right. So, Manus and I uh presented uh this framework uh last year at Fron which was basically uh a set of recording rules and alerting rules that will allow you to basically draw these uh bounds for your metrics and detect when they are like out of bounds and that there's an anomaly in your metric.

Um and we also said in the talk that uh we thought that you should impage on anomalies and we actually uh got some questions about this uh and you know why that's the case and what how should you use it then? And uh the first question that you should ask is like whether you should wake this guy up at night because there was an anomaly uh because there was a change in the in the pattern in your metrics. And very likely the answer is no because you know the anomaly detection system tells you that something is different but not necessarily that something is wrong. And so the next thing that you might think is like okay let let's just go and make it a warning. Uh but if you if your slack uh notification channel looks like mine uh I funny enough I was taking this uh I was preparing this uh slide and I noticed that I had completely muted mine and I never look at it. Right? So that would have been adding more noise to the mountain of noise that we have already there. And that's really the problem, right?

When everything is important, at the end nothing is important. But it's it's not useless, right? All of this is context. And that's kind of the key. We think that you should page on actionable symptoms, things like require immediate remediation that they need an action. Uh but everything else you can still use as context. And the question is how can we visualize it and make it useful enough that we can actually make use of this. And that's wha
