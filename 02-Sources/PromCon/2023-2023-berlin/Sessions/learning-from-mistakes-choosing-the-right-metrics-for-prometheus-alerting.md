---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2023"
edition_id: 2023-berlin
year: 2023
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Alerting", "Kubernetes", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2023-berlin/talks/learning-from-mistakes-choosing-the-right-metrics-for-prometheus-alerting/
youtube_url: https://www.youtube.com/watch?v=frgHo6WfhPw
youtube_search_url: https://www.youtube.com/results?search_query=Learning+from+Mistakes+-+Choosing+the+Right+Metrics+for+Prometheus+Alerting+PromCon+2023
video_match_score: 1.048
status: video-found
---

# Learning from Mistakes - Choosing the Right Metrics for Prometheus Alerting

## Identificação

- Edição: PromCon EU 2023
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Metrics]], [[Alerting]], [[Kubernetes]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2023-berlin/talks/learning-from-mistakes-choosing-the-right-metrics-for-prometheus-alerting/
- YouTube: https://www.youtube.com/watch?v=frgHo6WfhPw

## Resumo

Speaker(s): Ankur Rawal & Dheeraj Reddy Evolution forged the entirety of sentient life on this planet using only one tool: the mistake. We analysed the incident data of 150+ highly active organisations deploying Prometheus Alertmanager to monitor their K8s infrastructure. We discovered some unusually common yet fatal mistakes made when choosing metrics, as well as some clever configurations drastically reducing noise.

## Abstract oficial

Speaker(s): Ankur Rawal & Dheeraj Reddy


Evolution forged the entirety of sentient life on this planet using only one tool: the mistake.


We analysed the incident data of 150+ highly active organisations deploying Prometheus Alertmanager to monitor their K8s infrastructure. We discovered some unusually common yet fatal mistakes made when choosing metrics, as well as some clever configurations drastically reducing noise.

We further studied and tested statistical concepts like Z-Score, Elliptic Envelope, Seasonality and their ability to detect and predict anomalies via time-series data at different scales, and will end with a kicker of a financial analysis of how much an average company could be losing to improper alerting.

This talk will give listeners a run-through of best practices and ‘what not to do' when choosing Prometheus metrics for noiseless and proactive alerting; preventing a few more folks from burning their fingers in their o11y journey.

## Links

- Página oficial: https://promcon.io/2023-berlin/talks/learning-from-mistakes-choosing-the-right-metrics-for-prometheus-alerting/
- YouTube: https://www.youtube.com/watch?v=frgHo6WfhPw
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=frgHo6WfhPw
- YouTube title: PromCon 2023 - Learning From Mistakes – Choosing the Right Metrics for Prometheus Alerting
- Match score: 1.048
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2023/learning-from-mistakes-choosing-the-right-metrics-for-prometheus-alert/frgHo6WfhPw.txt
- Transcript chars: 21354
- Keywords: actually, alerts, metrics, getting, mistakes, monitoring, number, prometheus, setting, application, already, pretty, cost, minimum, capacity, scraping, manager, container

### Resumo baseado na transcript

[Music] [Applause] uh hi everyone we'll be speaking on how to set right alert metrics which we have learned through all mistakes uh uh we are from Zen Duty and incident end to end Incident Management and response oration platform I'm anur I have accumulated years of experience making mistakes learning from them and advocating for best practices for organization setting up their devops SRE and production engineering teams uh D will yeah I am de and uh I work as a founding engineer at Zen Duty and I majorly

### Excerpt da transcript

[Music] [Applause] uh hi everyone we'll be speaking on how to set right alert metrics which we have learned through all mistakes uh uh we are from Zen Duty and incident end to end Incident Management and response oration platform I'm anur I have accumulated years of experience making mistakes learning from them and advocating for best practices for organization setting up their devops SRE and production engineering teams uh D will yeah I am de and uh I work as a founding engineer at Zen Duty and I majorly deal with back and stuff and uh time to time I also deal with some of the first of that is why I am here and I'm an observability thinker and um thanks to the uh thanks to great presentation so it got me more excited on open tary so let's move on why we are here so one of the things why we are here is to uh is to find what what are the right what does the right metrics mean when you are trying to monitoring and alerting so I know it's uh it's not that pretty straightforward so something right is not that simple so and uh especially when you are new to Prometheus uh uh new to monitoring uh it might take time sorry I'm a bit nervous so but I'll quickly catch on yeah and learning from mistake yeah one of this mistake I'm nervous so and other thing uh come on who doesn't do mistakes so uh we we all do mistakes and we'll go through some of the things uh some of the mistakes uh which we uncovered and we'll go in deep that and uh now for the most difficult part uh to answer what does a right metrics mean so and uh okay sorry and uh yeah and also to answer the most two important uh questions that finding the finding the right metrics which can answer your p 0 inurance so yeah we tend to configure most of the uh most of the alerts which answer most of your inent but there are a few alerts you need to configure to answer your p insurance and at the end of the day it it's all about the cost so is bad monitoring costing you so and yeah building a uh building a monitoring system is very hard especially if you're new if you're new into monitoring space and it might become pretty chaotic uh so it can't be done overnight so you have to learn from your mistake and keep iterating and so we we we are emphasizing what uh right alerts are so right alerts are alerts basically uh basically should have an impact so and uh should be actionable should be concise concise and accurate so yeah that's all and now I'll go through some of the key performance indicators uh which measure
