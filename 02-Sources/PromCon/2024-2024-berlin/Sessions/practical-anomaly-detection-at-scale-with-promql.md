---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2024"
edition_id: 2024-berlin
year: 2024
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Alerting", "Scalability Reliability", "Visualization Dashboards"]
speakers: ["Jorge Creixell", "Manoj Acharya"]
source_url: https://promcon.io/2024-berlin/talks/practical-anomaly-detection-at-scale-with-promql/
youtube_url: https://www.youtube.com/watch?v=BTAba-Vq3xE
youtube_search_url: https://www.youtube.com/results?search_query=Practical+Anomaly+detection+at+scale+with+PromQL+PromCon+2024
video_match_score: 1.011
status: video-found
---

# Practical Anomaly detection at scale with PromQL

## Identificação

- Edição: PromCon EU 2024
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Metrics]], [[Alerting]], [[Scalability Reliability]], [[Visualization Dashboards]]
- Speakers: Jorge Creixell, Manoj Acharya
- Página oficial: https://promcon.io/2024-berlin/talks/practical-anomaly-detection-at-scale-with-promql/
- YouTube: https://www.youtube.com/watch?v=BTAba-Vq3xE

## Resumo

At Grafana Labs, we built a scalable anomaly detection system to aid in debugging issues. For example, within a specified time range, did a particular service exhibit any anomalies in its USE metrics, RED metrics, or other key KPIs? This helps us narrow down the scope to a few “interesting” services when debugging errors in a complex system.

## Abstract oficial

At Grafana Labs, we built a scalable anomaly detection system to aid in debugging issues. For example, within a specified time range, did a particular service exhibit any anomalies in its USE metrics, RED metrics, or other key KPIs? This helps us narrow down the scope to a few “interesting” services when debugging errors in a complex system.

We started by building automatic baselines per service for common USE and RED metrics, and expanded it to easily include any counter or gauge that users can tag with a special label. The baselines and alerting are based on standard deviation but take seasonality into account for the past two weeks. This approach avoids noisy alerts during regular daily or weekly spikes. We have been running this system at scale and in production and are about to roll it out to customers.

In this talk, we will present why we chose to adopt anomaly detection and the framework (to be open-sourced at PromCon) we used to detect the anomalies purely using PromQL. We will demonstrate how the baselines can be visualized in Grafana and how we group these alerts for troubleshooting purposes (DO NOT PAGE ON ANOMALY ALERTS!).

Additionally, we will showcase the flexibility of the framework and how our users can add anomaly detection to their custom metrics by simply adding a single label: asserts_anomaly="gauge".

## Links

- Página oficial: https://promcon.io/2024-berlin/talks/practical-anomaly-detection-at-scale-with-promql/
- YouTube: https://www.youtube.com/watch?v=BTAba-Vq3xE
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=BTAba-Vq3xE
- YouTube title: PromCon 2024 - Practical Anomaly Detection at Scale With PromQL
- Match score: 1.011
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2024/practical-anomaly-detection-at-scale-with-promql/BTAba-Vq3xE.txt
- Transcript chars: 27694
- Keywords: actually, metric, standard, deviation, basically, average, recording, expand, window, variability, prometheus, simple, everything, question, anomaly, called, filter, enough

### Resumo baseado na transcript

[Music] hey everyone uh I'm Manoj uh excited to join you all here this is a conference very close to my heart I've watched uh probably every promcon talk that's already there on YouTube uh I'm one of those Netflix promcon guy I guess uh so yeah I mean I'm excited very first time in promcon in person in life and uh and also to be joining all the talking you sharing with you how we have been using Prometheus at scale to solve some real world problems um and

### Excerpt da transcript

[Music] hey everyone uh I'm Manoj uh excited to join you all here this is a conference very close to my heart I've watched uh probably every promcon talk that's already there on YouTube uh I'm one of those Netflix promcon guy I guess uh so yeah I mean I'm excited very first time in promcon in person in life and uh and also to be joining all the talking you sharing with you how we have been using Prometheus at scale to solve some real world problems um and I over to jge hi I'm Jorge uh I'm a principal engineer at graan Labs I've been using Prometheus since around 2016 from my times at SoundCloud um yeah I contributed to grafana agent and I'm been getting more involved lately with Prometheus um yeah so the topic is uh I mean you can read it here animal detection so it's a very hotly debated topic and if you just go back to the very founding people of Prometheus the people who built Prometheus at SoundCloud um like people like BR Brazil and Fabian and uh and Beyond over here somewhere here they have talked about it over the years you will find blogs about it you will find talks you know promcon talks about it going back to 2015 and 2016 so nothing new here uh it's it's it's the story goes like this so we are Engineers we build code uh we get alerted and so because we're on call and then we click a link and we arrive on a chart like this and now we wondering is this okay is it normal I mean does this metric just spikes up every day at the same time is it even relevant so all those questions you know and how do you then what is the next step you do you probably expand your time window you go back one day uh you go back to previous week you start thinking about all the other metrics that probably are related to this and start building a story together in your head but what if this uh chart looked more like uh this where you already had a lot of context attached to this chart right so you can instantly answer a lot of the questions we were asking in the previous slide where it could tell you yes it is actually above the normal what it's supposed to be and so and that's what we going to talk about today so a big disclaimer uh like I mentioned this has been talked a lot about it and there's many ways to solve this problem this is not the only way and the reason we picked uh this approach is because if you desired Properties or constraints as you may call you know as Engineers we always are Building Systems we want to Define our constraints and that it should work i
