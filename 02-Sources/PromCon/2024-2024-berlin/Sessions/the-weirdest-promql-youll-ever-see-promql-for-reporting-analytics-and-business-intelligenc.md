---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2024"
edition_id: 2024-berlin
year: 2024
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Remote Write Storage", "Alerting", "Kubernetes", "Scalability Reliability"]
speakers: ["Sam Jewell"]
source_url: https://promcon.io/2024-berlin/talks/the-weirdest-promql-youll-ever-see-promql-for-reporting-analytics-and-business-intelligence/
youtube_url: https://www.youtube.com/watch?v=YlBn3LI7DLY
youtube_search_url: https://www.youtube.com/results?search_query=The+weirdest+PromQL+you%E2%80%99ll+ever+see%3A+PromQL+for+Reporting%2C+Analytics%2C+and+Business+Intelligence+PromCon+2024
video_match_score: 0.902
status: video-found
---

# The weirdest PromQL you’ll ever see: PromQL for Reporting, Analytics, and Business Intelligence

## Identificação

- Edição: PromCon EU 2024
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Metrics]], [[Remote Write Storage]], [[Alerting]], [[Kubernetes]], [[Scalability Reliability]]
- Speakers: Sam Jewell
- Página oficial: https://promcon.io/2024-berlin/talks/the-weirdest-promql-youll-ever-see-promql-for-reporting-analytics-and-business-intelligence/
- YouTube: https://www.youtube.com/watch?v=YlBn3LI7DLY

## Resumo

Prometheus is fantastic at managing high-frequency data. But what if you have an analytics use case? Sometimes we just want to lower the frequency; to see daily, weekly or monthly data and find long-term trends or growth rates.

## Abstract oficial

Prometheus is fantastic at managing high-frequency data. But what if you have an analytics use case? Sometimes we just want to lower the frequency; to see daily, weekly or monthly data and find long-term trends or growth rates.

We might want to consider any of these use cases per day, week, or month, such as:


Activity: requests or transactions
Usage or consumption for billing or auditing
Count of events: alerts or incidents, for example.


Why use Prometheus rather than more traditional analytics tools for this? By querying Prometheus directly we can avoid creating/maintaining a data-pipelines, avoid data exports and staleness problems, and lean on the power of the Prometheus ecosystem: For example, we can create overviews for management, plan ahead, and alert on our reports.

Yet querying Prometheus by calendar-month in particular can be surprisingly tricky. PromQL doesn’t support using 1M in subqueries because month-lengths vary.

In this talk I’ll:


Take you on a journey, discovering ways that the time dimension can be aggregated when querying Prometheus by using:


The offset keyword
Joins and the absent() function
Union and intersection operators or and and



Navigate a PromQL gotcha along the way, using a subquery
Conclude by showing two different ways we can render monthly data FTW:


Render a saw-tooth cumulative counter which resets to zero every month-start
Use day_of_month() to then derive a single value per calendar month.




After this talk you will be able to query for daily, weekly or monthly data directly from Prometheus. As a result, you’ll be able to spot longer term trends or growth rates. And you’ll be able to compare with data from your other sources, for correlation or auditing purposes.

## Links

- Página oficial: https://promcon.io/2024-berlin/talks/the-weirdest-promql-youll-ever-see-promql-for-reporting-analytics-and-business-intelligence/
- YouTube: https://www.youtube.com/watch?v=YlBn3LI7DLY
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YlBn3LI7DLY
- YouTube title: PromCon 2024 - The Weirdest PromQL You’ll Ever See: PromQL for Reporting, Analytics
- Match score: 0.902
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2024/the-weirdest-promql-youll-ever-see-promql-for-reporting-analytics-and/YlBn3LI7DLY.txt
- Transcript chars: 25541
- Keywords: months, august, actually, prometheus, second, metric, labels, promql, working, grafana, september, question, metrics, absent, period, received, interval, multiply

### Resumo baseado na transcript

yeah hi everybody this is the weirdest promql you'll ever see promql for reporting analytics and business intelligence now this is my first time at promcon it's actually my first conference talk um so you'll have to forgive the kind of somewhat Batey title I put together when I was uh pitching this um we've we've seen some weird prom today right um some of H and minoes and I was told about this uh legendary talk from five years ago um that's that's gone down in history so maybe

### Excerpt da transcript

yeah hi everybody this is the weirdest promql you'll ever see promql for reporting analytics and business intelligence now this is my first time at promcon it's actually my first conference talk um so you'll have to forgive the kind of somewhat Batey title I put together when I was uh pitching this um we've we've seen some weird prom today right um some of H and minoes and I was told about this uh legendary talk from five years ago um that's that's gone down in history so maybe this is the second weirdest prom you'll ever see who knows and uh yeah here it is if you want to go now you can uh you can go go away happy now um so yeah my name is Sam juel I'm a senior software engineer at graffan Labs I've been there three uh years now when I'm not working I'm working hard or maybe not so hard looking after my two boys um here we're dressed up as uh daffodils dressed up in yellow yellow flowers um when I am working most recently I've worked on cost attribution this is helping customers to split up their their bill their Graff Labs Bill uh by label typically um and for large companies large customers this is pretty important important it means they can break down that huge bill and see who is sending what um and it's also important for teams teams can then see their own contribution to that enormous company spend and start to kind of take ownership of that so it's it's pretty valuable you know in dollars we dog feed this at grafana and in the last month or two we've we've cut metrics that were worth $25,000 every month and um and we we're just getting started we plan to save even more over the coming months and we're using we're using Prometheus and we're using grafana um to do this which is which is interesting because it's not an observability use case um we're storing the data in Prometheus we're visualizing with grafana and that's why I'm here talking today um to share like how we're using Prometheus and to kind of say that you to can use Prometheus for non-observability use cases um such things as you know you could track dorom metrics you could track like site activity or transactions you could track alerts or incidents um or like us you could track usage of like meted Cloud spend Cloud you know meted cloud services and save money and and we heard yesterday from Swiss re they described themselves uh one of their functions as being a data shop and the other other teams were consuming some of their data [Music] so so why why use Prometheus and why not kind of
