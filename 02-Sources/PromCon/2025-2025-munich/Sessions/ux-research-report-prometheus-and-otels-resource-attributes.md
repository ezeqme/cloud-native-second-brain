---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2025"
edition_id: 2025-munich
year: 2025
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "OpenTelemetry", "Scalability Reliability", "Cost Optimization", "Community"]
speakers: ["Victoria Nduka", "Andrej Kiripolský"]
source_url: https://promcon.io/2025-munich/talks/ux-research-report-prometheus-and-otels-resource-attributes/
youtube_url: https://www.youtube.com/watch?v=p4YioGATN-s
youtube_search_url: https://www.youtube.com/results?search_query=UX+Research+Report%3A+Prometheus+and+OTel%27s+Resource+Attributes.+PromCon+2025
video_match_score: 1.032
status: video-found
---

# UX Research Report: Prometheus and OTel's Resource Attributes.

## Identificação

- Edição: PromCon EU 2025
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[OpenTelemetry]], [[Scalability Reliability]], [[Cost Optimization]], [[Community]]
- Speakers: Victoria Nduka, Andrej Kiripolský
- Página oficial: https://promcon.io/2025-munich/talks/ux-research-report-prometheus-and-otels-resource-attributes/
- YouTube: https://www.youtube.com/watch?v=p4YioGATN-s

## Resumo

There are currently three strategies for handling OTel resource attributes in Prometheus: Map all attributes into labels, which leads to high cardinality problems. Encode all attributes to the target_info metric and use PromQL Joins, which have a high entry barrier for Prometheus users. Select which attributes become labels with the promote_resource_attributes configuration option, which is not friendly to changes in that list.

## Abstract oficial

There are currently three strategies for handling OTel resource attributes in Prometheus:


Map all attributes into labels, which leads to high cardinality problems.
Encode all attributes to the target_info metric and use PromQL Joins, which have a high entry barrier for Prometheus users.
Select which attributes become labels with the promote_resource_attributes configuration option, which is not friendly to changes in that list.


Is this really all there is for resource attributes? Has Prometheus nailed their user story in this topic?

Through CNCF's LFX mentorship program, Victoria and Andrej conducted UX Research to understand how Prometheus should handle OTel's resource attributes. Using quantitative and qualitative approaches, they collected opinions from co-founders of both projects, active and old maintainers, and end-users.

By joining this talk, the audience will learn more about what is going well and what could be improved, while listening to Victoria and Andrej share educated suggestions for the project maintainers.

## Links

- Página oficial: https://promcon.io/2025-munich/talks/ux-research-report-prometheus-and-otels-resource-attributes/
- YouTube: https://www.youtube.com/watch?v=p4YioGATN-s
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=p4YioGATN-s
- YouTube title: Promcon 2025 - UX Research Report: Prometheus and OTel's Resource Attributes
- Match score: 1.032
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2025/ux-research-report-prometheus-and-otels-resource-attributes/p4YioGATN-s.txt
- Transcript chars: 22706
- Keywords: attributes, resource, prometheus, victoria, actually, approach, documentation, research, attribute, having, mentioned, already, target, understand, respondents, around, joints, thanks

### Resumo baseado na transcript

My name is Andre and I'll be speaking today about uh how should open telemetry uh attributes or how could open telemetry attributes be handled resource attributes be handled in Prometheus. So this is a presentation of an outcome of Linux Foundation mentorship project. So resource attributes are basically something like Prometheus labels uh that are sent from like if yeah resource attributes are parameters of resources in hotel and when they are stored in Prometheus they are basically Prometheus labels uh so that's quite clear when it becomes problematic is uh when we talk about the instrumentation so in with Prometheus you have to instrument things manually and then there is uh you kind of understand what are you storing and what are you sending with pre with open telemetry uh and with the automatic instrumentation uh people can start getting a whole lot of uh attributes that they might see for the first time and uh it might be causing problems and uh yeah in this project we wanted to cover three goals three research goals first one was to understand how engineers currently handle open telemetry resource attributes in Prometheus.

### Excerpt da transcript

[music] Good. Good. So, uh hi everyone. Uh thanks a lot for for uh having me or us actually. My name is Andre and I'll be speaking today about uh how should open telemetry uh attributes or how could open telemetry attributes be handled resource attributes be handled in Prometheus. So uh yeah I just now have to find a cursor. Nice. So this is a presentation of an outcome of Linux Foundation mentorship project. Uh so there are four of us involved. Uh the main person most important one and who should get the main spotlight today is Victoria Nuka. Uh unfortunately uh she's not able to be here today. So I will play her part of a presentation as a recording. Yeah. So Victoria uh was the mentee in this project and then there were three of us mentors. Arthur, you all know Arthur. Arthur is a permitous maintainer and uh also Graphana software engineer. Uh then there is Amy from also from Grafana a product designer and uh me from Graphana uh user researcher. Uh some quick background. Why did we why did we decide to look into this topic?

Uh Arthur was talking about this uh I think last year uh at CubeCon and uh also uh he was he was getting some like indirect feedback overall from different people that resource attributes from open telemetry are like the way how they are uh handled in Prometheus can be problematic for some users. So when we were coming up with the topic for the mentorship, we decided to look into uh this problem. And before I uh move forward, I know that resource attributes were mentioned many times already, but I'll try to explain for folks who might not know uh how they work. So resource attributes are basically something like Prometheus labels uh that are sent from like if yeah resource attributes are parameters of resources in hotel and when they are stored in Prometheus they are basically Prometheus labels uh so that's quite clear when it becomes problematic is uh when we talk about the instrumentation so in with Prometheus you have to instrument things manually and then there is uh you kind of understand what are you storing and what are you sending with pre with open telemetry uh and with the automatic instrumentation uh people can start getting a whole lot of uh attributes that they might see for the first time and uh it might be causing problems and uh yeah in this project we wanted to cover three goals three research goals first one was to understand how engineers currently handle open telemetry resource attributes in Prometheus.

Then wha
