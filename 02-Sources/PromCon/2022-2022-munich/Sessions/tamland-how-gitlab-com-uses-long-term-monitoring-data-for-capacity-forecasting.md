---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2022"
edition_id: 2022-munich
year: 2022
city: "Munich"
country: "Germany"
topics: ["Metrics", "Remote Write Storage", "Scalability Reliability", "Visualization Dashboards"]
speakers: []
source_url: https://promcon.io/2022-munich/talks/tamland-how-gitlabcom-uses-long-/
youtube_url: https://www.youtube.com/watch?v=2R42jW98MXg
youtube_search_url: https://www.youtube.com/results?search_query=Tamland%3A+How+GitLab.Com+Uses+Long-Term+Monitoring+Data+For+Capacity+Forecasting+PromCon+2022
video_match_score: 1.037
status: video-found
---

# Tamland: How GitLab.Com Uses Long-Term Monitoring Data For Capacity Forecasting

## Identificação

- Edição: PromCon EU 2022
- País/cidade: Germany / Munich
- Temas: [[Metrics]], [[Remote Write Storage]], [[Scalability Reliability]], [[Visualization Dashboards]]
- Speakers: N/A
- Página oficial: https://promcon.io/2022-munich/talks/tamland-how-gitlabcom-uses-long-/
- YouTube: https://www.youtube.com/watch?v=2R42jW98MXg

## Resumo

Speaker(s): Andrew Newdigate Tamland is a capacity planning tool built by GitLab to provide long-term forecasts of potential capacity issues across the services running GitLab.com. It's built on top of the long-term metric storage capabilities of Thanos, which provides utilization and saturation metric data stretching back over a 1 year period. From this, a predictive forecast model is constructed and used to predict future growth trends across hundreds of saturation points over the coming months.

## Abstract oficial

Speaker(s): Andrew Newdigate

Tamland is a capacity planning tool built by GitLab to provide long-term forecasts of potential capacity issues across the services running GitLab.com. It's built on top of the long-term metric storage capabilities of Thanos, which provides utilization and saturation metric data stretching back over a 1 year period. From this, a predictive forecast model is constructed and used to predict future growth trends across hundreds of saturation points over the coming months. This practical talk demonstrates how we capture long-term metrics data in a scalable way using Thanos, how we use Facebook's Prophet library for building forecast models, and how we integrate this with Jupyter to generate a report complete with visualizations. It discusses the benefits of switching to a data-driven and repeatable approach to capacity planning, as well as some of the practical challenges of building the tool. Tamland is an open-source project and attendees have access to the project source if they're interested in digging deeper into our implementation.

## Links

- Página oficial: https://promcon.io/2022-munich/talks/tamland-how-gitlabcom-uses-long-/
- YouTube: https://www.youtube.com/watch?v=2R42jW98MXg
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2R42jW98MXg
- YouTube title: PromCon EU 2022: Tamland: How GitLab.Com Uses Long-Term Monitoring Data For Capacity Forecasting
- Match score: 1.037
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2022/tamland-how-gitlab-com-uses-long-term-monitoring-data-for-capacity-for/2R42jW98MXg.txt
- Transcript chars: 26820
- Keywords: resource, utilization, capacity, resources, growth, saturation, application, within, forecast, report, cluster, forecasting, planning, profit, gitlab, process, months, clusters

### Resumo baseado na transcript

[Music] foreign [Music] hi everyone my name is Andrew nudigatz I am an engineer at gitlab where I focus on availability reliability automated Automation and observability of our SAS platform specifically gitlab.com and gitlab dedicated which is the new product that we're building and I I come from Cape Town in South Africa and this is a picture of of where I live it was 30 degrees so I was really worried about freezing here but it's not been too bad actually um to start as a way of introduction

### Excerpt da transcript

[Music] foreign [Music] hi everyone my name is Andrew nudigatz I am an engineer at gitlab where I focus on availability reliability automated Automation and observability of our SAS platform specifically gitlab.com and gitlab dedicated which is the new product that we're building and I I come from Cape Town in South Africa and this is a picture of of where I live it was 30 degrees so I was really worried about freezing here but it's not been too bad actually um to start as a way of introduction uh let's briefly take a look at a very high level overview of the gitlab application architecture so starting on the left we have several front-end services that handle incoming requests and for the most part these are written in go and then in the center of the application we have this monolithic rails application which the majority of our product Engineers spend most of their time working on and this runs as a ruby and rails web application and it also has background processing taking place through sidekick I'm behind the application we run git or gitzerly which is our git RPC service and this runs on a large number of VMS with block storage attached to them we have six redis clusters in our production Fleet but the number is is always increasing and the reason we always need to add more redis clusters is because for any given cluster a single core on the primary instance of that cluster is a resource bottleneck and this is because of much of the way or much of the redis workload runs on a single thread and this makes scaling these clusters tricky and so when we reach capacity on the primary we'll very often split the radius into into two clusters each with a subset of the traffic and then finally at the bottom of the of the image we have um our postgres cluster well we actually have two clusters we have the main cluster and a CI cluster and the work to decompose crci out of the main cluster successfully uh was completed in July of this year and before that all the SQL traffic was handled only by the main cluster and we're going to talk about that a little bit in this talk so let's define a few terms that we're going to use through through this talk um the first term that I'm going to Define is is a resource so resources any component within a computer system that has limited availability and so very often people tend to focus on physical resources such as CPU or memory or bandwidth and these are of course very important examples of resources but at every level of
