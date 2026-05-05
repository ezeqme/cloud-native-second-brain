---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2023"
edition_id: 2023-berlin
year: 2023
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Alerting", "Scalability Reliability", "Visualization Dashboards"]
speakers: []
source_url: https://promcon.io/2023-berlin/talks/alert-analytics/
youtube_url: https://www.youtube.com/watch?v=O2V7wQKtdIg
youtube_search_url: https://www.youtube.com/results?search_query=Alert+Analysis+as+a+Service+PromCon+2023
video_match_score: 0.936
status: video-found
---

# Alert Analysis as a Service

## Identificação

- Edição: PromCon EU 2023
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Alerting]], [[Scalability Reliability]], [[Visualization Dashboards]]
- Speakers: N/A
- Página oficial: https://promcon.io/2023-berlin/talks/alert-analytics/
- YouTube: https://www.youtube.com/watch?v=O2V7wQKtdIg

## Resumo

Speaker(s): Monika Singh At Cloudflare, we use Prometheus heavily. We have point-of-presense in more than 275+ number of cities and each point-of-presense have their own prometheus. All these prometheis send alerts to a central alertmanager.

## Abstract oficial

Speaker(s): Monika Singh

At Cloudflare, we use Prometheus heavily. We have point-of-presense in more than 275+ number of cities and each point-of-presense have their own prometheus. All these prometheis send alerts to a central alertmanager. We have various integrations to route the alerts. We also route all the alerts to a datastore for alert analytics.

The talk covers:


What is Alert fatigue and its impact?
What is alert analytics and why is it important? - The purpose of alert analysis is to give feedback to monitoring system.
Core concepts of Alertmanager.
How to do Alert Analysis using open source tools such as Promtheus, Alertmanager, Vector.dev, ClickHouse, Grafana.
Outcome and Conclusion.

## Links

- Página oficial: https://promcon.io/2023-berlin/talks/alert-analytics/
- YouTube: https://www.youtube.com/watch?v=O2V7wQKtdIg
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=O2V7wQKtdIg
- YouTube title: PromCon 2023 - Alert Analysis as a Service
- Match score: 0.936
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2023/alert-analysis-as-a-service/O2V7wQKtdIg.txt
- Transcript chars: 18786
- Keywords: alerts, manager, firing, labels, silence, number, silences, dashboard, overview, vector, wanted, analysis, prometheus, receiving, alerting, burnout, inhibited, active

### Resumo baseado na transcript

[Music] thank you hello everyone I hope you all are having great time at Prometheus conference I am very excited to be here and this is my first time attending promethus conference uh before we start just a quick heads up the most of the most of my slides and the Lego logos in it are hand done by Yours Truly uh please pardon any imperfect sections or scribbles you may come across so today I'm here to talk about what is alert analytics why is it important and how on call work can lead to chronic stress which can in turn contribute to burnout depression anxiety and any other mental health issues so let's look at how alert analytics can help reduce the burnout alert analysis is essentially reviewing alerts periodically and giving feedback to system to improve the quality of alerts have you ever wondered how many alerts your team is receiving which component or service is generating most alerts which is most noisy alert or which medium is receiving most number of alerts is it chat page Dev to collect data from sources transform the data and write it into a data store here we are using one HTTP server Vector instance to receive alert manager web hook integration two HTTP client sources to query alerts and silences API end points and we're using two syns for writing all the state logs in Click house into alerts and silencers tables I have used click house for storing the data...

### Excerpt da transcript

[Music] thank you hello everyone I hope you all are having great time at Prometheus conference I am very excited to be here and this is my first time attending promethus conference uh before we start just a quick heads up the most of the most of my slides and the Lego logos in it are hand done by Yours Truly uh please pardon any imperfect sections or scribbles you may come across so today I'm here to talk about what is alert analytics why is it important and how it can be done using open-source tools so hi my name is Monica I work as systems reliability engineer in observability team at Cloud flare in from Singapore observability is to enhance insights into technology stack by gathering and analyzing a broad broader spectrum of data in this talk I'm going to talk about alert observability this would look familiar to most of you this is how a typical day for a lot of on calls look like on calls receive a lot of alerts receiving too many alerts can lead to alert fatigue alert fatigue is essentially exhaustion caused by responding to unprioritized and unactionable alerts talk about on call I am on call 24/7 365 days a year being a mom to a toddler and talk to me about alert fatigue or toddler Tantrums I can talk about it all day long it's 2: a.m.

your kid wakes you up hey hey wake up I'm hungry I generally suggest kid to drink some water and go back to sleep just to make sure he's really hungry and not dreaming that he's hungry it does happen well well similarly in case of alerts we want to make sure that the alerts are accurate and not false positive receiving false positive alerts can make on call person desensitized so here are some general findings about health impacts of on call work being on call can lead to irregular sleep patterns potentially leading to sleep deprivation irregular work hours associated with being on call increases physical health risk being on call can also impact social life and leisure activities leading to decreased life satisfaction and increase psychological distress the unpredictability and intensity of on call work can lead to chronic stress which can in turn contribute to burnout depression anxiety and any other mental health issues so let's look at how alert analytics can help reduce the burnout alert analysis is essentially reviewing alerts periodically and giving feedback to system to improve the quality of alerts have you ever wondered how many alerts your team is receiving which component or service is generating most al
