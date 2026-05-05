---
type: promcon-talk
conference: PromCon
edition: "PromCon 2018"
edition_id: 2018-munich
year: 2018
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Alerting", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2018-munich/talks/implementing-a-cooperative-multi-tenant-capable-prometheus/
youtube_url: https://www.youtube.com/watch?v=AO_I1oVcqBM
youtube_search_url: https://www.youtube.com/results?search_query=Implementing+a+Cooperative+Multi-Tenant+Capable+Prometheus+PromCon+2018
video_match_score: 1.029
status: video-found
---

# Implementing a Cooperative Multi-Tenant Capable Prometheus

## Identificação

- Edição: PromCon 2018
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Alerting]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2018-munich/talks/implementing-a-cooperative-multi-tenant-capable-prometheus/
- YouTube: https://www.youtube.com/watch?v=AO_I1oVcqBM

## Resumo

Speaker: Jonas Große Sundrup Prometheus is capable of and used for monitoring large infrastructures, from corporate networks to world-spanning CDNs. But while performing excellent on setups of large scales, it is also extremely well suited for small setups due to its simplicity and modularity both in operation as well in usage. To further simplify leveraging the power of Prometheus for monitoning, we developed a cooperative, centrally managed multi-tenant-capable Prometheus system that minimizes the entry barrier for participants, introducing Prometheus to small-scale monitoring including out-of-the-box capabilities for blackbox montioring.

## Abstract oficial

Speaker: Jonas Große Sundrup

Prometheus is capable of and used for monitoring large infrastructures, from corporate networks to world-spanning CDNs. But while performing excellent on setups of large scales, it is also extremely well suited for small setups due to its simplicity and modularity both in operation as well in usage.

To further simplify leveraging the power of Prometheus for monitoning, we developed a cooperative, centrally managed multi-tenant-capable Prometheus system that minimizes the entry barrier for participants, introducing Prometheus to small-scale monitoring including out-of-the-box capabilities for blackbox montioring.

The multi-tenancy layer in this case serves two distinct purposes: First, it ensures that every user can only access their own metrics when querying. Second, it ensures that every user can only create alerts or alert silences for their own set of metrics.

In the process of doing so, we will investigate how the Prometheus frontend handles queries and how alerts and silences are submitted and modified accordingly, to implement multi-tenancy in Prometheus.

The entire setup is usable with out-of-the-box standard Prometheus components, no patches necessary.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2018-munich/talks/implementing-a-cooperative-multi-tenant-capable-prometheus/
- YouTube: https://www.youtube.com/watch?v=AO_I1oVcqBM
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=AO_I1oVcqBM
- YouTube title: PromCon 2018: Implementing a Cooperative Multi-Tenant Capable Prometheus
- Match score: 1.029
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2018/implementing-a-cooperative-multi-tenant-capable-prometheus/AO_I1oVcqBM.txt
- Transcript chars: 18766
- Keywords: prometheus, provide, alerting, targets, pretty, metrics, prompt, actually, multi-tenancy, course, monitoring, manager, directory, configuration, metric, alerts, getting, vector

### Resumo baseado na transcript

[Applause] so welcome to this talk implementing a corporate multi-tape about Prometheus or as we renamed renamed yesterday easy multi-tenancy so first of all implementing a cooperative multi-tenant capable Prometheus you might be wondering what are we doing there so the first thing I would like to talk about what is our target audience what are our target users the system was built with users in mind that runs small-scale infrastructure most of them run like single server setups but you still want to have monitoring for them right on

### Excerpt da transcript

[Applause] so welcome to this talk implementing a corporate multi-tape about Prometheus or as we renamed renamed yesterday easy multi-tenancy so first of all implementing a cooperative multi-tenant capable Prometheus you might be wondering what are we doing there so the first thing I would like to talk about what is our target audience what are our target users the system was built with users in mind that runs small-scale infrastructure most of them run like single server setups but you still want to have monitoring for them right on the other hand like getting a second monitoring server just to monitor one other server might be a little bit of overkill so our intention is to share monitoring infrastructure the other thing of our users we intend that our users must not be monitoring experts but the system should be very easy for them and very easy very approachable so that everyone can can basically use it with with a low entry bar so the goal that I've formulated here is we want to have a drop that simple fire-and-forget low resource monitoring or alerting solution that just works sounds sounds pretty cool right so let's see if we can do that so the roadmap for this talk will be will we will first speak a little bit about how we implement that on Prometheus we also as we want to have alerting we have an alert manager on the system after that we will speak a little bit about the system architecture and some additional services that we that we also provide for the system we of course have some requirements or requirements we are we want to have one parameters per machine we want to have a low memory footprint and the machine we want to run this on should be as cheap as possible and we also do not want to like have the operational overhead of managing multiple Prometheus instances we also obviously want to have multi-tenancy because that's a more system used by multiple tenants we want to have ansible compatibility because a lot of our users are running although the setups are small they're running it on ansible so we want to have ansible be capable of dropping monitoring targets in there and we want to have patch free operation we will not patch around in the in the code components of Prometheus because that will be a pain to operate and we're not gonna go down that road so that's what that was the preamble and now we need to talk about how to get data into Prometheus and usually when we speak about getting data into Prometheus people think about scraping b
